# $Id$
# Authority: dag

### EL6 ships with hplip-3.9.8-33.el6
%{?el6:# Tag: rfx}
### EL5 ships with hplip-1.6.7-4.1.el5_2.4
%{?el5:# Tag: rfx}

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: HP Linux Imaging and Printing Project
Name: hplip
Version: 3.10.6
Release: 0.1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://hplip.sourceforge.net/

Source0: http://dl.sf.net/hplip/hplip-%{version}.tar.gz
Source1: hplip.fdi
Patch8: hplip-3.10.5-libsane.patch
Patch13: hplip-2.8.10-ui-optional.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: cups-devel
BuildRequires: dbus-devel
BuildRequires: desktop-file-utils
BuildRequires: libjpeg-devel
BuildRequires: libusb-devel
BuildRequires: net-snmp-devel
BuildRequires: openssl-devel
BuildRequires: python-devel
BuildRequires: sane-backends-devel
Requires: /sbin/service
Requires: /sbin/chkconfig
Requires: hal
Requires: hpijs = 1:%{version}-%{release}
Requires: python-imaging
Conflicts: system-config-printer < 0.6.132
Obsoletes: hpoj <= 0.91
Obsoletes: xojpanel <= 0.91

%description
The Hewlett-Packard Linux Imaging and Printing Project provides
drivers for HP printers and multi-function peripherals.

%package -n hpijs
Summary: HP Printer Drivers
Group: Applications/Publishing
License: BSD
Epoch: 1
Requires: %{name} = %{version}-%{release}
#Requires: cupsddk-drivers
Requires: net-snmp
#Requires: python-reportlab

%description -n hpijs
hpijs is a collection of optimized drivers for HP printers.
hpijs supports the DeskJet 350C, 600C, 600C Photo, 630C, Apollo 2000,
Apollo 2100, Apollo 2560, DeskJet 800C, DeskJet 825, DeskJet 900,
PhotoSmart, DeskJet 990C, and PhotoSmart 100 series.

%package -n libsane-hpaio
Summary: SANE driver for scanners in HP's multi-function devices
Group: System Environment/Daemons
License: GPLv2+
Obsoletes: libsane-hpoj <= 0.91
Requires: sane-backends
Requires: %{name} = %{version}-%{release}
ExcludeArch: s390 s390x

%description -n libsane-hpaio
SANE driver for scanners in HP's multi-function devices (from HPOJ).

%prep
%setup

# Link libsane-hpaio against libsane (bug #234813).
%patch8 -p1 -b .libsane

# Make utils.checkPyQtImport() look for the gui sub-package (bug #243273).
%patch13 -p1 -b .ui-optional

%build
%configure \
    --with-hpppddir="%{_datadir}/ppd/HP" \
    --disable-cups-install \
    --disable-policykit \
    --disable-qt4 \
    --enable-cups-drv-install \
    --enable-cups-ppd-install \
    --enable-dbus-build \
    --enable-fax-build \
    --enable-foomatic-drv-install \
    --enable-foomatic-ppd-install \
    --enable-foomatic-rip-hplip-install \
    --enable-gui-build \
    --enable-hpcups-install \
    --enable-hpijs-install \
    --enable-network-build \
    --enable-scan-build \
    --enable-qt3
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/hal/fdi/policy/10osvendor/10-hplip.fdi

#%{__install} -p -m0644 ppd/*.ppd.gz %{buildroot}%{_datadir}/ppd/HP/

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor HP                \
    --dir %{buildroot}%{_datadir}/applications/ \
    --add-category Application                  \
    --add-category HardwareSettings             \
    --add-category Settings                     \
    --add-category System                       \
    hplip.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_sysconfdir}/sane.d/ \
    %{buildroot}%{_docdir} \
    %{buildroot}%{_sysconfdir}/udev/rules.d/ \
    %{buildroot}%{_datadir}/hplip/install.*

%{__rm} -f %{buildroot}%{_bindir}/foomatic-rip \
    %{buildroot}%{_datadir}/applications/hplip.desktop \
    %{buildroot}%{_datadir}/cups/model/foomatic-ppds \
    %{buildroot}%{_datadir}/hplip/hpaio.desc \
    %{buildroot}%{_datadir}/hplip/hpijs.drv.in.template \
    %{buildroot}%{_datadir}/hplip/hplip-install \
    %{buildroot}%{_libdir}/cups/filter/foomatic-rip \
    %{buildroot}%{_libdir}/*.la \
    %{buildroot}%{_libdir}/*.so

# Images in docdir should not be executable (bug #440552).
find doc/images -type f -exec chmod 644 {} \;

# The systray applet doesn't work properly (displays icon as a
# window), so don't ship the launcher yet. Needs python-dbus 0.80+
#rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop

%pre
### No daemons any more.
/sbin/chkconfig --del hplip 2>/dev/null || :
if [ -x /etc/init.d/hplip ]; then
    /sbin/service hplip stop
fi

%post
/usr/bin/update-desktop-database &>/dev/null || :

%postun
/usr/bin/update-desktop-database &>/dev/null || :

%postun -n libsane-hpaio -p /sbin/ldconfig
%post -n libsane-hpaio
/sbin/ldconfig
if [ -f /etc/sane.d/dll.conf ]; then
    if ! grep -q ^hpaio /etc/sane.d/dll.conf; then
        echo hpaio >> /etc/sane.d/dll.conf
    fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING doc/*
%dir %{_sysconfdir}/hp/
%config(noreplace) %{_sysconfdir}/hp/hplip.conf
%config %{_sysconfdir}/cups/pstotiff.convs
%config %{_sysconfdir}/cups/pstotiff.types
%config %{_sysconfdir}/xdg/autostart/hplip-systray.desktop
%{_bindir}/hp-align
%{_bindir}/hp-devicesettings
%{_bindir}/hp-check
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-fab
%{_bindir}/hp-faxsetup
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-makecopies
%{_bindir}/hp-makeuri
%{_bindir}/hp-mkuri
%{_bindir}/hp-pkservice
%{_bindir}/hp-plugin
%{_bindir}/hp-pqdiag
%{_bindir}/hp-print
%{_bindir}/hp-printsettings
%{_bindir}/hp-probe
%{_bindir}/hp-query
%{_bindir}/hp-scan
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-systray
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_bindir}/hp-toolbox
%{_bindir}/hp-unload
%{_bindir}/hp-wificonfig
%{_datadir}/applications/*.desktop
%dir %{_datadir}/hal/
%dir %{_datadir}/hal/fdi/
%dir %{_datadir}/hal/fdi/policy/
%dir %{_datadir}/hal/fdi/policy/10osvendor/
%{_datadir}/hal/fdi/policy/10osvendor/10-hplip.fdi
%dir %{_datadir}/hal/fdi/preprobe/
%dir %{_datadir}/hal/fdi/preprobe/10osvendor/
%{_datadir}/hal/fdi/preprobe/10osvendor/20-hplip-devices.fdi
%{_datadir}/hplip/
%dir %{_datadir}/ppd/
%{_datadir}/ppd/HP/
%{_libdir}/libhpmud.so*
%{python_sitearch}/*.so
%{_libdir}/python*/site-packages/*
%{_localstatedir}/lib/hp/
### Must be /usr/lib, since that is the CUPS serverbin directory
%dir %{_prefix}/lib/cups/
%dir %{_prefix}/lib/cups/backend/
%{_prefix}/lib/cups/backend/hp
%{_prefix}/lib/cups/backend/hpfax
%dir %{_prefix}/lib/cups/filter/
%{_prefix}/lib/cups/filter/foomatic-rip-hplip
%{_prefix}/lib/cups/filter/hpcac
%{_prefix}/lib/cups/filter/hpcups
%{_prefix}/lib/cups/filter/hpcupsfax
%{_prefix}/lib/cups/filter/pstotiff
%exclude %{python_sitearch}/*.la

%files -n hpijs
%defattr(-, root, root, 0755)
%{_bindir}/hpijs
%dir %{_datadir}/ppd/
%{_datadir}/ppd/HP/
%dir %{_datadir}/cups/
%{_datadir}/cups/drv/*
%{_libdir}/libhpip.so*
#### Must be /usr/lib, since that is the CUPS serverbin directory
%dir %{_prefix}/lib/cups/
%dir %{_prefix}/lib/cups/filter/
%{_prefix}/lib/cups/filter/hplipjs

%files -n libsane-hpaio
%defattr(-, root, root, 0755)
%{_libdir}/sane/libsane-*.so*
%exclude %{_libdir}/sane/libsane-*.la

%changelog
* Fri Jul 30 2010 Dag Wieers <dag@wieers.com> - 3.10.6-1
- Updated to release 3.10.6.

* Fri Jun 18 2010 Dag Wieers <dag@wieers.com> - 3.10.5-1
- Updated to release 3.10.5.

* Wed Dec 10 2008 Dag Wieers <dag@wieers.com> - 2.8.10-1
- Updated to release 2.8.10.

* Tue Oct 21 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-3
- Ship PPDs in the correct location (bug #343841).

* Fri Sep 26 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-2
- Moved Python extension into libs sub-package (bug #461236).

* Mon Aug  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.7-1
- 2.8.7.
- Avoid hard-coded rpaths.
- New libs sub-package (bug #444016).

* Thu Jul 31 2008 Tim Waugh <twaugh@redhat.com>
- Move libhpip.so* to the main package to avoid libsane-hpaio
  depending on hpijs (bug #457440).

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2.8.6b-2
- fix license tag

* Mon Jul 28 2008 Tim Waugh <twaugh@redhat.com> 2.8.6b-1
- 2.8.6b.

* Mon Jun 23 2008 Tim Waugh <twaugh@redhat.com> 2.8.6-1
- 2.8.6.  No longer need libm patch.

* Fri Jun  6 2008 Tim Waugh <twaugh@redhat.com> 2.8.5-2
- Make --qt4 the default for the systray applet, so that it appears
  in the right place.  Requires PyQt4.

* Tue Jun  3 2008 Tim Waugh <twaugh@redhat.com> 2.8.5-1
- 2.8.5.
- Configure with --enable-dbus.  Build requires dbus-devel.
- Fix chmod 644 line.
- Ship hp-systray in the gui sub-package, but don't ship the desktop
  launcher yet as the systray applet is quite broken.
- Don't run autoconf.

* Tue May 13 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-3
- Move installer directory to main package (bug #446171).

* Fri Apr  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-2
- Update hplip.fdi for Fedora 9: info.bus -> info.subsystem.
- Images in docdir should not be executable (bug #440552).

* Tue Mar  4 2008 Tim Waugh <twaugh@redhat.com> 2.8.2-1
- 2.8.2.  No longer need alloc, unload-traceback or media-empty patches.
- Ship cupsddk driver.  The hpijs sub-package now requires cupsddk-drivers.

* Tue Mar  4 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-6
- Fixed marker-supply-low strings.

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-5
- Rebuild for GCC 4.3.

* Fri Jan 25 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-4
- The hpijs compression module doesn't allocate enough memory (bug #428536).

* Wed Jan 23 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-3
- Really grant the ACL for the lp group (bug #424331).

* Fri Jan 18 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-2
- Ship installer directory (bug #428246).
- Avoid multilib conflict (bug #341531).
- The hpijs sub-package requires net-snmp (bug #376641).

* Fri Jan 18 2008 Tim Waugh <twaugh@redhat.com> 2.7.12-1
- 2.7.12.  No longer need ljdot4 patch.

* Fri Jan  4 2008 Tim Waugh <twaugh@redhat.com> 2.7.10-2
- Don't ship udev rules; instead, grant an ACL for group lp (bug #424331).

* Fri Dec 07 2007 Release Engineering <rel-eng at fedoraproject dot org> - 2.7.10-2
- Rebuild for deps

* Mon Oct 22 2007 Tim Waugh <twaugh@redhat.com> 2.7.10-1
- 2.7.10.

* Fri Oct 12 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-3
- Applied patch to fix remnants of CVE-2007-5208 (bug #329111).

* Tue Oct  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-2
- Use raw instead of 1284.4 communication for LJ4000 series (bug #249191).
- Build requires openssl-devel.

* Wed Oct  3 2007 Tim Waugh <twaugh@redhat.com> 2.7.9-1
- 2.7.9.
- Adjusted udev rules to be less permissive.  We use ConsoleKit to add
  ACLs to the device nodes, so world-writable device nodes can be avoided.

* Tue Sep 25 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-5
- Prevent hpfax trying to load configuration files as user lp.

* Thu Sep  6 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-4
- Reverted udev rules change.
- Ship a HAL FDI file to get correct access control on the USB device
  nodes (bug #251470).
- Make libsane-hpaio requires the main hplip package, needed for
  libhpip.so (bug #280281).

* Thu Aug 30 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-3
- Updated udev rules to allow scanning by console user.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-2
- Better buildroot tag.
- More specific license tag.

* Fri Aug  3 2007 Tim Waugh <twaugh@redhat.com> 2.7.7-1
- 2.7.7.

* Mon Jul 23 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-10
- Move libhpmud to hpijs package (bug #248978).

* Fri Jul 20 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-9
- Remove hplip service on upgrade.
- Updated selinux-policy conflict for bug #249014.
- Fixed the udev rules file (bug #248740, bug #249025).

* Tue Jul 17 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-8
- Fixed hp-toolbox desktop file (bug #248560).

* Mon Jul 16 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-7
- Low ink is a warning condition, not an error.

* Wed Jul 11 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-6
- Add hp-check back, but in the gui sub-package.
- Show the HP Toolbox menu entry again.

* Mon Jul  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-5
- Read system config when run as root (bug #242974).

* Mon Jul  9 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-4
- Moved reportlab requirement to gui sub-package (bug #189030).
- Patchlevel 1.

* Sat Jul  7 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-3
- Fixed pre scriptlet (bug #247349, bug #247322).

* Fri Jul  6 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-2
- Main package requires python-reportlab for hp-sendfax (bug #189030).
- Explicitly enable scanning.
- Main package requires python-imaging for hp-scan (bug #247210).

* Mon Jul  2 2007 Tim Waugh <twaugh@redhat.com>
- Updated selinux-policy conflict for bug #246257.

* Fri Jun 29 2007 Tim Waugh <twaugh@redhat.com> 2.7.6-1
- 2.7.6.

* Thu Jun 28 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-3
- Another go at avoiding AVC messages on boot (bug #244205).

* Thu Jun 14 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-2
- Don't try to write a /root/.hplip.conf file when running as a CUPS
  backend (bug #244205).

* Wed Jun 13 2007 Tim Waugh <twaugh@redhat.com> 1.7.4a-1
- Don't put the version in the desktop file; let desktop-file-install do it.
- 1.7.4a.  No longer need marker-supply or faxing-with-low-supplies
  patches.  Cheetah and cherrypy directories no longer shipped in source
  tarball.

* Mon Jun 11 2007 Tim Waugh <twaugh@redhat.com>
- Don't ship hp-check (bug #243273).
- Moved hp-setup back to the base package, and put code in
  utils.checkPyQtImport() to check for the gui sub-package as well as
  PyQt (bug #243273).

* Fri Jun  8 2007 Tim Waugh <twaugh@redhat.com>
- Moved hp-setup to the ui package (bug #243273).
- Prevent SELinux audit message from the CUPS backends (bug #241776)

* Thu May 10 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-10
- Prevent a traceback when unloading a photo card (bug #238617).

* Fri May  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-9
- When faxing, low ink/paper is not a problem (bug #238664).

* Tue Apr 17 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-8
- Update desktop database on %%postun as well (bug #236163).

* Mon Apr 16 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-7
- Some parts can run without GUI support after all (bug #236161).
- Added /sbin/service and /sbin/chkconfig requirements for the scriptlets
  (bug #236445).
- Fixed %%post scriptlet's condrestart logic (bug #236445).

* Fri Apr 13 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-6
- Fixed dangling symlinks (bug #236156).
- Move all fax bits to the gui package (bug #236161).
- Don't ship fax PPD and backend twice (bug #236092).
- Run update-desktop-database in the gui package's %%post scriptlet
  (bug #236163).
- Moved desktop-file-utils requirement to gui package (bug #236163).
- Bumped selinux-policy conflict version (bug #236092).

* Thu Apr  5 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-5
- Better media-empty-error state handling: always set the state.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-4
- Clear the media-empty-error printer state.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-3
- Fixed typo in marker-supply-low patch.

* Wed Apr  4 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-2
- Split out a gui sub-package (bug #193661).
- Build requires sane-backends-devel (bug #234813).

* Tue Apr  3 2007 Tim Waugh <twaugh@redhat.com>
- Change 'Hidden' to 'NoDisplay' in the desktop file, and use the System
  category instead of Utility (bug #170762).
- Link libsane-hpaio against libsane (bug #234813).

* Fri Mar 30 2007 Tim Waugh <twaugh@redhat.com>
- Use marker-supply-low IPP message.

* Wed Mar  1 2007 Tim Waugh <twaugh@redhat.com> 1.7.2-1
- 1.7.2.

* Wed Feb 14 2007 Tim Waugh <twaugh@redhat.com> 1.7.1-1
- 1.7.1.

* Wed Jan 10 2007 Tim Waugh <twaugh@redhat.com> 1.6.12-1
- 1.6.12.  No longer need broken-conf, loop, out-of-paper or
  sane-debug patches.

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.6.10-7
- rebuild against python 2.5

* Wed Dec  6 2006 Tim Waugh <twaugh@redhat.com>
- Minor state fixes for out-of-paper patch.

* Thu Nov 23 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-6
- Report out-of-paper and offline conditions in CUPS backend (bug #216477).

* Wed Nov  1 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-5
- Fixed debugging patch.

* Wed Nov  1 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-4
- Allow debugging of the SANE backend.

* Mon Oct 30 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-3
- IPv6 support (bug #198377).  Local-only sockets are IPv4, and ought
  to be changed to unix domain sockets in future.

* Fri Oct 27 2006 Tim Waugh <twaugh@redhat.com> 1.6.10-2
- 1.6.10.  No longer need compile patch.
- Fixed default config file (bug #211072).
- Moved libhpip to hpijs sub-package (bug #212531).

* Fri Sep 29 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-4
- Don't wake up every half a second (bug #204725).

* Mon Sep 25 2006 Tim Waugh <twaugh@redhat.com>
- Fixed package URL.

* Mon Aug 21 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-3
- Don't look up username in PWDB in the fax backend (removed redundant code).

* Mon Aug  7 2006 Tim Waugh <twaugh@redhat.com> 1.6.7-2
- 1.6.7.
- Conflict with selinux-policy < 2.3.4 to make sure new port numbers are
  known about (bug #201357).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - (none):1.6.6a-3.1
- rebuild

* Tue Jul  4 2006 Tim Waugh <twaugh@redhat.com> 1.6.6a-3
- libhpip should link against libm (bug #197599).

* Wed Jun 28 2006 Tim Waugh <twaugh@redhat.com> 1.6.6a-2
- 1.6.6a.

* Mon Jun 26 2006 Tim Waugh <twaugh@redhat.com>
- Patchlevel 1.
- Fixed libsane-hpaio %%post scriptlet (bug #196663).

* Fri Jun 16 2006 Tim Waugh <twaugh@redhat.com> 1.6.6-2
- 1.6.6.

* Mon Jun 12 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-6
- Build requires autoconf (bug #194682).

* Fri May 26 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-5
- Include doc files (bug #192790).

* Mon May 15 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-4
- Patchlevel 2.

* Wed May 10 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-3
- Move hpijs to 0.9.11 too.

* Wed May 10 2006 Tim Waugh <twaugh@redhat.com> 0.9.11-2
- 0.9.11.
- Keep hpijs at 0.9.8 for now.

* Fri Apr 21 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-6
- Patchlevel 2.

* Wed Apr 19 2006 Tim Waugh <twaugh@redhat.com>
- Don't package COPYING twice (bug #189162).

* Tue Apr 18 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-5
- Patchlevel 1.
- Fixed another case-sensitive match.
- Require hpijs sub-package (bug #189140).
- Don't package unneeded files (bug #189162).
- Put fax PPD in the right place (bug #186213).

* Tue Apr  4 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-4
- Use case-insensitive matching.  0.9.8 gave all-uppercase in some
  situations.
- Last known working hpijs comes from 0.9.8, so use that.

* Tue Mar 28 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-3
- Always use /usr/lib/cups/backend.

* Tue Mar 28 2006 Tim Waugh <twaugh@redhat.com> 0.9.10-2
- 0.9.10.
- Ship PPDs.

* Fri Mar 24 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-7
- Include hpfax.
- Build requires libusb-devel.

* Thu Mar 23 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-6
- CUPS backend directory is always in /usr/lib.

* Mon Mar 13 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-4
- Quieten hpssd on startup.

* Sat Mar 11 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-3
- Patchlevel 1.

* Thu Mar  9 2006 Tim Waugh <twaugh@redhat.com> 0.9.9-2
- 0.9.9.  No longer need quiet or 0.9.8-4 patches.

* Wed Mar 01 2006 Karsten Hopp <karsten@redhat.de> 0.9.8-6
- Buildrequires: desktop-file-utils

* Mon Feb 27 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-5
- Patchlevel 4.

* Tue Feb 14 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-4
- Added Obsoletes: hpoj tags back in (bug #181476).

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - (none):0.9.8-3.1
- bump again for double-long bug on ppc(64)

* Tue Feb  7 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-3
- Patchlevel 3.

* Fri Feb  3 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-2
- Patchlevel 2.

* Thu Feb  2 2006 Tim Waugh <twaugh@redhat.com> 0.9.8-1
- 0.9.8.
- No longer need initscript patch.
- Don't package hpfax yet.

* Wed Jan 18 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-8
- Don't package PPD files.

* Thu Jan  5 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-7
- Fix initscript (bug #176966).

* Mon Jan  2 2006 Tim Waugh <twaugh@redhat.com> 0.9.7-6
- Rebuild.

* Fri Dec 23 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-5
- Rebuild.

* Wed Dec 21 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-4
- Build requires python-devel, libjpeg-devel (bug #176317).

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Dec  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-3
- Use upstream patch 0.9.7-2.
- No longer need lpgetstatus or compile patches.

* Fri Nov 25 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-2
- Prevent LPGETSTATUS overrunning format buffer.

* Thu Nov 24 2005 Tim Waugh <twaugh@redhat.com> 0.9.7-1
- 0.9.7.

* Fri Nov 18 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-7
- Fix compilation.

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 0.9.6-6
- rebuilt against new openssl

* Mon Nov  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-5
- Rebuilt.

* Wed Oct 26 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-4
- Ship initscript in %%{_sysconfdir}/rc.d/init.d.

* Fri Oct 14 2005 Tim Waugh <twaugh@redhat.com>
- Install the desktop file with Hidden=True (bug #170762).

* Fri Oct 14 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-3
- Don't install desktop file (bug #170762).
- Quieten the hpssd daemon at startup (bug #170762).

* Wed Oct 12 2005 Tim Waugh <twaugh@redhat.com> 0.9.6-2
- 0.9.6.

* Tue Sep 20 2005 Tim Waugh <twaugh@redhat.com> 0.9.5-3
- Apply upstream patch to fix scanning in LaserJets and parallel InkJets.

* Mon Sep 19 2005 Tim Waugh <twaugh@redhat.com> 0.9.5-2
- 0.9.5.
- No longer need condrestart patch.
- Fix compile errors.

* Tue Jul 26 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-3
- Fix condrestart in the initscript.

* Mon Jul 25 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-2
- Use 'condrestart' not 'restart' in %%post scriptlet.

* Fri Jul 22 2005 Tim Waugh <twaugh@redhat.com> 0.9.4-1
- forward-decl patch not needed.
- 0.9.4.

* Fri Jul  1 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-8
- Removed Obsoletes: hpoj tags (bug #162222).

* Thu Jun 30 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-7
- Rebuild to get Python modules precompiled.

* Wed Jun 22 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-6
- For libsane-hpaio ExcludeArch: s390 s390x, because it requires
  sane-backends.

* Wed Jun 15 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-5
- Use static IP ports (for SELinux policy).

* Tue Jun 14 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-4
- Conflicts: hpijs from before this package provided it.
- Conflicts: system-config-printer < 0.6.132 (i.e. before HPLIP support
  was added)

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-3
- Added Obsoletes: for xojpanel and hpoj-devel (but we don't actually package
  devel files yet).

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-2
- Add 'hpaio' to SANE config file, not 'hpoj' (bug #159954).

* Thu Jun  9 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-1
- Use /usr/share/applications for putting desktop files in (bug #159932).
- Requires PyQt (bug #159932).

* Tue Jun  7 2005 Tim Waugh <twaugh@redhat.com> 0.9.3-0.1
- Initial package, based on Mandriva spec file.
