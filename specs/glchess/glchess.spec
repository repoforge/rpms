# $Id$
# Authority: dag
# Upstream: <glchess-devel@lists.sf.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: 3D chess interface
Name: glchess
Version: 0.4.7
Release: 1
License: GPL
Group: Amusements/Games
URL: http://glchess.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/glchess/glchess-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2.0, gtkglarea

%description
glChess is a 3D OpenGL based chess game that interfaces via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently use
Crafty and GNU Chess as AIs. You can also play Human vs. Human, but so far
not over a netwerk (see TODO).

%prep
%setup

%{__perl} -pi.orig -e 's|/usr/local/share/games/glchess|%{_datadir}/games/glchess|' glchessrc

%{__cat} <<EOF >glchess.desktop
[Desktop Entry]
Name=GLChess
Comment=Play chess in 3D
Exec=glchess
Icon=chess.png
Terminal=false
Type=Application
Categories=Application;Game;
EOF

%build
./autogen.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 src/glchess %{buildroot}%{_bindir}/glchess
%{__install} -D -m0644 man/glchess.6 %{buildroot}%{_mandir}/man6/glchess.6
%{__install} -D -m0644 glchessrc %{buildroot}%{_sysconfdir}/glchessrc
%{__install} -D -m0644 glchess.menu %{buildroot}%{_sysconfdir}/X11/wmconfig/glchess.menu

%{__install} -d -m0755 %{buildroot}%{_datadir}/games/glchess/textures/
%{__install} -m0644 textures/* %{buildroot}%{_datadir}/games/glchess/textures/

%if %{dfi}
	%{__install} -D -m0644 glchess.desktop %{buildroot}%{_datadir}/gnome/apps/Games/glchess.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor "net"                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		glchess.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man6/*
%config %{_sysconfdir}/glchessrc
%config %{_sysconfdir}/X11/wmconfig/*
%{_bindir}/*
%{_datadir}/games/glchess/
%if %{dfi}
        %{_datadir}/gnome/apps/Games/*.desktop
%else
        %{_datadir}/applications/*.desktop
%endif

%changelog
* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.4.7-0
- Initial package. (using DAR)
