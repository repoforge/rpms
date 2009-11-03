# $Id$
# Authority: dag
# Upstream: T. Bugra Uytun <t,bugra$uytun,com>

%define desktop_vendor rpmforge

Summary: Personal password manager
Name: gpasman
Version: 1.9.3
Release: 2.2%{?dist}
License: GPL
Group: Applications/Productivity
URL: http://gpasman.sourceforge.net/

Source: http://gpasman.sf.net/files/gpasman-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl(XML::Parser), intltool, pkgconfig, glib2-devel
BuildRequires: gtk2-devel

%description
Gpasman is a password manager. People working with the internet have to
remember lots of passwords. Saving them in a textfile is not a secure
idea. Gpasman is a GTK solution to this problem since it saves the
password information encrypted, so now you have to remember only one
password instead of ten (or more).

%prep
%setup

%{__cat} <<EOF >gpasman.desktop.in
[Desktop Entry]
Name=Password Manager
Comment=Manage various types of passwords
Icon=gpasman.png
Exec=gpasman
Terminal=false
Type=Application
Categories=GNOME;Application;Utility;
StartupNotify=true
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING LICENCE* NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.9.3-2.2
- Rebuild for Fedora Core 5.

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 1.9.3-2
- Fixed duplicate desktop-file.

* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 1.9.3-1
- Updated to release 1.9.3.

* Tue Mar 25 2003 Dag Wieers <dag@wieers.com> - 1.9.2-0
- Updated to release 1.9.2.

* Sun Mar 23 2003 Dag Wieers <dag@wieers.com> - 1.9.0-0
- Initial package. (using DAR)
