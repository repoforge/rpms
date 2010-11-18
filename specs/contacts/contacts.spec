# $Id$
# Authority: dag

%define desktop_vendor rpmforge

%define real_name Contacts

Summary: Contacts addressbook
Name: contacts
Version: 0.12
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Productivity
URL: http://pimlico-project.org/contacts.html

Source: http://ftp.gnome.org/pub/gnome/sources/contacts/%{version}/contacts-%{version}.tar.bz2
Patch0: contacts-0.12-fixmake.patch

BuildRequires: desktop-file-utils
BuildRequires: evolution-data-server-devel
BuildRequires: gettext
BuildRequires: gnome-vfs2-devel
BuildRequires: gtk2-devel
BuildRequires: intltool
BuildRequires: libtool
Requires: GConf2

%description
Contacts is a small, lightweight addressbook that uses libebook. 
This is the same library that GNOME Evolution uses, so all contact data that 
exists in your Evolution database is accessible via Contacts. Contacts features 
advanced vCard field type handling and is designed for use on hand-held 
devices, such as the Nokia 770 or the Sharp Zaurus series of PDAs.

%prep
%setup
%patch0 -p1 -b .fixmake
sed -i 's/SingleInstance/X-SingleInstance/' data/%{name}.desktop*

%build
%configure --disable-schemas-install --enable-gconf
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{real_name}

desktop-file-install --delete-original \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%pre
if [ $1 -gt 1 ]; then
    export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
    gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :
fi


%post
umask 022
export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
gconftool-2 --makefile-install-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null ||:

%preun
if [ $1 -eq 0 ]; then
    export GCONF_CONFIG_SOURCE="$(gconftool-2 --get-default-source)"
    gconftool-2 --makefile-uninstall-rule %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
    killall -HUP gconfd-2 || :
fi

%postun
umask 022
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi
update-desktop-database &> /dev/null ||:

%files -f %{real_name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING
%doc %{_mandir}/man1/contacts.1*
%config %{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/contacts
%{_datadir}/applications/%{desktop_vendor}-contacts.desktop
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Thu Nov 18 2010 Dag Wieers <dag@wieers.com> - 0.12-1
- Initial package. (using DAR)
