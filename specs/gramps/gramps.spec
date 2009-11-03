# $Id$
# Authority: dag
# Upstream: Laurent Protois <laurent,protois$free,fr>

%define desktop_vendor rpmforge
%define _localstatedir /var/lib

Summary: Genealogical Research and Analysis Management Programming System
Name: gramps
Version: 2.2.8
Release: 2%{?dist}
License: GPL
Group: Applications/Editors
URL: http://gramps.sourceforge.net/

Source: http://dl.sf.net/gramps/gramps-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf >= 2.52, automake >= 1.6, scrollkeeper >= 0.1.4
BuildRequires: gnome-python2-canvas, gnome-python2-gconf
BuildRequires: pygtk2, pygtk2-libglade, gettext, pkgconfig
BuildRequires: desktop-file-utils, gnome-doc-utils, intltool, perl(XML::Parser)

Requires(post): scrollkeeper
Requires: python >= 2.2, gnome-python2-canvas, gnome-python2-gconf
Requires: pygtk2, pygtk2-libglade

%description
gramps (Genealogical Research and Analysis Management Programming
System) is a GNOME based genealogy program supporting a Python
based plugin system.

%prep
%setup

%build
%configure --enable-packager-mode
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	GNOME_DATADIR="%{buildroot}%{_datadir}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --delete-original                   \
	--vendor %{desktop_vendor}                       \
	--add-category X-Red-Hat-Base                    \
	--add-category Application                       \
	--add-category Utility                           \
	--dir %{buildroot}%{_datadir}/applications       \
	%{buildroot}%{_datadir}/applications/gramps.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FAQ INSTALL NEWS README TODO
%doc %{_mandir}/man1/gramps.1*
%{_sysconfdir}/gconf/schemas/gramps.schemas
%{_bindir}/gramps
%{_datadir}/application-registry/gramps.applications
%{_datadir}/applications/%{desktop_vendor}-gramps.desktop
%{_datadir}/gramps/
%{_datadir}/pixmaps/gramps.png
%{_datadir}/icons/gnome/48x48/mimetypes/*.png
%{_datadir}/icons/gnome/scalable/mimetypes/*.svg
%{_datadir}/mime-info/gramps.*
%{_datadir}/mime/packages/gramps.xml
%{_datadir}/omf/gramps/
%{_datadir}/gnome/help/gramps/

%changelog
* Mon Jun 25 2007 Dries Verachtert <dries@ulyssis.org> - 2.2.8-2
- Added the pkgconfig buildrequirement, thanks to Jorrit Jorritsma.

* Mon May 28 2007 Dries Verachtert <dries@ulyssis.org> - 2.2.8-1
- Updated to release 2.2.8.

* Mon Jan 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.2.5-1
- Updated to release 2.2.5.

* Mon Nov 27 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.3-1
- Updated to release 2.2.3.

* Sat May 06 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.11-1
- Updated to release 2.0.11.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.10-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.10-1
- Updated to release 2.0.10.

* Sun Jan 15 2006 Dag Wieers <dag@wieers.com> - 2.0.9-2
- Fixed mime and desktop installation.

* Fri Dec 16 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.9-1
- Updated to release 2.0.9.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Updated to release 1.0.2.

* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Mon Dec 08 2003 Dag Wieers <dag@wieers.com> - 0.98-0
- Updated to release 0.98.

* Tue Oct 07 2003 Dag Wieers <dag@wieers.com> - 0.9.5-0
- Updated to release 0.9.5.

* Tue Sep 30 2003 Dag Wieers <dag@wieers.com> - 0.9.4-0
- Updated to release 0.9.4.

* Wed Jul 16 2003 Dag Wieers <dag@wieers.com> - 0.9.3-0
- Updated to release 0.9.3.

* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Updated to release 0.9.2.

* Mon Apr 21 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Updated to release 0.9.0.

* Sun Feb 16 2003 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Initial package. (using DAR)
