# $Id: $

# Authority: dries
# Upstream: Pasquale Tricarico <tricaric$wsu,edu>
# Screenshot: http://orsa.sourceforge.net/screenshots/orsa-0.6.1/orsa-0.6.1.png
# ScreenshotURL: http://orsa.sourceforge.net/screenshots.html

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: Interactive tool for scientific grade Celestial Mechanics computations
Name: orsa
Version: 0.6.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://orsa.sourceforge.net/

Source: http://dl.sf.net/orsa/orsa-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fftw-devel, qt-devel, readline-devel, gcc-c++
BuildRequires: desktop-file-utils, zlib-devel, libjpeg-devel
%{?_without_xorg:BuildRequires: XFree86-devel, XFree86-Mesa-libGLU}
%{!?_without_xorg:BuildRequires: xorg-x11-devel, xorg-x11-Mesa-libGLU}

%description
ORSA is an interactive tool for scientific grade Celestial Mechanics
computations. Asteroids, comets, artificial satellites, Solar, and
extra-Solar planetary systems can be accurately reproduced, simulated, and
analyzed.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Orsa
Comment=Tool for scientific grade Celestial Mechanics computations
Exec=xorsa
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Graphics;X-Red-Hat-Extra;
EOF

%build
source /etc/profile.d/qt.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source /etc/profile.d/qt.sh
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/applications/*.desktop
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/orsa
%exclude %{_libdir}/*.la

%changelog
* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Initial package.
