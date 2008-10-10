# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define python_version %(python2 -c 'import sys; print sys.version[:3]')

Summary: Python module for working with utmp
Name: python-utmp
Version: 0.7
Release: 2
License: GPL
Group: Development/Libraries
URL: http://melkor.dnp.fmph.uniba.sk/~garabik/python-utmp/

Source: http://melkor.dnp.fmph.uniba.sk/~garabik/python-utmp/python-utmp_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel
Requires: python >= %{python_version}

%description
This package provides 3 python modules to access utmp and wtmp
records.  utmpaccess is lowlevel module wrapping glibc functions,
UTMPCONST provides useful constants, and utmp is module build on top
of utmpaccess module, providing object oriented interface.

%prep
%setup

%build
%{__make} -f Makefile.glibc \
    PYTHONVER="%{python_version}" \
    PYTHONDIR="%{python_sitearch}"

%install
%{__rm} -rf %{buildroot}
%makeinstall -f Makefile.glibc \
    PYTHONVER="%{python_version}" \
    PYTHONDIR="%{buildroot}%{python_sitearch}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README TODO examples/*
%{python_sitearch}/UTMPCONST.py
%ghost %{python_sitearch}/UTMPCONST.pyc
%ghost %{python_sitearch}/UTMPCONST.pyo
%{python_sitearch}/utmp.py
%ghost %{python_sitearch}/utmp.pyc
%ghost %{python_sitearch}/utmp.pyo
%{python_sitearch}/utmpaccessmodule.so

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.7-2
- Fixed group name.

* Wed Jan 05 2005 Dag Wieers <dag@wieers.com> - 0.7-1
- Initial package. (using DAR)
