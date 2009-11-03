# $Id$
# Authority: dag
# Upstream: Ramos Rubens <rubensr$users,sourceforge,net>


%{?fc1:%define _without_shmime 1}
%{?el3:%define _without_shmime 1}
%{?rh9:%define _without_shmime 1}
%{?rh7:%define _without_shmime 1}
%{?el2:%define _without_shmime 1}

Summary: CHM file viewer
Name: gnochm
Version: 0.9.11
Release: 1%{?dist}
License: GPL
Group: Applications/Publishing
URL: http://gnochm.sourceforge.net/

Source: http://dl.sf.net/gnochm/gnochm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-chm >= 0.7.0, python, pygtk2, pygtk2-libglade, gnome-python2,
BuildRequires: gnome-python2-bonobo, gnome-python2-gtkhtml2, gnome-python2-gconf
BuildRequires: scrollkeeper, gettext
BuildRequires: perl(XML::Parser), intltool

Requires: python-chm >= 0.7.0, python, pygtk2, pygtk2-libglade, gnome-python2
Requires: gnome-python2-bonobo, gnome-python2-gtkhtml2, gnome-python2-gconf
Requires: gnome-python2-canvas
%{!?_without_shmime:Requires: shared-mime-info}

%description
A CHM file viewer. Features are: full text search, bookmarks
support for external ms-its links, configurable support for
http links and internationalisation.

%prep
%setup

%build
%configure \
	--disable-mime-update \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

echo "MimeType=application/x-chm" >> %{buildroot}%{_datadir}/applications/gnochm.desktop

%{__install} -Dp -m0644 pixmaps/chmfile.png %{buildroot}%{_datadir}/icons/gnome/48x48/mimetypes/application-x-chm.png
%{__install} -Dp -m0644 pixmaps/chmfile.png %{buildroot}%{_datadir}/icons/gnome/48x48/mimetypes/gnome-mime-application-x-chm.png
%{__install} -Dp -m0644 pixmaps/gnochm.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/gnochm.png

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q || :

%postun
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_datadir}/gnome/help/gnochm/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/gnochm
%{_datadir}/application-registry/gnochm.*
%{_datadir}/applications/gnochm.desktop
%{_datadir}/gnochm/
%{_datadir}/mime/packages/gnochm.xml
%{_datadir}/mime-info/gnochm.*
%{_datadir}/omf/gnochm/
%{_datadir}/pixmaps/chmfile.png
%{_datadir}/pixmaps/gnochm.png
%{_datadir}/pixmaps/gnochm_logo.png
%{_datadir}/icons/hicolor/
%{_datadir}/icons/gnome/

%changelog
* Thu Sep 20 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.11-1
- Updated to release 0.9.11.

* Sun May 27 2007 Dag Wieers <dag@wieers.com> - 0.9.10-1
- Updated to release 0.9.10.

* Sat Nov 11 2006 Dag Wieers <dag@wieers.com> - 0.9.9-1
- Updated to release 0.9.9.

* Sat May 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.8-1
- Updated to release 0.9.8.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1
- Updated to release 0.9.7.

* Sun Sep 11 2005 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Sun Feb 13 2005 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Mon Nov 08 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Aug 24 2004 Dag Wieers <dag@wieers.com> - 0.9.2-1
- Updated to release 0.9.2.

* Mon Jul 05 2004 Dag Wieers <dag@wieers.com> - 0.9.1-2
- Added mime-type information. (Mariusz Smykula)

* Sun Jul 04 2004 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

* Tue Feb 24 2004 Dag Wieers <dag@wieers.com> - 0.8.0-0
- Updated to release 0.8.0.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Initial package. (using DAR)
