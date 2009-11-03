# $Id$
# Authority: dag
# Upstream: <f-spot-list$gnome,org>

%define desktop_vendor rpmforge

Summary: Personal photo management application
Name: f-spot
Version: 0.0.12
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Graphics
URL: http://www.gnome.org/projects/f-spot/

Source: http://ftp.gnome.org/Public/GNOME/sources/f-spot/0.0/f-spot-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mono-devel, gtk-sharp-devel, libexif-devel, lcms-devel
BuildRequires: perl(XML::Parser), intltool
Requires: mono, gtk-sharp, libexif

%description
F-Spot is an application designed to provide personal photo management
to the GNOME desktop. Plans include import, export, printing and advanced
sorting of digital images.

%prep
%setup

%{__cat} <<EOF >f-spot.desktop.in.in
[Desktop Entry]
Name=F-spot Photo Manager
Comment=Manage your photos
Icon=f-spot-logo
Exec=f-spot
Terminal=false
Type=Application
Categories=GNOME;Application;Graphics;Photograph;
StartupNotify=true
X-GNOME-Bugzilla-Bugzilla=GNOME
X-GNOME-Bugzilla-Product=f-spot
X-GNOME-Bugzilla-Component=General
X-GNOME-Bugzilla-Version=@VERSION@
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL MAINTAINERS NEWS README TODO
%{_bindir}/f-spot
%{_libdir}/f-spot/
%{_datadir}/pixmaps/f-spot-logo.png
%{_datadir}/applications/f-spot.desktop
%exclude %{_libdir}/f-spot/*.a
%exclude %{_libdir}/f-spot/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.12-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 20 2005 Dag Wieers <dag@wieers.com> - 0.0.12-1
- Updated to release 0.0.12.

* Mon Mar 14 2005 Dag Wieers <dag@wieers.com> - 0.0.11-1
- Updated to release 0.0.11.

* Sat Mar 05 2005 Dag Wieers <dag@wieers.com> - 0.0.10-1
- Updated to release 0.0.10.

* Mon Feb 21 2005 Dag Wieers <dag@wieers.com> - 0.0.9-1
- Updated to release 0.0.9.

* Fri Feb 18 2005 Dag Wieers <dag@wieers.com> - 0.0.8-1
- Updated to release 0.0.8.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.0.7-1
- Updated to release 0.0.7.

* Fri Jan 21 2005 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Updated to release 0.0.6.

* Wed Jan 19 2005 Dag Wieers <dag@wieers.com> - 0.0.5-1
- Updated to release 0.0.5.

* Tue Jan 04 2005 Dag Wieers <dag@wieers.com> - 0.0.3-1
- Updated to release 0.0.3.

* Sat Mar 20 2004 Dag Wieers <dag@wieers.com> - 0.0.1-1
- Initial package. (using DAR)
