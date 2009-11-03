# $Id$

# Authority: dries
# Upstream:

# sqlite3 not yet added

Summary: Faciliates the use of SQL commands in shell scripts
Name: shellsql
Version: 0.7.3
Release: 1.2%{?dist}
License: GPL
Group: Applications/Databases
URL: http://www.edlsystems.com/shellsql/

Source: ftp://ftp.edlsystems.com/shellsql/shellsql-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: postgresql-devel, mysql-devel, unixODBC-devel, zlib-devel
BuildRequires: openssl-devel

%description
ShellSQL is a suite of programs designed to enable LINUX/UNIX shell scripts
to connect to SQL engines and execute SQL queries and commands in a simple
way enabling intergration with the rest of the script.

%prep
%setup -n shellsql-0.7

%build
%{__perl} -pi -e 's|^BINDIR=.*|BINDIR=%{buildroot}%{_bindir}|g;' install.sh
./install.sh postgres mysql odbc tools

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
./install.sh postgres mysql odbc tools

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS INSTALL README TODO doc/*
%{_bindir}/shmysql
%{_bindir}/shodbc
%{_bindir}/shpostgres
%{_bindir}/shsql
%{_bindir}/shsqlend
%{_bindir}/shsqlesc
%{_bindir}/shsqlline
%{_bindir}/shsqlstart

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1.2
- Rebuild for Fedora Core 5.

* Fri Jun 25 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.3-1
- Update to release 0.7.3.

* Tue Feb 08 2005 Dries Verachtert <dries@ulyssis.org> - 0.7.1
- Initial package.
