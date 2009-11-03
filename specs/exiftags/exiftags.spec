# $Id$
# Authority: dries
# Upstream: Eric M. Johnston <emj$postal,net>

Summary: Shows Exif (Exchangeable Image File) image metadata
Name: exiftags
Version: 1.01
Release: 1%{?dist}
License: BSD
Group: Applications/Multimedia
URL: http://johnst.org/sw/exiftags/

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

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|\$\(PREFIX\)/bin|\$(bindir)|g;
		s|\$\(PREFIX\)/man|\$(mandir)|g;
	' Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}

### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/

%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sun Dec 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.00-1.2
- Rebuild for Fedora Core 5.

* Thu Jun 09 2005 Dries Verachtert <dries@ulyssis.org> - 1.00
- Update to release 1.00.

* Mon May 31 2004 Dag Wieers <dag@wieers.com> - 0.99.1-2
- Added exiftime and use %%makeinstall. (Eric M. Johnston)

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 0.99.1-1
- Updated to release 0.99.1.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 0.99-2
- Cosmetic changes.

* Sat May 1 2004 Dries Verachtert <dries@ulyssis.org> 0.99-1
- initial package
