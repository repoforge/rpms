# $Id$
# Authority: dag
# Upstream: <pysqlite-devel$lists,sf,net>

%define real_name pysqlite

Summary: Python bindings for sqlite
Name: python-sqlite
Version: 0.5.0
Release: 1
License: GPL
Group: Development/Libraries
URL: http://pysqlite.sourceforge.net/

Source: http://dl.sf.net/pysqlite/pysqlite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python-devel, sqlite-devel, python

%description
This packages allows you to use sqlite with python.
sqlite is a simple database engine.

%prep
%setup -n %{real_name}
%{__rm} -f doc/rest/.*swp

%build

%install
%{__rm} -rf %{buildroot}
python ./setup.py install \
	--prefix="%{buildroot}/%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README doc/ examples/
%{_libdir}/python*/site-packages/*

%changelog
* Sat May 01 2004 Dag Wieers <dag@wieers.com> - 0.5.0-1
- Initial package. (using DAR)
