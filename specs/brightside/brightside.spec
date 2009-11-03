# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Add reactivity to the corners and edges of your GNOME desktop.
Name: brightside
Version: 1.4.0
Release: 1%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://catmur.co.uk/~ed/main/brightside/

Source: http://files.catmur.co.uk/brightside/brightside-%{version}.tar.bz2
Patch0: brightside-1.4.0-gconf-mouse-speed.patch
Patch1: brightside-1.4.0-libwnck.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, intltool
BuildRequires: libwnck-devel >= 2.6.0, libgnomeui-devel >= 2.6.0, libglade2-devel >= 2.2.0
BuildRequires: desktop-file-utils
Requires: GConf2 

%description
Brightside provides "edge flipping" to allow you to switch to the adjacent 
workspace simply by pressing your mouse against the edge of the screen.

Besides that Brightside also allows you to assign configurable actions to 
occur while you rest the mouse in a corner of the screen.

%prep
%setup
%patch0
#patch1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%{__make} install DESTDIR="%{buildroot}"

%find_lang Brightside

desktop-file-install --delete-original             \
	--vendor %{desktop_vendor}                 \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/control-center-2.0/capplets/brightside.desktop

%preun
export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%post
export GCONF_CONFIG_SOURCE=$(gconftool-2 --get-default-source)
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f Brightside.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README 
%{_bindir}/*
%{_datadir}/applications/%{desktop_vendor}-brightside.desktop
%{_datadir}/brightside/
%{_datadir}/pixmaps/brightside-48.png
%{_sysconfdir}/gconf/schemas/brightside.schemas

%changelog
* Wed Feb 07 2007 Dag Wieers <dag@wieers.com> - 1.4.0-1
- Initial package. (using DAR)
