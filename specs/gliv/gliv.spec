# $Id$
# Authority: dag
# Upstream: Guillaume Chazarain <guichaz$yahoo,fr>

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%define desktop_vendor rpmforge

Summary: Image viewing utility
Name: gliv
Version: 1.9.6
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://guichaz.free.fr/gliv/

Source: http://guichaz.free.fr/gliv/files/gliv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, gtk2-devel >= 2.6.0, gtkglext-devel >= 0.7.0
BuildRequires: gettext, desktop-file-utils
%{!?_without_modxorg:BuildRequires:imake}

%description
GLiv is an OpenGL image viewer. GLiv is very fast and smooth at rotating,
panning and zooming if you have an OpenGL accelerated graphics board.

%prep
%setup

%{__cat} <<EOF >gliv.desktop
[Desktop Entry]
Name=Gliv Image Viewer
Comment=View images fast and smoothly
Exec=gliv
Icon=gliv.png
Terminal=false
Type=Application
MimeType=image/gif;image/x-xpm;image/x-xbm;image/jpeg;image/x-bmp;image/png;image/x-tiff;image/x-tga;
Categories=GNOME;Application;Graphics;
EOF

%{__cat} <<EOF >gliv.applications
gliv
	command=gliv
	name=Gliv Image Viewer
	can_open_multiple_files=true
	expects_uris=no
	requires_terminal=false
	all_gnome_vfs_schemes_supported=yes
	uses_gnomevfs=true
	startup_notify=true
	mime_types=image/gif;image/x-xpm;image/x-xbm;image/jpeg;image/x-bmp;image/png;image/x-tiff;image/x-tga;
EOF


%build
%configure \
%{!?_without_modxorg:--x-libraries="%{_libdir}"} \
%{?_without_modxorg:--x-libraries="%{_prefix}/X11R6/%{_lib}"}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -Dp -m0644 gliv.applications %{buildroot}%{_datadir}/application-registry/gliv.applications
%{__install} -Dp -m0644 gliv.png %{buildroot}%{_datadir}/pixmaps/gliv.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	gliv.desktop

%post
update-desktop-database &>/dev/null || :

%postun
update-desktop-database &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING NEWS README THANKS
%doc %{_mandir}/man1/gliv.1*
%doc %{_mandir}/*/man1/gliv.1*
%{_bindir}/gliv
%{_datadir}/applications/%{desktop_vendor}-gliv.desktop
%{_datadir}/applications/gnome-gliv.desktop
%{_datadir}/application-registry/gliv.applications
%{_datadir}/pixmaps/gliv.png

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.6-1
- Updated to release 1.9.6.

* Mon Mar 20 2006 Dag Wieers <dag@wieers.com> - 1.9.5-1
- Updated to release 1.9.5.

* Thu Nov 17 2005 Dries Verachtert <dries@ulyssis.org> - 1.9.4-1
- Updated to release 1.9.4.

* Fri May 27 2005 Dag Wieers <dag@wieers.com> - 1.9.3-1
- Updated to release 1.9.3.

* Tue Mar 22 2005 Dag Wieers <dag@wieers.com> - 1.9.2-1
- Updated to release 1.9.2.

* Wed Jan 05 2005 Dag Wieers <dag@wieers.com> - 1.9.1-1
- Updated to release 1.9.1.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 1.8.4-1
- Updated to release 1.8.4.

* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 1.8.3-1
- Updated to release 1.8.3.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 1.8.1-0
- Updated to release 1.8.1.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.8-0
- Initial package. (using DAR)
