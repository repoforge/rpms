# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

Summary: Mission and Objective based 2D Platform Game
Name: blobwars
Version: 1.07
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.parallelrealities.co.uk/blobWars.php

#Source: http://www.parallelrealities.co.uk/download.php?type=gzip&file=blobwars-%{version}-1.tar.gz
Source: blobwars-%{version}-1.tar.gz
Patch0: blobwars-1.05-debian.patch
Patch1: blobwars-1.05-desktop.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL_mixer-devel, SDL_image-devel, SDL_ttf-devel, zlib-devel
BuildRequires: desktop-file-utils
Requires: hicolor-icon-theme

%description
Blob Wars: Metal Blob Solid. This is Episode I of the Blob Wars Saga.
You must undertake the role of fearless Blob solider, Bob, as he infiltrates
various enemy installations and hideouts in an attempt to rescue as many
MIAs as possible.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" DOCDIR="doc-rpm"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc doc/*
%{_bindir}/blobwars
%{_datadir}/applications/blobwars.desktop
%{_datadir}/blobwars/
%{_datadir}/icons/hicolor/*/apps/blobwars.png

%changelog
* Sat Jun 15 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
