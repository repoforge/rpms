# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

%{?dist: %{expand: %%define %dist 1}}

%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: Frantic shooting game where viruses invade your computer
Name: viruskiller
Version: 0.9
Release: 1
License: GPL
Group: Amusements/Games
URL: http://www.parallelrealities.co.uk/virusKiller.php
Source: viruskiller-%{version}-1.tar.gz
Patch0: viruskiller-0.9-makefile.patch
Patch1: viruskiller-0.9-zzip.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_ttf-devel
BuildRequires: zziplib-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

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
%patch0 -p1 -b .makefile
%patch1 -p1 -b .zzip


%build
%{__make} %{?_smp_mflags} PREFIX="%{_prefix}" OPTFLAGS="%{optflags}"


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# Remove shipped menu entry, no Comment, wrong Exec... :-(
%{__rm} -f %{buildroot}%{_datadir}/applications/viruskiller.desktop

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Virus Killer
Comment=Frantic shooting game where viruses invade your computer
Icon=viruskiller.png
Exec=%{_prefix}/games/viruskiller
Terminal=false
Type=Application
Categories=Application;Game;ArcadeGame;
Encoding=UTF-8
EOF

%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -D -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc doc/*
%{_prefix}/games/viruskiller
%{_prefix}/share/games/viruskiller
%{_datadir}/pixmaps/viruskiller.png
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%changelog
* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 0.9-1
- Initial RPM release.

