# $Id$
# Authority: dag
# Upstream: Ramos Rubens <rubensr$users,sourceforge,net>

%{?dist: %{expand: %%define %dist 1}}

%define _without_shmime 1
%{?el4:%undefine _without_shmime}
%{?fc3:%undefine _without_shmime}
%{?fc2:%undefine _without_shmime}

Summary: CHM file viewer
Name: gnochm
Version: 0.9.4
Release: 1
License: GPL
Group: Applications/Publishing
URL: http://gnochm.sourceforge.net/

Source: http://dl.sf.net/gnochm/gnochm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-chm >= 0.7.0, python, pygtk2, pygtk2-libglade, gnome-python2,
BuildRequires: gnome-python2-bonobo, gnome-python2-gtkhtml2, gnome-python2-gconf

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
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
%find_lang %{name}

#%{__install} -Dp -m0644 gnochm.xml %{buildroot}%{_datadir}/mime/packages/gnochm.xml

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
%doc %{_mandir}/man?/*
%doc %{_mandir}/it/man?/*
%doc %{_datadir}/gnome/help/gnochm/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/gnochm
%{_datadir}/application-registry/gnochm.*
%{_datadir}/applications/gnochm.desktop
%{_datadir}/gnochm/
%{_datadir}/mime/packages/gnochm.xml
%{!?_without_shmime:%{_datadir}/mime/application/x-chm.xml}
%{!?_without_shmime:%exclude %{_datadir}/mime/XMLnamespaces}
%{!?_without_shmime:%exclude %{_datadir}/mime/globs}
%{!?_without_shmime:%exclude %{_datadir}/mime/magic}
%{_datadir}/mime-info/gnochm.*
%{_datadir}/omf/gnochm/
%{_datadir}/pixmaps/*.png
%exclude %{_localstatedir}/scrollkeeper/

%changelog
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
