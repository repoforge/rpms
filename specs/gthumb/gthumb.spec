# $Id$

Summary: An image viewer and browser for the GNOME desktop.
Name: gthumb
Version: 2.2.1
Release: 1.fr
License: GPL
URL: http://gthumb.sourceforge.net/
Group: Applications/Multimedia
Source: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: scrollkeeper, libexif, libgnomeui >= 2.0.0, libgnomeprintui22
BuildRequires: pkgconfig, scrollkeeper, gettext, libexif-devel
BuildRequires: libpng-devel, libjpeg-devel, libtiff-devel
BuildRequires: libgnomeui-devel >= 2.0.0, libgnomeprintui22-devel

%description
Image viewer and browser for the GNOME Desktop. View single images (including
GIF animations). Supported image types are: BMP, JPEG, GIF, PNG, TIFF, ICO,
XPM. View EXIF data attached to JPEG images. View in fullscreen mode. View
images rotated, flipped, in black and white.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
rm -rf %{buildroot}%{_localstatedir}
strip %{buildroot}%{_libdir}/%{name}/{*.so,modules/*.so}
find %{buildroot}%{_libdir} -name "*.a" -o -name "*.la" | xargs rm -f
%find_lang %{name}

%post
/usr/bin/scrollkeeper-update -q || :
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%postun
/usr/bin/scrollkeeper-update -q || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%config %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_libdir}/bonobo/servers/*
%{_libdir}/%{name}
%{_libexecdir}/%{name}*
%{_datadir}/application-registry/%{name}.applications
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/omf/%{name}
%{_datadir}/pixmaps/%{name}.png

%changelog
* Mon Feb  9 2004 Matthias Saou <http://freshrpms.net/> 2.2.1-1.fr
- Update to 2.2.1.

* Sun Jan  4 2004 Matthias Saou <http://freshrpms.net/> 2.2.0-1.fr
- Update to 2.2.0.

* Wed Dec 10 2003 Matthias Saou <http://freshrpms.net/> 2.1.9-1.fr
- Update to 2.1.9.
- Remove all .a and .la files, as nothing uses them for now anyway.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.1.8-1.fr
- Update to 2.1.8.
- Rebuild for Fedora Core 1.

* Tue Sep 30 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.6.
- Added explicit stripping of modules.

* Sun Aug 24 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.4.

* Mon Aug  4 2003 Matthias Saou <http://freshrpms.net/>
- Fix for the gconf schema file.

* Fri Jul 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.3.
- Updated %%description.
- Fixed BuildRequires, thanks to mach :-)

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.2.

* Mon Apr  7 2003 Matthias Saou <http://freshrpms.net/>
- Quiet the gconftool post output.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.1.
- Added GCONF install stuff.
- Excluded all .a and .la files.
- Rebuilt for Red Hat Linux 9.

* Tue Jan 21 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.0.0.
- Added libexif support.

* Tue Nov 12 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.104.

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.103 (GNOME 2 branch).
- Rebuilt for Red Hat Linux 8.0.

* Wed Sep 18 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.13.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.12.
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Sun Feb 24 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.10.

* Sun Dec 30 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.9.

* Sun Dec  9 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.8.

* Sun Nov 18 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.7.

* Sun Oct 28 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

