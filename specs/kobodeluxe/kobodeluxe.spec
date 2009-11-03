# $Id$
# Authority: dag

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

%define real_name KoboDeluxe

Summary: SDL port of Akira Higuchi's game XKobo 
Name: kobodeluxe
Version: 0.4
Release: 0.pre10%{?dist}
License: GPL
Group: Amusements/Games
URL: http://www.olofson.net/kobodl/

Source0: http://olofson.net/kobodl/download/KoboDeluxe-%{version}pre10.tar.gz
Source5: kobodeluxe-16.png
Source6: kobodeluxe-32.png
Source7: kobodeluxe-48.png
Patch0: kobodeluxe-0.4pre10-gcc4.patch
Patch1: kobodeluxe-0.4pre10-various-from-debian.patch
Patch2: kobodeluxe-0.4pre10-fix-segfault-in-midi.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Obsoletes: skobo <= %{version}-%{release}
Provides: skobo = %{version}-%{release}
BuildRequires: SDL_image-devel

%description
Kobo Deluxe is an SDL port of Akira Higuchi's game XKobo. It adds sound,
smoother animation, filtered high resolution support, a more intuitive menu
driven user interface, joystick support and other features, and runs on most
of the major operating systems.

%prep
%setup -n %{real_name}-%{version}pre10
%patch0 -p0 -b .gcc4
%patch1 -p1
%patch2 -p1 -z .pix

%{__cat} <<EOF >kobodeluxe.desktop
[Desktop Entry]
Encoding=UTF-8
Name=Kobo Deluxe
Comment=Arcade video game
Exec=%{_bindir}/kobodl
Icon=kobodeluxe
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%build
%configure \
	--program-prefix="%{?_program_prefix}"
%{__make} kobo_scoredir="%{_localstatedir}/games/kobo-deluxe"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/games/kobo-deluxe/
%{__make} install DESTDIR="%{buildroot}" kobo_scoredir="%{_localstatedir}/games/kobo-deluxe/"

%{__install} -Dp -m0644 %{SOURCE6} %{buildroot}%{_datadir}/icons/hicolor/16x16/kobodeluxe.png
%{__install} -Dp -m0644 %{SOURCE5} %{buildroot}%{_datadir}/icons/hicolor/32x32/kobodeluxe.png
%{__install} -Dp -m0644 %{SOURCE7} %{buildroot}%{_datadir}/icons/hicolor/48x48/kobodeluxe.png

%if %{?_without_freedesktop:1}0
	%{__install} -Dp -m0644 kobodeluxe.desktop %{buildroot}%{_sysconfdir}/X11/applnk/Games/kobodeluxe.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install                               \
		--vendor %{desktop_vendor}                 \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		kobodeluxe.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%post 
update-desktop-database %{_datadir}/applications &>/dev/null || :

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING* README* TODO
%doc %{_mandir}/man6/kobodl.6*
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-kobodeluxe.desktop}
%{?_without_freedesktop:%{_sysconfdir}/X11/applnk/Games/kobodeluxe.desktop}
%{_datadir}/games/kobo-deluxe/
%{_datadir}/icons/hicolor/16x16/kobodeluxe.png
%{_datadir}/icons/hicolor/32x32/kobodeluxe.png
%{_datadir}/icons/hicolor/48x48/kobodeluxe.png

%defattr(2755, root, games, 0755)
%{_bindir}/kobodl

%defattr(0775, root, games, 0775)
%{_localstatedir}/games/kobo-deluxe/

%changelog
* Tue Feb 13 2007 Dag Wieers <dag@wieers.com> - 0.4-0.pre10
- Initial package. (using DAR)
