# $Id$
# Authority: dries
# Upstream: Robin Rowe <rower$movieeditor,com>

%define desktop_vendor rpmforge
%define real_version 0.21-2

Summary: Motion picture frame-by-frame retouching and dust-busting
Name: cinepaint
Version: 0.21.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://cinepaint.org/

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

%{__cat} <<EOF >cinepaint.desktop
[Desktop Entry]
Name=Cinepaint
Comment=Motion picture retouching
Exec=cinepaint
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;AudioVideo;
Encoding=UTF8
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__perl} -pi -e 's|programplugindir = /usr|programplugindir = %{buildroot}/usr|g;' $(find . -type f | egrep 'Makefile$')
%{__perl} -pi -e 's|programdatadir = /usr|programdatadir = %{buildroot}/usr|g;' $(find . -type f | egrep 'Makefile$')
%{__make} install DESTDIR="%{buildroot}"

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	cinepaint.desktop

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/cinepaint.1*
%doc %{_mandir}/man1/cinepainttool.1*
%{_bindir}/cinepaint
%{_bindir}/cinepainttool
%{_bindir}/cinepaint-remote
%{_libdir}/libcinepaint.so.*
%{_datadir}/applications/%{desktop_vendor}-cinepaint.desktop
%{_libdir}/cinepaint/
%{_datadir}/cinepaint/
# tofix?
%{_prefix}/libexec/bmp
%{_prefix}/libexec/gifload
%{_prefix}/libexec/rotate

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/cinepaint.m4
%{_includedir}/cinepaint/
%exclude %{_libdir}/libcinepaint.a
%exclude %{_libdir}/libcinepaint.la
%{_libdir}/libcinepaint.so
%{_libdir}/pkgconfig/cinepaint-gtk.pc

%changelog
* Sun Apr 01 2007 Dag Wieers <dag@wieers.com> - 0.21.2-1
- Updated to release 0.21-2.

* Thu Nov 10 2005 Dries Verachtert <dries@ulyssis.org> - 0.20.1-1
- Initial package.
