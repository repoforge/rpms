# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Python binding for the Samba Trivial Database
Name: python-tdb
Version: 0.0.6
Release: 2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://clarens.sourceforge.net/

Source: http://dl.sf.net/tdb/python-tdb-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tdb, tdb-devel, python >= 2.0
Requires: tdb, python >= 2.0

%description
A Python binding for TDB. TDB is a Trivial Database. In concept, it is very
much like GDBM, and BSD's DB except that it allows multiple simultaneous
writers and uses locking internally to keep writers from trampling on each
other. TDB is also extremely small.

This binding exposes a low-level TDB interface class, as well as a dictionary
(mapping) class.

%prep
%setup

%build
%{__python} setup.py --build

%install
%{__rm} -rf %{buildroot}
#%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%{__install} -Dp -m0755 build/*/tdb.so %{buildroot}%{python_sitearch}/tdb.so

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc test.py
%{python_sitearch}/tdb.so

%changelog
* Mon Oct 09 2006 Dag Wieers <dag@wieers.com> - 0.0.6-2
- Fixed group name.

* Mon May 23 2005 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
