# $Id$
# Authority: matthias


Summary: Make a chroot.
Name: mach
Version: 0.4.3.1
Release: 2
Group: Applications/System
License: GPL
URL: http://thomas.apestaart.org/projects/mach/
Source: http://thomas.apestaart.org/download/mach/%{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-root
Requires: rpm-python, apt, sed, cpio
BuildRequires:	python >= 2.0.0

%description
mach makes a chroot.
Using apt-get and a suid binary, it manages to install clean chroot
environments based on the original packages for that distribution.

The clean root can be used to run jail roots, to create image files, or
to build clean packages.

%prep
%setup

%build
%configure

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m 775 %{buildroot}%{_localstatedir}/lib/mach
%{__install} -d -m 775 %{buildroot}%{_localstatedir}/lib/mach/states
%{__install} -d -m 775 %{buildroot}%{_localstatedir}/lib/mach/roots
%{__install} -d -m 775 %{buildroot}%{_localstatedir}/cache/mach/packages
%{__install} -d -m 775 %{buildroot}%{_localstatedir}/cache/mach/archives

%clean
%{__rm} -rf %{buildroot}

%pre
# create user and group mach
/usr/sbin/useradd -c "mach user" \
    -r -m mach -d %{_localstatedir}/lib/mach >/dev/null 2>&1 || :

%preun
if [ $1 -eq 0 ]; then
    # Last removal
    # Be a good boy and clean out the dirs we filled with junk
    rm -rf %{_localstatedir}/lib/mach/states/*
    rm -rf %{_localstatedir}/lib/mach/roots/*
    rm -rf %{_localstatedir}/cache/mach/* >/dev/null 2>&1 || :
    rmdir %{_localstatedir}/lib/mach/states >/dev/null 2>&1 || :
    rmdir %{_localstatedir}/lib/mach/roots >/dev/null 2>&1 || :
    rmdir %{_localstatedir}/cache/mach >/dev/null 2>&1 || :
    rm -rf %{_localstatedir}/tmp/mach >/dev/null 2>&1 || :
fi

%postun
if [ $1 -eq 0 ]; then
    # Last removal
    userdel mach >/dev/null 2>&1 || : 
    groupdel mach >/dev/null 2>&1 || :
fi

%files
%defattr(-, root, root, -)
%doc ChangeLog COPYING README AUTHORS BUGS TODO FORGETMENOT RELEASE
%dir %{_sysconfdir}/mach
%config %{_sysconfdir}/mach/conf
%config %{_sysconfdir}/mach/dist
%{_bindir}/mach
%attr(04750, root, mach) %{_sbindir}/mach-helper
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/states
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/roots
%attr(-, mach, mach) %dir %{_localstatedir}/cache/mach/packages
%attr(-, mach, mach) %dir %{_localstatedir}/cache/mach/archives

%changelog
* Mon Mar  1 2004 Matthias Saou <http://freshrpms.net> - 0.4.3.1-1.fr
- Update to 0.4.3.1.

* Wed Dec 17 2003 Matthias Saou <http://freshrpms.net> - 0.4.3-1.fr
- Cosmetic spec file changes.
- Update to 0.4.3.

* Wed Sep 17 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- add Requires: cpio
- change home dir to /var/lib/mach

* Mon Sep 08 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- 0.4.0-0.fdr.1: first public release.

* Sat Aug 16 2003 Ville Skyttä <ville.skytta at iki.fi>
- Add COPYING to docs.

* Wed May 21 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- added mach-helper

* Wed Apr 30 2003 Thomas Vander Stichele <thomas at apestaart dot org>
- initial creation

