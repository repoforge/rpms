# $Id$
# Authority: dag
# Upstream: 

Summary: Reliable 802.11 (wireless) sniffer and WEP key cracker
Name: aircrack
Version: 1.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.cr0.net:8040/code/network/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cr0.net:8040/code/network/aircrack-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildRequires: 

%description
Reliable 802.11 (wireless) sniffer and WEP key cracker

%prep
%setup

%{__perl} -pi.orig -e 's|-Os -W -Wall|%{optflags}|' Makefile

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 aircrack %{buildroot}%{_bindir}/aircrack
%{__install} -D -m0755 airodump %{buildroot}%{_bindir}/airodump
%{__install} -D -m0755 airunwep %{buildroot}%{_bindir}/airunwep

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README*
%{_bindir}/aircrack
%{_bindir}/airodump
%{_bindir}/airunwep

%changelog
* Fri Jul 30 2004 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)
