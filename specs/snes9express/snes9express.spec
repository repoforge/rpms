# $Id$
# Authority: matthias

%define default_skin snes

%define desktop_vendor rpmforge

%{?dtag: %{expand: %%define %dtag 1}}
%{?el2:%define _without_freedesktop 1}
%{?rh7:%define _without_freedesktop 1}

Summary: Graphical front-end to snes9x, the SNES emulator
Name: snes9express
Version: 1.42
Release: 3%{?dist}
License: GPL
Group: Applications/Emulators
URL: http://www.linuxgames.com/snes9express/
Source0: http://dl.sf.net/snes9express/snes9express-%{version}.tar.gz
Source1: snes.png
Patch0: snes9express-1.42-errno.patch
Patch1: snes9express-1.42-gcc41.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: snes9x
BuildRequires: gcc-c++, gtk2-devel
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
Snes9express is a graphical interface for the X11 versions of snes9x, the
freeware Super Nintendo Entertainment System (TM) emulator, featuring an
organized layout of common snes9x options.


%prep
%setup
%patch0 -p1 -b .errno
%patch1 -p0 -b .gcc41


%build
%configure
%{__make} %{_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
echo %{default_skin} > %{buildroot}%{_datadir}/snes9express/defaultskin

# Install menu icon
%{__install} -Dp -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/snes.png

# Install menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=SNES9eXpress
Comment=Super Nintendo Entertainment System emulator
Icon=snes.png
Exec=snes9express
Terminal=false
Type=Application
Categories=Application;Game;
Encoding=UTF-8
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


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/snes9express
%{_datadir}/pixmaps/snes.png
%{_datadir}/snes9express/
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Games/%{name}.desktop
%endif


%changelog
* Sun Oct 22 2006 Matthias Saou <http://freshrpms.net/> 1.42-3
- Explicitly require snes9x, since not having it doesn't really make sense...

* Mon Sep  4 2006 Matthias Saou <http://freshrpms.net/> 1.42-2
- Add gcc41 patch from Gentoo.

* Sun Oct 19 2004 Matthias Saou <http://freshrpms.net/> 1.42-1
- Initial RPM release.

