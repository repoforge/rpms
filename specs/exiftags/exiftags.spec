# $Id $

# Authority: dries
# Upstream: Eric Johnston

Summary: Shows Exif (Exchangeable Image File) image metadata
Name: exiftags
Version: 0.99
Release: 1
License: BSD
Group: Applications/Multimedia
URL: http://johnst.org/sw/exiftags/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://johnst.org/sw/exiftags/exiftags-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The exiftags utility parses a specified JPEG file or, by
default, its standard input, looking for a JPEG APP1 section containing Exif
(Exchangeable Image File) image metadata. The properties contained in these
data are then printed to the standard output. Digital cameras typically add
Exif data to the image files they produce, containing information about the
camera and digitized image. 

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/%{_mandir}/man1
cp exiftags exifcom %{buildroot}/usr/bin
chmod a+x %{buildroot}/usr/bin/exif*
cp exiftags.1 exifcom.1 %{buildroot}/%{_mandir}/man1
chmod a+r %{buildroot}/%{_mandir}/man1/exif*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0755)
%doc README CHANGES
%{_bindir}/exif*
%{_mandir}/man1/exif*

%changelog
* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 0.99-1
- initial package
