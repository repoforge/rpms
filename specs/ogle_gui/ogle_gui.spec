# $Id$

#define	cvs -cvs

Summary: A GNOME interface for the ogle DVD player
Name: ogle_gui
Version: 0.9.2
Release: 1.fr
License: GPL
Group: Applications/Multimedia
URL: http://www.dtek.chalmers.se/groups/dvd/
Source: http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}%{?cvs}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: ogle >= 0.9.1, gnome-libs >= 1.2.0, libglade
BuildRequires: ogle-devel >= 0.9.1, gnome-libs-devel >= 1.2.0, libglade-devel

%description
This is a GNOME interface for the ogle DVD player. Install this if you want
a graphical GUI for the ogle DVD player.

%prep
%setup -q -n %{name}-%{version}%{?cvs}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc COPYING
%{_libdir}/ogle
%{_datadir}/ogle_gui

%changelog
* Thu Nov  6 2003 Matthias Saou <http://freshrpms.net/> 0.9.2-1.fr
- Update to 0.9.2.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.9.1-4.fr
- Rebuild for Fedora Core 1.

* Mon Apr 14 2003 Matthias Saou <http://freshrpms.net/>
- Added missing libglade dependency.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.1.

* Tue Feb 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0.

* Sun Feb 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to CVS version, "release imminent" :-)

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- Removed the menu entry which is now in the main ogle package, as it makes
  more sense.

* Tue Aug  6 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.5.

* Mon Jul  1 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.4.

* Wed Jun 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.3.

* Wed May 15 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 7.3 (added a workaround for libxml2).
- Added the %%{?_smp_mflags} expansion.
- Now use the %%find_lang macro.

* Sat Dec  8 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2.

* Sat Nov 24 2001 Matthias Saou <http://freshrpms.net/>
- Rebuild against the current CVS Ogle version (new libdvdcontrol).

* Sun Nov  4 2001 Matthias Saou <http://freshrpms.net/>
- Removed the execution of automake that would have the package depend on
  gcc3 if it was installed at build time.

* Thu Nov  1 2001 Matthias Saou <http://freshrpms.net/>
- Fix for a stupid typo in the desktop entry.

* Wed Oct 31 2001 Matthias Saou <http://freshrpms.net/>
- Spec file cleanup and fixes (Requires: and %files)
- Addedd a GNOME desktop entry.

* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- New version, added patch to install pixmaps correctly

* Thu Sep 20 2001 Martin Norbäck <d95mback@dtek.chalmers.se>
- initial version

