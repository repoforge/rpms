# $Id$

# Authority: dag

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: glChess - A 3D chess interface
Name: glchess
Version: 0.4.7
Release: 0
License: GPL
Group: Amusements/Games
URL: http://glchess.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/glchess/glchess-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: gtk+-devel >= 1.2.0, gtkglarea

%description
glChess is a 3D OpenGL based chess game that interfaces via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently use
Crafty and GNU Chess as AIs. You can also play Human vs. Human, but so far
not over a netwerk (see TODO).

%prep
%setup

%build
./autogen.sh
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man6 \
			%{buildroot}%{_datadir}/games/glchess/textures \
			%{buildroot}%{_sysconfdir}/X11/wmconfig
%{__install} -m0755 src/glchess %{buildroot}%{_bindir}
%{__install} -m0644 man/glchess.6 %{buildroot}%{_mandir}/man6/
%{__install} -m0644 textures/* %{buildroot}%{_datadir}/games/glchess/
%{__install} -m0644 glchessrc %{buildroot}%{_sysconfdir}
%{__install} -m0644 glchess.menu %{buildroot}%{_sysconfdir}/X11/wmconfig/

cat <<EOF >%{name}.desktop
[Desktop Entry]
Name=GLChess
Comment=A 3D Chess game
Exec=glchess
Icon=chess.png
Terminal=false
Type=Application
EOF

%if %{dfi}
	%{__install} -d -m0755 %{buildroot}%{_datadir}/gnome/apps/Games/
	%{__install} -m0644 %{name}.desktop %{buildroot}%{_datadir}/gnome/apps/Games/
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
	desktop-file-install --vendor "gnome"              \
		--add-category X-Red-Hat-Base              \
		--add-category Application                 \
		--add-category Game                        \
		--dir %{buildroot}%{_datadir}/applications \
		%{name}.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING NEWS README TODO
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
