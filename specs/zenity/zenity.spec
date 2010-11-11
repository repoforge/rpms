# $Id$
# Authority: dag
# Upstream: Glynn Foster <glynn,foster$sun,com>

### EL6 ships with zenity-2.28.0-1.el6
### EL5 ships with zenity-2.16.0-2.el5
# ExclusiveDist: el3

Summary: Display GNOME dialogs from the command line
Name: zenity
Version: 1.7
Release: 0.2%{?dist}
License: GPL
Group: Applications/System
URL: http://archive.progeny.com/GNOME/sources/zenity/

Source: http://ftp.gnome.org/pub/GNOME/sources/zenity/%{version}/zenity-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: popt, scrollkeeper, intltool, GConf2-devel, gettext
BuildRequires: gtk2-devel, libglade2-devel >= 2.0, libgnomecanvas-devel >= 2.0

Requires(post): scrollkeeper

%description
zenity is a rewrite of gdialog, the GNOME port of dialog which allows
you to display dialog boxes from the commandline and shell scripts.

If you understand, things are just as they are.
If you don't understand, things are just as they are.

%prep
%setup

%build
%configure \
	--disable-schemas-install
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall \
	DESTDIR="/"
%find_lang %{name}-0.1

%{__mv} -f %{buildroot}%{_bindir}/gdialog %{buildroot}%{_bindir}/gdialog-zenity

%post
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas &>/dev/null
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}-0.1.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/zenity/
%{_bindir}/*
%{_datadir}/omf/zenity/
%{_datadir}/zenity/
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-0.2
- Rebuild for Fedora Core 5.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 1.7-0
- Updated to release 1.7.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.6-0
- Updated to release 1.6.

* Mon Aug 25 2003 Dag Wieers <dag@wieers.com> - 1.5-0
- Updated to release 1.5.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Updated to release 1.4.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 1.3-0
- Updated to release 1.3.

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 1.2-0
- Updated to release 1.2.

* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using DAR)
