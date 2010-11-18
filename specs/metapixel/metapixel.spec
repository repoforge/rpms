# $Id$
# Authority: dag


%{?el4:%define _without_giflib 1}
%{?el3:%define _without_giflib 1}
%{?fc4:%define _without_giflib 1}
%{?fc3:%define _without_giflib 1}
%{?fc2:%define _without_giflib 1}
%{?fc1:%define _without_giflib 1}

Summary: Photo mosaic generator
Name: metapixel
Version: 1.0.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.complang.tuwien.ac.at/~schani/metapixel/

Source: http://www.complang.tuwien.ac.at/~schani/metapixel/files/metapixel-%{version}.tar.gz
Patch0: metapixel-1.0.2-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libjpeg-devel, libpng-devel, zlib-devel
# giflib-devel is needed for /usr/include/gif_lib.h
%{?!_without_giflib:BuildRequires: giflib-devel}
%{?_without_giflib:BuildRequires: libungif-devel}

%description
Metapixel is a program for generating photomosaics. It can generate classical
photomosaics, in which the source image is viewed as a matrix of equally sized
rectangles for each of which a matching image is substitued, as well as
collage-style photomosaics, in which rectangular parts of the source image at
arbitrary positions (i.e. not aligned to a matrix) are substituted by matching
images.

%prep
%setup
%patch0 -b .makefile

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__chmod} 0644 %{buildroot}%{_mandir}/man1/metapixel.1*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0775)
%doc COPYING README
%doc %{_mandir}/man1/metapixel.1.gz
%{_bindir}/metapixel
%{_bindir}/metapixel-imagesize
%{_bindir}/metapixel-prepare
%{_bindir}/metapixel-sizesort

%changelog
* Mon Dec 01 2006 Dag Wieers <dag@wieers.com> - 1.0.2-1
- Initial package. (using DAR)
