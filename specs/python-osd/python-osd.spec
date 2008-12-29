# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pyosd

Summary: Python wrapper for libosd
Name: python-osd
Version: 0.2.14
Release: 1
License: GPL
Group: Development/Libraries
URL: http://repose.cx/pyosd/

Source: pyosd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
BuildRequires: xosd-devel
Provides: pyosd = %{version}-%{release}
Obsoletes: pyosd <= %{version}-%{release}

%description 
PyOSD is a python module for displaying text on your X display, much like the 
"On Screen Displays" used on TVs and some monitors.

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
%doc AUTHORS ChangeLog COPYING README*
%{python_sitearch}/_pyosd.so
%{python_sitearch}/pyosd/*.py
%{python_sitearch}/pyosd/*.pyc
%ghost %{python_sitearch}/pyosd/*.pyo

%changelog
* Wed May 28 2008 Dag Wieers <dag@wieers.com> - 0.2.14-1
- Initial package. (using DAR)
