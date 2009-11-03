# $Id$
# Authority: dag
# Upstream: Marco Valleri <crwm$freemail,it>
# Upstream: Alberto Ornaghi <alor$users,sourceforge,net>

%{?dtag: %{expand: %%define %dtag 1}}

%{!?dtag:%define _with_libpcapdevel 1}
%{!?dtag:%define _with_libtoolltdl 1}

%{?el5:%define _with_libpcapdevel 1}
%{?el5:%define _with_libtoolltdl 1}

%{?fc6:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libtoolltdl 1}

%{?fc5:%define _with_libtoolltdl 1}
%{?fc4:%define _with_libtoolltdl 1}

Summary: Multipurpose sniffer/interceptor/logger for switched LAN
Name: ettercap
Version: 0.7.3
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://ettercap.sourceforge.net/

Source: http://dl.sf.net/ettercap/ettercap-NG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, ncurses-devel, gtk2-devel, gcc-c++, libpcap >= 14:0.8.1
Buildrequires: libnet
%{?_with_libtoolltdl:BuildRequires: libtool-ltdl-devel}
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Ettercap is a multipurpose sniffer/interceptor/logger for switched
LAN.  It supports active and passive dissection of many protocols
(even ciphered ones) and includes many feature for network and host
analysis.

%prep
%setup -n %{name}-NG-%{version}

%build
%configure \
	--enable-devel \
	--enable-plugins
%{__make} %{?_smp_mflags}
#CFLAG="%{optflags} -I/usr/kerberos/include"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG INSTALL LICENSE README* THANKS TODO* doc/*
%doc %{_mandir}/man?/etter*
%config(noreplace) %{_sysconfdir}/etter.conf
%{_bindir}/ettercap
%{_bindir}/etterfilter
%{_bindir}/etterlog
%{_libdir}/ettercap/
%{_datadir}/ettercap/

%changelog
* Mon Nov 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.3-2
- libtool-ltdl-devel added as buildrequirement, thanks to Ahmed Kamal.

* Sun May 29 2005 Dag Wieers <dag@wieers.com> - 0.7.3-1
- Updated to release 0.7.3.

* Wed Dec 22 2004 Dag Wieers <dag@wieers.com> - 0.7.2-1
- Updated to release 0.7.2.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Updated to release 0.7.1.

* Tue Jul 06 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.6.9-0.b
- Updated to release 0.6.b.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 0.6.9-0.a
- Updated to release 0.6.a.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 0.6.9-0
- Initial package. (using DAR)
