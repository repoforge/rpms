# $Id$
# Authority: dag
# Upstream: Walter de Jong <walter$heiho,net>

%define real_name pam-shield
%define _libdir /%{_lib}

Summary: PAM module that uses failed login count to lock system
Name: pam_shield
Version: 0.9.6
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.heiho.net/pam_shield/

#Source: http://www.heiho.net/pam_shield/pam_shield-%{version}.tar.gz
Source: https://github.com/downloads/jtniehof/pam_shield/pam-shield-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gdbm-devel
BuildRequires: pam-devel
Requires: pam

%description
pam_shield is a PAM module that uses iptables to lock out script kiddies
that probe your computer for open logins and/or easy guessable passwords.
pam_shield is meant as an aid to protect public computers on the open internet.

%prep
%setup -n %{real_name}-%{version}

%build
%configure
#%{__make} CFLAGS="%{optflags} -fPIC"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" moduledir="%{_libdir}/security"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING CREDITS INSTALL README
%doc %{_mandir}/man5/shield.conf.5*
%doc %{_mandir}/man8/shield-purge.8*
%doc %{_mandir}/man8/shield-trigger.8*
%doc %{_mandir}/man8/shield-trigger-iptables.8*
%doc %{_mandir}/man8/shield-trigger-ufw.8*
%config(noreplace) %{_sysconfdir}/cron.daily/pam_shield
%config(noreplace) %{_sysconfdir}/security/shield.conf
%{_datadir}/pam-configs/pam_shield
%dir %{_libdir}/security/
%{_libdir}/security/pam_shield.so
%{_sbindir}/shield-purge
%{_sbindir}/shield-trigger
%{_sbindir}/shield-trigger-iptables
%{_sbindir}/shield-trigger-ufw
%dir %{_localstatedir}/lib/pam_shield/

%changelog
* Tue Jul 24 2012 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Thu Jan 13 2011 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Sat Sep 04 2010 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Wed Sep 01 2010 Dag Wieers <dag@wieers.com> - 0.9.3-2
- Changed logging from AUTH to AUTHPRIV.
- Included shield-trigger-iptables.

* Wed Aug 25 2010 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Jul 10 2007 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Added missing BuildRequires gdbm-devel. (Leo Eraly)

* Mon Jul 02 2007 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Mon May 14 2007 Dag Wieers <dag@wieers.com> - 0.9.1-2
- Fix the name of the trigger script referenced in shield.conf.

* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Sun Jan 14 2007 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Initial package. (using DAR)
