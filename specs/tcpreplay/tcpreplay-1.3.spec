# Authority: dag
# Distcc: 0

Summary: A tool to replay captured network traffic.
Name: tcpreplay
Version: 1.3.3
Release: 0
License: BSD
Group: Applications/Internet
URL: http://tcpreplay.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/home-made/apt/

Source: http://dl.sf.net/tcpreplay/tcpreplay-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

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
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_sbindir} \
			%{buildroot}%{_mandir}/man1 \
			%{buildroot}%{_mandir}/man8
%{__install} -m0755 capinfo tcpprep %{buildroot}%{_sbindir}/
%{__install} -m0755 tcpreplay %{buildroot}%{_sbindir}/
%{__install} -m0644 capinfo.1 tcpprep.1 %{buildroot}%{_mandir}/man1
%{__install} -m0644 tcpreplay.8 %{buildroot}%{_mandir}/man8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README tcpprep.FAQ
%doc %{_mandir}/man?/*
%{_sbindir}/*

%changelog
* Sun May 04 2003 Dag Wieers <dag@wieers.com> - 1.3.3-0
- Initial package. (using DAR)
