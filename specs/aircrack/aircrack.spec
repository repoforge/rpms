# $Id$
# Authority: dag
# Upstream: Christophe Devine <c,devine$cr0,net>

Summary: Reliable 802.11 (wireless) sniffer and WEP key cracker
Name: aircrack
Version: 2.0.1
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
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog *.patch *.sh *.txt
%{_bindir}/802ether
%{_bindir}/aircrack
%{_bindir}/aireplay
%{_bindir}/airodump

%changelog
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
