# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: A playlist manager for XMMS with voting support.
Name: lplayer
Version: 0.99.1
Release: 0
License: GPL
Group: Applications/Multimedia
URL: http://lplayer.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/lplayer/lplayer-%{version}_src.tgz
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

%{__cat} <<EOF >%{name}.desktop
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
#cd src
%{?rhfc1:export QTDIR="/usr/lib/qt-3.1"}
%{?rhel3:export QTDIR="/usr/lib/qt-3.1"}
%{?rh90:export QTDIR="/usr/lib/qt3"}
%{?rh80:export QTDIR="/usr/lib/qt3"}
%{?rh73:export QTDIR="/usr/lib/qt2"}
%{?rhel21:export QTDIR="/usr/lib/qt2"}
%{?rh62:export QTDIR="/usr/lib/qt-2.1.0"}
#tmake lp.pro -o Makefile
%configure \
	--disable-dependency-tracking \
	--with-xinerama
%{__make} %{?_smp_mflags} clean all

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 src/lplayer/images/lplayerlogo.png %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0755 lplayer.sh %{buildroot}%{_bindir}/lplayer

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Multimedia/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Multimedia/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor net                  \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
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
