# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Frantic shooting game where viruses invade your computer
Name: viruskiller
Version: 1.0
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.parallelrealities.co.uk/virusKiller.php

#Source: http://www.parallelrealities.co.uk/download.php?file=viruskiller-1.0-1.tar.gz&type=zip
Source: viruskiller-%{version}-1.tar.gz
Patch0: viruskiller-1.0-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, zlib-devel
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_ttf-devel

%description
Your computer has been invaded! Dozens of little viruses are pouring in via
security holes in Microsoft Internet Explorer, Microsoft Outlook, Microsoft
MSN Messenger and Microsoft Recycle Bin!! Using your trusty mouse you must
shoot the buggers before they can destroy your files! Some will steal them
from their home directories and take them back to their security hole. Others
will just eat them right there on the spot! See how long you and your computer
can survive the onslaught!

Available rpmbuild rebuild options :
--without : freedesktop

%prep
%setup
%patch0 -p0 -b .orig

%{__cat} <<EOF >icons/viruskiller.desktop
[Desktop Entry]
Name=Virus Killer
Comment=Shoot viruses invading your computer
Icon=viruskiller.png
Exec=%{_prefix}/games/viruskiller
Terminal=false
Type=Application
Categories=Application;Game;ArcadeGame;
Encoding=UTF-8
EOF

%build
%{__make} %{?_smp_mflags} PREFIX="%{_prefix}" OPTFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%{_prefix}/games/viruskiller
%{_datadir}/games/viruskiller
%{_datadir}/applications/viruskiller.desktop
%{_datadir}/pixmaps/viruskiller.png

%changelog
* Thu Jan 10 2008 Vincent Knecht <vknecht@users.sourceforge.net> 1.0-1
- Updated to release 1.0.

* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 0.9-1
- Initial RPM release.
