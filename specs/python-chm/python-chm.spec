# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pychm

Summary: Python package to handle CHM files
Name: python-chm
Version: 0.8.4
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://gnochm.sourceforge.net/

Source: http://dl.sf.net/gnochm/pychm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, chmlib-devel, python-devel
Requires: python >= 2.2, chmlib

%description
The python chm package provides three modules, chm, chmlib and extra,
which provide access to the API implemented by the C library chmlib
and some additional classes and functions. They are used to access
MS-ITSS encoded files - Compressed Html Help files (.chm).

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
%doc COPYING NEWS README
%{python_sitearch}/chm/

%changelog
* Sat Nov 11 2006 Dag Wieers <dag@wieers.com> - 0.8.4-1
- Updated to release 0.8.4.

* Fri May 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.3-1
- Updated to release 0.8.3.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 0.8.2-1
- Updated to release 0.8.2.

* Mon Nov 08 2004 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Updated to release 0.8.1.

* Tue Feb 24 2004 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
