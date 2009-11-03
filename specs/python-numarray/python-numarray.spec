# $Id$
# Authority: dries

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name numarray

Summary: Numerical Extension to Python
Name: python-numarray
Version: 1.3.3
Release: 1.2%{?dist}
License: UNKNOWN
Group: Development/Libraries
URL: http://sourceforge.net/projects/numpy

Source: http://dl.sf.net/numpy/numarray-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python, python-devel

%description
Numerical Extension to Python with subpackages.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Doc/* LICENSE.txt MANIFEST PKG-INFO README.txt
%{python_sitearch}/numarray/
%{_includedir}/python*/numarray/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3.3-1.2
- Rebuild for Fedora Core 5.

* Sat Sep 24 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.3-1
- changelog added.
