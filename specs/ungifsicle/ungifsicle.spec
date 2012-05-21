# $Id$
# Authority: shuff


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
Name: ungifsicle
Version: 1.67
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.lcdf.org/gifsicle/

Source: http://www.lcdf.org/gifsicle/ungifsicle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
%{!?_without_modxorg:BuildRequires: libX11-devel, libICE-devel, libSM-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

BuildRequires: binutils
BuildRequires: gcc
BuildRequires: make

Conflicts: gifsicle

%description
Ungifsicle manipulates GIF image files on the command line. It supports merging
several GIFs into a GIF animation; exploding an animation into its component
frames; changing individual frames in an animation; turning interlacing on and
off; adding transparency; adding delays, disposals, and looping to animations;
adding or removing comments; optimizing animations for space; and changing
images' colormaps, among other things.

The ungifsicle package contains two other programs: gifview, a lightweight GIF
viewer for X, can show animations as slideshows or in real time, and gifdiff
compares two GIFs for identical visual appearance.

Ungifsicle, unlike gifsicle, creates files using a patent-free run length
encoding.  For more commentary, see the following site:

http://www.gnu.org/philosophy/gif.html

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --enable-ungif
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
* Mon May 21 2012 Steve Huff <shuff@vecna.org> - 1.67-1
- Initial package (ported from gifsicle spec).
