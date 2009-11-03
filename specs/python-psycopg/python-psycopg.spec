# $Id$
# Authority: dries

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name psycopg

Summary: PostgreSQL database adapter for Python
Name: python-psycopg
Version: 1.1.21
Release: 2%{?dist}
License: GPL/ZPL
Group: Development/Libraries
URL: http://initd.org/tracker/psycopg

Source: http://initd.org/pub/software/psycopg/psycopg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, python-devel, postgresql-devel, mx

%description
psycopg is a PostgreSQL database adapter for the Python programming
language. Its main advantages are that it supports the full Python
DBAPI 2.0 and it is thread safe at level 2. It was designed for heavily
multi-threaded applications that create and destroy lots of cursors and
make a conspicuous number of concurrent INSERTs or UPDATEs. The psycopg
distribution includes ZPsycopgDA, a Zope Database Adapter.

%prep
%setup -n %{real_name}-%{version}
# configure tries to read the version of postgresql from the pg_config.h file.. which doesn't contain 
# this info anymore.
%{__perl} -pi -e "s|/pg_config.h|/pg_config_%{_arch}.h|g;" configure

%build
%configure --with-postgres-includes="%{_includedir}/pgsql/server/"
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{python_sitearch}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog INSTALL doc/*
%{python_sitearch}/psycopg*

%changelog
* Sat Aug 13 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.21-2
- Reversed to psycopg1, made a second spec file for psycopg2.

* Thu Aug 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1
- Updated to release 2.0.4.

* Mon Jul 31 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.3-1
- Updated to release 2.0.3.

* Fri Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.21-1
- Updated to release 1.1.21.

* Tue Sep 13 2005 Dries Verachtert <dries$ulyssis.org> - 1.1.20-1
- Initial package.
