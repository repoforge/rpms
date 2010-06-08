# $Id$
# Authority: dries
# Upstream: Andreas Huggel <ahuggel$gmx,net>


### pkgconfig < 0.16.0 doesn't like 'URL:'
%{?el4:%define _without_pkgconfig16 1}
%{?el3:%define _without_pkgconfig16 1}

Summary: Exif and Iptc metadata manipulation library and tools
Name: exiv2
Version: 0.20
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://home.arcor.de/ahuggel/exiv2/index.html

Source: http://home.arcor.de/ahuggel/exiv2/exiv2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: graphviz
BuildRequires: libtool
BuildRequires: libxslt
BuildRequires: python

%description
Exiv2 comprises of a C++ library and a command line utility to access image
metadata. Exiv2 supports full read and write access to th Exif and Iptc
metadata, Exif MakerNote support, extract and delete methods for Exif
thumbnails, classes to access Ifd and so on.
The command line utility allow you to:
* print the Exif metadata of Jpeg images as summary info, interpreted values,
or the plain data for each tag (here is a sample)
* print the Iptc metadata of Jpeg images
* print the Jpeg comment of Jpeg images
* set, add and delete Exif and Iptc metadata of Jpeg images
* adjust the Exif timestamp (that's how it all started...)
* rename Exif image files according to the Exif timestamp
* extract, insert and delete Exif metadata, Iptc metadata and Jpeg comments
* extract, insert and delete the thumbnail image embedded in the Exif metadata

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
%{?_without_pkgconfig16:%{__perl} -pi -e 's|^URL:|#URL:|' config/exiv2.pc.in}

%build
%configure --disable-static
%{__make} %{?_smp_mflags}
%{__make} doc

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" prefix="%{_prefix}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/exiv2.1*
%{_bindir}/exiv2
%{_libdir}/libexiv2.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html
#%{_bindir}/exiv2-config
%{_includedir}/exiv2/
%{_libdir}/libexiv2.so
%{_libdir}/pkgconfig/exiv2.pc
%exclude %{_libdir}/libexiv2.la

%changelog
* Tue Jun 01 2010 Dag Wieers <dag@wieers.com> - 0.20-1
- Updated to release 0.20.

* Thu Dec 31 2009 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Sat Jul 04 2009 Dag Wieers <dag@wieers.com> - 0.18.2-1
- Updated to release 0.18.2.

* Sun Jun 22 2008 Dag Wieers <dag@wieers.com> - 0.17.1-1
- Updated to release 0.17.1.

* Fri Jun 06 2008 Dag Wieers <dag@wieers.com> - 0.17-1
- Updated to release 0.17.

* Thu Jan 10 2008 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Tue Jul 10 2007 Dries Verachtert <dries@ulyssis.org> - 0.15-1
- Updated to release 0.15.

* Mon Mar 26 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Updated to release 0.14.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Wed Dec 20 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-2
- Remove 'URL:' from pkgconfig file on older distro's, thanks to Rex Dieter.

* Mon Nov 27 2006 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Updated to release 0.12.

* Sat Sep 16 2006 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sun Jun 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Updated to release 0.9.1.

* Fri Jan 27 2006 Oron Peled <oron@actcom.co.il> - 0.9-1
- Updated to release 0.9
- Split into exiv2 and exiv2-devel packages
- Added the documentation into exiv2-devel

* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Sun Jun 25 2005 Dries Verachtert <dries@ulyssis.org> 0.7-1
- initial package
