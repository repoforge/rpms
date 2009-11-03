# $Id$
# Authority: dag

Summary: Handles user special directories
Name: xdg-user-dirs
Version: 0.10
Release: 1%{?dist}
License: GPL and MIT
Group: User Interface/Desktops
URL: http://freedesktop.org/wiki/Software/xdg-user-dirs

Source: http://user-dirs.freedesktop.org/releases/xdg-user-dirs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gettext
Requires: %{_sysconfdir}/X11/xinit/xinitrc.d

%description
Contains xdg-user-dirs-update that updates folders in a users
homedirectory based on the defaults configured by the administrator.

%prep
%setup

%{__cat} <<EOF >xdg-user-dirs.sh
#!/bin/sh
# Copyright (C) 2007 Red Hat, Inc. All rights reserved. This
# copyrighted material is made available to anyone wishing to use, modify,
# copy, or redistribute it subject to the terms and conditions of the
# GNU General Public License version 2.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
if [ -x /usr/bin/xdg-user-dirs-update ]; then
    /usr/bin/xdg-user-dirs-update
fi
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%{__install} -Dp -m0755 xdg-user-dirs.sh %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.conf
%config(noreplace) %{_sysconfdir}/xdg/user-dirs.defaults
%config %{_sysconfdir}/X11/xinit/xinitrc.d/xdg-user-dirs.sh
%{_bindir}/xdg-user-dir
%{_bindir}/xdg-user-dirs-update

%changelog
* Thu Dec 11 2008 Dag Wieers <dag@wieers.com> - 0.10-1
- Initial package. (using DAR)
