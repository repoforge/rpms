# Authority: freshrpms
%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A GTK2 front-end for xine-lib.
Name: totem
Version: 0.99.3
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://www.hadess.net/totem.php3

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

PreReq: GConf2
BuildRequires: glib2-devel >= 2.1, intltool >= 0.20, gnome-vfs2-devel >= 2.1.6
BuildRequires: libgnomeui-devel >= 2.1.1, xine-lib-devel >= 1.0
BuildRequires: perl pkgconfig libglade-devel gettext XFree86-devel

%description
Totem is simple movie player for GNOME desktops based on xine. It
features a simple playlist, a full-screen mode, seek and volume
controls, as well as a pretty complete keyboard navigation system.

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

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
	%{__install} -m0644 data/%{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--add-category Application                    \
		--add-category AudioVideo                     \
		--dir %{buildroot}/%{_datadir}/applications   \
		data/%{name}.desktop
%endif

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}-video-thumbnail.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/totem/
%{_datadir}/mime-info/*.keys
%{_datadir}/pixmaps/*
%{_datadir}/application-registry/*.applications
%{_sysconfdir}/gconf/schemas/*.schemas
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sun Apr 20 2003 Dag Wieers <dag@wieers.com> - 0.96-0
- Initial package. (using DAR)
