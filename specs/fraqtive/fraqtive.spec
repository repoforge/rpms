# $Id$
# Authority: dries
# Upstream: Michal Mecinski <mimec$wp,pl>

Summary: Draws Mandelbrot and Julia fractals
Name: fraqtive
Version: 0.3.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://zeus.polsl.gliwice.pl/~mimec/index.php?id=fraqtive

Source: http://zeus.polsl.gliwice.pl/~mimec/files/fraqtive-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext

%description
Fraqtive is a program for drawing Mandelbrot and Julia fractals. It uses a
very fast algorithm and generates high quality, smooth images. It is fully
interactive, allowing for real-time mouse navigation and dynamic generation
of the Julia fractal preview. OpenGL-rendered 3D view of the fractals is
also supported.

%prep
%setup

%build
%configure  LDFLAGS="$LDFLAGS -L/usr/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/fraqtive
%{_datadir}/applnk/Utilities/fraqtive.desktop
%{_datadir}/apps/fraqtive/
%{_datadir}/config/fraqtiverc
%{_datadir}/doc/HTML/*/fraqtive/
%{_datadir}/icons/*/*/apps/fraqtive.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1.2
- Rebuild for Fedora Core 5.

* Tue Oct 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.1-1
- Initial package.
