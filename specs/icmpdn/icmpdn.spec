# $Id$
# Authority: dag

%define _libdir /%{_lib}

Summary: ICMP host name utilities
Name: icmpdn
Version: 0.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.dolda2000.com/~fredrik/icmp-dn/

Source: http://www.dolda2000.com/~fredrik/icmp-dn/icmpdn-%version.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
icmpdn is an implementation of the RFC 1788 ICMP domain name
facilities for Linux. It includes icmpdnd, a daemon which responds to
ICMP domain name requests from other hosts, idnlookup, which requests
the domain name of another host, and nss_icmp, which is a nameswitch
module for doing reverse hostname lookups via idnlookup.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 admin/icmpdnd %{buildroot}%{_initrddir}/icmpdnd

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* NEWS README
%doc %{_mandir}/man1/idnlookup.1*
%doc %{_mandir}/man5/nss-icmp.conf.5*
%doc %{_mandir}/man7/nss-icmp.7*
%doc %{_mandir}/man8/icmpdnd.8*
%config(noreplace) %{_sysconfdir}/nss-icmp.conf
%config %{_initrddir}/icmpdnd
%{_libdir}/libnss_icmp.so
%{_libdir}/libnss_icmp.so.*
%{_sbindir}/icmpdnd

%defattr(4755, root, root, 0755)
%{_bindir}/idnlookup

%exclude %{_libdir}/libnss_icmp.la

%changelog
* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 0.3-1
- Initial package. (using DAR)
