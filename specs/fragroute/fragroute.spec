# $Id$
# Authority: dag
# Upstream: Dug Song <dugsong$monkey,org>


%{!?dtag:%define _with_libpcapdevel 1}
%{?fc7:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Intercepts, modifies, and rewrites egress traffic
Name: fragroute
Version: 1.2
Release: 4%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.monkey.org/~dugsong/fragroute/

Source: http://www.monkey.org/~dugsong/fragroute/fragroute-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdnet-devel, libpcap, libevent-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
Fragroute intercepts, modifies, and rewrites egress traffic destined
for a specified host, implementing most of the attacks described in
the Secure Networks "Insertion, Evasion, and Denial of Service:
Eluding Network Intrusion Detection" paper of January 1998.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE README TODO scripts/
%doc %{_mandir}/man8/fragroute.8*
%doc %{_mandir}/man8/fragtest.8*
%config(noreplace) %{_sysconfdir}/fragroute.conf
%{_sbindir}/fragroute
%{_sbindir}/fragtest

%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 1.2-4
- Rebuild against libevent-1.1a on EL5.

* Wed Mar 07 2007 Dag Wieers <dag@wieers.com> - 1.2-3
- Rebuild against libevent-1.3b.

* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 1.2-2
- Rebuild against libevent-1.3a.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Cosmetic rebuild for Group-tag.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Initial package. (using DAR)
