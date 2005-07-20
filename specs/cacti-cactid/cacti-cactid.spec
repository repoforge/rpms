# $Id$
# Authority: dag
# Upstream: <cacti-user$lists,sf,net>

%{?dist: %{expand: %%define %dist 1}}
%{?rh7:%define _without_net_snmp 1}
%{?el2:%define _without_net_snmp 1}
%{?rh6:%define _without_net_snmp 1}

Summary: Fast c-based poller for the cacti graphing solution
Name: cacti-cactid
Version: 0.8.6d
Release: 2
License: GPL
Group: Applications/System
URL: http://www.cacti.net/

Source: http://www.cacti.net/downloads/cactid/cacti-cactid-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel, openssl-devel

%{!?_without_net_snmp:BuildRequires: net-snmp-devel, net-snmp-utils}
%{?_without_net_snmp:BuildRequires: ucd-snmp-devel, ucd-snmp-utils}

Requires: cacti

%description
Cactid is a supplemental poller for Cacti that makes use of pthreads
to achieve excellent performance.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' configure

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 cactid %{buildroot}%{_bindir}/cactid
%{__install} -D -m0600 -p cactid.conf %{buildroot}%{_sysconfdir}/cactid.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG COPYING INSTALL NEWS README
%attr(0600, cacti, cacti) %config(noreplace) %{_sysconfdir}/cactid.conf
%{_bindir}/cactid

%changelog
* Thu May 19 2005 Matthias Saou <http://freshrpms.net/> 0.8.6d-2
- Make the config file mode 0600 (it contains the mysql db password) and owned
  by the cacti user (he executes the cron job).
- Add missing openssl-devel build requirement (at least on RHEL4).

* Mon Apr 04 2005 Dag Wieers <dag@wieers.com> - 0.8.6d-1
- Initial package. (using DAR)

