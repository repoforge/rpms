# $Id$
# Authority: dag

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%define desktop_vendor rpmforge
%define real_name deluge-torrent

Summary: Graphical BitTorrent client with support for DHT, UPnP, and PEX
Name: deluge
Version: 0.5.9.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://deluge-torrent.org/

Source: http://download.deluge-torrent.org/source/deluge-%{version}.tar.gz
Patch1: deluge-0.5.7.1-default-prefs-no-release-notifications.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: boost-devel
BuildRequires: desktop-file-utils
BuildRequires: libtool
BuildRequires: openssl-devel
BuildRequires: python-devel
Requires: dbus-python
Requires: pygtk2-libglade
Requires: pyOpenSSL
Requires: python-xdg

Obsoletes: python-libtorrent <= 0.5
Provides: python-libtorrent = %{version}-%{release}

%description
Deluge is a new BitTorrent client, created using Python and GTK+. It is
intended to bring a native, full-featured client to Linux GTK+ desktop
environments such as GNOME and XFCE. It supports features such as DHT
(Distributed Hash Tables), PEX (µTorrent-compatible Peer Exchange), and UPnP
(Universal Plug-n-Play) that allow one to more easily share BitTorrent data
even from behind a router with virtually zero configuration of port-forwarding.

%prep
%setup -n %{real_name}-%{version}
#patch1 -b .default-prefs-no-release-notifications

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root="%{buildroot}"
%find_lang %{name}

desktop-file-install --delete-original         \
    --vendor %{desktop_vendor}                 \
    --add-mime-type=application/x-bittorrent   \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/deluge.desktop

%clean
%{__rm} -rf %{buildroot}

%post
update-desktop-database %{_datadir}/applications &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor ||:

%postun
update-desktop-database %{_datadir}/applications &>/dev/null || :
touch --no-create %{_datadir}/icons/hicolor
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor ||:

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog HACKING LICENSE README* TODO libtorrent/AUTHORS
%{_bindir}/deluge
%{_datadir}/applications/%{desktop_vendor}-deluge.desktop
%{_datadir}/deluge/
%{_datadir}/icons/hicolor/*/apps/deluge.png
%{_datadir}/pixmaps/deluge.png
%{python_sitearch}/deluge/

%changelog
* Tue Jul 14 2009 Dag Wieers <dag@wieers.com> - 0.5.9.0-1
- Updated to release 0.5.9.0.

* Sat Mar 15 2008 Dag Wieers <dag@wieers.com> - 0.5.8.6-1
- Updated to release 0.5.8.6.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 0.5.7.98-1
Initial package. (using DAR)
