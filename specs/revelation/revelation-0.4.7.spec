# $Id: revelation.spec 4007 2006-01-26 22:55:25Z dag $
# Authority: dag
# Upstream: Erik Grinaker <erikg$codepoet,no>
# Upstream: <revelation-list$oss,codepoet,no>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Graphical password manager
Name: revelation
Version: 0.4.7
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://oss.codepoet.no/revelation/

Source: ftp://oss.codepoet.no/revelation/revelation-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: python >= 2.3, python-devel, python-crypto >= 1.9
BuildRequires: gnome-keyring-devel, pygtk2-devel >= 2.4, gnome-python2
BuildRequires: gnome-vfs2-devel, libgnomeui-devel, gnome-python2-bonobo
BuildRequires: GConf2-devel, gnome-python2-gconf
%{?fc4:BuildRequires: gnome-python2-extras, gnome-panel-devel}
Requires: python >= 2.3, pygtk2 >= 2.4, python-crypto >= 1.9
Requires: gnome-python2-canvas, gnome-python2-gconf, gnome-python2-gnomevfs
Requires: gnome-python2-bonobo, cracklib, gnome-python2-applet

%description
Revelation is a password manager. It organizes accounts in
a tree structure, and stores them as AES-encrypted XML files.

%prep
%setup

%build
%configure \
	--disable-desktop-update \
	--disable-mime-update \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q || :

%postun
/usr/bin/update-mime-database %{_datadir}/mime &>/dev/null || :
/usr/bin/update-desktop-database -q || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/revelation.schemas
%{_bindir}/revelation
%{python_sitearch}/revelation/
%{_datadir}/applications/revelation.desktop
%{_datadir}/revelation/
%{_datadir}/icons/hicolor/*/apps/revelation.png
%{_datadir}/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-revelation.png
%{_datadir}/icons/hicolor/scalable/filesystems/revelation-fallback-folder.svg
%{_datadir}/icons/hicolor/scalable/filesystems/revelation-fallback-folder-open.svg
%{_datadir}/mime/packages/revelation.xml

%config %{_sysconfdir}/gconf/schemas/revelation-applet.schemas
%{_libdir}/bonobo/servers/GNOME_RevelationApplet.server
%{_libexecdir}/revelation-applet
%{_datadir}/icons/hicolor/*/apps/revelation-locked.png

%changelog
* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 0.4.7-1 - 4007+/dag
- Updated to release 0.4.7.

* Fri Jan 26 2006 Dag Wieers <dag@wieers.com> - 0.4.6-1
- Updated to release 0.4.6.

* Fri Aug 26 2005 Dag Wieers <dag@wieers.com> - 0.4.5-1
- Updated to release 0.4.5.

* Sun Aug 07 2005 Dag Wieers <dag@wieers.com> - 0.4.4-1
- Updated to release 0.4.4.

* Fri Apr 01 2005 Dag Wieers <dag@wieers.com> - 0.4.3-1
- Updated to release 0.4.3.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Mon Mar 21 2005 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Wed Feb 09 2005 Dag Wieers <dag@wieers.com> - 0.4.0-2
- Added missing gnome-python2-gnomevfs requirement. (Bob Dundon)

* Tue Feb 08 2005 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0

* Tue Sep 28 2004 Dag Wieers <dag@wieers.com> - 0.3.4-1
- Updated to release 0.3.4.

* Mon Aug 30 2004 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Updated to release 0.3.3.

* Mon Aug 09 2004 Dag Wieers <dag@wieers.com> - 0.3.2-1
- Updated to release 0.3.2.
- Updated to release 0.3.1.

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 0.3.0-3
- Install schema.

* Thu Apr 08 2004 Dag Wieers <dag@wieers.com> - 0.3.0-2
- Added gnome-python2-gconf dependency. (Erik Grinaker)

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 0.3.0-1
- Updated to release 0.3.0.

* Wed Mar 31 2004 Dag Wieers <dag@wieers.com> - 0.2.1-1
- Cosmetic rebuild for Group-tag and BuildArch-tag.

* Tue Mar 02 2004 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Updated to release 0.2.1.

* Sun Feb 22 2004 Dag Wieers <dag@wieers.com> - 0.2.0-0
- Updated to release 0.2.0.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 0.1.2-0
- Updated to release 0.1.2.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 0.1.1-0
- Initial Package. (using DAR)
