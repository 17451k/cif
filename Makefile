# Directories with Aspectator prerequisites, sources, objects and executables.
ASPECTATOR_PREREQUISITES = aspectator-prerequisites
ASPECTATOR_SRC_DIR = aspectator
ASPECTATOR_BUILD_DIR = aspectator-build
ASPECTATOR_BIN_DIR = aspectator-bin

# Standard directory for installation of executables.
bindir = $(prefix)/bin

.PHONY: all install test clean

# Before build install prerequisites.
all: $(ASPECTATOR_SRC_DIR)/gmp $(ASPECTATOR_SRC_DIR)/mpc $(ASPECTATOR_SRC_DIR)/mpfr
	mkdir -p $(ASPECTATOR_BUILD_DIR)
	if [ ! -f $(ASPECTATOR_BUILD_DIR)/Makefile ]; then \
	  echo "Configure Aspectator for the first time"; \
	  cd $(ASPECTATOR_BUILD_DIR); \
	  ../$(ASPECTATOR_SRC_DIR)/configure --prefix=$(shell readlink -f $(ASPECTATOR_BIN_DIR)) --enable-languages=c --disable-nls; \
	fi
	@echo "Begin to (re)build Aspectator"
	make -C $(ASPECTATOR_BUILD_DIR)
	make -C $(ASPECTATOR_BUILD_DIR) install

$(ASPECTATOR_SRC_DIR)/gmp: $(ASPECTATOR_PREREQUISITES)/gmp.tar.bz2 $(ASPECTATOR_PREREQUISITES)/gmp-nodoc.patch
	@echo "Remove GMP source code from '$(ASPECTATOR_SRC_DIR)'"
	rm -rf $@
	@echo "Extract GMP source code to '$(ASPECTATOR_SRC_DIR)'"
	tar -xamf $(ASPECTATOR_PREREQUISITES)/gmp.tar.bz2 -C $(ASPECTATOR_SRC_DIR)
	@echo "Patch GMP source code to disable documentation building"
	patch -p1 -d $@ < $(ASPECTATOR_PREREQUISITES)/gmp-nodoc.patch

$(ASPECTATOR_SRC_DIR)/mpc: $(ASPECTATOR_PREREQUISITES)/mpc.tar.bz2 $(ASPECTATOR_PREREQUISITES)/mpc-nodoc.patch
	@echo "Remove MPC source code from '$(ASPECTATOR_SRC_DIR)'"
	rm -rf $@
	@echo "Extract MPC source code to '$(ASPECTATOR_SRC_DIR)'"
	tar -xamf $(ASPECTATOR_PREREQUISITES)/mpc.tar.bz2 -C $(ASPECTATOR_SRC_DIR)
	@echo "Patch MPC source code to disable documentation building"
	patch -p1 -d $@ < $(ASPECTATOR_PREREQUISITES)/mpc-nodoc.patch

$(ASPECTATOR_SRC_DIR)/mpfr: $(ASPECTATOR_PREREQUISITES)/mpfr.tar.bz2
	@echo "Remove MPFR source code from '$(ASPECTATOR_SRC_DIR)'"
	rm -rf $@
	@echo "Extract MPFR source code to '$(ASPECTATOR_SRC_DIR)'"
	tar -xamf $(ASPECTATOR_PREREQUISITES)/mpfr.tar.bz2 -C $(ASPECTATOR_SRC_DIR)

# Before installation check prefix and perform build.
install: check_prefix all
	mkdir -p $(bindir)
	@echo "Install CIF to '$(bindir)'"
	cp -u cif $(bindir)
	@echo "Install Aspectator to '$(bindir)'"
	cp -ru $(ASPECTATOR_BIN_DIR) $(bindir)
	@echo "Create symlinks for CIF and Aspectator binaries for convinience"
	ln -sf $(bindir)/cif $(bindir)/compiler
	ln -sf $(bindir)/$(ASPECTATOR_BIN_DIR)/bin/gcc $(bindir)/aspectator

check_prefix:
	@echo "Check that prefix where tools to be installed is specified"
	@case "$(prefix)" in \
	  /*) prefix_abs=1 ;; \
	  *) prefix_abs=0 ;; \
	esac; \
	if [ -z "$(prefix)" -o $$prefix_abs -eq 0 ]; then \
	  echo "For installation you should specify prefix: 'prefix=install_dir_abs make install'!"; \
	  exit 1; \
	else echo "C Instrumentation Framework and Aspectator will be installed to '$(prefix)'"; \
	fi

test:
	@echo "CIF hasn't tests at the moment" 

# Remove all directories created during Aspectator build.
clean:
	rm -rf $(ASPECTATOR_SRC_DIR)/gmp $(ASPECTATOR_SRC_DIR)/mpfr $(ASPECTATOR_SRC_DIR)/mpc $(ASPECTATOR_BUILD_DIR) $(ASPECTATOR_BIN_DIR)