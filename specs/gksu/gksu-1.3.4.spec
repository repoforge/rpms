# $Id$
# Authority: dries
# Upstream: Gustavo Noronha <kov$debian,org>

# Screenshot: http://www.nongnu.org/gksu/gksu2.png

Summary: Graphical frontend to su
Name: gksu
Version: 1.3.4
Release: 2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.nongnu.org/gksu/

Source: http://people.debian.org/~kov/gksu/old_stuff/gksu/gksu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gettext, intltool, perl(XML::Parser)
BuildRequires: bison, gtk-doc, gnome-keyring-devel
BuildRequires: glib2-devel, gtk2-devel, GConf2-devel
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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/gksu.1*
%doc %{_mandir}/man1/gksudo.1*
%doc %{_mandir}/man1/gksuexec.1*
%config %{_sysconfdir}/gconf/schemas/gksu.schemas
%{_bindir}/gksu
%{_bindir}/gksudo
%{_bindir}/gksuexec
%{_datadir}/applications/gksu.desktop
%{_datadir}/applications/gksuexec.desktop
%{_datadir}/gksu/
%{_datadir}/pixmaps/gksu-icon.png
%{_datadir}/pixmaps/gksu-root-terminal.png

%changelog
* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 1.3.4-2
- Fixed group.

* Sat Sep 17 2005 Dries Verachtert <dries@ulyssis.org> - 1.3.4-1
- Initial package.
