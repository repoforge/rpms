# $Id: $

# Authority: dries

# doesn't work
# i always get the error:
# Makefile:14: *** missing separator.  Stop.


Summary: Multiplex all your databases to one point of origin
Name: postgresql-relay
Version: 1.3
Release: 1
License: BSD
Group: Applications/Databases
URL: http://www.mavetju.org/unix/general.php

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.mavetju.org/download/postgresql-relay-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}

%description
Postgresql-relay can be used to as a single point of origin for all
your databases. Instead of having to remember (or modify in case of
changes) all the names of your databases, on which machines and on
which ports they are running, you only need to remember one machine
and the name of the database. The postgresql-relay will then forward 
the connection to the proper database on the proper port of the proper
server.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README

%changelog
* Sun Mar 21 2004 Dries Verachtert <dries@ulyssis.org> 1.3-1
- Initial package
