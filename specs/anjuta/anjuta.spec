# $Id$
# Authority: matthias
# Upstream: <anjuta-devel$lists,sourceforge,net>

Summary: Versatile Integrated Development Environment (IDE) for C and C++
Name: anjuta
Version: 1.2.3
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://anjuta.sourceforge.net/
Source: http://dl.sf.net/anjuta/anjuta-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: libgnome >= 2.0.2, libglade2 >= 2.0.0, libgnomeui >= 2.0.2
Requires: libgnomeprintui22 >= 2.0.1
%{!?dtag:Requires: gettext-devel}
%{?el4:Requires: gettext-devel}
%{?fc3:Requires: gettext-devel}
Requires: gettext
BuildRequires: libgnome-devel >= 2.0.2, libglade2-devel >= 2.0.0
BuildRequires: libgnomeui-devel >= 2.0.2, libgnomeprintui22-devel >= 2.0.1
BuildRequires: vte-devel, pcre-devel, libxml2-devel, gcc-c++
BuildRequires: scrollkeeper, ncurses-devel, perl(XML::Parser), intltool
%{!?dtag:BuildRequires: gettext-devel}
%{?el4:BuildRequires: gettext-devel}
%{?fc3:BuildRequires: gettext-devel}
BuildRequires: gettext

%description
Anjuta is a versatile Integrated Development Environment (IDE) for C and C++
on GNU/Linux. It has been written for GTK/GNOME, and features a number of
advanced programming features. It is basically a GUI interface for the
collection of command line programming utilities and tools available for Linux.
These are usually run via a text console, and can be unfriendly to use.


%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream)
%{__perl} -pi.orig -e 's|^(plugindir) = .+$|$1 = \$(libdir)/anjuta|' \
    Makefile.in */Makefile.in */*/Makefile.in


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}


%post
scrollkeeper-update
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
scrollkeeper-update
update-desktop-database %{_datadir}/applications &>/dev/null || :


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog FUTURE NEWS README TODO
%doc doc/ScintillaDoc.html
%{_bindir}/anjuta*
%{_libdir}/anjuta/
%exclude %{_libdir}/anjuta/*.a
%{_datadir}/anjuta/
%{_datadir}/applications/anjuta.desktop
%{_datadir}/gnome/help/anjuta/
%{_datadir}/mime-info/anjuta.mime
%{_datadir}/mimelnk/application/x-anjuta-project.desktop
%{_datadir}/omf/anjuta/
%{_datadir}/pixmaps/anjuta/
%{_mandir}/man1/*
%exclude %{_datadir}/doc/anjuta/
%exclude %{_localstatedir}/scrollkeeper/


%changelog
* Thu Jun  2 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3, bugfix release.

* Thu Feb  3 2005 Matthias Saou <http://freshrpms.net/> 1.2.2-4
- Added gettext-devel dep on FC3 to get gettext stuff included in new projects
  properly (thanks to Paul Frields).

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 1.2.2-3
- Made the lack of update-desktop-database less dramatic.

* Sat Oct 16 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-2
- Added update-desktop-database scriplet calls.

* Sun Jun 13 2004 Dag Wieers <dag@wieers.com> - 1.2.2-1
- Fixes for x86_64.
- Added scrollkeeper to %%post and %%postun.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2.
- Removed THANKS doc file.

* Mon Feb 16 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-1
- Update to 1.2.1.

* Fri Feb  6 2004 Matthias Saou <http://freshrpms.net/> 1.2.0-2
- Added ncurses-devel build dependency.

* Tue Dec  9 2003 Matthias Saou <http://freshrpms.net/> 1.2.0-1
- Update to 1.2.0 final.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.1.98-1
- Update to 1.1.98.
- Remove libzvt and pcre dependencies.
- Added gettext and scrollkeeper build dependencies, fails otherwise.
- Added help and omf files, and remove scrollkeeper files from the package.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 1.1.97-2
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

