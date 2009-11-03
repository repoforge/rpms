# $Id$
# Authority: dries
# Upstream:
# Screenshot: http://gemhun.sourceforge.net/images/screenshots/20031016/jungle.jpg

Summary: Group gems together
Name: gemhunters
%define real_version 20040529
Version: 0.20040529
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://gemhun.sourceforge.net/

Source: http://dl.sf.net/gemhun/GemHunters-src-%{real_version}.tar.gz
# Source1: http://dl.sf.net/gemhun/GemHunters-data-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, kyra-devel, SDL_image-devel, gcc-c++, bison
BuildRequires: SDL_mixer-devel, SDL_net-devel, automake14, gettext
BuildRequires: ncurses-devel, libvorbis-devel, desktop-file-utils

%description
Gemhun is all about grouping gems/stones of a chosen amount together which
will then dissappear. There will be plenty of different game-modes, theme-
and network-support. It is inspired by FrozenBubble/Tetris and some others.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n GemHunters-%{real_version}

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Gem Hunters
Comment=Hunt the gems
Exec=gemhun
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=Application;Game;X-Red-Hat-Extra;
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -Rf %{buildroot}/usr/doc/GemHunters

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/GemHunters

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/GemHunters/*.h

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.20040529-1.2
- Rebuild for Fedora Core 5.

* Sun May 30 2004 Dries Verachtert <dries@ulyssis.org>
- Initial package.

