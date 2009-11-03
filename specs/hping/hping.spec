# $Id$
# Authority: dag

%define real_version 2.0.0-rc3

Summary: Command-line oriented TCP/IP packet assembler/analyzer
Name: hping
Version: 2.0.0
Release: 1.rc3.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.hping.org/

Source: http://www.hping.org/hping%{real_version}.tar.gz
Patch0: hping-2.0.0-x86_64.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: hping2 <= %{version}-%{release}

%description
hping is a command-line oriented TCP/IP packet assembler/analyzer.
The interface is inspired to the ping(8) unix command, but hping
isn't only able to send ICMP echo requests. It supports TCP, UDP,
ICMP and RAW-IP protocols, has a traceroute mode, the ability to
send files between a covered channel, and many other features.

%prep
%setup -n %{name}2-rc3
%patch0 -p0

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 hping2 %{buildroot}%{_sbindir}/hping2
%{__ln_s} -f hping2 %{buildroot}%{_sbindir}/hping
%{__install} -Dp -m0755 docs/hping2.8 %{buildroot}%{_mandir}/man8/hping2.8
%{__ln_s} -f hping2.8 %{buildroot}%{_mandir}/man8/hping.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES COPYING KNOWN-BUGS NEWS README TODO docs/*.txt
%doc %{_mandir}/man8/hping.8*
%doc %{_mandir}/man8/hping2.8*
%{_sbindir}/hping
%{_sbindir}/hping2

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-1.rc3.2
- Rebuild for Fedora Core 5.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 2.0.0-1.rc3
- Added patch for x86_64.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 2.0.0-0.rc3
- Updated to release 2.0.0-rc3.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0.rc2
- Updated to release 2.0.0-rc2.

* Sat Sep 28 2002 Dag Wieers <dag@wieers.com> - 2.0.0-rc1
- Initial package.
