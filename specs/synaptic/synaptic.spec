# $Id$
# Authority: matthias
# Upstream: Michael Vogt <mvo$debian,org>

Summary: Graphical package management program using apt
Name: synaptic
Version: 0.57.2
Release: 6
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/synaptic/

Source: http://savannah.nongnu.org/download/synaptic/synaptic-%{version}.tar.gz
Patch0: http://apt-rpm.org/patches/synaptic-0.57.2-gcc41.patch
Patch1: http://apt-rpm.org/patches/synaptic-0.57.2-repomd-1.patch
Patch2: http://apt-rpm.org/patches/synaptic-0.57.2-showprog.patch
Patch3: http://apt-rpm.org/patches/synaptic-0.57.2-progressapi-hack.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apt-devel >= 0.5.15lorg3.2
BuildRequires: rpm-devel >= 4.0
BuildRequires: gtk2-devel >= 2.4
BuildRequires: libglade2-devel >= 2.0
BuildRequires: gcc-c++
BuildRequires: docbook-utils
BuildRequires: gettext
BuildRequires: xmlto
BuildRequires: scrollkeeper
BuildRequires: perl(XML::Parser)
Requires: apt >= 0.5.15lorg3.2
Requires: usermode
Requires(pre): scrollkeeper
Requires(postun): scrollkeeper

%description
Synaptic (previously known as raptor) is a graphical package management
program for apt. It provides the same features as the apt-get command line
utility with a GUI front-end based on Gtk+

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__cat} <<EOF >synaptic.apps
USER=root
PROGRAM=%{_sbindir}/synaptic
SESSION=true
FALLBACK=false
EOF

%{__cat} <<EOF >synaptic.pam
#%PAM-1.0
auth    sufficient      /lib/security/pam_rootok.so
auth    sufficient      /lib/security/pam_timestamp.so
auth    required        /lib/security/pam_stack.so service=system-auth
session required        /lib/security/pam_permit.so
session optional        /lib/security/pam_xauth.so
session optional        /lib/security/pam_timestamp.so
account required        /lib/security/pam_permit.so
EOF

%{__cat} <<EOF >data/synaptic.desktop.in
[Desktop Entry]
Name=Synaptic Package Manager
Comment=Install and remove applications
Exec=synaptic
Icon=synaptic.png
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;SystemSetup;X-Red-Hat-Base;
EOF

%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

### Install the consolehelper symlink
%{__mkdir_p} %{buildroot}%{_bindir}
%{__ln_s} consolehelper %{buildroot}%{_bindir}/synaptic

### Install the consolehelper required files
%{__install} -Dp -m0644 synaptic.apps %{buildroot}%{_sysconfdir}/security/console.apps/synaptic
%{__install} -Dp -m0644 synaptic.pam %{buildroot}%{_sysconfdir}/pam.d/synaptic

### Remove legacy menu entry
%{__rm} -f %{buildroot}%{_sysconfdir}/X11/sysconfig/synaptic.desktop

%clean
%{__rm} -rf %{buildroot}

%post
%{_bindir}/scrollkeeper-update -q || :

%postun
%{_bindir}/scrollkeeper-update -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man8/synaptic.8*
%config(noreplace) %{_sysconfdir}/pam.d/synaptic
%config(noreplace) %{_sysconfdir}/security/console.apps/synaptic
%{_bindir}/synaptic
%{_datadir}/applications/synaptic.desktop
%{_datadir}/applications/synaptic-kde.desktop
%{_datadir}/gnome/help/synaptic/
%{_datadir}/omf/synaptic/
%{_datadir}/pixmaps/synaptic.png
%{_datadir}/synaptic/
%{_sbindir}/synaptic

%changelog
* Thu Nov 06 2008 Dag Wieers <dag@wieers.com> - 0.57.2-6
- Rebuild with missing patches from panu. (Nicolas Thierry-Mieg)

* Wed Oct 29 2008 Dag Wieers <dag@wieers.com> - 0.57.2-5
- Rebuild against apt-0.5.15lorg3.94a.

* Thu Jun 12 2008 Dag Wieers <dag@wieers.com> - 0.57.2-4
- Rebuild against apt-0.5.15lorg3.2.

* Fri Jun 23 2006 Dag Wieers <dag@wieers.com> - 0.57.2-3
- Added more patches to make synaptic work with apt-0.5.15lorg3.2.

* Sun Apr 23 2006 Dag Wieers <dag@wieers.com> - 0.57.2-2
- Build against apt-0.5.15lorg3.

* Thu Mar 16 2006 Dag Wieers <dag@wieers.com> - 0.57.2-1
- Updated to release 0.57.2.
- Added repomd support.

* Tue Jan 11 2005 Dag Wieers <dag@wieers.com> - 0.55.3-1
- Updated to release 0.55.3.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 0.55.1-1
- Update to 0.55.1.

* Thu Jul 22 2004 Dag Wieers <dag@wieers.com> - 0.52-1
- Updated to release 0.52.
- Merged with my SPEC file.

* Tue May 18 2004 Dag Wieers <dag@wieers.com> - 0.48.2-2
- Bumped release to work with my pre-merge packages.

* Fri Apr 30 2004 Matthias Saou <http://freshrpms.net/> 0.48.2-1
- Update to 0.48.2.
- Added macros to the spec file.

* Mon Feb 16 2004 Matthias Saou <http://freshrpms.net/> 0.47-1
- Update to 0.47.
- Added docbook-utils and scrollkeeper build deps.
- Added omf file and scriptlets with calls to scrollkeeper-update.
- Update the menu entry stuff from capplet to applications location.

* Wed Oct 29 2003 Matthias Saou <http://freshrpms.net/> 0.45-1
- Rebuild for Fedora Core 1.
- Update to 0.45.
- Added missing gettext build requirement (fails miserably without!).
- Simplify the desktop entry, reusing the included one.

* Tue Aug 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.42.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.40.
- Put back into "System tools" instead of "System settings".
- Added control center file and excluded X11/sysconfig one.

* Tue Apr 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.36.1.

* Wed Apr  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.35.1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.35.
- Rebuilt for Red Hat Linux 9.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.32.

* Tue Jan 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.31.

* Thu Jan  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.30.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.28.1.

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.25.
- New icon, thanks to Alan Cramer.

* Mon Sep 30 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.24.1.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.24.
- Rebuilt for Red Hat Linux 8.0.
- Major spec file cleanup since the app now uses apt 0.5, gtk+ etc.
- Use the redhat-config-packages icon.
- Menu entry now uses the freedesktop approach.
- Use timestamp too in the pam file.

* Tue May  7 2002 Matthias Saou <http://freshrpms.net/>
- Removed the libPropList dependency.
- Changed pam entry and console.apps entry.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Fri Mar 22 2002 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat Linux 7.2.

* Tue Nov 13 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.16-1cl
- nothing new, 0.16 is for apt 0.5 support

* Sun Jul  1 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.15-1cl
- auto-fix broken dependencies on Upgrade/Install package (closes: #3967)
- always create config dir in /root

* Sat Jun 30 2001 Osvaldo Santana Neto <osvaldo@conectiva.com>
+ synaptic-0.14-3cl
- added icon in desktop (Closes: #3955)

* Sat Jun 30 2001 Osvaldo Santana Neto <osvaldo@conectiva.com>
+ synaptic-0.14-2cl
- added icon tag in menu descriptor (Closes: #3955)

* Thu Jun 28 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.14-1cl
- fixed show summary dialog (closes: #4007)
- fixed broken texts (closes: #4006)
- updated pt_BR potfile

* Wed Jun 27 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.13-1cl
- fixed some stuff in filter editor
- added default task filter
- fixed crash when changing filter (closes: #3959)


* Tue Jun 26 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.12-1cl
- added consolehelper support
- added menu (closes: #1369)
- reassigned icons credits to KDE ppl
- added little note to config window (closes: #1282)

* Wed Jun 20 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.11-1cl
- changed pkg fetch error message (closes: #1306)
- compiled against new apt (closes: #3256)
- compiled against patched wmaker (closes: #3291, #3370, #3235)
- added new potfiles (closes: #1614, #3072)
- fixed locale setting


* Fri May 18 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.10-1cl
- fixed various glitches (closes: #3235)
- bug fixed by new apt (closes: #3068)

* Tue May 14 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.9-1cl
- no longer reset package selection state when download only option is set
  (closes: #1307)
- added tooltips
- replaced N/A -> "" in version field in package list (closes: #1277)
- fixed bug in error dialogs (closes: #1280)
- added about dlg close btn (closes: #1285)
- s/Scratch Filter/Search Filter/ (closes: #1283)
- recompiled (closes: #1559)
- recompiled against new wmaker (closes: #1309, #1428, #3031)
- fixed bug when listing too many packages
- did some magick (closes: #2818)
- fixed filter button bug (closes: #1332)

* Sat Apr 28 2001 Arnaldo Carvalho de Melo <acme@conectiva.com>
+ synaptic-0.8-4cl
- minor spec changes for policy compliance
- BuildRequires libbz2-devel, not bzip2-devel

* Fri Mar 23 2001 Conectiva <dist@conectiva.com>
+ synaptic-0.8-2cl
- rebuilt with newer rpm

* Wed Feb 21 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.8-2cl
- recompiled (closes: #1559)

* Wed Feb 14 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.8-1cl
- first official release (closes: #1417)

* Wed Jan 24 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.7-1cl
- i18n
- pt_BR

* Wed Jan 24 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.6-1cl
- depends on apt cnc32

* Thu Jan 23 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ synaptic-0.5-1cl
- renamed from raptor to Synaptic

* Mon Jan 22 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ raptor-0.4-1cl

* Tue Jan 18 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ raptor-0.3-1cl

* Mon Jan 15 2001 Alfredo K. Kojima <kojima@conectiva.com.br>
+ raptor-0.2-1cl
- release version 0.2 (first)

