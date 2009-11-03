# $Id$
# Authority: dag


%{!?dtag:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Scan for wireless access points and save captured traffic
Name: ssidsniff
Version: 0.36
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.bastard.net/~kos/wifi/

Source: http://www.bastard.net/~kos/wifi/ssidsniff-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
ssidsniff is a nifty tool to use when looking to discover access points
and save captured traffic. ssidsniff supports Cisco Aironet and random
prism2 based cards.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/ssidsniff
%{_bindir}/pcapset
%{_bindir}/nldump
%{_bindir}/pcapdump

%changelog
* Sat Jul 12 2003 Dag Wieers <dag@wieers.com> - 0.36-0
- Initial package. (using DAR)
