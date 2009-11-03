# $Id$
# Authority: dries
# Upstream: Edwin Groothuis <edwin$mavetju,org>

Summary: Multiplex all your databases to one point of origin
Name: postgresql-relay
Version: 1.3
Release: 2.2%{?dist}
License: BSD
Group: Applications/Databases
URL: http://www.mavetju.org/unix/general.php

Source: http://www.mavetju.org/download/postgresql-relay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__cat} <<'EOF' >Makefile
prefix = /usr
bindir = $(prefix)/bin
datadir = $(prefix)/share
mandir = $(datadir)/man

CC = gcc
CFLAGS=-Wall -g

DESTDIR =

all: postgresql-relay postgresql-relay.8

postgresql-relay: postgresql-relay.o
	$(CC) $(AFLAGS) $(LFLAGS) -o $@ $? $(MYLDFLAGS)

postgresql-relay.o: postgresql-relay.c
	$(CC) $(MYCFLAGS) $(AFLAGS) $(CFLAGS) -o $@ -c $?

postgresql-relay.8: postgresql-relay.pod
	pod2man --release="March 22, 2004" --date="March 22, 2004" --center="General Commands Manual" --section=8 $? > $@

install: postgresql-relay postgresql-relay.8
	%{__install} -Dp -m0755 postgresql-relay $(DESTDIR)$(bindir)/postgresql-relay
	%{__install} -Dp -m0644 postgresql-relay.8 $(DESTDIR)$(mandir)/man8/postgresql-relay.8

clean:
	rm -f postgresql-relay *.o postgresql-relay.8
EOF

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES
%doc %{_mandir}/man?/*
%{_bindir}/postgresql-relay

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-2.2
- Rebuild for Fedora Core 5.

* Sat Jun 05 2004 Dag Wieers <dag@wieers.com> - 1.3-2
- Cosmetic cleanup.

* Sun Mar 21 2004 Dries Verachtert <dries@ulyssis.org> 1.3-1
- Initial package
