# $Id$

# Authority: dag
# Upstream: Marco Valleri <crwm@freemail.it>
# Upstream: Alberto Ornaghi <alor@users.sourceforge.net>

%define real_version 0.6.b

Summary: Multipurpose sniffer/interceptor/logger for switched LAN
Name: ettercap
Version: 0.6.9
Release: 0.b
License: GPL
Group: Applications/Internet
URL: http://ettercap.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/ettercap/ettercap-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: openssl-devel, ncurses-devel, gtk2-devel

%description
Ettercap is a multipurpose sniffer/interceptor/logger for switched
LAN.  It supports active and passive dissection of many protocols
(even ciphered ones) and includes many feature for network and host
analysis.

%prep
%setup -n %{name}-%{real_version}

%build
%configure \
	--enable-devel
%{__make} %{?_smp_mflags} CFLAG="%{optflags} -I/usr/kerberos/include"

%install
%{__rm} -rf %{buildroot}
%{__make} complete_install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_datadir}/doc/ettercap/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGELOG COPYING HISTORY KNOWN-BUGS PORTINGS README* THANKS
%doc TODO* docs/development/*.txt plugins/*/*.HOWTO
%doc %{_mandir}/man?/*
%{_sbindir}/*
%{_libdir}/ettercap/
%{_datadir}/ettercap/

%changelog
* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.6.9-0.b
- Updated to release 0.6.b.

* Wed May 07 2003 Dag Wieers <dag@wieers.com> - 0.6.9-0.a
- Updated to release 0.6.a.

* Mon May 05 2003 Dag Wieers <dag@wieers.com> - 0.6.9-0
- Initial package. (using DAR)
