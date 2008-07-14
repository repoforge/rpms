# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name numpy

Summary: Fast multidimensional array facility for Python
Name: python-numpy
Version: 1.0.1
Release: 1
License: BSD
Group: Development/Libraries
URL: http://numeric.scipy.org/

Source: http://dl.sf.net/numpy/numpy-%{version}.tar.gz
Patch0: numpy-1.0.1-f2py.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: blas-devel
BuildRequires: gcc-gfortran
BuildRequires: lapack-devel
BuildRequires: python-devel
#BuildRequires: python-setuptools

Provides: f2py
Obsoletes: f2py <= 2.45.241_1927
Provides: numpy = %{version}-%{release}
Obsoletes: numpy <= %{version}-%{release}

%description
NumPy is a general-purpose array-processing package designed to
efficiently manipulate large multi-dimensional arrays of arbitrary
records without sacrificing too much speed for small multi-dimensional
arrays.  NumPy is built on the Numeric code base and adds features
introduced by numarray as well as an extended C-API and the ability to
create arrays of arbitrary type.

There are also basic facilities for discrete fourier transform,
basic linear algebra and random number generation. Also included in
this package is a version of f2py that works properly with NumPy.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1 -b .f2py

%build
env ATLAS="%{_libdir}" FFTW="%{_libdir}" BLAS="%{_libdir}" \
LAPACK="%{_libdir}" CFLAGS="%{optflags}" \
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
env ATLAS="%{_libdir}" FFTW="%{_libdir}" BLAS="%{_libdir}" \
LAPACK="%{_libdir}" CFLAGS="%{optflags}" \
%{__python} setup.py install -O1 --root="%{buildroot}" --prefix="%{_prefix}"
#%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

### Clean up buildroot
%{__mv} -v %{buildroot}%{python_sitearch}/numpy/f2py/docs/ rpm-doc/

%{__install} -dp -m0755 %{buildroot}%{_mandir}/man1/
%{__mv} -v %{buildroot}/%{python_sitearch}/numpy/f2py/f2py.1 %{buildroot}%{_mandir}/man1/numpy.1

%{__ln_s} -f f2py %{buildroot}%{_bindir}/f2py.numpy

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.txt rpm-doc/* numpy/doc/
%doc %{_mandir}/man1/numpy.1*
%{_bindir}/f2py
%{_bindir}/f2py.numpy
%{python_sitearch}/numpy/
%ghost %{python_sitearch}/numpy/*.pyo
%ghost %{python_sitearch}/numpy/*/*.pyo
%ghost %{python_sitearch}/numpy/*/*/*.pyo
%ghost %{python_sitearch}/numpy/*/*/*/*.pyo
%ghost %{python_sitearch}/numpy/*/*/*/*/*.pyo

%changelog
* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 1.0.3.1-1
- Initial package. (based on Fedora)
