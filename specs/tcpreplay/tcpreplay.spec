# $Id$

# Authority: dag
# Upstream: <tcpreplay-users@lists.sf.net>

Summary: Replay captured network traffic
Name: tcpreplay
Version: 2.0.3
Release: 1
License: BSD
Group: Applications/Internet
URL: http://tcpreplay.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/tcpreplay/tcpreplay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1.0

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
%{__install} -d -m0755 %{buildroot}%{_sbindir} \
%{__install} -m0755 capinfo tcpprep tcpreplay %{buildroot}%{_sbindir}
%{__install} -D -m0644 capinfo.1 %{buildroot}%{_mandir}/man1/capinfo.1
%{__install} -D -m0644 tcpprep.1 %{buildroot}%{_mandir}/man1/tcpprep.1
%{__install} -D -m0644 tcpreplay.8 %{buildroot}%{_mandir}/man8/tcpreplay.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README tcpprep.FAQ
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 2.0.3-1
- Updated to release 2.0.3.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Sun Aug 31 2003 Dag Wieers <dag@wieers.com> - 1.4.5-0
- Updated to release 1.4.5.

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 1.4.1-0
- Updated to release 1.4.1.

* Thu May 08 2003 Dag Wieers <dag@wieers.com> - 1.4.0-0
- Updated to release 1.4.0.

* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 1.3.3-0
- Initial package. (using DAR)
