# $Id$
# Authority: dries
# Upstream: xaos-devel@lists.sourceforge.net

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Fast, portable, real-time, and interactive fractal zoomer
Name: xaos
Version: 3.5
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://wmi.math.u-szeged.hu/xaos/doku.php

Source: http://dl.sf.net/xaos/xaos-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: aalib-devel
%{!?_without_modxorg:BuildRequires: libXext-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
XaoS is a fast, portable, real-time, and interactive fractal zoomer. It 
displays the Mandelbrot set (among other escape time fractals) and allows 
you zoom smoothly into the fractal. Various coloring modes are provided 
for both the points inside and outside the selected set. In addition, 
switching between Julia and Mandelbrot fractal types and on-the-fly 
plane switching is provided.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=XaoS
Comment=Fractal zoomer
Exec=xaos
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;Graphics;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}
%{__rm} -f %{buildroot}%{_infodir}/dir

%if %{?_without_freedesktop:1}0
%{__install} -D -m0644 xaos.desktop %{buildroot}/etc/X11/applnk/Multimedia/xaos.desktop
%else
%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --add-category X-Red-Hat-Base               \
    --dir %{buildroot}%{_datadir}/applications  \
    xaos.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TODO
%doc %{_infodir}/xaos.info*
%doc %{_mandir}/man6/xaos.6*
%{_bindir}/xaos
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-xaos.desktop}
%{?_without_freedesktop:/etc/X11/applnk/Multimedia/xaos.desktop}
%{_datadir}/XaoS/

%changelog
* Mon Jul 20 2009 Dries Verachtert <dries@ulyssis.org> - 3.5-1
- Updated to release 3.5.

* Fri Nov 30 2007 Dries Verachtert <dries@ulyssis.org> - 3.2.3-1
- Updated to release 3.2.3.
