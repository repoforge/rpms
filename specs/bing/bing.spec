# $Id$
# Authority: dag
# Upstream: Pierre Beyssac <pb$fasterix,freenix,fr>

Summary: Measures bandwidth between two point-to-point connections
Name: bing
Version: 1.0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://web.cnam.fr/reseau/bing.html

Source: ftp://ftp.ibp.fr/pub/networking/bing-%{version}.tar.gz
Patch: bing-1.0.4.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Bing determines the real (raw, as opposed to available or average)
throughput on a link by measuring ICMP echo requests roundtrip times
for different packet sizes for each end of the link.

%prep
%setup
%patch

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 bing %{buildroot}%{_bindir}/bing
%{__install} -Dp -m0644 bing.8 %{buildroot}%{_mandir}/man8/bing.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc bing.ps ChangeLog README
%doc %{_mandir}/man8/bing.8*
%{_bindir}/bing

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 16 2004 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Initial package. (using DAR)

