# $Id$
# Authority: matthias

Summary: The GNU Krell Monitor, stacked system monitors in one process
Name: gkrellm
Version: 2.1.26
Release: 1
License: GPL
Group: Applications/System
Source: http://web.wt.net/~billw/gkrellm/gkrellm-%{version}.tar.bz2
Patch: gkrellm_i18n.patch
URL: http://www.gkrellm.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gtk2
BuildRequires: gtk2-devel, glib-devel, gettext, pkgconfig, sed
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
Requires : gkrellm = %{version}-%{release}, gtk2-devel

%description devel
Install this package if you intend to compile plugins to use with the
GKrellM monitor.


%package daemon
Summary: The GNU Krell Monitor Daemon
Group: System Environment/Daemons
Requires: glib >= 1.2
Obsoletes: gkrellm-server <= 2.1.21

%description daemon
This contains only the gkrellm daemon, which you can install on its own on
machines you intend to monitor with gkrellm from a different location.


%prep
%setup
%patch -p0 -b .i18n

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" glib12=1

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_libdir}/gkrellm2/plugins
mkdir -p %{buildroot}%{_datadir}/gkrellm2/themes
%{__make} install INSTALLROOT=%{buildroot}%{_prefix}
cat server/gkrellmd.conf | sed 's/#allow-host/allow-host/g' \
    > %{buildroot}%{_sysconfdir}/gkrellmd.conf
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYRIGHT CREDITS Changelog* README Themes.html
%{_bindir}/gkrellm
%{_libdir}/gkrellm2
%{_datadir}/gkrellm2
%{_mandir}/man1/gkrellm.1*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/gkrellm2
%{_libdir}/pkgconfig/gkrellm.pc

%files daemon
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/gkrellmd.conf
%{_bindir}/gkrellmd
%{_mandir}/man1/gkrellmd.1*

%changelog
* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 2.1.26-1.fr
- Update to 2.1.26.

* Wed Jan 21 2004 Matthias Saou <http://freshrpms.net/> 2.1.25-1.fr
- Update to 2.1.25.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 2.1.24-1.fr
- Update to 2.1.24.

* Thu Dec 18 2003 DenV <den@nekto.com> 2.1.23-2.fr
- Fix broken localisation.

* Thu Dec 18 2003 Matthias Saou <http://freshrpms.net/> 2.1.23-1.fr
- Update to 2.1.23.

* Wed Dec 17 2003 Matthias Saou <http://freshrpms.net/> 2.1.22-1.fr
- Update to 2.1.22.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.1.21-2.fr
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

