# $Id$
# Authority: dag
# Upstream: Christophe Devine <c,devine$cr0,net>

Summary: Reliable 802.11 (wireless) sniffer and WEP key cracker
Name: aircrack
Version: 1.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.cr0.net:8040/code/network/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cr0.net:8040/code/network/aircrack-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Reliable 802.11 (wireless) sniffer and WEP key cracker

%prep
%setup

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -D_GNU_SOURCE"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 802ether %{buildroot}%{_bindir}/802ether
%{__install} -D -m0755 aircrack %{buildroot}%{_bindir}/aircrack
%{__install} -D -m0755 aireplay %{buildroot}%{_bindir}/aireplay
%{__install} -D -m0755 airodump %{buildroot}%{_bindir}/airodump

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog *.patch *.txt
%{_bindir}/802ether
%{_bindir}/aircrack
%{_bindir}/aireplay
%{_bindir}/airodump

%changelog
* Fri Aug 20 2004 Dag Wieers <dag@wieers.com> - 1.3-1
- Updated to release 1.3.

* Wed Aug 18 2004 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Updated to release 1.2.1.

* Wed Aug 11 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
