# $Id$
# Authority: dag

%define real_name gDesklets

Summary: Advanced architecture for desktop applets
Name: gdesklets
Version: 0.35.2
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.gdesklets.org/

Source: http://gdesklets.org/downloads/gDesklets-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgtop2-devel >= 2.8, python-devel >= 2.3, gcc-c++
BuildRequires: gnome-python2 >= 2.6, gnome-python2-gconf >= 2.4
BuildRequires: libcroco-devel, perl(XML::Parser), intltool, pygtk2-devel >= 2.4
BuildRequires: gtk2-devel, librsvg2 >= 2.8, pyorbit-devel
BuildRequires: librsvg2-devel, gettext, shared-mime-info
Requires: python >= 2.3, gnome-python2 >= 2.4, gnome-python2-gconf >= 2.4
Requires: gnome-python2-gnomevfs

%description
gDesklets provides an advanced architecture for desktop applets - tiny
displays sitting on your desktop in a symbiotic relationship of eye candy
and usefulness.

Populate your desktop with status meters, icon bars, weather sensors,
news tickers... whatever you can imagine! Virtually anything is possible
and maybe even available some day.

%prep
%setup -n %{real_name}-%{version}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|\@coredir\@|\$(datadir)/gdesklets|g;
		s|\@gnulocaledir\@|\$(datadir)/gdesklets/locale|g;
		s|\@localedir\@|\$(datadir)/gdesklets/locale|g;
		s|\@PIXMAPDIR\@|\$(datadir)/pixmaps|g;
	' Makefile.in */Makefile.in */*/Makefile.in */*/*/Makefile.in

%build
%configure \
	--disable-install-schemas
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}
%{__rm} -f %{buildroot}%{_datadir}/mime/aliases
%{__rm} -f %{buildroot}%{_datadir}/mime/subclasses
%{__rm} -f %{buildroot}%{_datadir}/mime/XMLnamespaces
%{__rm} -f %{buildroot}%{_datadir}/mime/globs
%{__rm} -f %{buildroot}%{_datadir}/mime/magic
%{__rm} -f %{buildroot}%{_datadir}/applications/mimeinfo.cache

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/gdesklets-display-thumbnail.schemas &>/dev/null
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/gdesklets.1*
%config %{_sysconfdir}/gconf/schemas/gdesklets-display-thumbnail.schemas
%{_bindir}/gdesklets*
%{_datadir}/applications/gdesklets.desktop
%{_datadir}/gdesklets/
%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-x-gdesklets-display.png
%{_datadir}/pixmaps/gdesklets.png
%{_datadir}/mime/application/x-gdesklets-display.xml
%{_datadir}/mime/packages/gdesklets.xml

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.35.2-1.2
- Rebuild for Fedora Core 5.

* Sat Oct  1 2005 Martin Ebourne <martin@zepler.org> - 0.35.2-2
- Fix build deps and mime install for FC4

* Mon Aug 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.35.2-1
- Updated to release 0.35.2.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 0.35.1-1
- Updated to release 0.35.1.

* Thu Mar 24 2005 Dag Wieers <dag@wieers.com> - 0.34.3-1
- Updated to release 0.34.3.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Sat Jan 01 2005 Dag Wieers <dag@wieers.com> - 0.32-1
- Updated to release 0.32.

* Wed Aug 28 2004 Dag Wieers <dag@wieers.com> - 0.30-1
- Updated to release 0.30.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 0.26.2-1
- Updated to release 0.26.2.

* Sun Mar 28 2004 Dag Wieers <dag@wieers.com> - 0.26.1-0
- Updated to release 0.26.1.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.26-0
- Updated to release 0.26.

* Tue Dec 30 2003 Dag Wieers <dag@wieers.com> - 0.25.1-0
- Updated to release 0.25.1.

* Mon Dec 29 2003 Dag Wieers <dag@wieers.com> - 0.25-0
- Updated to release 0.25.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.24.1-0
- Initial package. (using DAR)
