# $Id$

# Authority: dag
# Upstream: Conglomerate Developers <conglomerate-devel@lists.copyleft.no>

Summary: Information authoring, management, and transformation system.
Name: conglomerate
Version: 0.7.12
Release: 0
License: GPL
Group: Applications/Text
URL: http://www.conglomerate.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/conglomerate/conglomerate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libxml2-devel >= 2.0, libgnomeui-devel >= 2.0, libglade2-devel >= 2.0
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

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

#### FIXME: Fix the intltool problem. (Please fix upstream)
#%{__perl} -pi.orig -e 's|/home/david/jhbuilt/share/intltool|%{_datadir}/intltool|' intltool-merge.in

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/ 
%{__rm} -f %{buildroot}%{_datadir}/pixmaps/ChangeLog

%post
scrollkeeper-update -q || :
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%doc %{_datadir}/gnome/help/conglomerate/
#%doc %{_datadir}/gtk-doc/html/conglomerate/
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/application-registry/*.applications
%{_datadir}/applications/*.desktop
%{_datadir}/conglomerate/
%{_datadir}/mime-info/*
%{_datadir}/omf/conglomerate/
%{_datadir}/pixmaps/*.png

%changelog
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
