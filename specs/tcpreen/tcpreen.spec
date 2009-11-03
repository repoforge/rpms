# $Id$
# Authority: dag
# Upstream: Rémi Denis-Courmont <rdenis$simphalempin,com>
# Upstream: <tcpreen-devel$lists,sourceforge,net>

Summary: TCP/IP re-engineering and monitoring program
Name: tcpreen
Version: 1.4.4
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.remlab.net/tcpreen/

Source: http://www.remlab.net/files/tcpreen/stable/tcpreen-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
A tool to monitor and analyse data transmitted between a client and a server
via a TCP connection. This tool focuses on the data stream (software layer),
not on the lower level transmission protocol as packet sniffers do.

TCPreen supports both TCP/IPv4 and TCP/IPv6 for data transport.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_mandir}/man1/tcpreen.1*
%{_bindir}/tcpreen

%changelog
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 1.4.4-1
- Updated to release 1.4.4.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 1.4.3-1
- Updated to release 1.4.3.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Updated to release 1.4.1.

* Mon Jun 28 2004 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Updated to release 1.4.0.

* Wed Mar 03 2004 Dag Wieers <dag@wieers.com> - 1.3.7-1
- Updated to release 1.3.7.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 1.3.6-0
- Updated to release 1.3.6.

* Mon Oct 06 2003 Dag Wieers <dag@wieers.com> - 1.3.5-0
- Initial package. (using DAR)
