# $Id$
# Authority: dries
# Upstream: Billy Biggs <vektor$dumbterm,net>

Summary: Command line utilities for manipulating high dynamic range images
Name: exrtools
Version: 0.4
Release: 1
License: MIT/X Consortium License
Group: Applications/Multimedia
URL: http://scanline.ca/exrtools/

Source: http://scanline.ca/exrtools/exrtools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openexr-devel, gcc-c++, libpng-devel, zlib-devel, libjpeg-devel

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
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README
%doc %{_mandir}/man1/*
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
* Tue Nov 15 2005 Dries Verachtert <dries@ulyssis.org> - 0.4-1
- Initial package.
