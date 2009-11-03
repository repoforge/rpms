# $Id$
# Authority: dag

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
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define gimp %(rpm -q gimp-devel | grep -q 1\.2; echo $?)

Summary: GUI frontend program and library for autotrace
Name: frontline
Version: 0.5.4
Release: 2.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://autotrace.sourceforge.net/frontline/

Source: http://dl.sf.net/autotrace/frontline-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libart_lgpl-devel >= 2.0, gimp-devel, autotrace-devel
BuildRequires: gnome-libs-devel, autotrace
BuildRequires: ImageMagick-devel, libtiff-devel, freetype-devel
BuildRequires: libjpeg-devel, libpng-devel, bzip2-devel, libxml2-devel, zlib-devel
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Frontline provides a Gtk+/GNOME based GUI frontend for
autotrace.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if %{gimp}0
%else
%{__install} -d -m0755 %{buildroot}%{_libdir}/gimp/1.2/plug-ins/
%{__mv} -f %{buildroot}/usr/libexec/trace %{buildroot}%{_libdir}/gimp/1.2/plug-ins/
%endif

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.a
%{_includedir}/gundo/
%{_includedir}/frontline/
%{_datadir}/gnome/apps/Graphics/frontline.desktop
%{_datadir}/mime-info/*
%{_datadir}/pixmaps/*
%{_datadir}/aclocal/frontline.m4
%{_libdir}/pkgconfig/frontline.pc
%if %{gimp}0
%else
%{_libdir}/gimp/1.2/plug-ins/trace
%endif

%changelog
* Tue Nov 26 2002 Dag Wieers <dag@wieers.com> - 0.5.4
- Updated to 0.5.4

* Sun Sep  8 2002 Masatake YAMATO <jet@gyve.org>
- Initial build.
