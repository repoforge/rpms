# $Id$
# Authority: dag
# Upstream: <gnocatan-develop$sf,net>


%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Addictive game based on "The Settlers of Catan"
Name: gnocatan
Version: 0.8.1.43
Release: 1.2%{?dist}
License: GPL
Group: Amusements/Games
URL: http://gnocatan.sourceforge.net/

Source: http://dl.sf.net/gnocatan/gnocatan-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel, gtk2-devel, libgnome-devel, glib2-devel
BuildRequires: scrollkeeper, gcc-c++, libgnomeui-devel
BuildRequires: gettext
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}
Requires(post): scrollkeeper

%description
Gnocatan is an Internet playable implementation of the Settlers of
Catan board game. The aim is to remain as faithful to the board game
as is possible.

This package contains the game itself and an AI player.

%package server
Summary: Gnocatan gaming server
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

%if %{!?_without_freedesktop:1}0
	desktop-file-install \
		--vendor %{desktop_vendor} --delete-original  \
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
%{_datadir}/applications/%{desktop_vendor}-gnocatan.desktop
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
%{_datadir}/applications/%{desktop_vendor}-gnocatan-server.desktop

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.8.1.43-1.2
- Rebuild for Fedora Core 5.

* Tue Nov 23 2004 Dag Wieers <dag@wieers.com> - 0.8.1.43-1
- Updated to release 0.8.1.43.

* Mon Nov 01 2004 Dag Wieers <dag@wieers.com> - 0.8.1.30-1
- Updated to release 0.8.1.30.

* Sat Mar 06 2004 Dag Wieers <dag@wieers.com> - 0.8.1.16-1
- Updated to release 0.8.1.16.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 0.8.0.0-1
- Split gnocatan into a seperate server package.

* Wed Oct 15 2003 Dag Wieers <dag@wieers.com> - 0.8.0.0-0
- Initial package. (using DAR)
