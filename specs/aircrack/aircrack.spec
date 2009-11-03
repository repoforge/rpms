# $Id$
# Authority: dag
# Upstream: Christophe Devine <c,devine$cr0,net>

Summary: Reliable 802.11 (wireless) sniffer and WEP key cracker
Name: aircrack
Version: 2.41
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.cr0.net:8040/code/network/

Source: http://www.cr0.net:8040/code/network/aircrack-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Reliable 802.11 (wireless) sniffer and WEP key cracker

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__rm} -f %{buildroot}%{_bindir}/hopper.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README* linux/patch/*.patch linux/kismet.conf~ airmon.sh
#%{_bindir}/802ether
%{_bindir}/aircrack
%{_bindir}/airdecap
%{_bindir}/aireplay
%{_bindir}/airmon.sh
%{_bindir}/airodump
%{_bindir}/arpforge
%{_bindir}/mergeivs
%{_bindir}/pcap2ivs

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.41-1.2
- Rebuild for Fedora Core 5.

* Sat Nov 26 2005 Dag Wieers <dag@wieers.com> - 2.41-1
- Updated to release 2.41.

* Thu Aug 18 2005 Dag Wieers <dag@wieers.com> - 2.23-1
- Updated to release 2.23.

* Mon Aug 05 2005 Dag Wieers <dag@wieers.com> - 2.22-1
- Updated to release 2.22.

* Thu Aug 04 2005 Dag Wieers <dag@wieers.com> - 2.2-1
- Updated to release 2.2.

* Fri Oct 01 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.

* Sat Sep 25 2004 Dag Wieers <dag@wieers.com> - 2.0.2-1
- Updated to release 2.0.2.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.0.1-1
- Updated to release 2.0.1.

* Fri Sep 03 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Updated to release 2.0.

* Thu Aug 26 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Updated to release 1.4.

* Fri Aug 20 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Wed Aug 11 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
