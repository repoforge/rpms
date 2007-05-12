# $Id$
# Authority: dag

%define _libdir /%{_lib}

Summary: PAM module that uses failed login count to lock system
Name: pam_shield
Version: 0.9.1
Release: 1
License: GPL
Group: Applications/System
URL: http://www.ka.sara.nl/home/walter/pam_shield/

Source: http://www.ka.sara.nl/home/walter/pam_shield/pam_shield-%{version}.tar.gz
Patch: pam_shield-0.9.1-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pam-devel
Requires: pam

%description
pam_shield is a PAM module that uses iptables to lock out script kiddies
that probe your computer for open logins and/or easy guessable passwords.
pam_shield is meant as an aid to protect public computers on the open internet.

%prep
%setup -n %{name}
%patch0 -p0

%build
%{__make} CFLAGS="%{optflags} -fPIC"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" libdir="%{_libdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc INSTALL GPL README
%config(noreplace) %{_sysconfdir}/cron.daily/pam-shield
%config(noreplace) %{_sysconfdir}/security/shield.conf
%dir %{_libdir}/security/
%{_libdir}/security/pam_shield.so
%{_sbindir}/shield-purge
%{_sbindir}/shield-trigger.sh

%changelog
* Sat May 12 2007 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Sun Jan 14 2007 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Initial package. (using DAR)
