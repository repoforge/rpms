# $Id$

# Authority: dag
# Upstream: <gnocatan-develop@sourceforge.net>

%define dfi %(which desktop-file-install &>/dev/null; echo $?)

Summary: An addictive game based on "The Settlers of Catan".
Name: gnocatan
Version: 0.8.1.16
Release: 1
License: GPL
Group: Amusements/Games
URL: http://gnocatan.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gnocatan/gnocatan-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: libxml2-devel, gtk2-devel, libgnome-devel, glib2-devel
BuildRequires: scrollkeeper

Requires(post): scrollkeeper

%description
Gnocatan is an Internet playable implementation of the Settlers of
Catan board game. The aim is to remain as faithful to the board game
as is possible.

This package contains the game itself and an AI player.

%package server
Summary: Gnocatan gaming server.
Group: Amusements/Games

%description server
Gnocatan is an Internet playable implementation of the Settlers of
Catan board game. The aim is to remain as faithful to the board game
as is possible.

This package contains the server and meta server with a console and
GUI frontend.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%if !%{dfi}
	desktop-file-install --vendor gnome --delete-original \
		--add-category X-Red-Hat-Base                 \
		--add-category GNOME                          \
		--add-category Application                    \
		--add-category Game                           \
		--dir %{buildroot}%{_datadir}/applications    \
		%{buildroot}%{_datadir}/gnome/apps/Games/gnocatan.desktop \
		%{buildroot}%{_datadir}/gnome/apps/Games/gnocatan-server.desktop
%endif

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
scrollkeeper-update -q || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man6/gnocatan.6*
%doc %{_mandir}/man6/gnocatanai.6*
%doc %{_datadir}/gnome/help/gnocatan/
%{_bindir}/gnocatan
%{_bindir}/gnocatanai
%dir %{_datadir}/games/gnocatan/
%{_datadir}/games/gnocatan/computer_names
%{_datadir}/games/gnocatan/themes/
%{_datadir}/applications/gnome-gnocatan.desktop
%{_datadir}/omf/gnocatan/
%{_datadir}/pixmaps/*

%files server
%defattr(-, root, root, 0755)
%doc %{_mandir}/man6/gnocatan-meta-server.6*
%doc %{_mandir}/man6/gnocatan-server-console.6*
%doc %{_mandir}/man6/gnocatan-server-gtk.6*
%{_bindir}/gnocatan-meta-server
%{_bindir}/gnocatan-server-console
%{_bindir}/gnocatan-server-gtk
%dir %{_datadir}/games/gnocatan/
%{_datadir}/games/gnocatan/*.game
%{_datadir}/applications/gnome-gnocatan-server.desktop

%changelog
* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.8.1.16-1
- Updated to release 0.8.1.16.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 0.8.0.0-1
- Split gnocatan into a seperate server package.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 0.8.0.0-0
- Initial package. (using DAR)
