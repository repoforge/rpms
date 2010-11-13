# $Id$
# Authority: dag

Summary: Default Style for Ximian Desktop
Name: ximian-artwork
Version: 0.2.32
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://www.ximian.com/

Source: http://vortex.floppyhat.net/ximian-artwork-%{version}.tar.gz
Patch0: ximian-artwork-de.po.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, gtk2-devel, pkgconfig, gettext, intltool, perl(XML::Parser)
BuildRequires: gettext
Requires: gnome-themes-extras

%description
ximian-artwork contains the default style configuration for the Ximian Desktop.
This package contains themes for GNOME2, gdm, xmms and galeon.

%prep
%setup
%patch0 -p1

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"
%find_lang %{name}

### Fix erroneous filenames
for file in %{buildroot}%{_libdir}/gtk*/*/engines/libindustrial; do
	%{__mv} -f $file $file.so
done

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%{_datadir}/icons/Industrial/
%{_datadir}/icons/gnome/*/*/*
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/backgrounds/ximian/
%{_datadir}/pixmaps/ximian/
%{_datadir}/galeon/themes/Industrial/
%{_datadir}/gdm/themes/industrial/
%{_datadir}/pixmaps/nautilus/industrial/
%{_datadir}/themes/Industrial/
%{_datadir}/xmms/Skins/Industrial/
%exclude %{_libdir}/gtk-2.0/*/engines/libindustrial.a
%exclude %{_libdir}/gtk-2.0/*/engines/libindustrial.la
%exclude %{_libdir}/gtk-2.0/*/engines/libindustrial.so
%exclude %{_libdir}/gtk/themes/engines/libindustrial.a
%exclude %{_libdir}/gtk/themes/engines/libindustrial.la
%{_libdir}/gtk/themes/engines/libindustrial.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.32-1.2
- Rebuild for Fedora Core 5.

* Sat Feb 12 2005 Dag Wieers <dag@wieers.com> - 0.2.32-1
- Updated to release 0.2.32.

* Sun Jun 15 2003 Che
- initial rpm release
