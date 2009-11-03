# $Id$
# Authority: dag
# Upstream: <pysqlite-devel$lists,sf,net>

# ExcludeDist: el4

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pysqlite

Summary: Python bindings for sqlite
Name: python-sqlite
Version: 2.3.3
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://pysqlite.org/

Source: http://initd.org/pub/software/pysqlite/releases/2.3/%{version}/pysqlite-%{version}.tar.gz
#Source: http://dl.sf.net/pysqlite/pysqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel >= 2.3, sqlite-devel

%description
This packages allows you to use sqlite with python.
sqlite is a simple database engine.

%prep
%setup -n %{real_name}-%{version}
%{__rm} -f doc/rest/.*swp

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE doc/
%{python_sitearch}/pysqlite2/
%ghost %{python_sitearch}/pysqlite2/*.pyo
%exclude %{_prefix}/pysqlite2-doc/

%changelog
* Wed Feb 14 2007 Dag Wieers <dag@wieers.com> - 2.3.3-1
- Updated to release 2.3.3.

* Fri Feb 10 2006 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Updated to release 2.0.6.

* Mon Jan 09 2006 Dag Wieers <dag@wieers.com> - 2.0.5-1
- Updated to release 2.0.5.

* Sat Jun 25 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1
- Updated to release 2.0.3.

* Sat May 01 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Initial package. (using DAR)
