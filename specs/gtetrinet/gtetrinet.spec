# $Id$
# Authority: matthias

Summary: A GNOME version of a tetris game playable on the net.
Name: gtetrinet
Version: 0.7.5
Release: 1
License: GPL
Group: Amusements/Games
Source0: http://download.sourceforge.net/gtetrinet/%{name}-%{version}.tar.bz2
Source1: tetrinet.txt
Source2: http://www.mavit.pwp.blueyonder.co.uk/mmr-sounds-1.0.tar.gz
URL: http://gtetrinet.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libgnome >= 2.0.0, libgnomeui >= 2.0.0
BuildRequires: libgnome-devel >= 2.0.0, libgnomeui-devel >= 2.0.0, GConf2-devel
BuildRequires: gettext

%description
GTetrinet is a client program for the popular Tetrinet game, a multiplayer
tetris game that is played over the internet. (If you don't know what Tetrinet
is, check out tetrinet.org)

%prep
%setup

%build
%configure
perl -pi -e 's|Exec=%{name}|Exec=%{_prefix}/games/%{name}|g' %{name}.desktop
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%find_lang %{name}
cp -a %{SOURCE1} .
tar -xzvf %{SOURCE2} -C %{buildroot}/%{_datadir}/gtetrinet/themes/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README tetrinet.txt
%config %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_prefix}/games/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man6/%{name}.6*

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.7.5-1.fr
- Update to 0.7.5.
- Rebuild for Fedora Core 1.

* Fri Aug 29 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.4.
- Update to reflect the new style desktop entry.

* Wed Jun 25 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.3.

* Wed Jun 11 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.2.

* Tue Apr 15 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar 18 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.7.0.

* Tue Feb 11 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.2.

* Wed Feb  5 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.6.0.

* Sat Jan 11 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.2.

* Tue Jan  7 2003 Matthias Saou <http://freshrpms.net/>
- Updated to 0.5.1.

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Updated to 0.4.3.
- Spec file cleanup, now use %%find_lang.
- New menu entry.

* Sun Oct 20 2002 Peter Oliver <p.d.oliver@mavit.freeserve.co.uk>
- Updated to 0.4.2.
- Added my preferred theme to the package.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %%{?_smp_mflags} expansion.

* Wed Apr 26 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and rebuilt for Red Hat 7.1.
- I think this was one of my first RPMs ;-)

* Mon Jul 03 2000 Matthias Saou <http://freshrpms.net/>
  [gtetrinet-0.4.1-1]
- Updated to version 0.4.1
- Cleaned up the build process
- Added the original tetrinet.txt help file

* Mon Jan 24 2000       <jasper@stack.nl>
  - Fixed typo in spec file <Shane Smit>

* Tue Dec 21 1999       <jasper@stack.nl>
  - First RPM release

