# $Id$

# Authority: leet
# Upstream: Shlomi Loubaton <shlomister$gmail,com>
# Screenshot: http://spacepong.sourceforge.net/spacepong1.jpg

%define desktop_vendor rpmforge
%{?dtag: %{expand: %%define %dtag 1}}

%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: An innovative Python SDL game that is controlled with the mouse
Name: spacepong
Version: 0.0.2
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://spacepong.sourceforge.net/

Source: http://dl.sf.net/sourceforge/spacepong/spacepong-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python
Requires: python, python-game
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%define prefix %{_prefix}/games/%{name}

%description
An innovative game that is controlled with the mouse.
Steer you spacecraft ball around the screen and pickup
speed by bouncing off the walls. The goal is to collect
a certain amount of space boxes in a short time

Available rpmbuild rebuild options :
--without : freedesktop

%prep
%setup -q -n %{name}-%{version}

# FIXME upstream
%{__mv} %{name} %{name}.py
%{__mv} data/COPYRIGHT .
# These should not be shipped with the source tar
%{__rm} data/msg_intro.xcf
%{__rm} data/level_data.pyc

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
Name=SpacePong
Comment=An innovative Python SDL game that is controlled with the mouse
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

%{__install} -Dp -m 0644 data/ship.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

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
%doc COPYRIGHT
%{_bindir}/%{name}
%{prefix}
%{_datadir}/pixmaps/%{name}.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Games/%{name}.desktop}
%ghost %{prefix}/*.pyc
%ghost %{prefix}/data/*.pyc

%changelog
* Fri Nov 4 2005 C.Lee Taylor <leet@leenx.co.za> 0.0.2-1
- Added ghost section for compiled python modules
- Made changes suggested by Dries

* Mon Oct 31 2005 C.Lee Taylor <leet@leenx.co.za> 0.0.2-0
- Initial packaging for Fedora Core
