# $Id$

# Authority: dag
# Upstream: Wilmer van der Gaast <lintux@lintux.cx>

Summary: An IRC to other chat networks gateway.
Name: bitlbee
Version: 0.84
Release: 0
License: GPL
Group: System Environment/Daemons
URL: http://www.lintux.cx/bitlbee.html

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.lintux.cx/downloads/bitlbee-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
An IRC to other chat networks gateway. This program can be used
as an IRC server which forwards everything you say to people on
other chat networks like MSN/ICQ/Jabber.

%prep
%setup

%{__cat} <<EOF >%{name}.xinet
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
	--config="%{_localstatedir}/lib/biblbee"
%{__make} %{?_smp_mflags}
### FIXME: Documentation needs old sgmltools tool, deprecated.
#%{__make} -C doc

%install
%{__rm} -rf %{buildroot}
### FIXME: makeinstall-phase doesn't use autotool dirs and wants to change ownerships.
#makeinstall
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_datadir}/bitlbee/ \
			%{buildroot}%{_mandir}/man8/ \
			%{buildroot}%{_sysconfdir}/xinetd.d \
			%{buildroot}%{_localstatedir}/lib/bitlbee
%{__install} -m0755 bitlbee %{buildroot}%{_sbindir}
%{__install} -m0644 help.txt %{buildroot}%{_datadir}/bitlbee/
%{__install} -m0644 doc/*.8 %{buildroot}%{_mandir}/man8/
%{__install} -m0644 %{name}.xinet %{buildroot}%{_sysconfdir}/xinetd.d/bitlbee

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING help.txt doc/AUTHORS doc/CHANGES doc/CREDITS doc/FAQ doc/README doc/TODO doc/*.sgml utils/
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/xinetd.d/*
%{_sbindir}/*
%{_datadir}/bitlbee/
%attr(0700, daemon, root) %{_localstatedir}/lib/bitlbee/

%changelog
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
