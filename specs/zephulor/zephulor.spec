# $Id$
# Authority: leet
# Screenshot: http://games.hollowworks.com/image.php?image=zephulor001.png
# ScreenshotURL: http://games.hollowworks.com/screens.php

#%define desktop_vendor freshrpms

%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: Adventures on Planet Zephulor
Name: zephulor
Version: 0.9b
Release: 1%{?dist}
License: LGPL
Group: Amusements/Games
URL: http://games.hollowworks.com/index.php

Source: http://www.hollowworks.com/downloads/adventuresonplanetzephulor/files/%{name}-source.tar.gz
Source1: %{name}.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#Requires: python, python-game
Requires: python-game
Requires: %{name}-data
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%define prefix %{_prefix}/games/%{name}

%description
Adventures on Planet Zephulor, is a side scrolling arcade game, with fairly
simple controls. It's made in Python with Pygame.

Available rpmbuild rebuild options :
--without : freedesktop

%package data
Summary: Adventures on Planet Zephulor Game Data
Group: Amusements/Games
Requires: %{name}

%description data
Adventures on Planet Zephulor Game Data.

%package tools
Summary: Adventures on Planet Zephulor Extra Game Tools
Group: Amusements/Games
Requires: %{name}

%description tools
Adventures on Planet Zephulor Extra Game Tools.

%prep
# Need to ask to fix upstream ...
%setup -n %{name}-source

%build
# Remove execute from txt
%{__chmod} -x *.txt
%{__chmod} -x maptool/*.txt

# Create a general run file ...
%{__cat} > %{name} << EOF
#!/bin/bash
cd /usr/share/games/zephulor
python ./zephulor.py
EOF

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Zephulor
Comment=Adventures on Planet Zephulor
Exec=zephulor
Icon=zephulor.png
Terminal=false
Version=0.9b
Type=Application
Encoding=UTF-8
Categories=Application;Game;
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -d -m 0755 %{buildroot}%{_datadir}/games/%{name}
%{__install} -d -m 0755 %{buildroot}%{_datadir}/games/%{name}/data
%{__install} -d -m 0755 %{buildroot}%{_datadir}/games/%{name}/maptool
%{__install} -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%{__install} -D -m 0644 *.py %{buildroot}%{_datadir}/games/%{name}
%{__install} -D -m 0644 data/* %{buildroot}%{_datadir}/games/%{name}/data
%{__install} -D -m 0644 maptool/* %{buildroot}%{_datadir}/games/%{name}/maptool

%{__chmod} +x %{buildroot}%{_datadir}/games/%{name}/%{name}.py
%{__chmod} +x %{buildroot}%{_datadir}/games/%{name}/chared.py
%{__chmod} +x %{buildroot}%{_datadir}/games/%{name}/maploadtool.py
%{__chmod} +x %{buildroot}%{_datadir}/games/%{name}/scnloadtool.py
%{__chmod} +x %{buildroot}%{_datadir}/games/%{name}/maptool/chared.py
%{__chmod} +x %{buildroot}%{_datadir}/games/%{name}/maptool/main.py

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
#    %{buildroot}%{_datadir}/applications/%{name}.desktop
%else
%{__install} -D -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif

# Convert the ICO file to png to be used as the menu entry icon
#%{__install} -d -m 0755 %{buildroot}%{_datadir}/pixmaps
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING.txt LGPL.txt manual.txt README.txt
%{_bindir}/%{name}
%{_datadir}/games/%{name}/*.py
%exclude %{_datadir}/games/%{name}/chared.py
%exclude %{_datadir}/games/%{name}/maploadtool.py
%exclude %{_datadir}/games/%{name}/scnloadtool.py
%exclude %{_datadir}/games/%{name}/data
%{_datadir}/pixmaps/%{name}.png
#%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Games/%{name}.desktop}

%files data
%defattr(-, root, root, 0755)
%{_datadir}/games/%{name}/data

%files tools
%defattr(-, root, root, 0755)
%doc readme-chared.txt readme-maploadtool.txt readme-scnloadtool.txt
%{_datadir}/games/%{name}/maptool
%{_datadir}/games/%{name}/chared.py
%{_datadir}/games/%{name}/maploadtool.py
%{_datadir}/games/%{name}/scnloadtool.py

%changelog
* Thu Jun 09 2005 C.Lee Taylor <leet@leenx.co.za> (20041026) 0.9b-1
- fix rpmlint warning
- Made some updates for Fedora Extra

* Fri Jan 14 2005 C.Lee Taylor <leet@leenx.co.za> (20041026) 0.9b-0
- Add icon and change version to what the aurther explained

* Tue Jan 11 2005 C.Lee Taylor <leet@leenx.co.za> (20041026) 0.1-0
- first packaging for Fedora Core

