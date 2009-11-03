# $Id$
# Authority: dag

%define desktop_vendor rpmforge

Summary: Playable implementation of the Settlers of Catan 
Name: pioneers
Version: 0.11.3
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://pio.sourceforge.net/

Source: http://dl.sf.net/pio/pioneers-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libxml2-devel, gtk2-devel, libgnome-devel, glib2-devel >= 2.6
BuildRequires: scrollkeeper, gcc-c++, libgnomeui-devel
BuildRequires: gettext, desktop-file-utils
Requires(post): scrollkeeper

Provides: gnocatan
Obsoletes: gnocatan

%description
Pioneers is an Internet playable implementation of the Settlers of
Catan board game. The aim is to remain as faithful to the board game
as is possible.

This package contains the client software to play the game, the help
files, the game editor that allows maps and game descriptions to
be created and edited graphically and a computer player that can take
part in Pioneers games.

%package server
Summary: Pioneers Data
Group: Amusements/Games

Provides: gnocatan-server
Obsoletes: gnocatan-server

%description server
Pioneers is an Internet playable implementation of the Settlers of
Catan board game. The aim is to remain as faithful to the board game
as is possible.

This package contains the data files for a game server and the meta
server that registers available game servers and offers them to new
players. It can also create new servers on client request.

%package server-gui
Summary: Pioneers GTK Server
Group: Amusements/Games
Requires: pioneers-server

%description server-gui
Pioneers is an Internet playable implementation of the Settlers of
Catan board game. The aim is to remain as faithful to the board game
as is possible.

The server has a user interface in which you can customise the game
parameters. Customisation is fairly limited at the moment, but this
should change in later versions.  Once you are happy with the game
parameters, press the Start Server button, and the server will start
listening for client connections.

%prep
%setup

%build
%configure
%{__make} %{?_smp_flags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install \
    --vendor %{desktop_vendor} --delete-original  \
    --add-category X-Red-Hat-Base                 \
    --add-category GNOME                          \
    --add-category Application                    \
    --add-category Game                           \
    --dir %{buildroot}%{_datadir}/applications    \
    %{buildroot}%{_datadir}/applications/pioneers.desktop \
    %{buildroot}%{_datadir}/applications/pioneers-editor.desktop \
    %{buildroot}%{_datadir}/applications/pioneers-server.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_localstatedir}/scrollkeeper/

%post
scrollkeeper-update -q -o %{_datadir}/omf/pioneers/ || :

%postun
scrollkeeper-update -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS TODO
%doc %{_mandir}/man6/pioneers.6*
%doc %{_mandir}/man6/pioneersai.6*
%doc %{_datadir}/gnome/help/pioneers/
%{_bindir}/pioneers
%{_bindir}/pioneersai
%{_bindir}/pioneers-editor
%{_datadir}/applications/%{desktop_vendor}-pioneers-editor.desktop
%{_datadir}/applications/%{desktop_vendor}-pioneers.desktop
%dir %{_datadir}/games/pioneers/
%{_datadir}/games/pioneers/themes/
%{_datadir}/omf/pioneers/
%{_datadir}/pixmaps/pioneers.png
%{_datadir}/pixmaps/pioneers-editor.png
%{_datadir}/pixmaps/pioneers/

%files server
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS TODO
%doc %{_mandir}/man6/pioneers-meta-server.6*
%doc %{_mandir}/man6/pioneers-server-console.6*
%{_bindir}/pioneers-meta-server
%{_bindir}/pioneers-server-console
%dir %{_datadir}/games/pioneers/
%{_datadir}/games/pioneers/computer_names
%{_datadir}/games/pioneers/*.game

%files server-gui
%defattr(-, root, root, 0755)
%doc %{_mandir}/man6/pioneers-server-gtk.6*
%{_bindir}/pioneers-server-gtk
%{_datadir}/applications/%{desktop_vendor}-pioneers-server.desktop
%{_datadir}/pixmaps/pioneers-server.png

%changelog
* Mon Oct 22 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.3-1
- Updated to release 0.11.3.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 0.11.2-1
- Updated to release 0.11.2.

* Mon Jul 23 2007 Dries Verachtert <dries@ulyssis.org> - 0.11.1-1
- Updated to release 0.11.1.

* Mon Nov 13 2006 Dries Verachtert <dries@ulyssis.org> - 0.10.2-1
- Updated to release 0.10.2.

* Tue Jun 06 2006 Dag Wieers <dag@wieers.com> - 0.9.61-1
- Project was renamed from gnocatan to pioneers.
- Updated to release 0.9.61.

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
