# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: Playlist manager for XMMS with voting support
Name: lplayer
Version: 1.01
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://lplayer.sourceforge.net/

Source: http://dl.sf.net/lplayer/lplayer_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: tmake, xmms-devel, qt, qt-devel >= 3.1

%description
longPlayer is a program that automatically fills your winamp or xmms
playlist.

It is meant for those who have converted all of their CD's into mp3's
and want to use their PC as a jukebox. Instead of turning on the
radio, they just start winamp, enqueue their entire music directory
and put the whole thing on random play.

%prep
%setup

%{__cat} <<EOF >lplayer.sh
#!/bin/sh
cd %{_datadir}/lplayer/
test -f ~/.lptable.lp2.1 && cp -f ~/.lptable.lp2.1 ~/.lptable.lp2.2
test -f ~/.lptable.lp2 && cp -f ~/.lptable.lp2 ~/.lptable.lp2.1
exec %{_bindir}/lplayer-bin
EOF

%{__cat} <<EOF >lplayer.desktop
[Desktop Entry]
Name=longplayer
Comment=%{summary}
Icon=lplayerlogo.png
Exec=%{_bindir}/lplayer
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF

%build
source "%{_sysconfdir}/profile.d/qt.sh"
#tmake lp.pro -o Makefile
%configure \
	--disable-dependency-tracking \
	--with-xinerama
%{__make} %{?_smp_mflags} clean all

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0644 src/lplayer/images/lplayerlogo.png %{buildroot}%{_datadir}/pixmaps/lplayerlogo.png
%{__install} -Dp -m0755 lplayer.sh %{buildroot}%{_bindir}/lplayer

%if %{dfi}
	%{__install} -Dp -m0644 lplayer.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/lplayer.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		lplayer.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING FAQ NEWS README TODO
%{_bindir}/*
%{_datadir}/lplayer/
%{_datadir}/pixmaps/*
%if %{dfi}
        %{_datadir}/gnome/apps/Multimedia/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.99.1-0.2
- Rebuild for Fedora Core 5.

* Thu Oct 30 2003 Dag Wieers <dag@wieers.com> - 0.99.1-0
- Updated to release 0.99.1.

* Tue Oct 01 2003 Dag Wieers <dag@wieers.com> - 0.99.0-0
- Updated to release 0.99.0.

* Tue Feb 18 2003 Dag Wieers <dag@wieers.com> - 0.98.2-2
- Added lplayer.desktop

* Tue Jan 21 2003 Dag Wieers <dag@wieers.com> - 0.98.2-1
- Updated to release 0.98.2.

* Sat Dec 28 2002 Dag Wieers <dag@wieers.com> - 0.98.1-1
- Updated to release 0.98.1. (using DAR)

* Sat Nov 30 2002 Dag Wieers <dag@wieers.com> - 0.98.0
- Initial package.
