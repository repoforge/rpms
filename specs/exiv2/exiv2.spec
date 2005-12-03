# $Id$
# Authority: dries
# Upstream: Andreas Huggel <ahuggel$gmx,net>

Summary: Exif and Iptc metadata manipulation library and tools
Name: exiv2
Version: 0.8
Release: 1
License: GPL
Group: Applications/Multimedia
URL: http://home.arcor.de/ahuggel/exiv2/index.html

Source: http://home.arcor.de/ahuggel/exiv2/exiv2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, libtool

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

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall incdir=%{buildroot}%{_includedir}/exiv2

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/exiv2
${_bindir}/exiv2-config
%{_includedir}/exiv2
%{_libdir}/libexiv2*

%changelog
* Mon Nov 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Updated to release 0.8.

* Sun Jun 25 2005 Dries Verachtert <dries@ulyssis.org> 0.7-1
- initial package
