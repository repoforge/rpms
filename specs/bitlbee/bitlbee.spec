# $Id$
# Authority: dag
# Upstream: Wilmer van der Gaast <lintux@lintux.cx>

Summary: IRC to other chat networks gateway
Name: bitlbee
Version: 0.90
Release: 2.a
License: GPL
Group: System Environment/Daemons
URL: http://www.bitlbee.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://get.bitlbee.org/src/bitlbee-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Bitlbee is an IRC to other chat networks gateway. bitlbee can be used as
an IRC server which forwards everything you say to people on other chat
networks like MSN/ICQ/Jabber.

%prep
%setup

%{__cat} <<EOF >bitlbee.xinet
# default: off
# description: Bitlbee is an IRC gateway to other networks.

service ircd
{
	disable		= yes
	socket_type	= stream
	protocol	= tcp
	wait		= no
	user		= daemon
	server		= %{_sbindir}/bitlbee
	port		= 6667
	log_on_failure	+= USERID
}
EOF

%build
./configure \
	--prefix="%{_prefix}" \
	--bindir="%{_sbindir}" \
	--etcdir="%{_sysconfdir}/bitlbee" \
	--mandir="%{_mandir}" \
	--datadir="%{_datadir}/bitlbee" \
	--config="%{_localstatedir}/lib/bitlbee"
%{__make} %{?_smp_mflags}
### FIXME: Documentation needs old sgmltools tool, deprecated.
#%{__make} -C doc

%install
%{__rm} -rf %{buildroot}
### FIXME: makeinstall-phase doesn't use autotool dirs and wants to change ownerships.
#makeinstall
%{__install} -D -m0755 bitlbee %{buildroot}%{_sbindir}/bitlbee
%{__install} -D -m0644 help.txt %{buildroot}%{_datadir}/bitlbee/help.txt
%{__install} -D -m0644 bitlbee.xinet %{buildroot}%{_sysconfdir}/xinetd.d/bitlbee

%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__install} -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/bitlbee/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING bitlbee.conf help.txt motd.txt doc/AUTHORS doc/CHANGES doc/CREDITS
%doc doc/FAQ doc/INSTALL doc/README doc/TODO doc/*.xml utils/
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/xinetd.d/*
%{_sbindir}/*
%{_datadir}/bitlbee/

%defattr(-, daemon, root, 0700)
%{_localstatedir}/lib/bitlbee/

%changelog
* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 0.90-2.a
- Updated to release 0.90a.

* Sat May 29 2004 Dag Wieers <dag@wieers.com> - 0.90-1
- Updated to release 0.90.

* Thu Apr 08 2004 Dag Wieers <dag@wieers.com> - 0.85-2
- Fixed typo in config configure option. (Len Trigg)

* Sun Mar 14 2004 Dag Wieers <dag@wieers.com> - 0.85-1
- Updated to release 0.85.

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.84-0
- Updated to release 0.84.

* Wed Dec 31 2003 Dag Wieers <dag@wieers.com> - 0.83-0
- Updated to release 0.83.

* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 0.80-0
- Updated to release 0.80.

* Wed Jun 11 2003 Dag Wieers <dag@wieers.com> - 0.74-0.a
- Updated to release 0.74a.

* Mon Jun 09 2003 Dag Wieers <dag@wieers.com> - 0.73-2
- Fixed bitlbee.xinet to use ircd/tcp.
- Added --datadir to configure.

* Sun Jun 08 2003 Dag Wieers <dag@wieers.com> - 0.73-0
- Initial package. (using DAR)
