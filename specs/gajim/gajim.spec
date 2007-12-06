# $Id$
# Authority: dag

Summary: Jabber client written in PyGTK
Name: gajim
Version: 0.11.4
Release: 1
License: GPL
Group: Applications/Internet
URL: http://gajim.org/

Source: http://gajim.org/downloads/gajim-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext, intltool, pkgconfig, desktop-file-utils
BuildRequires: dbus-devel, gtk2-devel, gtkspell-devel
BuildRequires: python-devel, pygtk2-devel
Requires: dbus-python, bind-utils, python, pygtk2-libglade, gnome-python2-gconf, python-sqlite2

%description
Gajim is a Jabber client written in PyGTK. The goal of Gajim's developers is
to provide a full featured and easy to use xmpp client for the GTK+ users.
Gajim does not require GNOME to run, even though it exists with it nicely.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static \
    --enable-gtkspell \
    --enable-idle \
    --enable-remote \
    --enable-trayicon
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_docdir}/gajim/
%doc %{_mandir}/man1/gajim.1*
%doc %{_mandir}/man1/gajim-remote.1*
%{_bindir}/gajim
%{_bindir}/gajim-remote
%{_datadir}/applications/gajim.desktop
%{_datadir}/gajim/
%{_datadir}/pixmaps/gajim*
%{_libdir}/gajim/
%exclude %{_libdir}/gajim/*.la

%changelog
* Thu Dec 06 2007 Heiko Adams <info-2007@fedora-blog.de> - 0.11.4-1
- Updated to release 0.11.4.

* Sun Nov 18 2007 Heiko Adams <info@fedora-blog.de> - 0.11.3-1
- Updated to release 0.11.3.

* Mon Oct 08 2007 Heiko Adams <info@fedora-blog.de> - 0.11.2-1
- Updated to release 0.11.2.

* Sat Jul 07 2007 Heiko Adams <info@fedora-blog.de> - 0.11.1-2
- Added depency on python-sqlite2.

* Thu Jun 07 2007 Dag Wieers <dag@wieers.com> - 0.11.1-1
- Initial package. (using DAR)
