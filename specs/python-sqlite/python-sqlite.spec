# $Id$
# Authority: dag
# Upstream: <pysqlite-devel$lists,sf,net>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name pysqlite

Summary: Python bindings for sqlite
Name: python-sqlite
Version: 2.0.3
Release: 1
License: GPL
Group: Development/Libraries
URL: http://initd.org/tracker/pysqlite

Source: http://initd.org/pub/software/pysqlite/releases/2.0/%{version}/pysqlite-%{version}.tar.gz
#Source: http://dl.sf.net/pysqlite/pysqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, sqlite-devel, python

%description
This packages allows you to use sqlite with python.
sqlite is a simple database engine.

%prep
%setup -n %{real_name}-%{version}
%{__rm} -f doc/rest/.*swp

%build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
	--root="%{buildroot}" \
	--prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE doc/ 
%{python_sitearch}/*

%changelog
* Sat Jun 25 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1
- Update to release 2.0.3.

* Sat May 01 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Initial package. (using DAR)
