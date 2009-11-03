# $Id$
# Authority: koenraad
# Upstream: Stephen Bach <sjbach$users,sourceforge,net>

# Screenshot: http://viewglob.sourceforge.net/screenshots/2.0/1_small.jpeg
# ScreenshotURL: http://viewglob.sourceforge.net/screenshots.html

%define desktop_vendor rpmforge

Summary: Current tree visualisation add-on for Bash and Zsh and also shows glob patterns.
Name: viewglob
Version: 2.0.1
Release: 2%{?dist}
License: GPL and http://www.basepath.com/aup/copyright.htm
Group: Applications/System
URL: http://viewglob.sourceforge.net/

Source: http://dl.sf.net/viewglob/viewglob-%{version}.tar.gz
Patch: viewglob-2.0.1-default_terminal.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bash, gtk2-devel >= 2.4, pkgconfig, autoconf, automake
BuildRequires: desktop-file-utils
Requires: bash, gtk2 >= 2.4

%description
A visualition add-on for Bash and Zsh that shows the current tree (visual ls of
the current dir) and the glob patterns. This allows one to evaluate the
ramifications of a command while typing. and it eases the tab-completion driven
input. It uses a client-daemon model which makes it useful through ssh
connections. It's no filemanager or replacement for ls.

%prep
%setup
%patch

%{__cat} <<EOF >viewglob.desktop
[Desktop Entry]
Name=Viewglob
Comment=Add-on visualizer for bash and zsh
Icon=viewglob.png
Exec=viewglob
Terminal=true
Type=Application
StartupNotify=true
Categories=GNOME;Application;System;
EOF


%build
autoreconf --force --install --symlink
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0755 vgdisplay/icon_36x36.png  %{buildroot}%{_datadir}/pixmaps/viewglob.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	viewglob.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING* HACKING INSTALL NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/viewglob/
%{_datadir}/pixmaps/viewglob.png
%{_datadir}/applications/%{desktop_vendor}-viewglob.desktop

%changelog
* Sat May 07 2005 Koenraad Heijlen <krpms@heijlen.be> 2.0.1-2
- Patched the viewglob command with support for gconf settings
  for the default terminal (sent upstream).

* Sat May 07 2005 Koenraad Heijlen <krpms@heijlen.be> - 2.0.1-1
- Initial package.
