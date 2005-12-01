# $Id$
# Authority: dries
# Upstream: jcupitt <john,cupitt$ng-london,org,uk>

Summary: Image processing suite for extremely large images and colorimetry
Name: vips
Version: 7.10.16
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://www.vips.ecs.soton.ac.uk/

Source: http://www.vips.ecs.soton.ac.uk/vips-7.10/vips-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, pkgconfig, glib2-devel, libpng-devel
BuildRequires: libtiff-devel, zlib-devel, libjpeg-devel, ImageMagick-devel
BuildRequires: fftw-devel, intltool, perl(XML::Parser)

%description
VIPS is an image processing suite designed for extremely large images and 
colorimetry. It consists of a powerful re-usable library and a graphical 
user interface.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__mv} %{buildroot}%{_datadir}/doc/vips rpmdocs

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO rpmdocs/*
%doc %{_mandir}/man?/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/vips/
%{_bindir}/batch_crop
%{_bindir}/batch_image_convert
%{_bindir}/batch_rubber_sheet
%{_bindir}/binfile
%{_bindir}/cooc
%{_bindir}/cooc_features
%{_bindir}/debugim
%{_bindir}/edvips
%{_bindir}/find_mosaic
%{_bindir}/glds
%{_bindir}/glds_features
%{_bindir}/header
%{_bindir}/light_correct
%{_bindir}/mergeup
%{_bindir}/mitsub
%{_bindir}/printlines
%{_bindir}/shrink_width
%{_bindir}/simcontr
%{_bindir}/sines
%{_bindir}/spatres
%{_bindir}/squares
%{_bindir}/vdump
%{_bindir}/vips
%{_bindir}/vips-*
%{_bindir}/vips2dj
%{_libdir}/libvips.so.*
%{_libdir}/libvipsCC.so.*

%files devel
%{_includedir}/vips/
%{_libdir}/libvips.a
%{_libdir}/libvipsCC.a
%{_libdir}/libvips.so
%{_libdir}/libvipsCC.so
%{_libdir}/pkgconfig/vips*.pc
%exclude %{_libdir}/*.la

%changelog
* Tue Nov 22 2005 Dries Verachtert <dries@ulyssis.org> - 7.10.16-1
- Initial package.
