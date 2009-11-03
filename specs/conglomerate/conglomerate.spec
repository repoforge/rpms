# $Id$
# Authority: dag
# Upstream: Conglomerate Developers <conglomerate-devel$lists,copyleft,no>

Summary: Information authoring, management, and transformation system
Name: conglomerate
Version: 0.9.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Text
URL: http://www.conglomerate.org/

Source: http://dl.sf.net/conglomerate/conglomerate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libxml2-devel >= 2.0, gcc-c++, gtk2-devel >= 2.4
BuildRequires: libgnomeui-devel >= 2.0, libglade2-devel >= 2.0
BuildRequires: libgnomeprintui22-devel, gtksourceview-devel, gtk-doc
BuildRequires: scrollkeeper, intltool, perl(XML::Parser)

Requires: scrollkeeper

%description
Conglomerate is a project to create a complete structured information
authoring, management, archival, revision control and transformation
system. Conglomerate uses XML semantics and powerful graphical editing,
coupled with a centralised storage model and a flexible transformation
language to create an environment which is easy to use, produces high-
quality structured output, and lets the user target several output media
with a single source document.

%prep
%setup

%build
%configure \
    --enable-optimization \
    --enable-printing \
    --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
scrollkeeper-update -q || :
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun
scrollkeeper-update -q || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/conglomerate/
%doc %{_datadir}/gtk-doc/html/conglomerate/
%config %{_sysconfdir}/gconf/schemas/conglomerate.schemas
%{_bindir}/conglomerate
%{_datadir}/application-registry/conglomerate.applications
%{_datadir}/applications/conglomerate.desktop
%{_datadir}/conglomerate/
%{_datadir}/mime-info/conglomerate.*
%{_datadir}/omf/conglomerate/
%{_datadir}/pixmaps/conglomerate-icon-16.png
%{_datadir}/pixmaps/conglomerate/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1.2
- Rebuild for Fedora Core 5.

* Wed Jul 13 2005 Dag Wieers <dag@wieers.com> - 0.9.1-1
- Updated to release 0.9.1.

* Sun Mar 20 2005 Dag Wieers <dag@wieers.com> - 0.9.0-1
- Updated to release 0.9.0.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 0.7.16-1
- Updated to release 0.7.16.

* Tue Nov  2 2004 Matthias Saou <http://freshrpms.net> 0.7.15-1
- Update to 0.7.15.
- Enable printing again, it seems to work now.

* Tue Jul  6 2004 Matthias Saou <http://freshrpms.net> 0.7.14-2
- Added missing build requirements.
- Enabled printing support and optimization... not! Build for printing broken.

* Thu Jun 14 2004 Dag Wieers <dag@wieers.com> - 0.7.14-1
- Updated to release 0.7.14.
- Updated to release 0.7.13.

* Wed Feb 18 2004 Dag Wieers <dag@wieers.com> - 0.7.12-0
- Updated to release 0.7.12.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.7.11-0
- Updated to release 0.7.11.

* Tue Jan 06 2004 Dag Wieers <dag@wieers.com> - 0.7.9-0
- Updated to release 0.7.9.

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 0.7.8-0
- Updated to release 0.7.8.

* Thu Oct 30 2003 Dag Wieers <dag@wieers.com> - 0.7.6-0
- Updated to release 0.7.6.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.7.5-0
- Updated to release 0.7.5.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.7.3-0
- Updated to release 0.7.3.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Updated to release 0.7.2.

* Tue Sep 02 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated to release 0.7.1.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Thu Jun 26 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Initial package. (using DAR)
