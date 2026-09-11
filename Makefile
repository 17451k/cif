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
	    --disable-libsanitizer --disable-multilib --disable-nls --disable-plugin \
	    --enable-checking=release --with-pkgversion=$(ASPECTATOR_VERSION) \
	    --with-bugurl="https://github.com/17451k/cif/issues" \
	    $(CONFIGURE_ARGS_MACOS) $(ASPECTATOR_CONFIGURE_OPTS); \
	fi
	@echo "Begin to (re)build Aspectator"
	@if [[ -d $(UBUNTU_LIB) && ! -z LIBRARY_PATH ]]; then export LIBRARY_PATH=$(UBUNTU_LIB); fi
	$(MAKE) BOOT_CFLAGS='-O2' -C build
	@echo "Install C Instrumentation Framework and Aspecator locally"
	$(MAKE) DESTDIR=${LOCAL_DESTDIR} build/install

cif:
	mkdir -p build
	# You need to add option "-g" below to get a debug version of CIF.
	g++ -D CIF_VERSION=\"$(CIF_VERSION)\" -Wall -Werror -O2 --std=c++17 cif.cpp -o build/cif

build/install: uninstall install-keep-previous-instances

# Install Aspectator (GCC) within dedicated directory to simplify its uninstall.
install-keep-previous-instances:
	$(MAKE) DESTDIR="$(DESTDIR)/cif" -C build install-strip
	cp build/cif "$(DESTDIR)/cif/bin/cif"
	strip "$(DESTDIR)/cif/bin/cif"
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
	cd tests && pytest

clean:
	rm -rf build build-debug

debug:
	mkdir -p build-debug
	@if [ ! -f build-debug/Makefile ]; then \
	  cd build-debug; \
	  MAKEINFO=missing ../aspectator/configure --enable-languages=c --disable-multilib --disable-nls \
	  --enable-checking=release $(CONFIGURE_ARGS_MACOS); \
	fi
	$(MAKE) -C build-debug STAGE1_CXXFLAGS="-g -O0" all-stage1
