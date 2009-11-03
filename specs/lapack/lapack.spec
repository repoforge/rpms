# $Id$
# Authority: dag

Summary: LAPACK libraries for numerical linear algebra.
Name: lapack
Version: 3.1.1
Release: 1%{?dist}
License: BSD
Group: Development/Libraries
URL: http://www.netlib.org/lapack/

Source0: http://www.netlib.org/lapack/lapack-%{version}.tgz
Source2: Makefile.blas
Source3: Makefile.lapack
Source4: http://www.netlib.org/lapack/lapackqref.ps
Source5: http://www.netlib.org/blas/blasqr.ps
Patch3: lapack-3.1.1-make.inc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-gfortran
Obsoletes: lapack-man

%description
LAPACK (Linear Algebra PACKage) is a standard library for numerical
linear algebra. LAPACK provides routines for solving systems of
simultaneous linear equations, least-squares solutions of linear
systems of equations, eigenvalue problems, and singular value
problems. Associated matrix factorizations (LU, Cholesky, QR, SVD,
Schur, and generalized Schur) and related computations (i.e.,
reordering of Schur factorizations and estimating condition numbers)
are also included. LAPACK can handle dense and banded matrices, but
not general sparse matrices. Similar functionality is provided for
real and complex matrices in both single and double precision. LAPACK
is coded in Fortran77 and built with gcc.

%package devel
Summary: LAPACK development libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
LAPACK development libraries for applications that link statically.

%package -n blas
Summary: The BLAS (Basic Linear Algebra Subprograms) library.
Group: Development/Libraries
Obsoletes: lapack-blas blas-man

%description -n blas
BLAS (Basic Linear Algebra Subprograms) is a standard library which
provides a number of basic algorithms for numerical algebra. Man
pages for blas are available in the blas-man package.

%package -n blas-devel
Summary: LAPACK development libraries
Group: Development/Libraries
Requires: blas = %{version}-%{release}

%description -n blas-devel
BLAS development libraries for applications that link statically.

%prep
%setup
%setup -D -T
%patch3 -p1
%{__cp} -vf INSTALL/make.inc.gfortran make.inc
%{__cp} -vf %{SOURCE2} BLAS/SRC/Makefile
%{__cp} -vf %{SOURCE3} SRC/Makefile

%{__rm} -f man/manl/zbcon.l

%build
RPM_OPT_O_FLAGS="$(echo '%{optflags}' | sed 's|-O2|-O0|')"
export FC="gfortran"

### Build BLAS
%{__make} -C BLAS/SRC dcabs1.o FFLAGS="$RPM_OPT_O_FLAGS"
%{__make} -C BLAS/SRC static FFLAGS="%{optflags}" CFLAGS="%{optflags}"
%{__cp} -v BLAS/SRC/libblas.a .
%{__make} -C BLAS/SRC clean
%{__make} -C BLAS/SRC dcabs1.o FFLAGS="$RPM_OPT_O_FLAGS -fPIC"
%{__make} -C BLAS/SRC shared FFLAGS="%{optflags} -fPIC" CFLAGS="%{optflags} -fPIC"
%{__cp} -v BLAS/SRC/libblas.so.3.1.1 .

%{__ln_s} -f libblas.so.3.1.1 libblas.so

### Some files don't like -O2, but -Os is fine
RPM_OPT_SIZE_FLAGS="$(echo '%{optflags}' | sed 's|-O2|-Os|')"

### Build the static dlamch, dsecnd, lsame, second, slamch bits
%{__make} -C INSTALL all NOOPT="$RPM_OPT_SIZE_FLAGS" OPTS="%{optflags}"

### Build the static lapack library
%{__make} -C SRC clean static FFLAGS="%{optflags}" CFLAGS="%{optflags}"
%{__cp} -v SRC/liblapack.a .

### Build the shared dlamch, dsecnd, lsame, second, slamch bits
%{__make} -C INSTALL clean all NOOPT="$RPM_OPT_SIZE_FLAGS -fPIC" OPTS="%{optflags} -fPIC"

### Build the shared lapack library
%{__make} -C SRC clean shared FFLAGS="%{optflags} -fPIC" CFLAGS="%{optflags} -fPIC"
%{__cp} -v SRC/liblapack.so.3.1.1 .

### Build the static with pic dlamch, dsecnd, lsame, second, slamch bits
%{__make} -C INSTALL clean all NOOPT="$RPM_OPT_SIZE_FLAGS -fPIC" OPTS="%{optflags} -fPIC"

### Build the static with pic lapack library
%{__make} -C SRC clean static FFLAGS="%{optflags} -fPIC" CFLAGS="%{optflags} -fPIC"
%{__cp} -v SRC/liblapack.a ${RPM_BUILD_DIR}/%{name}-%{version}/liblapack_pic.a

%{__cp} -v %{SOURCE4} lapackqref.ps
%{__cp} -v %{SOURCE5} blasqr.ps

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/manl/

for lib in liblapack.so.3.1.1 libblas.so.3.1.1 libblas.a liblapack.a liblapack_pic.a; do
  %{__cp} -vf $lib %{buildroot}%{_libdir}/$lib
done

### These are also in the BLAS package
%{__rm} -f manpages/man/manl/lsame.l*
%{__rm} -f manpages/man/manl/xerbla.l*

#find manpages/blas/man/manl -type f -name '*.l' -printf '\%%doc %{_mandir}/manl/%f*\n' > blasmans
#find manpages/man/manl -type f -name '*.l' -printf '\%%doc %{_mandir}/manl/%f*\n' > lapackmans
find manpages/blas/man/manl -type f -name '*.l' -printf '%{_mandir}/manl/%f*\n' > blasmans
find manpages/man/manl -type f -name '*.l' -printf '%{_mandir}/manl/%f*\n' > lapackmans

%{__cp} -vf manpages/blas/man/manl/*.l %{buildroot}%{_mandir}/manl/
%{__cp} -vf manpages/man/manl/*.l %{buildroot}%{_mandir}/manl/

%{__ln_s} -f liblapack.so.3.1.1 %{buildroot}%{_libdir}/liblapack.so
%{__ln_s} -f liblapack.so.3.1.1 %{buildroot}%{_libdir}/liblapack.so.3
%{__ln_s} -f liblapack.so.3.1.1 %{buildroot}%{_libdir}/liblapack.so.3.1
%{__ln_s} -f libblas.so.3.1.1 %{buildroot}%{_libdir}/libblas.so
%{__ln_s} -f libblas.so.3.1.1 %{buildroot}%{_libdir}/libblas.so.3
%{__ln_s} -f libblas.so.3.1.1 %{buildroot}%{_libdir}/libblas.so.3.1

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%post -n blas -p /sbin/ldconfig
%postun -n blas -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f lapackmans
%defattr(-, root, root, 0755)
%doc README lapackqref.ps
%{_libdir}/liblapack.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/liblapack.so
%{_libdir}/liblapack*.a

%files -n blas -f blasmans
%defattr(-, root, root, 0755)
%doc blasqr.ps
%{_libdir}/libblas.so.*

%files -n blas-devel
%defattr(-, root, root, 0755)
%{_libdir}/libblas.so
%{_libdir}/libblas*.a

%changelog
* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Initial package. (based on Fedora)
