# $Id$
# Authority: dries
# Upstream: Robin Rowe <rower$movieeditor,com>

%define real_version 0.20-1

Summary: Motion picture frame-by-frame retouching and dust-busting
Name: cinepaint
Version: 0.20.1
Release: 1.2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://sourceforge.net/projects/cinepaint

Source: http://dl.sf.net/cinepaint/cinepaint-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openexr-devel, pkgconfig, libtiff-devel, lcms-devel
BuildRequires: gcc-c++, gtk+-devel, glib-devel, libjpeg-devel
BuildRequires: fltk-devel, libpng-devel, desktop-file-utils
BuildRequires: python-devel, python

%description
CinePaint is an application primarily used for motion picture frame-by-frame
retouching and dust-busting. It has been used on many feature films,
including The Last Samurai. It is different from other painting tools
because in addition to common 8-bit per channel formats like JPEG, it
supports deep color image formats such as Cineon, DPX, OpenEXR, and
32-bit TIFF, which are standard in motion picture visual effects and
animation.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Cinepaint
Comment=Motion picture retouching
Exec=cinepaint
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's|programplugindir = /usr|programplugindir = %{buildroot}/usr|g;' $(find . -type f | egrep 'Makefile$')
%{__perl} -pi -e 's|programdatadir = /usr|programdatadir = %{buildroot}/usr|g;' $(find . -type f | egrep 'Makefile$')
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/cinepaint*
%{_bindir}/cinepaint
%{_bindir}/cinepainttool
%{_bindir}/cinepaint-remote
%{_libdir}/libcinepaint.so.*
%{_datadir}/applications/*cinepaint.desktop
%{_libdir}/cinepaint/
%{_datadir}/cinepaint/
# tofix?
%{_prefix}/libexec/bmp
%{_prefix}/libexec/gifload
%{_prefix}/libexec/rotate

%files devel
%{_includedir}/cinepaint/
%{_libdir}/libcinepaint.a
%{_libdir}/libcinepaint.so
%{_libdir}/pkgconfig/cinepaint-gtk.pc
%{_datadir}/aclocal/cinepaint.m4
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.20.1-1.2
- Rebuild for Fedora Core 5.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.20.1-1
- Initial package.
