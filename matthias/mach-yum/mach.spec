# $Id$
# Authority: matthias
# Upstream: Thomas Vander Stichele <thomas$apestaart,org>

%{!?builduser:  %define builduser  machbuild}
%{!?buildgroup: %define buildgroup machbuild}
# Override with --define 'python python2'
%{!?python:     %define python     python}

Summary: Make A CHroot
Name: mach
Version: 0.4.6.1
Release: 4.yum
Group: Applications/System
License: GPL
URL: http://thomas.apestaart.org/projects/mach/
Source0: http://thomas.apestaart.org/download/mach/mach-%{version}.tar.bz2
Source1: buildroots.xml
Patch: mach-0.4.6.1-config.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: rpm-python, yum, sed, cpio, python >= 2.0.0, createrepo
BuildRequires: %{python} >= 2.0.0, libselinux-devel

%description
mach makes a chroot.
Using apt-get and a suid binary, it manages to install clean chroot
environments based on the original packages for that distribution.

The clean root can be used to run jail roots, to create image files, or
to build clean packages.


%prep
%setup
%patch -p1 -b .config


%build
%configure \
    --enable-builduser=%{builduser} \
    --enable-buildgroup=%{buildgroup}
%{__make}


%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mach
%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mach/states
%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mach/roots
%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mach/rpms
%{__install} -d -m0775 %{buildroot}%{_localstatedir}/cache/mach/packages
%{__install} -d -m0775 %{buildroot}%{_localstatedir}/cache/mach/archives

# The buildroots group file
%{__install} -p -m 0644 -D %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/mach/buildgroups/buildroots.xml


%clean
%{__rm} -rf %{buildroot}


%pre
# create mach group
/usr/sbin/groupadd -r mach &>/dev/null || :

%post
# create repodata for the group build group information
createrepo -g buildroots.xml %{_sysconfdir}/mach/buildgroups/ &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
    # Last removal
    # Be a good boy and clean out the dirs we filled with junk
    # Actually... the roots may be used later on, so better keep them
    #%{__rm} -rf %{_localstatedir}/lib/mach/states/*
    umount %{_localstatedir}/lib/mach/roots/*/proc &>/dev/null || :
    #%{__rm} -rf %{_localstatedir}/lib/mach/roots/* &>/dev/null || :
    %{__rm} -rf %{_localstatedir}/cache/mach/* &>/dev/null || :
    #rmdir %{_localstatedir}/lib/mach/states &>/dev/null || :
    #rmdir %{_localstatedir}/lib/mach/roots &>/dev/null || :
    rmdir %{_localstatedir}/cache/mach &>/dev/null || :
    %{__rm} -rf %{_localstatedir}/tmp/mach &>/dev/null || :
    %{__rm} -rf %{_sysconfdir}/mach/buildgroups/repodata &>/dev/null || :
fi


%files
%defattr(-, root, root, -)
%doc ChangeLog COPYING README AUTHORS BUGS TODO FORGETMENOT RELEASE
%dir %{_sysconfdir}/mach/
%dir %{_sysconfdir}/mach/buildgroups/
%config %{_sysconfdir}/mach/conf
%config %{_sysconfdir}/mach/location
%config %{_sysconfdir}/mach/dist.d/
%config %{_sysconfdir}/mach/buildgroups/buildroots.xml
%{_bindir}/mach
%{_libdir}/libselinux-mach.*
%attr(04750, root, mach) %{_sbindir}/mach-helper
%attr(0755, root, root) %dir %{_localstatedir}/lib/mach/
%attr(2775, root, mach) %dir %{_localstatedir}/lib/mach/states/
%attr(2775, root, mach) %dir %{_localstatedir}/lib/mach/roots/
%attr(2775, root, mach) %dir %{_localstatedir}/lib/mach/rpms/
%attr(0755, root, root) %dir %{_localstatedir}/cache/mach/
%attr(2775, root, mach) %dir %{_localstatedir}/cache/mach/packages/
%attr(2775, root, mach) %dir %{_localstatedir}/cache/mach/archives/


%changelog
* Thu Jun 30 2005 Matthias Saou <http://freshrpms.net> 0.4.6.1-4.yum
- Add RHEL 3 & 4 config files.

* Tue Jun 28 2005 Matthias Saou <http://freshrpms.net> 0.4.6.1-3.yum
- Update patch to fix inclusion of FC4 entries.

* Tue Jun 14 2005 Matthias Saou <http://freshrpms.net> 0.4.6.1-2.yum
- Add FC4 entries.

* Sun Apr 17 2005 Matthias Saou <http://freshrpms.net> 0.4.6.1-1.yum
- Update to seth's yum-ified fork and update spec accordingly.

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

