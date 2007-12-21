# $Id$
# Authority: dag

Summary: Packet generator
Name: ipsorc
Version: 1.7.5
Release: 0.2
License: GPL
Group: Applications/Internet
URL: http://www.informony.com/ipsorcery.html

Source: http://www.legions.org/~phric/ipsorc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel

%description
A console and gtk based packet generator allowing the custom building of IP, TCP, UDP, ICMP, IGMP, RIP, OSPF packets.

%prep
%setup

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" con
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" gtk

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ipmagic %{buildroot}%{_sbindir}/ipmagic
%{__install} -Dp -m0755 magic %{buildroot}%{_sbindir}/magic

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS changelog GPL HOWTO README
%{_sbindir}/ipmagic
%{_sbindir}/magic

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.7.5-0.2
- Rebuild for Fedora Core 5.

* Thu May 01 2003 Dag Wieers <dag@wieers.com> - 1.7.5-0
- Initial package. (using DAR)
