# $Id$
# Authority: dries
# Upstream: Alexander Pipelka <pipelka$teleweb,at>

# Screenshot: http://aeskulap.nongnu.org/gfx/screenshot1-full.jpg

Summary: Medial image viewer for DICOM images
Name: aeskulap
Version: 0.2.1
Release: 1.2%{?dist}
License: GPL/LGPL
Group: Applications/Multimedia
URL: http://aeskulap.nongnu.org

Source: http://www.bms-austria.com/~pipelka/aeskulap/aeskulap-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gtkmm24-devel, libglademm24-devel, gconfmm26-devel
BuildRequires: zlib-devel, libpng-devel, libtiff-devel, gettext

%description
Aeskulap is a medical image viewer. It is able to load a series of special
images stored in the DICOM format for review. It is able to query and fetch
DICOM images from archive nodes (also called PACS) over the network. The
goal of this project is to create a full open source replacement for
commercially available DICOM viewers. It is based on gtkmm, glademm, and
gconfmm and designed to run under Linux. Ports of these packages are
available for different platforms. It should be quite easy to port It to
any platform were these packages are available.

%prep
%setup

%build
%configure \
    --disable-schemas-install \
    --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#makeinstall imagesdir="%{buildroot}%{_datadir}/aeskulap/images"
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README
%config %{_sysconfdir}/gconf/schemas/aeskulap.schemas
%{_bindir}/aeskulap
%{_prefix}/lib/aeskulap/
%{_libdir}/aeskulap/
#%{_libdir}/libijg*.so
#%{_libdir}/libimagepool.*
#%{_libdir}/libofstd.so*
%{_datadir}/aeskulap/
%{_datadir}/applications/aeskulap.desktop

%changelog
* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1-1
- Updated to release 0.2.1.

* Fri Oct 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.0-2
- zlib-devel and libpng-devel buildrequirements added.

* Mon Oct 03 2005 Dries Verachtert <dries@ulyssis.org> - 0.2.0-1
- Updated to release 0.2.0.

* Tue Sep 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.1.1-1
- Initial package.
