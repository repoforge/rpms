# $Id$
# Authority: dag
# Upstream: Erik Grinaker <erikg$codepoet,no>
# Upstream: <revelation-list$oss,codepoet,no>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

Summary: Graphical password manager
Name: revelation
Version: 0.4.14
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://revelation.olasagasti.info/

Source: https://bitbucket.org/erikg/revelation/downloads/revelation-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?el6:BuildRequires: cracklib-devel, gnome-python2-devel}
BuildRequires: cracklib-dicts
BuildRequires: cracklib-python
BuildRequires: GConf2-devel
BuildRequires: gnome-keyring-devel
BuildRequires: gnome-panel-devel
BuildRequires: gnome-python2-applet
BuildRequires: gnome-python2-bonobo
BuildRequires: gnome-python2-desktop
BuildRequires: gnome-python2-extras
BuildRequires: gnome-python2-gconf
BuildRequires: gnome-vfs2-devel
BuildRequires: intltool
BuildRequires: libgnomeui-devel
BuildRequires: perl(XML::Parser)
BuildRequires: pygtk2-devel >= 2.8
BuildRequires: python-crypto >= 1.9
BuildRequires: python-devel >= 2.3
Requires: cracklib
Requires: cracklib-dicts
Requires: cracklib-python
Requires: gnome-python2-applet
Requires: gnome-python2-bonobo
Requires: gnome-python2-canvas
Requires: gnome-python2-gconf
Requires: gnome-python2-gnomevfs
Requires: pygtk2 >= 2.4
Requires: python >= 2.3
Requires: python-crypto >= 1.9

%description
Revelation is a password manager. It organizes accounts in
a tree structure, and stores them as AES-encrypted XML files.

%prep
%setup

%build
%configure \
    --disable-desktop-update \
    --disable-mime-update \
    --disable-schemas-install \
    --with-cracklib-dict="/usr/share/cracklib/pw_dict"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__rm} -f %{buildroot}%{_datadir}/revelation/pwdict*

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database -q || :
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &> /dev/null || :

%preun
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null || :

%postun
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database -q || :
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &> /dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/revelation.schemas
%{_bindir}/revelation
%{python_sitearch}/revelation/
%{_datadir}/applications/revelation.desktop
%{_datadir}/revelation/
%{_datadir}/icons/hicolor/*/apps/revelation.png
%{_datadir}/icons/hicolor/*/apps/revelation.svg
%{_datadir}/icons/hicolor/*/apps/revelation-locked.png
%{_datadir}/icons/hicolor/48x48/mimetypes/gnome-mime-application-x-revelation.png
%{_datadir}/mime/packages/revelation.xml

%changelog
* Sun Jul 15 2012 Dag Wieers <dag@wieers.com> - 0.4.14-1
- Updated to release 0.4.14.

* Fri Jun 08 2012 Dag Wieers <dag@wieers.com> - 0.4.13-1
- Updated to release 0.4.13.

* Tue Nov 15 2011 Dag Wieers <dag@wieers.com> - 0.4.12-1
- Updated to release 0.4.12.

* Tue Jan 16 2007 Dag Wieers <dag@wieers.com> - 0.4.11-1
- Updated to release 0.4.11.

* Mon Jan 15 2007 Dag Wieers <dag@wieers.com> - 0.4.9-1
- Updated to release 0.4.9.

* Wed Jan 10 2007 Dag Wieers <dag@wieers.com> - 0.4.8-1
- Updated to release 0.4.8.

* Tue Feb 07 2006 Dag Wieers <dag@wieers.com> - 0.4.7-1
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
