# Authority: freshrpms
# Upstream: David A Knight <david@ritter.demon.co.uk>

Summary: Web Site CReating and Editing EnvironMent
Name: screem
Version: 0.7.0
Release: 0
License: GPL
Group: Development/Tools
URL: http://www.screem.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.screem.org/src/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgnome-devel >= 2.0, glib2-devel >= 2.0, ORBit2-devel >= 2.0
BuildRequires: libbonobo-devel >= 2.0, GConf2-devel >= 1.2, gnome-vfs2-devel >= 2.0
BuildRequires: linc-devel, bonobo-activation-devel, libxml2-devel
BuildRequires: libgnomeui-devel >= 2.2, libgnomecanvas-devel >= 2.0, gtk2-devel >= 2.0
BuildRequires: libart_lgpl-devel >= 2.0, libbonoboui-devel >= 2.2, pango-devel >= 1.0
BuildRequires: freetype-devel >= 2.0, atk-devel >= 1.0
BuildRequires: libglade2-devel >= 2.0, gtkhtml2-devel >= 2.0
BuildRequires: libgnomeprint22-devel, libgnomeprintui22-devel
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
SCREEM (Site CReating and Editing EnvironMent) is an integrated development
environment for the creation and maintainance of websites and pages.

%prep
%setup

%build
%configure \
	--disable-schemas-install \
	--with-gconf-source="%{buildroot}%{_localstatedir}/scrollkeeper/" \
	--with-gconf-schema="%{buildroot}%{_sysconfdir}/gconf/schemas/" \
	--with-ssl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's|/usr/share|\$\(datadir\)|g' pixmaps/Makefile
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall Applicationsdir="%{buildroot}%{_datadir}/gnome/apps/Development"
%find_lang %{name}
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING* docs/ NEWS README TODO
%doc %{_datadir}/gnome/help/screem/
%config %{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_libdir}/screem/
%{_datadir}/screem/
%{_datadir}/omf/screem/
%{_datadir}/gnome/apps/Development/*.desktop
%{_datadir}/application-registry/*
#%{_datadir}/mc/templates/*
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*

%changelog
* Sat Apr 12 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Sat Apr 12 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Sun Mar 23 2003 Dag Wieers <dag@wieers.com> - 0.6.1-0
- Updated to release 0.6.1.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.0-1
- Fixed artwork and hints-file due to Makefile problems.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.0-0
- Initial package. (using DAR)
