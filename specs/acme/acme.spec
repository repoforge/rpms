# $Id$
# Authority: matthias

Summary: Multimedia keyboard button tool for GNOME.
Name: acme
Version: 2.4.2
Release: 2
Group: System Environment/Daemons
License: GPL
URL: http://www.hadess.net/misc-code.php3
Source: http://www.hadess.net/files/software/%{name}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: libgnomeui-devel >= 2.0.0, libglade2-devel >= 2.0.0
BuildRequires: libwnck-devel, startup-notification-devel, gettext

%description
ACME is a small GNOME tool to make use of the multimedia buttons present on
most laptops and internet keyboards: Volume, Brightness, Power, Eject, My Home,
Search, E-Mail, Sleep, Screensaver, Finance and Help buttons.

%prep
%setup

%build
%configure --disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%config %{_sysconfdir}/gconf/schemas/*
%{_bindir}/*
%{_datadir}/acme/
%{_datadir}/control-center-2.0/capplets/*

%changelog
* Thu Feb 12 2004 Matthias Saou <http://freshrpms.net/> 2.4.2-2.fr
- Removed gob2 build dep, it was unneeded AFAICT and didn't exist on YDL.

* Wed Feb  4 2004 Matthias Saou <http://freshrpms.net/> 2.4.2-1.fr
- Update to 2.4.2.
- Remove ldconfig from postun.

* Wed Apr 02 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)

