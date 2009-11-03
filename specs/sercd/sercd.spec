# $Id$
# Authority: dag
# Upstream: Janet Casey <jcasey$gnu,org>
# Upstream: <sercd$lists,lysator,liu,se>

Summary: RFC 2217-compliant serial port redirector
Name: sercd
Version: 2.3.2
Release: 1%{?dist}
License: GPL
Group: Applications/Communications
URL: http://www.lysator.liu.se/~astrand/projects/sercd/

Source: http://www.lysator.liu.se/~astrand/projects/sercd/sercd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
sercd is a RFC 2217 compliant serial port redirector. It is basedxi
on sredird. Other similiar projects are ser2net and msredird.

%prep
%setup

%{__cat} <<EOF >sercd.xinetd
# default: off
# description: RFC 2217 compliant Telnet serial port redirector
service sredir
{
	disable = yes
	type            = UNLISTED
	flags           = REUSE
	socket_type     = stream
	protocol        = tcp
	wait            = no
	user            = root
	server          = %{_sbindir}/sercd
	server_args     = 5 /dev/ttyS0 /var/lock/LCK..ttyS0
	port            = 7000
# Some versions of xinetd does not work with only_from=localhost
#	only_from       = localhost
}
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 sercd.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/sercd

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man8/sercd.8*
%config(noreplace) %{_sysconfdir}/xinetd.d/sercd
%{_sbindir}/sercd

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 2.3.2-1
- Updated to release 2.3.2.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.3.1-1.2
- Rebuild for Fedora Core 5.

* Fri Mar 18 2005 Dag Wieers <dag@wieers.com> - 2.3.1-1
- Initial package. (using DAR)
