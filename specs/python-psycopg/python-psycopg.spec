# $Id$
# Authority: dries

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define real_name psycopg

Summary: PostgreSQL database adapter for Python
Name: python-psycopg
Version: 1.1.21
Release: 1
License: GPL/ZPL
Group: Development/Libraries
URL: http://initd.org/projects/psycopg1

Source: http://initd.org/pub/software/psycopg/psycopg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.2, python-devel, postgresql-devel

%description
psycopg is a PostgreSQL database adapter for the Python programming 
language. Its main advantages are that it supports the full Python 
DBAPI 2.0 and it is thread safe at level 2. It was designed for heavily 
multi-threaded applications that create and destroy lots of cursors and 
make a conspicuous number of concurrent INSERTs or UPDATEs. The psycopg 
distribution includes ZPsycopgDA, a Zope Database Adapter.

%prep
%setup -n %{real_name}-%{version}

%build
./configure --help
%configure --with-postgres-includes=%{_includedir}/pgsql/
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{python_sitearch}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS FAQ INSTALL NEWS README RELEASE* SUCCESS TODO VERSION* doc/examples doc/python*.txt
%{python_sitearch}/psycopg*

%changelog
* Fri Jan 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.21-1
- Updated to release 1.1.21.

* Tue Sep 13 2005 Dries Verachtert <dries$ulyssis.org> - 1.1.20-1
- Initial package.
