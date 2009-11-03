# $Id$
# Authority: dag

Summary: tool to replay captured network traffic
Name: tcpreplay
Version: 1.3.3
Release: 0%{?dist}
License: BSD
Group: Applications/Internet
URL: http://tcpreplay.sourceforge.net/

Source: http://dl.sf.net/tcpreplay/tcpreplay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet

%description
Tcpreplay is a tool to replay captured network traffic.  Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats.  Also included, is tcpprep
a tool to pre-process capture files to allow increased performance under
certain conditions as well as capinfo which provides basic information about
capture files.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 capinfo %{buildroot}%{_sbindir}/capinfo
%{__install} -Dp -m0755 tcpprep %{buildroot}%{_sbindir}/tcpprep
%{__install} -Dp -m0755 tcpreplay %{buildroot}%{_sbindir}/tcpreplay
%{__install} -Dp -m0644 capinfo.1 %{buildroot}%{_mandir}/man1/capinfo.1
%{__install} -Dp -m0644 tcpprep.1 %{buildroot}%{_mandir}/man1/tcpprep.1
%{__install} -Dp -m0644 tcpreplay.8 %{buildroot}%{_mandir}/man8/tcpreplay.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README tcpprep.FAQ
%doc %{_mandir}/man1/capinfo.1*
%doc %{_mandir}/man1/tcpprep.1*
%doc %{_mandir}/man8/tcpreplay.8*
%{_sbindir}/capinfo
%{_sbindir}/tcpprep
%{_sbindir}/tcpreplay

%changelog
* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 1.3.3-0
- Initial package. (using DAR)
