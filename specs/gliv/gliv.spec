# $Id$
# Authority: dag
# Upstream: Guillaume Chazarain <guichaz$yahoo,fr>

Summary: Image viewing utility
Name: gliv
Version: 1.8.3
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://guichaz.free.fr/gliv/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://guichaz.free.fr/gliv/gliv-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison, gtk2-devel >= 2.2.0, gtkglext-devel >= 0.7.0

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
Icon=redhat-graphics.png
Terminal=false
Type=Application
Categories=GNOME;Application;Graphics;
EOF

%build
%configure \
	--x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	gliv.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING NEWS README THANKS
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/applications/gnome-gliv.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Thu Jun 24 2004 Dag Wieers <dag@wieers.com> - 1.8.3-1
- Updated to release 1.8.3.

* Sat Feb 07 2004 Dag Wieers <dag@wieers.com> - 1.8.1-0
- Updated to release 1.8.1.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 1.8-0
- Initial package. (using DAR)
