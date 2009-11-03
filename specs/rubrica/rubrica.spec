# $Id$
# Authority: dag
# Upstream: Nicola Fragale <nicolafragale$libero,it>

Summary: Address book application
Name: rubrica
Version: 1.1.60
Release: 1.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://rubrica.berlios.de/

Source: http://download.berlios.de/rubrica/rubrica-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0, libxslt-devel >= 1.0
BuildRequires: libmcrypt-devel, gettext, gcc-c++, libral-devel

%description
An address book for GNOME.

%prep
%setup

%{__cat} <<EOF >rubrica.desktop.in
[Desktop Entry]
Name=Rubrica Addressbook
Comment=Manage contacts and addresses
Icon=rubrica.png
Exec=rubrica
Terminal=false
Type=Application
Categories=GNOME;Application;Office;
StartupNotify=true
EOF

%build
%configure \
	--disable-install-schemas \
	--enable-nls
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}/rubrica/

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
%doc AUTHORS ChangeLog COPYING CREDITS doc/examples.rub NEWS README TODO
%config %{_sysconfdir}/gconf/schemas/rubrica.schemas
%{_bindir}/rubrica
%{_datadir}/applications/rubrica.desktop
%{_datadir}/pixmaps/rubrica.png
%{_datadir}/pixmaps/rubrica/
%{_datadir}/rubrica/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.60-1.2
- Rebuild for Fedora Core 5.

* Fri Nov 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.60-1
- Updated to release 1.1.60.

* Tue May 24 2005 Dag Wieers <dag@wieers.com> - 1.0.14-1
- Updated to release 1.0.14.

* Sun Nov 14 2004 Dag Wieers <dag@wieers.com> - 1.0.13-1
- Updated to release 1.0.13.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 1.0.12-1
- Updated to release 1.0.12.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 1.0.10-0
- Updated to release 1.0.10.

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 1.0.5-0
- Updated to release 1.0.5.

* Sun May 25 2003 Dag Wieers <dag@wieers.com> - 1.0.2-0
- Updated to release 1.0.2.

* Sat May 10 2003 Dag Wieers <dag@wieers.com> - 1.0.1-0
- Updated to release 1.0.1.

* Fri May 02 2003 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Initial package. (using DAR)
