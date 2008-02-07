# $Id$
# Authority: dag

Summary: Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Name: aircrack-ng
Version: 0.9.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.aircrack-ng.org/

Source: http://download.aircrack-ng.org/aircrack-ng-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an
enhanced/reborn version of aircrack. It consists of

  airodump-ng (an 802.11 packet capture program),
  aireplay-ng (an 802.11 packetinjection program),
  aircrack (static WEP and WPA-PSK cracking),
  airdecap-ng (decrypts WEP/WPA capture files)

and some tools to handle capture files (merge, convert,etc.).

%prep
%setup

chmod a+x evalrev

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	destdir="%{buildroot}" \
	prefix="%{_prefix}" \
	mandir="%{_mandir}/man1"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README patches/ test/
%doc %{_mandir}/man1/aircrack-ng.1*
%doc %{_mandir}/man1/airdecap-ng.1*
%doc %{_mandir}/man1/airmon-ng.1*
%doc %{_mandir}/man1/aireplay-ng.1*
%doc %{_mandir}/man1/airodump-ng.1*
%doc %{_mandir}/man1/airtun-ng.1*
%doc %{_mandir}/man1/ivstools.1*
%doc %{_mandir}/man1/kstats.1*
%doc %{_mandir}/man1/makeivs.1*
%doc %{_mandir}/man1/packetforge-ng.1*
%{_bindir}/aircrack-ng
%{_bindir}/airdecap-ng
%{_bindir}/ivstools
%{_bindir}/kstats
%{_bindir}/makeivs
%{_bindir}/packetforge-ng
%{_sbindir}/airmon-ng
%{_sbindir}/aireplay-ng
%{_sbindir}/airodump-ng
%{_sbindir}/airtun-ng

%changelog
* Thu Feb 07 2008 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Wed Jun 27 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 0.9-1
- Updated to release 0.9.

* Thu Apr 26 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Sun Jan 21 2007 Dag Wieers <dag@wieers.com> - 0.7-1
- Updated to release 0.7.

* Mon Oct 02 2006 Dag Wieers <dag@wieers.com> - 0.6.2-1
- Updated to release 0.6.2.

* Tue Aug 29 2006 Dag Wieers <dag@wieers.com> - 0.6.1-1
- Updated to release 0.6.1.

* Tue Jun 27 2006 Dag Wieers <dag@wieers.com> - 0.6-1
- Updated to release 0.6.

* Fri May 05 2006 Dag Wieers <dag@wieers.com> - 0.5-1
- Updated to release 0.5.

* Tue Apr 25 2006 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Initial package. (using DAR)
