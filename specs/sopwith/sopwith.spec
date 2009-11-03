# $Id$
# Authority: dag
# Upstream: Simon Howard <fraggle$alkali,org>

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define real_version sdl_sopwith
%define desktop_vendor rpmforge

Summary: Classic sopwith game
Name: sopwith
Version: 1.7.1
Release: 1.2%{?dist}
Group: Amusements/Games
License: GPL
URL: http://sdl-sopwith.sourceforge.net/

Source: http://dl.sf.net/sdl-sopwith/sdl_sopwith-%{version}.tar.gz
Source1: sopwith.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
BuildRequires: gtk2-devel, SDL-devel

%description
This is a port of the classic computer game "Sopwith" to run on modern
computers and operating systems.

%prep
%setup -n %{real_version}-%{version}

%{__perl} -pi -e 's|^extern BOOL *titleflg|static BOOL titleflg|g;' src/swmain.h

%{__cat} <<EOF >sopwith.desktop
[Desktop Entry]
Name=Sopwith
Comment=The classic sopwith game
Exec=gtksopwith
Type=Application
Terminal=false
Icon=sopwith.png
Categories=Application;Game;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%if %{?_without_freedesktop:1}0
        %{__install} -Dp -m0644 sopwith.desktop %{buildroot}%{_datadir}/gnome/apps/Games/sopwith.desktop
%else
        %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
        desktop-file-install --vendor %{desktop_vendor}    \
                --add-category X-Red-Hat-Base              \
                --dir %{buildroot}%{_datadir}/applications \
                sopwith.desktop
%endif

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/sopwith.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/*.txt FAQ NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_bindir}/gtksopwith
%{_datadir}/pixmaps/*.png
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-sopwith.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/sopwith.desktop}
%exclude %{_docdir}/sopwith/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.7.1-1.2
- Rebuild for Fedora Core 5.

* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 1.7.1-1
- Initial package. (using DAR)
