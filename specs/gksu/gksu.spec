# $Id$
# Authority: dries
# Upstream: Gustavo Noronha <kov$debian,org>

# Screenshot: http://www.nongnu.org/gksu/gksu2.png

Summary: Graphical frontend to su
Name: gksu
Version: 2.0.0
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/gksu/

Source: http://people.debian.org/~kov/gksu/gksu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, intltool, perl(XML::Parser)
BuildRequires: gtk2-devel >= 2.4.0, GConf2-devel
BuildRequires: bison, gtk-doc, gnome-keyring-devel, nautilus-devel
BuildRequires: libgksu-devel, libgksuui-devel

%description
Gtk+ frontend to /bin/su. It supports login shells and preserving environment
when acting as a su frontend. It is useful to menu items or other graphical
programs that need to ask a user's password to run another program as another
user.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/gksu.1*
%doc %{_mandir}/man1/gksudo.1*
%{_bindir}/gksu
%{_bindir}/gksudo
%{_datadir}/applications/gksu.desktop
%{_datadir}/gksu/
%{_datadir}/pixmaps/gksu-icon.png
%{_datadir}/pixmaps/gksu-root-terminal.png
%dir %{_libdir}/nautilus/
%dir %{_libdir}/nautilus/extensions-1.0/
%{_libdir}/nautilus/extensions-1.0/libnautilus-gksu.so
%exclude %{_libdir}/nautilus/extensions-1.0/libnautilus-gksu.a
%exclude %{_libdir}/nautilus/extensions-1.0/libnautilus-gksu.la

%changelog
* Fri Oct 12 2007 Dag Wieers <dag@wieers.com> - 2.0.0-1
- Updated to release 2.0.0.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 1.3.4-2
- Fixed group.

* Sat Sep 17 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.4-1
- Initial package.
