# $Id$
# Authority: dag
# Upstream: Marco Valleri <crwm$freemail,it>
# Upstream: Alberto Ornaghi <alor$users,sourceforge,net>

Summary: Multipurpose sniffer/interceptor/logger for switched LAN
Name: ettercap
Version: 0.7.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://ettercap.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ettercap/ettercap-NG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel, ncurses-devel, gtk2-devel, gcc-c++, libpcap

%description
Ettercap is a multipurpose sniffer/interceptor/logger for switched
LAN.  It supports active and passive dissection of many protocols
(even ciphered ones) and includes many feature for network and host
analysis.

%prep
%setup -n %{name}-NG-%{version}

%build
%configure \
	--enable-devel
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
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/etter.conf
%{_bindir}/ettercap
%{_bindir}/etterfilter
%{_bindir}/etterlog
%{_libdir}/ettercap/
%{_datadir}/ettercap/

%changelog
* Tue Jul 06 2004 Dag Wieers <dag@wieers.com> - 0.7.0-1
- Updated to release 0.7.0.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.6.9-0.b
- Updated to release 0.6.b.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 0.6.9-0.a
- Updated to release 0.6.a.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 0.6.9-0
- Initial package. (using DAR)
