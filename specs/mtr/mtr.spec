# $Id$
# Authority: dag
# Upstream: Roger Wolff <R.E.Wolff$BitWizard,nl>

# Rationale: EL3 and EL4 include a real old mtr version.
### EL6 ships with mtr-0.75-5.el6
### EL5 ships with mtr-0.71-3.1
### EL4 ships with mtr-0.54-10
### EL3 ships with mtr-0.52-2
### EL2 ships with mtr-0.44-1
# Tag: rfx

%define desktop_vendor rpmforge

Summary: Network diagnostic tool
Name: mtr
Version: 0.82
Release: 1%{?dist}
Epoch: 2
License: GPL
Group: Applications/Internet
URL: http://www.BitWizard.nl/mtr

Source: ftp://ftp.bitwizard.nl/mtr/mtr-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake
BuildRequires: gtk2-devel >= 2.6.0
BuildRequires: libtermcap-devel
BuildRequires: ncurses-devel

%description
Mtr is a network diagnostic tool that combines ping and traceroute
into one program. Mtr provides two interfaces: an ncurses interface,
useful for using Mtr from a telnet session; and a GTK+ interface for X
(provided in the mtr-gtk package).

%package gtk
Summary: The GTK+ interface for mtr.
Group: Applications/Internet
Requires: mtr = %{epoch}:%{version}-%{release}
Requires: usermode >= 1.37

%description gtk
The mtr-gtk package provides the GTK+ interface for the mtr network
diagnostic tool.

%prep
%setup

touch ChangeLog

%{__cat} <<EOF >xmtr.desktop
[Desktop Entry]
Name=Traceroute
Type=Application
Comment=Trace packets between two network hosts
Exec=xmtr
Terminal=false
Icon=xmtr.xpm
Encoding=UTF-8
X-Desktop-File-Install-Version=0.2
Categories=System;Application;
EOF

%{__cat} <<EOF >xmtr.pam
#%PAM-1.0
auth       sufficient   pam_rootok.so
auth       required pam_stack.so service=system-auth
session    required pam_permit.so
session    optional pam_xauth.so
account    required pam_permit.so
EOF

%{__cat} <<EOF >xmtr.consolehelper
USER=root
PROGRAM=%{_sbindir}/xmtr
SESSION=true
EOF

%build
aclocal
automake -a
autoconf
%configure \
    --with-gtk \
    --enable-ipv6
%{__make} %{?_smp_mflags}
%{__mv} -f mtr xmtr

%{__make} distclean
%configure \
    --without-gtk \
    --enable-ipv6
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 mtr %{buildroot}%{_sbindir}/mtr
%{__make} install \
    DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 xmtr %{buildroot}%{_sbindir}/xmtr
%{__install} -Dp -m0644 img/mtr_icon.xpm %{buildroot}%{_datadir}/pixmaps/xmtr.xpm
%{__install} -Dp -m0644 xmtr.consolehelper %{buildroot}%{_sysconfdir}/security/console.apps/xmtr
%{__install} -Dp -m0644 xmtr.pam %{buildroot}%{_sysconfdir}/pam.d/xmtr
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__ln_s} -f consolehelper %{buildroot}%{_bindir}/xmtr

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 xmtr.desktop %{buildroot}%{_datadir}/gnome/apps/Internet/xmtr.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        xmtr.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING FORMATS NEWS README SECURITY
%doc %{_mandir}/man8/mtr.8*
%{_sbindir}/mtr

%files gtk
%defattr(-, root, root, 0755)
%config %{_sysconfdir}/pam.d/xmtr
%config %{_sysconfdir}/security/console.apps/xmtr
%{_bindir}/xmtr
%{_datadir}/applications/%{desktop_vendor}-xmtr.desktop
%{_datadir}/pixmaps/xmtr.xpm
%{_sbindir}/xmtr

%changelog
* Wed Dec 21 2011 Dag Wieers <dag@wieers.com> - 2:0.82-1
- Updated to release 0.82.

* Mon Oct 10 2011 Dag Wieers <dag@wieers.com> - 2:0.81-1
- Updated to release 0.81.

* Thu Jul 15 2010 Dag Wieers <dag@wieers.com> - 2:0.80-1
- Updated to release 0.80.

* Wed Jun 09 2010 Dag Wieers <dag@wieers.com> - 2:0.79-1
- Updated to release 0.79.

* Tue Jun 08 2010 Dag Wieers <dag@wieers.com> - 2:0.78-1
- Updated to release 0.78.

* Wed Jun 02 2010 Dag Wieers <dag@wieers.com> - 2:0.77-1
- Updated to release 0.77.

* Tue Oct 28 2008 Dag Wieers <dag@wieers.com> - 2:0.75-1
- Updated to release 0.75.

* Thu Sep 04 2008 Dag Wieers <dag@wieers.com> - 2:0.74-1
- Updated to release 0.74.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 2:0.72-1
- Updated to release 0.72.

* Mon Apr 03 2006 Dag Wieers <dag@wieers.com> - 2:0.71-1
- Updated to release 0.71.

* Mon Feb 07 2005 Dag Wieers <dag@wieers.com> - 2:0.69-1
- Updated to release 0.69.

* Thu Nov 25 2004 Dag Wieers <dag@wieers.com> - 2:0.65-1
- Updated to release 0.65.

* Mon Oct 18 2004 Phil Knirsch <pknirsch@redhat.com> 2:0.54-10
- rebuilt

* Wed Oct 06 2004 Phil Knirsch <pknirsch@redhat.com> 2:0.54-9
- Add CVE patch for security reasons (#129386)
- Add patch to fix broken --address option (#132628)
- Add patch to fix broken reverse DNS lookups for ipv6 (#134532)

* Tue Aug 24 2004 Warren Togami <wtogami@redhat.com> 2:0.54-8
- #121705 and other spec cleanups
- remove redundant documentation

* Thu Jul 01 2004 Phil Knirsch <pknirsch@redhat.com> 0.54-7
- Fixed broken behaviour with resolver SERVFAIL results (#125392)
- Added ncurses-devel libtermcap-devel as BuildPreReq (#124553)
- Added gtk+ Requires for mtr-gtk package (#121705)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 21 2004 Phil Knirsch <pknirsch@redhat.com> 0.54-5
- Removed absolute path for Icon in desktop file (#120170)

* Mon Feb 16 2004 Phil Knirsch <pknirsch@redhat.com>
- Added IPv6 patch from ftp://ftp.kame.net/pub/kame/misc/mtr-054-*
- Enabled IPv6 in mtr.
- Included fix from Robert Scheck to make GTK optional in configure.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 04 2004 Phil Knirsch <pknirsch@redhat.com> 0.54-2
- Fix to build on current tree.

* Sat Oct 18 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 0.54

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Nov 29 2002 Phil Knirsch <pknirsch@redhat.com> 0.52-1
- Update to latest upstream version (0.52).

* Tue Nov 12 2002 Nalin Dahyabhai <nalin@redhat.com> 0.49-9
- Remove absolute paths from the PAM configuration, ensuring that the modules
  for the right arch get used on multilib systems.
- Remove Icon:.

* Tue Sep 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.49-7a
- Fix build on s390x

* Mon Aug 19 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-7
- Fixed consolehelper support.

* Wed Aug 07 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-6
- Desktop file fixes (#69550).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.49-5
- automated rebuild

* Tue Jun 18 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-4
- Added consolehelper support to xmtr.

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-2
- Fixed autoFOO problems.

* Fri Mar 08 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- 0.49 update

* Thu Mar 07 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- 0.48 update

* Mon Jun 25 2001 Preston Brown <pbrown@redhat.com>
- 0.44 bugfix release
- fix display of icon in .desktop entry

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Feb 12 2001 Preston Brown <pbrown@redhat.com>
- don't advertise gtk support in non-gtk binary (#27172)

* Fri Oct 20 2000 Bill Nottingham <notting@redhat.com>
- fix autoconf check for resolver functions

* Fri Jul 21 2000 Bill Nottingham <notting@redhat.com>
- fix group

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul  6 2000 Bill Nottingham <notting@redhat.com>
- fix setuid bit
- remove symlink
- force build of non-gtk version

* Mon Jun 19 2000 Preston Brown <pbrown@redhat.com>
- disable SUID bits
- desktop entry

* Mon Jun 19 2000 Than Ngo <than@redhat.de>
- FHS fixes

* Fri May 26 2000 Preston Brown <pbrown@redhat.com>
- adopted for Winston

* Thu Aug 19 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.41-1]
- Added afr's patch to allow disabeling of gtk without Robn's hack.
- Made report mode report the newly added extra resolution.

* Wed Aug 18 1999 Ryan Weaver <ryanw@infohwy.com>
- renamed mtr-gtk to xmtr
- added symlink from /usr/bin/mtr to /usr/sbin/mtr

  [mtr-0.40-1]
- Fixed some problems with HPUX and SunOS.
- Included Olav Kvittem's patch to do packetsize option.
- Made the timekeeping in micro seconds.

* Wed Jun 10 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.39-1]
- Updated to version 0.39.

* Wed Jun  9 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.38-1]
- Updated to version 0.38.

* Thu Apr 15 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.37-2]
- Changed RPM headers to conform to Red Hat Contrib|Net specs.

* Mon Apr 12 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.37-1]
- v0.37
- Added Bill Bogstad's "show the local host & time" patch.
- Added R. Sparks' show-last-ping patch, submitted by Philip Kizer.

- v0.36
- Added Craigs change-the-interval-on-the-fly patch.
- Added Moritz Barsnick's "do something sensible if host not found"
  patch.
- Some cleanup of both Craigs and Moritz' patches.

* Wed Apr  7 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.35-1]
- v0.35
- Added Craig Milo Rogers pause/resume for GTK patch.
- Added Craig Milo Rogers cleanup of "reset". (restart at the beginning)
- Net_open used to send a first packet. After that the display-driver
  got a chance to distort the timing by taking its time to initialize.

* Mon Apr  5 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.34-1]
- v0.34
- Added Matt's nifty "use the icmp unreachables to do the timing" patch.
- Added Steve Kann's pause/resume patch.

* Wed Mar 10 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.33-1]
- v0.33
- Fixed the Linux glibc resolver problems.
- Fixed the off-by-one problem with -c option.

* Mon Mar  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.32-1]
- v0.32
- Fixed the FreeBSD bug detection stuff.

* Fri Mar  5 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.31-1]
- v0.31
- Fixed a few documentation issues. -- Matt
-  Changed the autoconf stuff to find the resolver library on
     Solaris. -- REW
-  Cleaned up the autoconf.in file a bit. -- Matt.

* Thu Mar  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.30-1]
- Build gtk version against gtk+-1.2.0
- v0.30
- Fixed a typo in the changelog (NEWS) entry for 0.27. :-)
- added use of "MTR_OPTIONS" environment variable for defaults.
