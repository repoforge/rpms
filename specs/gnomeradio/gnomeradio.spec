# $Id$
# Authority: dag
# Upstream: Jörgen Scheibengruber <mfcn$wh-hms,uni-ulm,de>

Summary: Graphical FM-Tuner program
Name: gnomeradio
Version: 1.5
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://mfcn.ilo.de/gnomeradio/

Source: http://www.wh-hms.uni-ulm.de/~mfcn/gnomeradio/packages/gnomeradio-%{version}.tar.gz
Patch: gnomeradio-1.4-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, intltool, libgnomeui-devel
BuildRequires: scrollkeeper, gnome-libs-devel, gcc-c++

Requires(post): scrollkeeper

%description
A FM-Tuner program for GNOME.

%prep
%setup
#patch -p1

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%doc %{_datadir}/gnome/help/gnomeradio/
%config %{_sysconfdir}/gconf/schemas/gnomeradio.schemas
%{_bindir}/gnomeradio
%{_datadir}/applications/gnomeradio.desktop
%{_datadir}/omf/gnomeradio/
%{_datadir}/pixmaps/*.png

%changelog
* Sun Mar 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.6-2
- gcc-c++ buildrequirement added.

* Wed Mar 08 2006 Dag Wieers <dag@wieers.com> - 1.6-1
- Updated to release 1.6.

* Wed Mar 08 2006 Dag Wieers <dag@wieers.com> - 1.5-1
- Updated to release 1.5.

* Sat Nov 06 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Fixed build problem with gnome 2.6+. (Alan Cox)

* Fri Jan 31 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
