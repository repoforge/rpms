# $Id: tcpreplay.spec 2964 2005-03-08 19:22:25Z dag $
# Authority: dag
# Upstream: <tcpreplay-users$lists,sf,net>

Summary: Replay captured network traffic
Name: tcpreplay
Version: 2.3.5
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://tcpreplay.sourceforge.net/

Source: http://dl.sf.net/tcpreplay/tcpreplay-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libnet >= 1.1.1, tcpdump, libpcap

%description
Tcpreplay is a tool to replay captured network traffic.  Currently, tcpreplay
supports pcap (tcpdump) and snoop capture formats.  Also included, is tcpprep
a tool to pre-process capture files to allow increased performance under
certain conditions as well as capinfo which provides basic information about
capture files.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e 's|\@mandir\@|\$(mandir)|' Makefile.in

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
%doc README Docs/CHANGELOG Docs/CREDIT Docs/INSTALL Docs/LICENSE Docs/TODO
#%doc Docs/*.css Docs/*.html Docs/*.txt
%doc %{_mandir}/man1/capinfo.1*
%doc %{_mandir}/man1/flowreplay.1*
%doc %{_mandir}/man1/pcapmerge.1*
%doc %{_mandir}/man1/tcpprep.1*
%doc %{_mandir}/man8/tcpreplay.8*
%{_bindir}/capinfo
%{_bindir}/flowreplay
%{_bindir}/pcapmerge
%{_bindir}/tcpprep
%{_sbindir}/tcpreplay

%changelog
* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 2.3.5-1
- Updated to release 2.3.5.

* Sun Jun 05 2005 Dag Wieers <dag@wieers.com> - 2.3.4-1
- Updated to release 2.3.4.

* Fri Feb 11 2005 Dag Wieers <dag@wieers.com> - 2.3.3-1
- Updated to release 2.3.3.

* Mon Nov 08 2004 Dag Wieers <dag@wieers.com> - 2.3.2-1
- Updated to release 2.3.2.

* Mon Sep 27 2004 Dag Wieers <dag@wieers.com> - 2.3.1-1
- Updated to release 2.3.1.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Mon Jun 21 2004 Dag Wieers <dag@wieers.com> - 2.2.2-1
- Updated to release 2.2.2.

* Thu May 27 2004 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Mon May 17 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Updated to release 2.2.0.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 2.1.1-1
- Updated to release 2.1.1.

* Sat Apr 24 2004 Dag Wieers <dag@wieers.com> - 2.1.0-1
- Updated to release 2.1.0.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 2.0.3-2
- Rebuild against libnet 1.1.2.1.

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
