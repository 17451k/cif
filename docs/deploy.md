# Deployment

You can download archives with CIF binaries prepared in advance from artifacts attached to
[GitHub Releases](https://github.com/17451k/cif/releases).
Also, you can build CIF yourself from scratch according to instructions below.
Section [Building debug version of Aspectator](development.md#debug_deploy) describes various variants of development builds.

## Build dependencies

To build CIF you need to install the following packages:

* make
* gcc
* g++
* flex
* bison

## Build and install

First you need to download archives with the source code of prerequisites needed by GCC (*gmp*, *mpfr*, *mpc* and
*isl*):

```console
$ cd aspectator
$ ./contrib/download_prerequisites
```

Then return back to the root of the repository and execute *make*:

```console
$ cd ..
$ make
```

You can use option *-jN* for *make* to significantly speed up building, e.g.:

```console
$ make -j16
```

In addition, you can speed up building further by disabling bootstrap:

```console
$ ASPECTATOR_CONFIGURE_OPTS="--disable-bootstrap" make -j16
```

After successful build you can install CIF, e.g.:

```console
$ sudo make install
```

You can specify the alternative directory where CIF will be installed, e.g.:

```console
$ DESTDIR=/home/user/cif make install
```

## Automatic testing

You can run the following command for automatic testing of CIF:

```console
$ make test
```

It requires Python 3 and pytest to be installed.

## Uninstall

You can uninstall CIF by running the following command:

```console
$ sudo make uninstall
```

If CIF was installed into an alternative directory with the *DESTDIR* option then you need to use it again:

```console
$ DESTDIR=/home/user/cif make uninstall
```

## Cleanup

You should run the following command to remove build directories:

```console
$ make clean
```
