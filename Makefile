SHELL := /bin/bash

DESTDIR ?= /usr/local
LOCAL_DESTDIR := "$(shell pwd -P)"/inst

CIF_VERSION := $(shell git rev-parse --short HEAD || echo unknown)
ASPECTATOR_VERSION := $(shell cd aspectator && git rev-parse --short HEAD || echo unknown)

# Workaround for "cannot find crti.o" error (only for x86-64 Ubuntu systems).
UBUNTU_LIB = /usr/lib/x86_64-linux-gnu

# System headers are no longer located in /usr/include in macOS >= Mojave.
ifeq ($(shell uname), Darwin)
	CONFIGURE_ARGS_MACOS = --with-native-system-header-dir=/usr/include
	CONFIGURE_ARGS_MACOS += --with-sysroot=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk
else
	CONFIGURE_ARGS_MACOS =
endif

.PHONY: all uninstall-previous-instances install-keep-previous-instances install test clean

all:
	$(MAKE) cif
	@if [ ! -f build/Makefile ]; then \
	  echo "Configure Aspectator for the first time"; \
	  cd build; \
	  MAKEINFO=missing ../aspectator/configure --prefix=/ --enable-languages=c \
	    --disable-libsanitizer --disable-multilib --disable-nls\
	    --enable-checking=release --with-pkgversion=$(ASPECTATOR_VERSION) \
	    --with-bugurl="https://forge.ispras.ru/projects/cif/issues" \
	    $(CONFIGURE_ARGS_MACOS) $(ASPECTATOR_CONFIGURE_OPTS); \
	fi
	@echo "Begin to (re)build Aspectator"
	@if [[ -d $(UBUNTU_LIB) && ! -z LIBRARY_PATH ]]; then export LIBRARY_PATH=$(UBUNTU_LIB); fi
	$(MAKE) BOOT_CFLAGS='-O2' -C build
	@echo "Install C Instrumentation Framework and Aspecator locally"
	$(MAKE) DESTDIR=${LOCAL_DESTDIR} build/install

cif:
	mkdir -p build
	gcc -Wall -Werror -D CIF_VERSION=\"$(CIF_VERSION)\" cif.c -o build/cif

build/install: uninstall install-keep-previous-instances

# Install Aspectator (GCC) within dedicated directory to simplify its uninstall.
install-keep-previous-instances:
	$(MAKE) DESTDIR="$(DESTDIR)/cif" -C build install-strip
	cp build/cif "$(DESTDIR)/cif/bin/cif"
	mkdir -p "$(DESTDIR)/bin"
	ln -sf "../cif/bin/cif" "$(DESTDIR)/bin/cif"
	ln -sf "../cif/bin/gcc" "$(DESTDIR)/bin/aspectator"

install:
	@echo "Install C Instrumentation Framework and Aspecator to '$(DESTDIR)'"
	@mkdir -p $(DESTDIR)
	rsync -rlu inst/* $(DESTDIR)

uninstall:
	rm -rf "$(DESTDIR)/bin/cif" "$(DESTDIR)/bin/aspectator" "$(DESTDIR)"/cif*

test:
	@if [[ ! -d ${LOCAL_DESTDIR} || ! -f ${LOCAL_DESTDIR}/bin/cif || ! -f ${LOCAL_DESTDIR}/bin/aspectator ]]; then \
	  echo "You must build CIF before running tests"; \
	  exit -1; \
	fi
	cd tests && pytest

clean:
	rm -rf build

archives:
	$(MAKE) archive
	$(MAKE) archives/cross

archive:
	$(MAKE) docker
	docker run -d -it --name cif cif
	docker exec cif mkdir /tmp/cif
	docker exec cif cp -r /usr/local/bin/ /tmp/cif/bin
	docker exec cif cp -r /usr/local/cif/ /tmp/cif/cif
	docker exec cif apt-get update
	docker exec cif apt-get install -y xz-utils
	docker exec cif mkdir /tmp/cif-archives
	docker exec cif bash -c "tar cJf /tmp/cif-archives/\`cif --version\`.tar.xz /tmp/cif"
	docker cp cif:/tmp/cif-archives/. .
	docker stop cif
	docker rm cif
	docker rmi cif

archive/arm-unknown-eabi:
	$(MAKE) archives/cross-pre
	docker exec cross-cif python3 build.py -o /tmp/cif-archives arm-unknown-eabi
	$(MAKE) archives/cross-post

archive/arm-unknown-linux-gnueabi:
	$(MAKE) archives/cross-pre
	docker exec cross-cif python3 build.py -o /tmp/cif-archives arm-unknown-linux-gnueabi
	$(MAKE) archives/cross-post

archive/aarch64_be-unknown-linux-gnu:
	$(MAKE) archives/cross-pre
	docker exec cross-cif python3 build.py -o /tmp/cif-archives aarch64_be-unknown-linux-gnu
	$(MAKE) archives/cross-post

archives/cross:
	$(MAKE) archives/cross-pre
	docker exec cross-cif python3 build.py -o /tmp/cif-archives
	$(MAKE) archives/cross-post

archives/cross-pre:
	docker build -f Dockerfile.cross --tag cross-cif .
	docker run -d -it --name cross-cif cross-cif

archives/cross-post:
	docker cp cross-cif:/tmp/cif-archives/. .
	docker stop cross-cif
	docker rm cross-cif
	docker rmi cross-cif

docker:
	docker build --tag cif .
	docker image prune --force --filter label=stage=builder

docker/clean:
	-docker stop cif
	-docker stop cross-cif
	-docker rm cif
	-docker rm cross-cif
	-docker rmi cif
	-docker rmi cross-cif
