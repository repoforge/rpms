# $Id$
# Authority: dag
# Upstream: Simon Horman <horms$verge,net,au>

Summary: Switches in redundant servers using arp spoofing
Name: fake
Version: 1.1.8
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.vergenet.net/linux/fake/

Source: http://www.vergenet.net/linux/fake/download/%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
Fake is a utility that enables the IP address be taken over
by bringing up a second interface on the host machine and
using gratuitous arp. Designed to switch in backup servers
on a LAN.

%prep
%setup

%build
%{__make} %{?_smp_mflags} patch
%{__make} %{?_smp_mflags} CFLAGS="%{optflags} -s"

%install
%{__rm} -rf %{buildroot}
%makeinstall ROOT_DIR="%{buildroot}" MAN8_DIR="%{buildroot}%{_mandir}/man8"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING docs/*.txt heartbeat/fake instance_config/*.cfg README
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/fake/
%{_sbindir}/*
%{_libdir}/heartbeat/fake

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.8-1.2
- Rebuild for Fedora Core 5.

* Wed Apr 30 2003 Dag Wieers <dag@wieers.com> - 1.1.8-0
- Initial package. (using DAR)
