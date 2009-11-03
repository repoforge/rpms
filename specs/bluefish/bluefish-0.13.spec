# $Id$
# Authority: matthias

%define desktop_vendor freshrpms

Summary: Graphical web development application for experienced users
Name: bluefish
Version: 0.13
Release: 1.dag%{?dist}
Group: Development/Tools
License: GPL
URL: http://bluefish.openoffice.nl/
Source: http://pkedu.fbt.eitn.wau.nl/~olivier/downloads/bluefish-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel >= 2.0.6, pcre-devel >= 3.9, gnome-vfs2-devel
BuildRequires: aspell-devel, gettext, desktop-file-utils, perl

%description
Bluefish is a GTK+ HTML editor for the experienced web designer or
programmer. It is not finished yet, but already a very powerful site
creating environment. Bluefish has extended support for programming
dynamic and interactive websites, there is for example a lot of PHP
support.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
# These directories need to be created before make install
%{__mkdir_p} %{buildroot}%{_datadir}/{application-registry,applications}
%{__mkdir_p} %{buildroot}%{_datadir}/{mime-info,pixmaps}
# The actual install
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING README TODO
%{_bindir}/bluefish
%{_datadir}/bluefish
%{_datadir}/application-registry/*
%{_datadir}/applications/*.desktop
%{_datadir}/gnome/apps/Applications/bluefish.desktop
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*.png


%changelog
* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 0.13-1
- Update to 0.13.
- Clean up install section to use DESTDIR again.
- Added mime-info, application-registry and new pixmap files.
- Added doc files.

* Wed Mar  3 2004 Matthias Saou <http://freshrpms.net/> 0.12-2
- Added gnome-vfs support to the build.
- Updated source URL.
- Removed the conditional stuff for pre-versions.

* Tue Nov 25 2003 Matthias Saou <http://freshrpms.net/> 0.12-1
- Update to 0.12.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.11-2
- Rebuild for Fedora Core 1.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.11.

* Thu Jul 17 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.10.
- Spec file cleanup... still ugly workarounds for the problematic Makefiles.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Feb 18 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.
- Added Makefile patch to support DESTDIR.

* Wed Jan 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to the latest snapshot which should be more stable.

* Sat Jan 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.
- Major spec file updates based on the one from Matthias Haase.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Nov 19 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.
- Spec file simplifications since the build is now cleaner :-)

* Wed May  2 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup for Red Hat 7.1.
- Added a GNOME desktop entry.
- Compiled with kgcc and reported the problems encountered with gcc 2.96.

* Fri May 5 2000   Bo Forslund  <bo.forslund@abc.se>
  - fine tuning of the spec file
  - possible to build with all processors on smp machines
  - an entry for RedHats wmconfig

* Tue Mar 21 2000 CW Zuckschwerdt <zany@triq.net>
  - complete rewrite of spec file
  - relocateable on build-time
  - no privileges required while building
  - fix for install_location (should really be $(LIBDIR)/bluefish!)
  - included man, locale and lib into RPM (was seriously broken)

* Thu Jan 13 2000 Chris Lea <chrislea@luciddesigns.com>
  - Fixed up spec file some. bluefish-0.3.5

* Wed Nov 17 1999 Chris Lea <chrislea@luciddesigns.com>
  - added spec file. this is my third RPM that I've made a spec
    file for, so please be merciful if I've screwed something up

