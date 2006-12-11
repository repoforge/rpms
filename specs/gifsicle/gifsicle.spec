# $Id$
# Authority: dag

Summary: Powerful program for manipulating GIF images and animations
Name: gifsicle
Version: 1.44
Release: 1
License: GPL
Group: Applications/Graphics
URL: http://www.lcdf.org/gifsicle/

Source: http://www.lcdf.org/gifsicle/gifsicle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%doc NEWS README
%doc %{_mandir}/man1/gifdiff.1*
%doc %{_mandir}/man1/gifsicle.1*
%doc %{_mandir}/man1/gifview.1*
%{_bindir}/gifdiff
%{_bindir}/gifsicle
%{_bindir}/gifview

%changelog
* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 1.44-1
- Initial package. (using DAR)
