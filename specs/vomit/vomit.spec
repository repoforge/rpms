# $Id$
# Authority: dag
# Upstream: Niels Provos <provos$citi,umich,edu>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{?fc7:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Decodes VoIP audio from tcpdump captures
Name: vomit
Version: 0.2c
Release: 4%{?dist}
License: GPL
Group: Applications/Internet
URL: http://vomit.xtdnet.nl/

Source: http://vomit.xtdnet.nl/vomit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdnet-devel, libevent-devel, libpcap, automake >= 1.4
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

Requires: libdnet, libevent, libpcap

%description
vomit (Voice Over Misconfigured Internet Telephones) converts a Cisco IP
phone conversation into a wave file that can be played with ordinary
sound players. Vomit requires a tcpdump output file. Vomit is not a VoIP
sniffer also it could be but the naming is probably related to H.323.

%prep
%setup

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man1/vomit.1*
%{_bindir}/vomit

%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 0.2c-4
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 0.2c-3
- Rebuild against libevent-1.3b.

* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 0.2c-2
- Rebuild against libevent-1.3a.

* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 0.2c-1
- Initial package. (using DAR)
