# $Id$

# Authority: dag
# Upstream: The ZoneCheck Team <zonecheck$nic,fr>

Summary: Perform consistency checks on DNS zones
Name: zonecheck
Version: 2.0.4
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.zonecheck.fr/

Source: http://www.zonecheck.fr/download/src/zonecheck-%{version}.tgz
#Source: http://savannah.nongnu.org/download/zonecheck/zonecheck-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: ruby >= 1.8, ruby-libs
Requires: ruby >= 1.8, ruby-libs

%description
ZoneCheck is intended to help solve DNS misconfigurations or
inconsistencies that are usually revealed by an increase in
the latency of the application. The DNS is a critical resource
for every network application, so it is quite important to
ensure that a zone or domain name is correctly configured in
the DNS.

%prep
%setup -n %{name}

%build

%install
%{__rm} -rf %{buildroot}
#makeinstall
ruby ./installer.rb common cli cgi \
	-DPREFIX="%{_prefix}" \
	-DETCDIR="%{_sysconfdir}" \
	-DLIBEXEC="%{_libdir}" \
	-DMANDIR="%{_mandir}" \
        -DETCDIST="" \
	-DCHROOT="%{buildroot}" \
	-DRUBY="%{_bindir}/ruby"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING CREDITS doc/html GPL HISTORY README TODO
%doc %{_mandir}/man?/*
%dir %{_sysconfdir}/zonecheck/
%config %{_sysconfdir}/zonecheck/rootservers
%config %{_sysconfdir}/zonecheck/*.profile
%config(noreplace) %{_sysconfdir}/zonecheck/zc.conf
%{_bindir}/*
%{_libdir}/zonecheck/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1.2
- Rebuild for Fedora Core 5.

* Tue Jan 03 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.4-1
- Updated to release 2.0.4.
- RUBY parameter added so installer.rb doesn't search for the interpreter,
  thanks to Michael Mansour and Wil Cooley.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> -2.0.3-0
- Updated to release 2.0.3.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Updated to release 2.0.2.

* Thu Oct 30 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0.b9
- Updated to release 2.0.0b9.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 2.0.0-0.b7
- Initial package. (using DAR)
