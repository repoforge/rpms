# $Id$

# Authority: dag

Summary: FM-Tuner program for GNOME
Name: gnomeradio
Version: 1.4
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://mfcn.ilo.de/gnomeradio/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://mfcn.ilo.de/gnomeradio/gnomeradio-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, intltool, libgnomeui-devel
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
A FM-Tuner program for GNOME.

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

%{__rm} -rf %{buildroot}/%{_localstatedir}/scrollkeeper/

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
%config %{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/omf/gnomeradio/
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Fri Jan 31 2003 Dag Wieers <dag@wieers.com> 1.4-0
- Initial package. (using DAR)
