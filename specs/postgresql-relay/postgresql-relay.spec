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
echo '
prefix=/usr
CC=gcc
CFLAGS=-Wall -g
all: postgresql-relay postgresql-relay.8

postgresql-relay: postgresql-relay.o
	${CC} ${AFLAGS} ${LFLAGS} -o $@ $? ${MYLDFLAGS}

postgresql-relay.o: postgresql-relay.c
	${CC} ${MYCFLAGS} ${AFLAGS} ${CFLAGS} -o $@ -c $?

postgresql-relay.8: postgresql-relay.pod
	pod2man --release="March 22, 2004" --date="March 22, 2004" --center="General Commands Manual" --section=8 $? > $@

install: postgresql-relay postgresql-relay.8
	install -u bin -g bin -m 755 postgresql-relay ${prefix}/bin
	install -u bin -g bin -m 644 postgresql-relay.8 ${prefix}/share/man/man8

clean:
	rm -f postgresql-relay *.o postgresql-relay.8

' > Makefile

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
