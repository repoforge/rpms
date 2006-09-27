# $Id$
# Authority: dag
# Upstream: <glchess-devel$lists,sf,net>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define desktop_vendor rpmforge

Summary: 3D chess interface
Name: glchess
Version: 0.9.8
Release: 1
License: GPL
Group: Amusements/Games
URL: http://glchess.sourceforge.net/

Source: http://dl.sf.net/glchess/glchess-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gettext, gtk+-devel >= 1.2.0
#BuildRequires: gtkglarea

%description
glChess is a 3D OpenGL based chess game that interfaces via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently use
Crafty and GNU Chess as AIs. You can also play Human vs. Human, but so far
not over a netwerk (see TODO).

%prep
%setup

#%{__perl} -pi.orig -e 's|/usr/local/share/games/glchess|%{_datadir}/games/glchess|' glchessrc

#%{__cat} <<EOF >glchess.desktop
#[Desktop Entry]
#Name=GLChess
#Comment=Play chess in 3D
#Exec=glchess
#Icon=chess.png
#Terminal=false
#Type=Application
#Categories=Application;Game;
#EOF

%build
#configure
#%{__make} %{?_smp_mflags}
%{__make} translations
python setup.py build

%install
%{__rm} -rf %{buildroot}
#%{__install} -Dp -m0755 src/glchess %{buildroot}%{_bindir}/glchess
#%{__install} -Dp -m0644 man/glchess.6 %{buildroot}%{_mandir}/man6/glchess.6
#%{__install} -Dp -m0644 glchessrc %{buildroot}%{_sysconfdir}/glchessrc
#%{__install} -Dp -m0644 glchess.menu %{buildroot}%{_sysconfdir}/X11/wmconfig/glchess.menu
#
#%{__install} -d -m0755 %{buildroot}%{_datadir}/games/glchess/textures/
#%{__install} -p -m0644 textures/* %{buildroot}%{_datadir}/games/glchess/textures/

#%if %{?_without_freedesktop:1}0
#	%{__install} -Dp -m0644 glchess.desktop %{buildroot}%{_datadir}/gnome/apps/Games/glchess.desktop
#%else
#	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
#	desktop-file-install --vendor "%{desktop_vendor}"  \
#		--add-category X-Red-Hat-Base              \
#		--dir %{buildroot}%{_datadir}/applications \
#		glchess.desktop
#%endif
%{__make} install DESTDIR="%{buildroot}"
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}" --prefix="%{_prefix}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc BUGS ChangeLog COPYING INSTALL README TODO
%{_bindir}/glchess
%{_datadir}/applications/glchess.desktop
%{_datadir}/games/glchess/
%{_datadir}/pixmaps/glchess.svg
%{python_sitelib}/glchess/
%ghost %{python_sitelib}/glchess/*.pyo
%ghost %{python_sitelib}/glchess/*/*.pyo

%changelog
* Thu Sep 14 2006 Dag Wieers <dag@wieers.com> - 0.9.8-1
- Updated to release 0.9.8.
- Converted to python installation. (Andrew Ziem)

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Sat Apr 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.0-1
- Updated to release 0.9.0.

* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.4.7-0
- Initial package. (using DAR)
