# $Id: anjuta.spec,v 1.1 2004/02/26 10:51:55 thias Exp $

Summary: A versatile Integrated Development Environment (IDE) for C and C++.
Name: anjuta
Version: 1.2.1
Release: 1.fr
License: GPL
Group: Development/Tools
Source: http://prdownloads.sourceforge.net/anjuta/anjuta-%{version}.tar.gz
URL: http://anjuta.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-root
Requires: libgnome >= 2.0.2, libglade2 >= 2.0.0, libgnomeui >= 2.0.2
Requires: libgnomeprintui22 >= 2.0.1
Requires: vte, pcre, libxml2
BuildRequires: libgnome-devel >= 2.0.2, libglade2-devel >= 2.0.0
BuildRequires: libgnomeui-devel >= 2.0.2, libgnomeprintui22-devel >= 2.0.1
BuildRequires: vte-devel, pcre-devel, libxml2-devel, gettext, gcc-c++
BuildRequires: scrollkeeper, ncurses-devel

%description
Anjuta is a versatile Integrated Development Environment (IDE) for C and C++ 
on GNU/Linux. It has been written for GTK/GNOME, and features a number of 
advanced programming features. It is basically a GUI interface for the 
collection of command line programming utilities and tools available for Linux. 
These are usually run via a text console, and can be unfriendly to use.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall
%find_lang %{name}
# Remove unpackaged files
rm -rf \
    %{buildroot}/usr/share/doc/%{name} \
    %{buildroot}%{_localstatedir}/scrollkeeper || :

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog FUTURE NEWS README THANKS TODO
%doc doc/ScintillaDoc.html
%{_bindir}/%{name}*
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}
%{_datadir}/mime-info/%{name}.mime
%{_datadir}/mimelnk/application/x-%{name}-project.desktop
%{_datadir}/omf/%{name}
%{_datadir}/pixmaps/%{name}
%{_mandir}/man1/*

%changelog
* Mon Feb 16 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-1.fr
- Update to 1.2.1.

* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 1.2.0-2.fr
- Added ncurses-devel build dependency.

* Tue Dec  9 2003 Matthias Saou <http://freshrpms.net/> 1.2.0-1.fr
- Update to 1.2.0 final.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1.98-1.fr
- Update to 1.1.98.
- Remove libzvt and pcre dependencies.
- Added gettext and scrollkeeper build dependencies, fails otherwise.
- Added help and omf files, and remove scrollkeeper files from the package.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 1.1.97-2.fr
- Rebuild for Fedora Core 1.

* Fri Jul 18 2003 Matthias Saou <http://freshrpms.net/>
- Update (at last) to 1.1.97.
- Removed freedesktop build switch (systems with libs recent enough have it!).
- Added mimelnk file.
- Removed scrollkeeper pre/post scriplets.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Removed epoch.

* Fri Mar 28 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.2.

* Sun Mar 16 2003 Matthias Saou <http://freshrpms.net/>
- Added freedesktop build options.

* Fri Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.1.

* Tue Nov  5 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0.0.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New menu entry.
- Removed scrollkeeper execution from pre/post scripts as it barfs badly!

* Thu Aug 15 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.0 beta1 (0.9.99).
- Added man pages.
- Added gnome-print dependency.

* Thu May  2 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.

* Sat Apr 27 2002 Matthias Saou <http://freshrpms.net/>
- Added missing Requires and BuildRequires, thanks to Ralf Ertzinger.

* Wed Apr 24 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release with rewrite of the default included spec file.

