# $Id$
# Authority: matthias

%define real_version   021212
%define desktop_vendor rpmforge


%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: Clone of the Rick Dangerous classic game
Name: xrick
Version: 0.0.%{real_version}
Release: 2%{?dist}
License: GPL/Proprietary
Group: Amusements/Games
URL: http://www.bigorno.net/xrick/
Source: http://www.bigorno.net/xrick/xrick-%{real_version}.tgz
Patch: xrick-rpmoptflags-makefile.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, zlib-devel, ImageMagick
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Way before Lara Croft, back in the 1980's and early 1990's, Rick Dangerous was
the Indiana Jones of computer games, running away from rolling rocks, avoiding
traps, from South America to a futuristic missile base via Egypt and the
Schwarzendumpf castle.

Available rpmbuild rebuild options :
--without : freedesktop


%prep
%setup -n %{name}-%{real_version}
%patch -p1 -b .optflags
%{__perl} -pi.orig -e 's|data.zip|%{_datadir}/games/%{name}/data.zip|g' \
    src/xrick.c


%build
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot} xrick.png
# Uncompress the man page for now, it may get re-compressed later on
%{__gzip} -d xrick.6.gz
%{__install} -Dp -m 0755 xrick %{buildroot}%{_bindir}/xrick
%{__install} -Dp -m 0644 data.zip %{buildroot}%{_datadir}/games/%{name}/data.zip
%{__install} -Dp -m 0644 xrick.6 %{buildroot}%{_mandir}/man6/xrick.6

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=X Rick
Comment=A "Rick Dangerous" clone
Exec=xrick
Icon=xrick.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;Game;
EOF

%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -Dp -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif

# Convert the ICO file to png to be used as the menu entry icon
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
convert src/xrickST.ico %{buildroot}%{_datadir}/pixmaps/xrick.png


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/xrick
%{_datadir}/games/%{name}/
%{_mandir}/man6/xrick.6*
%{_datadir}/pixmaps/xrick.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop}
%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Games/%{name}.desktop}


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.0.021212-2
- Release bump to drop the disttag number in FC5 build.

* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 0.0.021212-1
- Spec file cleanup.

* Tue Aug  5 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.4.021212
- using convert at build time to do ico->png conversion

* Thu Jul 17 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.3.021212
- Added icon for menu

* Wed Jun 18 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.2.0212120
- Desktop entry : oops !! Sorry.

* Tue Jun 17 2003 Dams <anvil[AT]livna.org> 0:0.0-0.fdr.1.0212120
- Modified Summary
- Package now own datadir/games/xrick directory

* Mon May 19 2003 Dams <anvil[AT]livna.org> 0:021212-0.fdr.4
- Added a desktop entry. BuildRequires desktop-file-utils.
- Modified the patch to keep ansi/pedantic and other gcc warning flags

* Tue May 13 2003 Dams <anvil[AT]livna.org> 0:021212-0.fdr.3
- Patch to accept RPM_OPT_FLAGS from Michael Schwendt

* Tue May 13 2003 Dams <anvil[AT]livna.org> 0:021212-0.fdr.2
- buildroot -> RPM_BUILD_ROOT
- Modified Source0

* Wed Apr 23 2003 Dams <anvil[AT]livna.org>
- Initial build.
