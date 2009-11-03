# $Id$
# Authority: dries
# Upstream: Billy Biggs <vektor$dumbterm,net>

Summary: Command line utilities for manipulating high dynamic range images
Name: exrtools
Version: 0.4
Release: 2%{?dist}
License: MIT/X Consortium License
Group: Applications/Multimedia
URL: http://scanline.ca/exrtools/

Source: http://scanline.ca/exrtools/exrtools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openexr-devel, gcc-c++, libpng-devel, zlib-devel, libjpeg-devel
BuildRequires: pkgconfig

%description
exrtools is a set of simple command line utilities for manipulating high
dynamic range images in OpenEXR format. It was developed to help experiment
with batch processing of HDR images for tone mapping. Each application is
small and reasonably self-contained so that the source code may be of most
value to others.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README
%doc %{_mandir}/man1/exrblur.1*
%doc %{_mandir}/man1/exrchr.1*
%doc %{_mandir}/man1/exricamtm.1*
%doc %{_mandir}/man1/exrnlm.1*
%doc %{_mandir}/man1/exrnormalize.1*
%doc %{_mandir}/man1/exrpptm.1*
%doc %{_mandir}/man1/exrstats.1*
%doc %{_mandir}/man1/exrtools.1*
%doc %{_mandir}/man1/exrtopng.1*
%doc %{_mandir}/man1/jpegtoexr.1*
%doc %{_mandir}/man1/pngtoexr.1*
%doc %{_mandir}/man1/ppmtoexr.1*
%{_bindir}/exrblur
%{_bindir}/exrchr
%{_bindir}/exricamtm
%{_bindir}/exrnlm
%{_bindir}/exrnormalize
%{_bindir}/exrpptm
%{_bindir}/exrstats
%{_bindir}/exrtopng
%{_bindir}/jpegtoexr
%{_bindir}/pngtoexr
%{_bindir}/ppmtoexr

%changelog
* Tue May 15 2007 Dag Wieers <dag@wieers.com> - 0.4-2
- Rebuild against openexr 0.4a.

* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Initial package.
