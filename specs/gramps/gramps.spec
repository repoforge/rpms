# $Id$

# Authority: dag
# Upstream: Laurent Protois <laurent,protois$free,fr>

%define _localstatedir /var/lib

Summary: Genealogical Research and Analysis Management Programming System
Name: gramps
Version: 2.0.9
Release: 1
License: GPL
Group: Applications/Editors
URL: http://gramps.sourceforge.net/

Source: http://dl.sf.net/gramps/gramps-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf >= 2.52, automake >= 1.6, scrollkeeper >= 0.1.4
BuildRequires: gnome-python2-canvas, gnome-python2-gconf
BuildRequires: pygtk2, pygtk2-libglade, gettext
BuildRequires: desktop-file-utils

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
%configure \
	 --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall \
	GNOME_DATADIR="%{buildroot}%{_datadir}"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge --delete-original \
	--add-category X-Red-Hat-Base                    \
	--add-category Application                       \
	--add-category Utility                           \
	--dir %{buildroot}%{_datadir}/applications       \
	%{buildroot}%{_datadir}/applications/%{name}.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* FAQ INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
#%doc %{_datadir}/gnome/help/gramps-manual/
#%doc %{_datadir}/gnome/help/extending-gramps/
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/gramps/
%{_datadir}/omf/gramps/
%{_sysconfdir}/gconf/schemas/gramps.schemas
%{_datadir}/application-registry/gramps.applications
%{_datadir}/icons/*/*/*/*.png
%{_datadir}/mime-info/gramps.*
%{_datadir}/mime/application/*.xml
%{_datadir}/mime/packages/gramps.xml
%exclude %{_datadir}/mime/aliases
%exclude %{_datadir}/mime/XMLnamespaces
%exclude %{_datadir}/mime/globs
%exclude %{_datadir}/mime/magic
%exclude %{_datadir}/mime/subclasses
 
%changelog
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
