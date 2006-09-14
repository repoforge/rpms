# $Id$
# Authority: dag
# Upstream: <code$kryo,se>

Summary: Tunnel IPv4 data through a DNS server
Name: iodine
Version: 0.3.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://code.kryo.se/iodine/

Source: http://code.kryo.se/iodine/iodine-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
iodine lets you tunnel IPv4 data through a DNS server. This can be useful
in different situations where internet access is firewalled, but DNS
queries are allowed. 

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 iodine %{buildroot}%{_bindir}/iodine
%{__install} -Dp -m0755 iodined %{buildroot}%{_bindir}/iodined

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG README
%{_bindir}/iodine
%{_bindir}/iodined

%changelog
* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.

* Thu Aug 03 2006 Dag Wieers <dag@wieers.com> - 0.3.1-1
- Initial package. (using DAR)
