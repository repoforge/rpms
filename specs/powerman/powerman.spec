# $Id$
# Authority: yury
# Upstream: powerman-discuss mailing list <powerman-discuss$lists,sourceforge,net>

Name: powerman
Version: 2.3.5
Release: 3%{?dist}
Summary: PowerMan - Power to the Cluster

Group: Applications/System
License: GPLv2+
Url: http://sourceforge.net/projects/powerman
Source0: http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0: powerman.init.patch
Patch1: powerman-multilib.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex bison readline-devel
BuildRequires: tcp_wrappers-devel
BuildRequires: curl-devel
BuildRequires: ncurses-devel

%description
PowerMan is a tool for manipulating remote power control (RPC) devices from a 
central location. Several RPC varieties are supported natively by PowerMan and 
Expect-like configurability simplifies the addition of new devices.

%package devel
Summary:  Development files for Powerman
Group:    Applications/System
Requires: powerman = %{version}-%{release}
Requires: pkgconfig
%description devel
Development files for Powerman


%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .initpatch
%patch1 -p1 -b .multilibpatch

%build

sed -i 's/@PACKAGE_VERSION/%{version}/' -i lib/libpowerman.pc.in

%configure --with-httppower --with-genders

%{__make} %{?_smp_mflags} -e VERSION=%{version}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} %{?_smp_mflags} install -e DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}

# work around a problem in the install make file target
%{__rm} $RPM_BUILD_ROOT/%{_bindir}/pm
pushd $RPM_BUILD_ROOT/%{_bindir}; ln -s powerman pm; popd

# get rid of execute bit on powerman script files to fix rpmlint errror
chmod -x $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add powerman

%preun
if [ "$1" = 0 ]
then
  # No conditional stop provided. :(
  /sbin/service powerman status
  if [ "$?" -eq 0 ]
  then
    /sbin/service powerman stop
  fi
  /sbin/chkconfig --del powerman
fi

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog DISCLAIMER COPYING NEWS TODO
%{_bindir}/powerman
%{_bindir}/pm
%{_sbindir}/plmpower
%{_sbindir}/powermand
%{_sbindir}/httppower
%{_sbindir}/vpcd
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man*/*
%{_sysconfdir}/init.d/%{name}
%{_libdir}/libpowerman.so.0
%{_libdir}/libpowerman.so.0.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/libpowerman.h
%exclude %{_libdir}/libpowerman.a
%exclude %{_libdir}/libpowerman.la
%{_libdir}/pkgconfig/libpowerman.pc
%{_libdir}/libpowerman.so
%{_libdir}/stonith/plugins/external/powerman

%changelog
* Fri Dec 25 2009 Yury V. Zaytsev <yury@shurup.com> - 2.3.5-3
- Ported over RPMForge with minor changes.

* Sat Oct 10 2009 Steven M. Parrish <smparrish@gmail.com> - 2.3.5-2
- Fix multilib issue #509691

* Wed Aug 26 2009 Steven Parrish <smparrish@gmail.com> - 2.3.5-1
- Deprecated undocumented powerman.conf port directive.
- Added powerman.conf listen directive to configure which interfaces
-   and ports the server listens on.  Make the default localhost:10101.
- Add support for HP integrated power control devices [Bjorn Helgaas]
- Add support for Sun LOM.
- Misc. documentation improvements
- Add heartbeat STONITH plugin.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 11 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> 2.3.4-4
- Updated post and postun with ldconfig
- added init script patch to default to autostart no

* Tue Feb 10 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> 2.3.4-3
- Fix errors in files lists

* Tue Feb 10 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> 2.3.4-2
- Fix errors in files lists

* Tue Feb 10 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> 2.3.4-1
- New upstream release.  New -devel subpackage created

* Mon Feb 09 2009 Steven M. Parrish <tuxbrewr@fedoraproject.org> 2.3-1
- New upstream release

* Mon Sep 15 2008 Steven M. Parrish <smparrish@shallowcreek.net> 2.2-1
- New upstream release

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.1-2
- fix license tag

* Wed Jun 18 2008 Steven Parrish <smparrish[at]shallowcreek.net> 2.1-1
- New upstream release

* Wed Jun 04 2008 Jarod Wilson <jwilson@redhat.com> 2.0-2
- Clean up some legacy distro cruft

* Wed Jun 04 2008 Jarod Wilson <jwilson@redhat.com> 2.0-1
- New upstream release

* Wed Feb 13 2008 Jarod Wilson <jwilson@redhat.com> 1.0.32-5
- Fix up header includes to build w/gcc 4.3

* Thu Jan 31 2008 Jarod Wilson <jwilson@redhat.com> 1.0.32-4
- And now make it build with ncurses instead of termcap in f9+

* Mon Jan 28 2008 Jarod Wilson <jwilson@redhat.com> 1.0.32-3
- Ugh, add libtermcap-devel BR

* Mon Jan 28 2008 Jarod Wilson <jwilson@redhat.com> 1.0.32-2
- Add {lib,}curl-devel and readline-devel BR

* Mon Jan 28 2008 Jarod Wilson <jwilson@redhat.com> 1.0.32-1
- New upstream release

* Wed Feb 07 2007 Jarod Wilson <jwilson@redhat.com> 1.0.25-2
- Release bump to fix devel upgrade path

* Mon Feb 05 2007 Jarod Wilson <jwilson@redhat.com> 1.0.25-1
- New upstream release
- Fixed up compile flags

* Tue Sep 05 2006 Jarod Wilson <jwilson@redhat.com> 1.0.24-3
- Rebuild for new glibc

* Mon Jul 24 2006 Jarod Wilson <jwilson@redhat.com> 1.0.24-2
- Update BuildRequires for updated (minimal-er) mock buildroots

* Tue Jun 13 2006 Jarod Wilson <jwilson@redhat.com> 1.0.24-1
- Assorted mods to conform more with Fedora Extras guidelines

* Fri Apr 21 2006 Ben Woodard <woodard@redhat.com> 1.0.23-4
- Added tcp_wrappers as a requirement so that it can build in mock

* Mon Feb 27 2006 Ben Woodard <woodard@redhat.com> 1.0.23-3
- change perms on files in etc/powerman so that they don't look like scripts
  to rpmlint.
- mark powerman hardware files config files.
- add patch to init file which turns off powerman by default and works around
  a minor problem in rpmlint's handling of chkconfig lines.

* Fri Feb 23 2006 Ben Woodard <woodard@redhat.com>
- Change source to dl.sf.net
- Add args to make
- added flags to allow for parallel building
- changed defattr which was interfering with perms of included files.
- removed explicit attrs for files
- removed man directories from package.
- changed etc to sysconfdir macro.
- powerman initscript not a config file.
- change pm from an absolute symlink to a relative symlink

* Thu Feb 16 2006 Ben Woodard <woodard@redhat.com> 1.0.23-2
- fix permissions on spec file and source file
- Put complete URL in Source0
- Condensed some of the files listed.

* Wed Feb 15 2006 Jim Garlick <garlick@llnl.gov> 1.0.23-1
- new release 1.0.23

* Tue Feb 14 2006 Ben Woodard <woodard@redhat.com> 1.0.22-3
- Changed /usr/bin to bindir
- Changed /usr/sbin to sbindir
- Added COPYING to list of docs.
- Changed /etc/rc.d/init.d/ to initrddir
- Changed /usr/man to mandir
- Added a fully qualified path to the source file.
- Fixed buildroot
- Added a patch which should fix a fc4 build problem.

* Thu Feb 09 2006 Ben Woodard <woodard@redhat.com> 1.0.22-2
- changed the buildroot to match fedora guidlines
- changed permissions of spec and src files.
- added changelog to spec file
