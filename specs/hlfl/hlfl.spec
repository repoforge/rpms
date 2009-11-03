# $Id$
# Authority: dag
# Upstream: Arnaud Launay <asl$launay,org>

%define _datadir %{_prefix}/share/hlfl

Summary: High-Level Firewall Language
Name: hlfl
Version: 0.60.1
Release: 0.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://www.hlfl.org/

Source: http://www.hlfl.org/hlfl/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
HLFL stands for "High-Level Firewall Language". It translates your
high-level language firewalling rules into usable rules for IPChains,
NetFilter, IPFilter, Cisco, and many others.

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
%doc doc/*.hlfl doc/RoadMap doc/syntax.txt doc/TODO
%doc %{_mandir}/man1/hlfl.1*
%{_bindir}/hlfl
%{_datadir}/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.60.1-0.2
- Rebuild for Fedora Core 5.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
