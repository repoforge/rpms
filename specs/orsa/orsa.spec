# $Id: $

# Authority: dries
# Upstream: Pasquale Tricarico <tricaric$wsu,edu>
# Screenshot: http://orsa.sourceforge.net/screenshots/orsa-0.6.1/orsa-0.6.1.png
# ScreenshotURL: http://orsa.sourceforge.net/screenshots.html

Summary: Interactive tool for scientific grade Celestial Mechanics computations
Name: orsa
Version: 0.6.2
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://orsa.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/orsa/orsa-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fftw, qt-devel readline-devel

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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
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
%exclude %{_libdir}/*.la

%changelog
* Sat Oct 02 2004 Dries Verachtert <dries@ulyssis.org> - 0.6.2-1
- Initial package.
