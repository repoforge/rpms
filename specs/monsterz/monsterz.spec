# $Id$

# Authority: leet
# Upstream: Sam Hocevar <sam$zoy,org>
# Screenshot: http://sam.zoy.org/monsterz/monsterz-1.png

%define desktop_vendor rpmforge
%{?dtag: %{expand: %%define %dtag 1}}

%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: Little arcade puzzle game, similar to the famous Bejeweled
Name: monsterz
Version: 0.7.0
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://sam.zoy.org/monsterz/

Source: http://sam.zoy.org/monsterz/monsterz-%{version}.tar.gz

BuildRequires: python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

Requires: python, python-game
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%define prefix %{_prefix}/games/%{name}

%description
 The goal of the game is to create rows of similar monsters, either
horizontally or vertically. The only allowed move is the swap of two
adjacent monsters, on the condition that it creates a row of three
or more. When alignments are cleared, pieces fall from the top of
the screen to fill the board again. Chain reactions earn you even
more points.

Available rpmbuild rebuild options :
--without : freedesktop

%prep
%setup -q

# Create a general run file ...
%{__cat} > %{name} << EOF
#!/bin/bash
cd %{prefix}
killall artsd
killall esd
python ./%{name}.py \$*
EOF

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Monsterz
Comment=Little arcade puzzle game, similar to the famous Bejeweled
Exec=%{name}
Icon=%{name}.png
Terminal=false
Version=%{version}
Type=Application
Encoding=UTF-8
Categories=Application;Game;ArcadeGame;
EOF

%build
#make

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%{__install} -D -m 0644 %{name}.py %{buildroot}%{prefix}/%{name}.py
%{__chmod} +x %{buildroot}%{prefix}/%{name}.py

%{__install} -Dp -m 0644 graphics/icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%{__mv} graphics %{buildroot}%{prefix}
%{__mv} sound %{buildroot}%{prefix}

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
%{__install} -D -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif

# Used to create *.pyc files to use in the ghost section
python -c "import compileall; compileall.compile_dir('%{buildroot}')"

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
%doc AUTHORS COPYING INSTALL README TODO
%{_bindir}/%{name}
%{prefix}
%{_datadir}/pixmaps/%{name}.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Games/%{name}.desktop}
%ghost %{prefix}/*.pyc

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Updated to release 0.7.0.

* Fri Nov 4 2005 C.Lee Taylor <leet@leenx.co.za> 0.6.1-1
- Ghost section and changes by Dries

* Mon Oct 31 2005 C.Lee Taylor <leet@leenx.co.za> 0.6.1-0
- Initial packaging for Fedora Core
