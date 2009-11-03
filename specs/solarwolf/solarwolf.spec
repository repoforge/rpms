# $Id$

# Authority: dries
# Upstream: Pete Shinners <pete$shinners,org>
# Screenshot: http://www.pygame.org/shredwheat/solarwolf/screen/shot4.jpg
# ScreenshotURL: http://www.pygame.org/shredwheat/solarwolf/

%define desktop_vendor rpmforge

%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: Python SDL game where you have to collect energy cubes
Name: solarwolf
Version: 1.5
Release: 2.2%{?dist}
License: LGPL
Group: Amusements/Games
URL: http://www.pygame.org/shredwheat/solarwolf/

Source: http://www.pygame.org/shredwheat/solarwolf/%{name}-%{version}.tar.gz
#Source1: makefileandshellscript.tar.bz2
#Source2: %{name}.png

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: python, python-game
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%define prefix %{_prefix}/games/%{name}

%description
In SolarWolf you play a pilot collecting energy cubes from the defending
guardians. Avoid the deadly bullets, which become ever more popular as you
race through 48 levels. Good Luck.

Available rpmbuild rebuild options :
--without : freedesktop

%prep
%setup

# Create a general run file ...
%{__cat} > %{name} << EOF
#!/bin/bash
cd %{prefix}
killall artsd
killall esd
python ./%{name}.py \$*
EOF

## Add the icon to desktop
#%{__cat} >> dist/%{name}.desktop << EOF
#Comment=%{Summary}
#Icon=%{name}.png
#Version=%{version}
#EOF

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=SolarWolf
Comment=Python SDL game where you have to collect energy cubes
Exec=%{name}
Icon=%{name}.png
Terminal=false
Version=%{version}
Type=Application
Encoding=UTF-8
Categories=Application;Game;ArcadeGame
EOF

%build
#make

%install
%{__rm} -rf %{buildroot}
#export DESTDIR=%{buildroot}
#make install

%{__install} -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%{__install} -D -m 0644 %{name}.py %{buildroot}%{prefix}/%{name}.py
%{__chmod} +x %{buildroot}%{prefix}/%{name}.py

%{__mv} code %{buildroot}%{prefix}
%{__mv} data %{buildroot}%{prefix}

%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    --delete-original \
    --add-category X-Fedora \
    --add-category Application \
    --add-category Game \
    %{name}.desktop
%else
%{__install} -D -m 0644 dist/%{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif

#%{__install} -Dp -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -Dp -m 0644 dist/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -Dp -m 0644 dist/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

%{__install} -Dp -m 0644 dist/%{name}.6.gz %{buildroot}%{_mandir}/man6/%{name}.6.gz

%clean
%{__rm} -rf %{buildroot}

%post
%if %{!?_without_freedesktop:1}0
    # Updating icons
    update-desktop-database &> /dev/null ||:
%endif
touch --no-create %{_datadir}/pixmaps/ || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    # Would try and update icons here
    # FIXME - Does some funny things on my box, but is correct
#    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/pixmaps/ || :
    echo " " &> /dev/null ||:
fi

%postun
%if %{!?_without_freedesktop:1}0
    #Updating icons
    update-desktop-database &> /dev/null ||:
%endif
touch --no-create %{_datadir}/pixmaps/ || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
    # Would try and update icons here
    # FIXME - Does some funny things on my box, but is correct
#    %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/pixmaps/ || :
    echo " " &> /dev/null ||:
fi

%files
%defattr(-, root, root, 0755)
%doc lgpl.txt readme.txt
%doc %{_mandir}/man?/*
%{_bindir}/%{name}
%{prefix}
%{_datadir}/pixmaps/%{name}.*
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Games/%{name}.desktop}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-2.2
- Rebuild for Fedora Core 5.

* Mon Oct 31 2005 C.Lee Taylor <leet@leenx.co.za> 1.5-2
- Add icon for menu and update Desktop cache.
- Remove Make patch

* Mon Mar 14 2005 Dries Verachtert <dries@ulyssis.org> 1.5-1
- update to release 1.5

* Sun Jan 25 2004 Dries Verachtert <dries@ulyssis.org> 1.4-2
- update of spec file

* Fri Dec 9 2003 Dries Verachtert <dries@ulyssis.org> 1.4-1
- update to version 1.4

* Fri Dec 2 2003 Dries Verachtert <dries@ulyssis.org> 1.3-2
- added a desktop file

* Wed Nov 24 2003 Dries Verachtert <dries@ulyssis.org> 1.3-1
- first packaging for Fedora Core 1
