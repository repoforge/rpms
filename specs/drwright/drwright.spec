# $Id$

# Authority: dag

# Upstream: Richard Hult <rhult@codefactory.se>

Summary: A program that reminds you to take wrist breaks
Name: drwright
Version: 0.17
Release: 0
License: GPL
Group: Applications/System
URL: http://www.imendio.com/projects/drwright/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.imendio.com/projects/drwright/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: pango-devel >= 1.0.99, gtk2-devel >= 2.0.4, GConf2-devel >= 1.2.0
BuildRequires: libglade2-devel >= 2.0.0, fontconfig

%description
DrWright is a program that forces you to take wrist breaks to rest your hands.

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

desktop-file-install --vendor gnome --delete-original \
  --dir %{buildroot}%{_datadir}/applications          \
  --add-category X-Red-Hat-Extra                      \
  %{buildroot}%{_datadir}/applications/*

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/drwright/

%changelog
* Tue Jun 24 2003 Dag Wieers <dag@wieers.com> - 0.17-0
- Updated to release 0.17.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 0.16-0
- Updated to release 0.16.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.15-0
- Initial package. (using DAR)
