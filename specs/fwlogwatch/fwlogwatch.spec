# $Id: fwlogwatch.spec,v 1.49 2003/06/23 13:42:44 bw Exp $

# Authority: dag
# Upstream: Boris Wesslowski <boris@wesslowski.com>

Summary: Firewall log analyzer, report generator and realtime response agent.
Name: fwlogwatch
Version: 0.9.3
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://cert.uni-stuttgart.de/projects/fwlogwatch/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.kyb.uni-stuttgart.de/boris/sw/fwlogwatch-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: flex

%description
fwlogwatch produces Linux ipchains, Linux netfilter/iptables,
Solaris/BSD/Irix/HP-UX ipfilter, Cisco IOS, Cisco PIX, NetScreen,
Windows XP firewall, Elsa Lancom router and Snort IDS log summary reports
in plain text and HTML form and has a lot of options to analyze and display
relevant patterns. It can produce customizable incident reports and send
them to abuse contacts at offending sites or CERTs. Finally, it can also
run as daemon (with web interface) doing realtime log monitoring and
reporting anomalies or starting attack countermeasures.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|/etc|\$(sysconfdir)|g;
		s|/usr/local|\$(prefix)|g;
		s|/usr|\$(prefix)|g;
	' Makefile
%{__perl} -pi.orig -e '
		s|/usr/local/sbin|\%{_sbindir}|g;
		s|/usr/local|%{_prefix}|g;
	' fwlogwatch.config main.h contrib/*

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
### FIXME: Create directories as Makefile doesn't take care of this.
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_initrddir} \
			%{buildroot}%{_mandir}/man8/ \
			%{buildroot}%{_datadir}/locale/{de,pt_BR,sv,zh_CN,zh_TW}/LC_MESSAGES
%makeinstall install-config install-i18n install-rhinit
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS README
%doc contrib/fwlogsummary.cgi contrib/fwlogsummary_small.cgi
%doc contrib/fwlogwatch.php
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/fwlogwatch.config
%config(noreplace) %{_sysconfdir}/fwlogwatch.template
%config(noreplace) %{_initrddir}/fwlogwatch
%{_sbindir}/f*

%changelog
* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Initial package. (using DAR)
