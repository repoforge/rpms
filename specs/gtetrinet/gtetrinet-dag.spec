# Authority: freshrpms
# Upstream: Ka-shu Wong <kswong@zip.com.au>

Summary: A GNOME version of the online multiplayer Tetrinet game.
Name: gtetrinet
Version: 0.7.2
Release: 0
License: GPL
Group: Amusements/Games
URL: http://gtetrinet.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://ftp.gnome.org/pub/GNOME/sources/gtetrinet/0.7/%{name}-%{version}.tar.bz2
Source1: tetrinet.txt
Source2: http://www.mavit.pwp.blueyonder.co.uk/mmr-sounds-1.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: libgnome-devel >= 2.0.0, libgnomeui-devel >= 2.0.0

%description
GTetrinet is a client program for the popular Tetrinet game, a multiplayer
tetris game that is played over the internet. (If you don't know what Tetrinet
is, check out tetrinet.org)

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--disable-install-schemas
%{__perl} -pi.orig -e 's|^Exec=%{name}|Exec=%{_prefix}/games/%{name}|' %{name}.desktop
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL="1"
%makeinstall
%find_lang %{name}
%{__install} -m0644 %{SOURCE1} .
tar -xzvf %{SOURCE2} -C %{buildroot}%{_datadir}/gtetrinet/themes/

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README tetrinet.txt TODO
%doc %{_mandir}/man?/*
%config %{_sysconfdir}/gconf/schemas/*.schemas
%{_prefix}/games/*
%{_datadir}/applications/*.desktop
%{_datadir}/gtetrinet/
%{_datadir}/pixmaps/*

%changelog
* Wed Jun 11 2003 Dag Wieers <dag@wieers.com> - 0.7.2-0
- Updated to release 0.7.2.

* Mon Apr 14 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated to release 0.7.1.

* Mon Mar 17 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Mon Feb 24 2003 Dag Wieers <dag@wieers.com> - 0.6.2-0
- Updated to release 0.6.2.

* Wed Feb 05 2003 Dag Wieers <dag@wieers.com> - 0.5.0-0
- Initial package. (using DAR)
