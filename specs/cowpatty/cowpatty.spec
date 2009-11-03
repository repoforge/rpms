# $Id$
# Authority: dag


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Brute-force dictionary attack against WPA-PSK
Name: cowpatty
Version: 2.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://new.remote-exploit.org/index.php/Codes_main

Source: http://www.remote-exploit.org/images/5/5a/Cowpatty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, libpcap
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
coWPAtty is designed to audit the pre-shared key (PSK) selection for WPA
networks based on the TKIP protocol. Supply a libpcap file that includes the
TKIP four-way handshake to mount an offline dictionary attack with a supplied
wordlist.

%prep
%setup -n %{name}

%build
%{__make} %{?_smp_mflags} all love

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 cowpatty %{buildroot}%{_bindir}/cowpatty

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING FAQ README TODO WISHLIST dict
%{_bindir}/cowpatty

%changelog
* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
