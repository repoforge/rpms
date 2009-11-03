# $Id$
# Authority: dag
# Upstream: Thomas Vander Stichele <thomas$apestaart,org>

%{?dtag: %{expand: %%define %dtag 1}}
%{?fc1:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?el3:%define _without_selinux 1}
%{?rh9:%define _without_selinux 1}
%{?rh7:%define _without_selinux 1}
%{?el2:%define _without_selinux 1}

%{!?builduser:  %define builduser  machbuild}
%{!?buildgroup: %define buildgroup machbuild}

%define logmsg logger -t mach/rpm

Summary: Make a chroot
Name: mach
Version: 0.9.0
Release: 1%{?dist}
Group: Applications/System
License: GPL
URL: http://thomas.apestaart.org/projects/mach/
Source: http://thomas.apestaart.org/download/mach/mach-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python >= 2.0, autoconf, automake, libtool
%{!?_without_selinux:BuildRequires: libselinux-devel}
Requires: createrepo, rpm-build, sed, cpio
ExclusiveArch: %{ix86} x86_64 ppc

%description
mach allows you to set up clean build roots from scratch for any distribution
or distribution variation supported. In this clean build root you can then
easily generate pristine packages.


%prep
%setup


%build
%configure \
	--enable-builduser="%{builduser}" \
	--enable-buildgroup="%{buildgroup}" \
%{?_without_selinux:--disable-selinux}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0775 %{buildroot}%{_localstatedir}/cache/mach/
%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mach/
%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mach/states/
%{__install} -d -m2775 %{buildroot}%{_localstatedir}/lib/mach/roots/
%{__install} -d -m0775 %{buildroot}%{_localstatedir}/tmp/mach/


%clean
%{__rm} -rf %{buildroot}


%pre
if ! /usr/bin/id mach &>/dev/null; then
	/usr/sbin/useradd -r -d %{_localstatedir}/lib/mach -s /bin/sh -c "mach user" -m mach || \
		%logmsg "Unexpected error adding user \"mach\". Aborting installation."
fi


%preun
if [ $1 -eq 0 ]; then
	umount %{_localstatedir}/lib/mach/roots/*/proc &>/dev/null || :
	rm -rf %{_localstatedir}/cache/mach/ &>/dev/null || :
	#rm -rf %{_localstatedir}/lib/mach/states/ &>/dev/null || :
	#rm -rf %{_localstatedir}/lib/mach/roots/ &>/dev/null || :
	rm -rf %{_localstatedir}/tmp/mach &>/dev/null || :
fi

%postun
if [ $1 -eq 0 ]; then
	/usr/sbin/userdel mach || %logmsg "User \"mach\" could not be deleted."
	/usr/sbin/groupdel mach || %logmsg "Group \"mach\" could not be deleted."
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING FORGETMENOT README RELEASE TODO mach.doap
%dir %{_sysconfdir}/mach/
%config %{_sysconfdir}/mach/conf
%config(noreplace) %{_sysconfdir}/mach/location
%config %{_sysconfdir}/mach/dist.d/
%{_bindir}/mach

%if %{!?_without_selinux:1}0
%exclude %{_libdir}/*.la
%{_libdir}/*.so*
%endif

%defattr(4750, root, mach)
%{_sbindir}/mach-helper

%defattr(-, mach, mach, 2755)
%dir %{_localstatedir}/cache/mach/
%dir %{_localstatedir}/lib/mach/
%dir %{_localstatedir}/lib/mach/states/
%dir %{_localstatedir}/lib/mach/roots/
%dir %{_localstatedir}/tmp/mach


%changelog
* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

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

