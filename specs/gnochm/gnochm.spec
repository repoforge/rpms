# $Id$
# Authority: dag
# Upstream: Ramos Rubens <rubensr$users,sourceforge,net>

Summary: CHM file viewer
Name: gnochm
Version: 0.9.1
Release: 2
License: GPL
Group: Applications/Publishing
URL: http://gnochm.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gnochm/gnochm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python-chm >= 0.7.0, python, pygtk2, pygtk2-libglade, gnome-python2,
BuildRequires: gnome-python2-bonobo, gnome-python2-gtkhtml2, gnome-python2-gconf

Requires: python-chm >= 0.7.0, python, pygtk2, pygtk2-libglade, gnome-python2
Requires: gnome-python2-bonobo, gnome-python2-gtkhtml2, gnome-python2-gconf
Requires: gnome-python2-canvas
#Requires: shared-mime-info

%description
A CHM file viewer. Features are: full text search, bookmarks
support for external ms-its links, configurable support for
http links and internationalisation.

%prep
%setup

%{__cat} <<EOF >gnochm.xml
<?xml version="1.0" encoding="utf-8"?>
<mime-info xmlns="http://www.freedesktop.org/standards/shared-mime-info">
	<mime-type type="application/x-chm">
		<comment>HTML Help</comment>
		<glob pattern="*.chm"/>
	</mime-type>
</mime-info>
EOF

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall
%find_lang %{name}

%{__install} -D -m0644 gnochm.xml %{buildroot}%{_datadir}/mime/packages/gnochm.xml

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%postun
scrollkeeper-update -q || :
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/gnochm/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/gnochm
%{_datadir}/application-registry/gnochm.*
%{_datadir}/applications/gnochm.desktop
%{_datadir}/gnochm/
%{_datadir}/mime/packages/gnochm.xml
%{_datadir}/mime-info/gnochm.*
%{_datadir}/omf/gnochm/
%{_datadir}/pixmaps/*.png
%exclude %{_localstatedir}/scrollkeeper/

%changelog
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
