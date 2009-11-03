# $Id$
# Authority: dag

Summary: Generate thousands of counterfeit 802.11b access points
Name: fakeap
Version: 0.3.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.blackalchemy.to/project/fakeap/

#Source: http://www.blackalchemy.to:8060/project/fakeap/download.php?name=fakeap-0.3.2.tar.gz
Source: fakeap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch
BuildRequires: perl

%description
FakeAP generates thousands of counterfeit 802.11b access points. Hide in
plain sight amongst Fake AP's cacophony of beacon frames. As part of a
honeypot or as an instrument of your site security plan, Fake AP confuses
Wardrivers, NetStumblers, Script Kiddies, and other undesirables.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 fakeap.pl %{buildroot}%{_bindir}/fakeap

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS INSTALL README lists/
%{_bindir}/fakeap

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.2-1.2
- Rebuild for Fedora Core 5.

* Mon Aug 22 2005 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Initial package. (using DAR)
