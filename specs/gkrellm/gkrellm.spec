# $Id$
# Authority: matthias

%define desktop_vendor rpmforge
%define wifi_version   0.9.12

Summary: The GNU Krell Monitor, stacked system monitors in one process
Name: gkrellm
Version: 2.2.7
Release: 0%{?dist}
License: GPL
Group: Applications/System
URL: http://www.gkrellm.net/
Source0: http://members.dslextreme.com/users/billw/gkrellm/gkrellm-%{version}.tar.bz2
Source1: gkrellmd.init
Source2: http://dev.gentoo.org/~brix/files/gkrellm-wifi/gkrellm-wifi-%{wifi_version}.tar.gz
Patch0: gkrellm_i18n.patch
Patch1: gkrellm-2.1.28-config.patch
Patch2: gkrellm-wifi-0.9.12-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, openssl-devel, gettext, pkgconfig
BuildRequires: ImageMagick, desktop-file-utils
Conflicts: gkrellm-plugins < 2.0.0

%description
GKrellM charts SMP CPU, load, Disk, and all active net interfaces
automatically. An on/off button and online timer for the PPP interface
is provided. Monitors for memory and swap usage, file system, internet
connections, APM laptop battery, mbox style mailboxes, and cpu temps.
Also includes an uptime monitor, a hostname label, and a clock/calendar.


%package devel
Summary: Include headers from the GNU Krell Monitor
Group: Development/Libraries
Requires : gkrellm = %{version}-%{release}, gtk2-devel, openssl-devel

%description devel
Install this package if you intend to compile plugins to use with the
GKrellM monitor.


%package daemon
Summary: The GNU Krell Monitor Daemon
Group: System Environment/Daemons
Requires: glib2 >= 2.0
Obsoletes: gkrellm-server <= 2.1.21

%description daemon
This contains only the gkrellm daemon, which you can install on its own on
machines you intend to monitor with gkrellm from a different location.


%ifnarch s390 s390x
%package wireless
Summary: Wireless monitor for the GNU Krell Monitor
Group: Applications/System
Requires: %{name} = %{version}

%description wireless
This plug-in monitors the wireless LAN cards in your computer and
displays a graph of the link quality percentage for each card.
%endif


%prep
%setup
%patch0 -p0 -b .i18n
%patch1 -p1 -b .config
%ifnarch s390 s390x
%{__tar} xzf %{SOURCE2}
%patch2 -p0 -b .wifibuild
%endif

# Fix for lib vs. lib64
%{__perl} -pi.orig -e 's|/usr/X11R6/lib|/usr/X11R6/%{_lib}|g' \
    Makefile Makefile.i18n */Makefile
%{__perl} -pi.orig -e 's|lib/pkgconfig|%{_lib}/pkgconfig|g' Makefile
# Also for the plugins search path and documentation
%{__perl} -pi.orig -e 's|/usr/lib/|%{_libdir}/|g;
                       s|/usr/local/lib/|/usr/local/%{_lib}/|g' \
    server/gkrellmd.h src/gkrellm.h README Changelog* *.1


%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" debug=1
%ifnarch s390 s390x
(cd gkrellm-wifi-%{wifi_version}; %{__make} OPTFLAGS="%{optflags}")
%endif


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_sysconfdir}
%{__mkdir_p} %{buildroot}%{_libdir}/gkrellm2/plugins
%{__mkdir_p} %{buildroot}%{_datadir}/gkrellm2/themes
%{__make} install DESTDIR=%{buildroot} PREFIX=%{_prefix}
%find_lang %{name}

# Install the daemon config file
%{__install} -D -p -m 0755 server/gkrellmd.conf \
    %{buildroot}%{_sysconfdir}/gkrellmd.conf

# Install the icon for the menu entry
# (it seems like new versions of ImageMagick rename with a dash now)
convert gkrellm.ico gkrellm.png
[ -f gkrellm3.png ]  && ICON="gkrellm3.png"
[ -f gkrellm-3.png ] && ICON="gkrellm-3.png"
%{__install} -D -p -m 0644 ${ICON} \
    %{buildroot}%{_datadir}/pixmaps/gkrellm.png

# Install the menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=GKrellM System Monitor
Type=Application
Comment=Monitor for CPU, memory, disks, network, mail
Exec=gkrellm
Icon=gkrellm.png
Terminal=false
Encoding=UTF-8
Categories=Application;System;Monitor;X-Red-Hat-Extra;
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

# Install the init script
%{__install} -D -p -m 0755 %{SOURCE1} \
    %{buildroot}/etc/rc.d/init.d/gkrellmd

# Install the wireless plugin
%ifnarch s390 s390x
%{__install} -p gkrellm-wifi-%{wifi_version}/gkrellm-wifi.so \
    %{buildroot}%{_libdir}/gkrellm2/plugins/
%endif


%clean
%{__rm} -rf %{buildroot}


%pre daemon
# The daemon shouldn't run as nobody
/usr/sbin/groupadd -g 101 gkrellmd 2>/dev/null || :
/usr/sbin/useradd -u 101 -s /sbin/nologin -M -d / -c "GNU Krell daemon" -r -g gkrellmd gkrellmd 2>/dev/null || :

%post daemon
chkconfig --add gkrellmd

%preun daemon
if [ $1 -eq 0 ]; then
    /sbin/service gkrellmd stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del gkrellmd
fi

%postun daemon
if [ $1 -eq 0 ]; then
    /usr/sbin/userdel gkrellmd 2>/dev/null || :
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYRIGHT CREDITS Changelog* README Themes.html
%{_bindir}/gkrellm
%{_libdir}/gkrellm2
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/gkrellm2
%{_datadir}/pixmaps/gkrellm.png
%{_mandir}/man1/gkrellm.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gkrellm2
%{_libdir}/pkgconfig/gkrellm.pc

%files daemon
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/gkrellmd.conf
/etc/rc.d/init.d/gkrellmd
%{_bindir}/gkrellmd
%{_mandir}/man1/gkrellmd.1*

%ifnarch s390 s390x
%files wireless
%defattr(-, root, root, 0755)
%{_libdir}/gkrellm2/plugins/gkrellm-wifi.so
%endif


%changelog
* Tue Oct 11 2005 Matthias Saou <http://freshrpms.net/> 2.2.7-0
- Update to 2.2.7.
- Fix lib64 plugin search path and references to it in the docs.

* Tue Mar 29 2005 Matthias Saou <http://freshrpms.net/> 2.2.5-0
- Update to 2.2.5.
- Update source location.
- Workaround new ImageMagick renaming gkrellm-3.png instead of gkrellm3.png.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net/> 2.2.4-0
- Update to 2.2.4.
- Add wifi plugin to this package, as the main RH/FC package does.
- Minor tweaks.

* Tue Aug 24 2004 Matthias Saou <http://freshrpms.net/> 2.2.2-2
- Fix the gkrellmd location in the init script, thanks to Sammy Atmadja.

* Fri Jul 23 2004 Matthias Saou <http://freshrpms.net/> 2.2.2-1
- Update to 2.2.2.
- Add fixes for x86_64.

* Mon Jun  7 2004 Matthias Saou <http://freshrpms.net/> 2.2.1-1
- Update to 2.2.1.

* Tue Jun  1 2004 Matthias Saou <http://freshrpms.net/> 2.2.0-2
- Change the daemon to be built with gtk2 from now on.
- Add debug=1 to the build to get symbols into the debuginfo package.
- Added openssl-devel to the build requirements to get POP3S and IMAPS.
- Add the menu entry and icon in the same way as the original FC2 package.
- Added the init script for the daemon package from the FC2 package.
- Change the sed config changes to a patch to the config file.

* Mon May 24 2004 Matthias Saou <http://freshrpms.net/> 2.2.0-1
- Update to 2.2.0.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 2.1.28-1
- Update to 2.1.28.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 2.1.26-1
- Update to 2.1.26.

* Wed Jan 21 2004 Matthias Saou <http://freshrpms.net/> 2.1.25-1
- Update to 2.1.25.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 2.1.24-1
- Update to 2.1.24.

* Thu Dec 18 2003 DenV <den@nekto.com> 2.1.23-2
- Fix broken localisation.

* Thu Dec 18 2003 Matthias Saou <http://freshrpms.net/> 2.1.23-1
- Update to 2.1.23.

* Wed Dec 17 2003 Matthias Saou <http://freshrpms.net/> 2.1.22-1
- Update to 2.1.22.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.1.21-2
- Rebuild for Fedora Core 1.
- Renamed server to daemon to match distribution naming.

* Mon Oct 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.21.

* Wed Oct  8 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.20.

* Sat Sep 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.19.

* Fri Aug 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.16.

* Wed Jun 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.14.

* Thu Jun 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.13.

* Wed Jun 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.12a.
- Added pkgconfig entry to the devel package.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.10.
- Simplified install since there is now INSTALLROOT in the Makefile.
- Moved gkrellmd from sbin to bin.

* Tue Apr 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.9.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Removed epoch.

* Thu Mar 13 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.8a.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
* Tue Feb 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.7a.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.7.

* Sat Jan 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.6.

* Tue Jan 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.5.

* Thu Jan  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.4.

* Mon Dec  9 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.3.
- Back to glib 1.2 for the daemon.

* Thu Nov 28 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.1.
- The gkrellmd now depends on glib2 as it won't compile with 1.2 any more.
- Allow only localhost by default in the gkrellmd.conf file.

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.0.

* Sun Oct  6 2002 Ville Skyttä <ville.skytta at iki.fi> 1:2.0.4-fr2
- Install server to sbin instead of bin.
- Include default config for the server.

* Fri Oct  4 2002 Matthias Saou <http://freshrpms.net/>
- Fix plugin dir location.

* Tue Sep 17 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.4.

* Tue Sep 17 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.2.
- Split the daemon, thanks to William Stearns for the suggestion and patch.
- Build the daemon with glib 1.2 and not 2.0.

* Sun Aug 26 2002 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.0.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.13.

* Fri Jun 14 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.2.12.
- Use %%find_lang.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Thu Mar 28 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.11.

* Thu Mar 21 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.10.

* Sat Feb 16 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.9.

* Sat Jan  5 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.8.

* Thu Jan  3 2002 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.7.

* Mon Dec 18 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.6.

* Wed Dec  5 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.5.

* Wed Oct 31 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.4.

* Wed Oct 24 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.3.

* Thu Aug 23 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.2.

* Thu Aug  2 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.1.

* Wed Aug  1 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.2.0.

* Tue Apr 17 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.0.8.

* Tue Mar 20 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.0.7, added the new manpage and changed the URL.

* Tue Jan 30 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.0.6

* Wed Jan 24 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.0.5
- Now build the NLS stuff

* Mon Jan 15 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.0.4

* Mon Jan  8 2001 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.0.3

* Mon Jan  1 2001 Matthias Saou <http://freshrpms.net/>
- There is now a separate -devel package
- Fixed permissions
- Added an empty plugins directory
- Happy new year :-)

* Mon Dec  4 2000 Matthias Saou <http://freshrpms.net/>
- Upgraded to 1.0.2
- Added an empty themes directory

* Wed Nov  8 2000 Matthias Saou <http://freshrpms.net/>
- Re-did the spec file for RedHat 7.0

* Thu Apr 6 2000 Bill Wilson
- added INCLUDEDIR to the make install

* Fri Oct 29 1999 Gary Thomas <gdt@linuxppc.org>
- .spec file still broken

* Thu Oct 7 1999 David Mihm <davemann@ionet.net>
- fixed spec.

