# $Id$
# Authority: dag

Summary: Graphical webcam application featuring various image filters
Name: camorama
Version: 0.17
Release: 0.2%{?dist}
Group: Applications/Multimedia
License: GPL
URL: http://camorama.fixedgear.org/

Source: http://camorama.fixedgear.org/downloads/camorama-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gdk-pixbuf-devel, libgnomeui-devel >= 2.0, gtk+-devel >= 1.2
BuildRequires: GConf, libglade-devel, libpng-devel, gettext

%description
Camorama is a GNOME 2 Webcam application featuring various image filters.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

### FIXME: Error on file "camorama.desktop": Error in section Desktop Entry at line 16: Invalid characters in locale name
#desktop-file-install --vendor gnome --delete-original \
#	--add-category X-Red-Hat-Base                 \
#	--dir %{buildroot}%{_datadir}/applications    \
#	%{buildroot}%{_datadir}/applications/%{name}.desktop


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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%config %{_sysconfdir}/gconf/schemas/*
%{_bindir}*
%{_datadir}/pixmaps/*
%{_datadir}/camorama/
%{_datadir}/applications/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-0.2
- Rebuild for Fedora Core 5.

* Thu Aug 21 2003 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Tue Jan 21 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Initial package. (using DAR)
