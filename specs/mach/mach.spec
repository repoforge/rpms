# $Id$
# Authority: matthias
# Upstream: Thomas Vander Stichele <thomas$apestaart,org>

# ExcludeDist: rh7

%{!?builduser:  %define builduser  machbuild}
%{!?buildgroup: %define buildgroup machbuild}
# Override with --define 'python python2'
%{!?python:     %define python     python}

Summary: Make A CHroot
Name: mach
Version: 0.4.6
Release: 2
Group: Applications/System
License: GPL
URL: http://thomas.apestaart.org/projects/mach/
Source: http://thomas.apestaart.org/download/mach/mach-%{version}.tar.bz2
Source1: fedora-2-x86_64
Source2: fedora-3-i386
Source3: fedora-3-x86_64
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: %{python} >= 2.0.0
Requires: rpm-python, apt, sed, cpio, python >= 2.0

%description
mach makes a chroot.
Using apt-get and a suid binary, it manages to install clean chroot
environments based on the original packages for that distribution.

The clean root can be used to run jail roots, to create image files, or
to build clean packages.


%prep
%setup


%build
%configure \
    --enable-builduser=%{builduser} \
    --enable-buildgroup=%{buildgroup}


%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m 2775 %{buildroot}%{_localstatedir}/lib/mach
%{__install} -d -m 2775 %{buildroot}%{_localstatedir}/lib/mach/states
%{__install} -d -m 2775 %{buildroot}%{_localstatedir}/lib/mach/roots
%{__install} -d -m 775 %{buildroot}%{_localstatedir}/cache/mach/packages
%{__install} -d -m 775 %{buildroot}%{_localstatedir}/cache/mach/archives

# Additionnal config files
%{__install} -m 0644 %{SOURCE1} %{SOURCE2} %{SOURCE3} \
    %{buildroot}%{_sysconfdir}/mach/dist.d/


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
    # Actually... the roots may be used later on, so better keep them
    #rm -rf %{_localstatedir}/lib/mach/states/*
    umount %{_localstatedir}/lib/mach/roots/*/proc >/dev/null 2>&1 || :
    #rm -rf %{_localstatedir}/lib/mach/roots/* >/dev/null 2>&1 || :
    rm -rf %{_localstatedir}/cache/mach/* >/dev/null 2>&1 || :
    #rmdir %{_localstatedir}/lib/mach/states >/dev/null 2>&1 || :
    #rmdir %{_localstatedir}/lib/mach/roots >/dev/null 2>&1 || :
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
%dir %{_sysconfdir}/mach/
%config %{_sysconfdir}/mach/conf
%config %{_sysconfdir}/mach/location
%config %{_sysconfdir}/mach/dist.d/
%{_bindir}/mach
%attr(04750, root, mach) %{_sbindir}/mach-helper
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/states/
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/roots/
%attr(-, mach, mach) %dir %{_localstatedir}/cache/mach/packages/
%attr(-, mach, mach) %dir %{_localstatedir}/cache/mach/archives/


%changelog
* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net> 0.4.6-2
- Added Fedora Core 3 files for i386 and x86_64.

* Sun Jul 11 2004 Matthias Saou <http://freshrpms.net> 0.4.6-1
- Update to 0.4.6.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net> 0.4.5-3
- Rebuild for Fedora Core 2.
- Don't remove the roots and states upon last removal.

* Thu May  6 2004 Matthias Saou <http://freshrpms.net> 0.4.5-2
- Added %%{python} macro to allow python2 dependency.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net> 0.4.5-1
- Update to 0.4.5.

* Mon Mar  1 2004 Matthias Saou <http://freshrpms.net> 0.4.3.1-1
- Update to 0.4.3.1.

* Wed Dec 17 2003 Matthias Saou <http://freshrpms.net> 0.4.3-1
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

