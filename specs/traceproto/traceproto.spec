# $Id$
# Authority: dag

Summary: Flexible multiprotocol traceroute
Name: traceproto
Version: 1.1.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://traceproto.sourceforge.net/

Source: http://dl.sf.net/traceproto/traceproto-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1.0, libpcap
Requires: libnet >= 1.1.0, libpcap

%description
Traceproto is an enhanced traceroute-like tool that can use protocols
as chosen by the user. Traceproto is not limited to UDP/ICMP so can be
used to test / bypass firewalls and packet filters and check if ports
are open.

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
%defattr (-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man8/traceproto.8*
%{_bindir}/traceproto

%changelog
* Fri Mar 04 2005 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Initial package. (using DAR)
