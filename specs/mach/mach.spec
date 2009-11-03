# $Id$
# Authority: matthias
# Upstream: Thomas Vander Stichele <thomas$apestaart,org>

%{!?builduser:  %define builduser  machbuild}
%{!?buildgroup: %define buildgroup machbuild}
# Override with --define 'python python2'
%{!?python:     %define python     python}

Summary: Make A CHroot
Name: mach
Version: 0.4.8.2
Release: 0%{?dist}
Group: Applications/System
License: GPL
URL: http://thomas.apestaart.org/projects/mach/
Source: http://thomas.apestaart.org/download/mach/mach-%{version}.tar.bz2
Patch0: mach-0.4.8.2-cfg.patch
Patch1: mach-0.4.8.2-runuser.patch
Patch2: mach-0.4.8.2-uid500fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: yum, createrepo, rpm-build, sed, cpio
BuildRequires: %{python} >= 2.0, libselinux-devel
BuildRequires: autoconf, automake, libtool
ExclusiveArch: %{ix86} x86_64 ppc

%description
mach allows you to set up clean build roots from scratch for any distribution
or distribution variation supported. In this clean build root you can then
easily generate pristine packages.


%prep
%setup
%patch0 -p1 -b .cfg
%patch1 -p1 -b .runuser
%patch2 -p1 -b .uid500fix
autoreconf


%build
%configure \
    --enable-builduser=%{builduser} \
    --enable-buildgroup=%{buildgroup} \
    %{?_without_selinux:--disable-selinux}


%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m 2775 %{buildroot}%{_localstatedir}/lib/mach
%{__install} -d -m 2775 %{buildroot}%{_localstatedir}/lib/mach/states
%{__install} -d -m 2775 %{buildroot}%{_localstatedir}/lib/mach/roots
%{__install} -d -m 0775 %{buildroot}%{_localstatedir}/cache/mach/packages
%{__install} -d -m 0775 %{buildroot}%{_localstatedir}/cache/mach/archives


%clean
%{__rm} -rf %{buildroot}


%pre
# create user and group mach
/usr/sbin/useradd -c "mach user" \
    -r -m mach -d %{_localstatedir}/lib/mach &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
    # Last removal
    # Be a good boy and clean out the dirs we filled with junk
    # Actually... the roots may be used later on, so better keep them
    umount %{_localstatedir}/lib/mach/roots/*/proc &>/dev/null || :
    #rm -rf %{_localstatedir}/lib/mach/states/ &>/dev/null || :
    #rm -rf %{_localstatedir}/lib/mach/roots/ &>/dev/null || :
    #rm -rf %{_localstatedir}/tmp/mach/ &>/dev/null || :
    rm -rf %{_localstatedir}/cache/mach/ &>/dev/null || :
fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING FORGETMENOT README RELEASE TODO
%dir %{_sysconfdir}/mach/
%config %{_sysconfdir}/mach/conf
%config %{_sysconfdir}/mach/location
%dir %{_sysconfdir}/mach/dist.d/
# PPC configuration
%ifarch ppc
%config %{_sysconfdir}/mach/dist.d/*-ppc
%else
%exclude %{_sysconfdir}/mach/dist.d/*-ppc
%endif
# x86 -> only i386, but x86_64 -> x86_64 _and_ i386
%ifarch %{ix86} x86_64
%config %{_sysconfdir}/mach/dist.d/*-i386
%ifarch x86_64
%config %{_sysconfdir}/mach/dist.d/*-x86_64
%else
%exclude %{_sysconfdir}/mach/dist.d/*-x86_64
%endif
%else
%exclude %{_sysconfdir}/mach/dist.d/*-i386
%exclude %{_sysconfdir}/mach/dist.d/*-x86_64
%endif
%{_bindir}/mach
%attr(04750, root, mach) %{_sbindir}/mach-helper
%exclude %{_libdir}/*.la
%{_libdir}/*.so*
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/states/
%attr(-, mach, mach) %dir %{_localstatedir}/lib/mach/roots/
%attr(-, mach, mach) %dir %{_localstatedir}/cache/mach/packages/
%attr(-, mach, mach) %dir %{_localstatedir}/cache/mach/archives/


%changelog
* Tue Jan 24 2006 Matthias Saou <http://freshrpms.net> 0.4.8.2-1
- Update to 0.4.8.2 pre-release.

* Thu Jan 19 2006 Matthias Saou <http://freshrpms.net> 0.4.8-0.2
- Add freshrpms to FC development dist.d files.

* Wed Dec 21 2005 Matthias Saou <http://freshrpms.net> 0.4.8-0.2
- Fix fedora development core location (remove trailing "os").

* Mon Dec 12 2005 Matthias Saou <http://freshrpms.net> 0.4.8-0.1
- Update to 0.4.8 (and only support yum, not apt).
- Include only relevant dist.d files for given archs.
- Include configuration patch (heavy!).
- Include script patch to fix non-uid 500 user problems, and rip out apt.

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

