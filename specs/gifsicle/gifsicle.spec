# $Id$
# Authority: dag


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Powerful program for manipulating GIF images and animations
Name: gifsicle
Version: 1.68
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.lcdf.org/gifsicle/

Source: http://www.lcdf.org/gifsicle/gifsicle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{!?_without_modxorg:BuildRequires: libX11-devel, libICE-devel, libSM-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make

Conflicts: ungifsicle

%description
Gifsicle manipulates GIF image files on the
command line. It supports merging several GIFs
into a GIF animation; exploding an animation into
its component frames; changing individual frames
in an animation; turning interlacing on and off;
adding transparency; adding delays, disposals, and
looping to animations; adding or removing
comments; optimizing animations for space; and
changing images' colormaps, among other things.

The gifsicle package contains two other programs:
gifview, a lightweight GIF viewer for X, can show
animations as slideshows or in real time, and
gifdiff compares two GIFs for identical visual
appearance.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING INSTALL NEWS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Wed Jan 09 2013 David Hrbáč <david@hrbac.cz> - 1.68-1
- new upstream release

* Mon May 21 2012 Steve Huff <shuff@vecna.org> - 1.67-1
- Updated to release 1.67.

* Sun Sep 16 2007 Dries Verachtert <dries@ulyssis.org> - 1.48-1
- Updated to release 1.48.

* Sun Jan 21 2007 Dag Wieers <dag@wieers.com> - 1.46-1
- Updated to release 1.46.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 1.44-1
- Initial package. (using DAR)
