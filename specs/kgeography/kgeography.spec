# $Id: $

# Authority: dries
# Upstream: 

Summary: Geography learning tool
Name: kgeography
Version: 0.1
Release: 1
License: GPL
Group: Amusements/Games
URL: http://kgeography.berlios.de/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://download.berlios.de/kgeography/kgeography-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel

# Screenshot: http://kgeography.berlios.de/screen1.png
# ScreenshotURL: http://kgeography.berlios.de/screenshots.html

%description
KGeography is a geography learning tool. Right now it has three usage modes: 
* Browse the maps clicking in a map division to see it's name
* The game tells you a map division name and you have to click on it
* The game shows you a map division flag and you have to guess its name

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Name Thingy Tool
Comment=Do things with things
Icon=name.png
Exec=name
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Network;X-Red-Hat-Extra;
EOF

%build
. /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
. /etc/profile.d/qt.sh
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Tue May 4 2004 Dries Verachtert <dries@ulyssis.org> - 0.1-1 
- Initial package.
