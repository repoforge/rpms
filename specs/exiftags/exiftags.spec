# $Id$
# Authority: dries
# Upstream: Eric Johnston <emj@postal.net>

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
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 exifcom %{buildroot}%{_bindir}/exifcom
%{__install} -D -m0755 exiftags %{buildroot}%{_bindir}/exiftags
%{__install} -D -m0644 exifcom.1 %{buildroot}%{_mandir}/man1/exifcom.1
%{__install} -D -m0644 exiftags.1 %{buildroot}%{_mandir}/man1/exiftags.1

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man?/*
%{_bindir}/exif*

%changelog
* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 0.99-2
- Cosmetic changes.

* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 0.99-1
- initial package
