# $Id: $

# Authority: dries

Summary: Drawing program designed for young children
Name: tuxpaint
Version: 0.9.13
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.newbreedsoftware.com/tuxpaint/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source0: http://dl.sf.net/tuxpaint/tuxpaint-%{version}.tar.gz
Source1: http://dl.sf.net/tuxpaint/tuxpaint-stamps-2003.12.23.tar.gz
BuildRequires: gettext, libart_lgpl-devel, libjpeg-devel, libpng-devel, arts-devel, zlib-devel, kdelibs-devel, gcc, make, gcc-c++, XFree86-devel, qt-devel, SDL-devel, SDL_ttf-devel, SDL_image-devel, SDL_mixer-devel

# Sreenshot: http://www.newbreedsoftware.com/tuxpaint/screenshots/example_simple-t.png
# ScreenshotURL: http://www.newbreedsoftware.com/tuxpaint/screenshots/

%description
Tux Paint is a free drawing program designed for young children (kids ages 3
and up). It has a simple, easy-to-use interface, fun sound effects, and an
encouraging cartoon mascot who helps guide children as they use the program. 

%prep
%{__rm} -rf %{buildroot}
%setup

%build
. /etc/profile.d/qt.sh
cd src
%{__make} %{?_smp_mflags}

%install
. /etc/profile.d/qt.sh
cd src
%makeinstall

%files
%defattr(-,root,root,0755)

%changelog
* Thu Dec 25 2003 Dries Verachtert <dries@ulyssis.org> 0.9.13-1
- Initial packaging
