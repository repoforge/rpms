# $Id$
# Authority: matthias
# Upstream: David A Knight <david$ritter,demon,co,uk>

Summary: Web Site CReating and Editing EnvironMent for GNOME
Name: screem
Version: 0.12.1
Release: 1%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.screem.org/
Source: http://dl.sf.net/screem/screem-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): scrollkeeper, GConf2
Requires(postun): scrollkeeper
BuildRequires: GConf2-devel, pkgconfig, scrollkeeper, gettext, krb5-devel
BuildRequires: gcc-c++, neon-devel, openssl-devel, perl(XML::Parser)
BuildRequires: libgnomeui-devel >= 2.2.0
BuildRequires: libgnomeprintui22-devel >= 2.2.0
BuildRequires: gtkhtml2-devel >= 2.2.0
BuildRequires: gtksourceview-devel >= 0.3.0
BuildRequires: libcroco-devel >= 0.5.0
BuildRequires: dbus-devel, dbus-glib

%description
SCREEM (Site CReating and Editing EnvironMent) is an integrated development
environment for the creation and maintainance of websites and pages.


%prep
%setup


%build
%configure \
    --with-ssl \
    --disable-update-mime \
    --disable-update-desktop
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}


%clean
%{__rm} -rf %{buildroot}


%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 --makefile-install-rule \
    %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
scrollkeeper-update -q || :
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database %{_datadir}/applications || :

%postun
scrollkeeper-update -q || :
update-mime-database %{_datadir}/mime &>/dev/null || :
update-desktop-database %{_datadir}/applications || :


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/screem
%{_libdir}/screem/
%{_datadir}/application-registry/screem.applications
%{_datadir}/applications/screem.desktop
%{_datadir}/gnome/help/screem/
%{_datadir}/mime/packages/screem.xml
%{_datadir}/mime-info/screem.*
%{_datadir}/omf/screem/
%{_datadir}/pixmaps/screem*
%{_datadir}/screem/


%changelog
* Fri Apr  1 2005 Matthias Saou <http://freshrpms.net/> 0.12.1-1
- Update to 0.12.1 after nearly one year without updating...
- Add mime database file.
- Add update-mime-database and update-desktop-database calls.

* Fri Apr 30 2004 Matthias Saou <http://freshrpms.net/> 0.10.2-1
- Update to 0.10.2.

* Mon Mar 29 2004 Matthias Saou <http://freshrpms.net/> 0.10.0-1
- Update to 0.10.0, only builds on Fedora Development for now.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.8.2-2
- Rebuild for Fedora Core 1.
- Enabled neon.

* Fri Oct 10 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2.
- Added all required build dependencies, thanks to mach.

* Thu Sep 18 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.1.

* Mon Sep 15 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.0.

* Fri Apr 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.2.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt (yes, it rebuilds at last!) for Red Hat Linux 9.

* Sun Mar 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.1.

* Fri Feb 14 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.6.0.

* Mon Sep 16 2002 Matthias Saou <http://freshrpms.net/>
- Fixed gdk-pixbuf dependency.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Mon Apr  8 2002 Matthias Saou <http://freshrpms.net/>
- Fixed the libxml dependency (was gnome-xml).

* Wed Apr 25 2001 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat 7.1.

* Thu Mar 15 2001 Matthias Saou <http://freshrpms.net/>
- Update to 0.4.1.

* Wed Feb 28 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

