# $Id: _template.spec 130 2004-03-17 10:51:35Z dude $

# Authority: dag
# Upstream: <f-spot-list@gnome.org>

Summary: Personal photo management application.
Name: f-spot
Version: 0.0.1
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://www.gnome.org/projects/f-spot/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/Public/GNOME/sources/f-spot/0.0/f-spot-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: mono-devel, libexif-devel
Requires: mono, gtk-sharp, libexif

%description
F-Spot is an application designed to provide personal photo management
to the GNOME desktop. Plans include import, export, printing and advanced
sorting of digital images.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=F-spot Photo Manager
Comment=Manage your photos.
Icon=f-spot.png
Exec=f-spot
Terminal=false
Type=Application
Categories=GNOME;Application;Graphics;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0644 icons/f-spot-camera.png %{buildroot}%{_datadir}/pixmaps/f-spot.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome                \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        %{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL MAINTAINERS NEWS README TODO
%{_bindir}/*
%{_libdir}/f-spot/
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop
%exclude %{_libdir}/f-spot/*.a
%exclude %{_libdir}/f-spot/*.la

%changelog
* Sat Mar 20 2004 Dag Wieers <dag@wieers.com> - 0.0.1-1
- Initial package. (using DAR)
