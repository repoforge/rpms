# $Id$

# Authority: dag

%define real_version 2.0.0-rc2

Summary: Command-line oriented TCP/IP packet assembler/analyzer
Name: hping
Version: 2.0.0
Release: 0.rc2
License: GPL
Group: Applications/Internet
URL: http://www.hping.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.hping.org/hping%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
hping is a command-line oriented TCP/IP packet assembler/analyzer.
The interface is inspired to the ping(8) unix command, but hping
isn't only able to send ICMP echo requests. It supports TCP, UDP,
ICMP and RAW-IP protocols, has a traceroute mode, the ability to
send files between a covered channel, and many other features.

%prep
%setup -n %{name}2-rc2

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man8
%{__install} -m0755 hping2 %{buildroot}%{_sbindir}
%{__ln_s} -f hping2 %{buildroot}%{_sbindir}/hping
%{__install} -m0755 docs/hping2.8 %{buildroot}%{_mandir}/man8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING KNOWN-BUGS NEWS README TODO docs/*.txt
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0.rc2
- Updated to release 2.0.0-rc2.

* Sat Sep 28 2002 Dag Wieers <dag@wieers.com> - 2.0.0-rc1
- Initial package.
