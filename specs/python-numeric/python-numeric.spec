# $Id$
# Authority: dag

### EL6 ships with numpy-1.3.0-6.2.el6
### EL5 ships with python-numeric-23.7-2.2.2
# ExclusiveDist: el2 el3 el4

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name Numeric

Summary: Numerical Extension to Python
Name: python-numeric
Version: 23.1
Release: 0.2%{?dist}
License: UNKNOWN
Group: Development/Libraries
URL: http://www.pfdubois.com/numpy/

Source: http://dl.sf.net/numpy/Numeric-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python, python-devel

Provides: numpy = %{version}-%{release}
Provides: Numeric = %{version}-%{release}
Obsoletes: numpy <= %{version}-%{release}
Obsoletes: Numeric <= %{version}-%{release}

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
%doc Demo/
%{python_sitearch}/Numeric/
%{python_sitearch}/Numeric.pth
%{_includedir}/python*/Numeric/

%changelog
* Sat Sep 24 2005 Dries Verachtert <dries@ulyssis.org> - 23.1-1
- changelog added.
