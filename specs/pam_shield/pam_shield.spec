# $Id$
# Authority: dag
# Upstream: Walter de Jong <walter$heiho,net>

%define _libdir /%{_lib}

Summary: PAM module that uses failed login count to lock system
Name: pam_shield
Version: 0.9.4
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.heiho.net/pam_shield/

Source: http://www.heiho.net/pam_shield/pam_shield-%{version}.tar.gz
Patch0: pam_shield-0.9.4-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gdbm-devel
BuildRequires: pam-devel
Requires: pam

%description
pam_shield is a PAM module that uses iptables to lock out script kiddies
that probe your computer for open logins and/or easy guessable passwords.
pam_shield is meant as an aid to protect public computers on the open internet.

%prep
%setup
%patch0 -p1

%build
%{__make} CFLAGS="%{optflags} -fPIC"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" libdir="%{_libdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog CREDITS GPL INSTALL README shield-trigger-iptables
%config(noreplace) %{_sysconfdir}/cron.daily/pam-shield
%config(noreplace) %{_sysconfdir}/security/shield.conf
%dir %{_libdir}/security/
%{_libdir}/security/pam_shield.so
%{_sbindir}/shield-purge
%{_sbindir}/shield-trigger
%dir %{_localstatedir}/lib/pam_shield/

%changelog
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
