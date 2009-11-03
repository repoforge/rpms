# $Id$
# Authority: dries
# Upstream: Laszio Pere <pipas$linux,pte,hu>

Summary: Composite User Interface terminal
Name: cuiterm
Version: 0.9.9
Release: 1%{?dist}
License: GPL
Group: User Interface/X
URL: http://linux.pte.hu/~pipas/CUI/

Source: ftp://linux.pte.hu/pub/CUI/cuiterm-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pkgconfig, pango-devel, libgnomeui-devel, scrollkeeper, gettext
BuildRequires: libxml2-devel
BuildRequires: desktop-file-utils

%description
Cuiterm is a CUI (Composite User Interface) terminal, a compound type of 
user interface that incorporates the features of the GUI (Graphical User 
Interface) and the CLI (Command Line Interface) by realizing both 
interfaces in one area at the same time.

%prep
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Cuiterm
Comment=Composite User Interface
Exec=cuiterm
Terminal=false
Type=Application
StartupNotify=true
Categories=Application;System;
Encoding=UTF-8
EOF

%build
%configure --disable-gtk-doc
%{__perl} -pi -e 's| /usr/share/pixmaps| %{buildroot}%{_datadir}/pixmaps|g;' Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor rpmforge             \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_datadir}/gnome/help/cuiterm/
%doc %{_datadir}/gtk-doc/html/cuiterm/
%{_datadir}/pixmaps/cuiterm/
%{_bindir}/cuiterm
%{_datadir}/applications/*cuiterm.desktop
%{_datadir}/omf/cuiterm/

%changelog
* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.9-1
- Updated to release 0.9.9.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.8-1
- Updated to release 0.9.8.

* Mon May 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1
- Updated to release 0.9.7.

* Sat Apr 29 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Initial package.
