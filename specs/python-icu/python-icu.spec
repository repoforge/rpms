# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name PyICU

Summary: PyICU is a python extension wrapping IBM's ICU C++ API
Name: pyicu
Version: 0.8.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Base
URL: http://pyicu.osafoundation.org/

Source: http://pypi.python.org/packages/source/P/PyICU/PyICU-%{version}.tar.gz
Patch0: python-icu-0.8.1-python23.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: libicu-devel >= 3.6
BuildRequires: python-devel >= 2.3
Requires: python >= 2.3

Obsoletes: PyICU <= %{version}-%{release}
Provides: PyICU = %{version}-%{release}
Obsoletes: pyicu <= %{version}-%{release}
Provides: pyicu = %{version}-%{release}

%description
PyICU is a python extension wrapping IBM's ICU C++ API.

%prep
%setup -n %{real_name}-%{version}
%patch0 -p0

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS LICENSE README
%{python_sitearch}/_PyICU.so
%{python_sitearch}/PyICU.py
%{python_sitearch}/PyICU.pyc
%{python_sitearch}/PyICU.pyo

%changelog
* Mon Dec  8 2008 Filipe Brandenburger <filbranden@gmail.com> - 0.8.1-1
- Initial package.
