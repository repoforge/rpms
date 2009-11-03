# $Id$
# Authority: dag
# Upstream: Cristiano De Michele <demichel$na,infn,it>

Summary: Extended version of the GNOME terminal
Name: multi-gnome-terminal
Version: 1.6.2
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://multignometerm.sourceforge.net/

Source: http://dl.sf.net/multignometerm/multi-gnome-terminal-%{version}.tar.bz2
Patch0: multi-gnome-terminal-1.6.2-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, gnome-libs-devel, gdk-pixbuf-devel
BuildRequires: desktop-file-utils, flex, libxml-devel, gettext, libglade-devel
BuildRequires: bzip2-libs, scrollkeeper

%description
Multi Gnome Terminal offers a lot of useful and powerful extensions to the
gnome-terminal. The extensions are : multiple terminal support (as konsole),
various ways of switching to other terminals, changing the title of a
terminal, and many other keyboard controlled features...

%prep
%setup
%patch0

%{__cat} <<EOF >multi-gnome-terminal.desktop
[Desktop Entry]
Name=Multi GNOME Terminal
Comment=Multi screen command line
Exec=multi-gnome-terminal --use-factory --start-factory-server
Icon=multi-gnome-terminal.png
Terminal=false
Type=Application
DocPath=%{name}/index.html
Categories=GNOME;Application;System;Utility;
EOF

%build
%configure
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -DREDHAT_TERM"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 pixmaps/multignometerm.png %{buildroot}%{_datadir}/pixmaps/multi-gnome-terminal.png

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome           \
  --add-category X-Red-Hat-Extra              \
  --dir %{buildroot}%{_datadir}/applications/ \
  multi-gnome-terminal.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/multi-gnome-terminal/
%{_sysconfdir}/CORBA/servers/*.gnorba
%{_bindir}/*
%{_sbindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/idl/*.idl
%{_datadir}/mgt/
%{_datadir}/omf/mgt/
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/mgt/
%exclude %{_datadir}/gnome/apps/System/*.desktop
%exclude %{_infodir}
%exclude %{_localstatedir}/scrollkeeper/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.6.2-1.2
- Rebuild for Fedora Core 5.

* Tue Apr 22 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.6.2.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.

* Wed Jan 15 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 8.0 (new menu entry and minor cleanups).

* Mon Sep  9 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.6.1.

* Fri Jul 26 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.5.2.

* Wed Jul 17 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Fixed missing mgt-helper file, thanks to Alex Lancaster.

* Wed Jul  3 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.5.1.

* Mon Jun 17 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.5.0.

* Wed May  8 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added -DREDHAT_TERM.

* Thu May  2 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt against Red Hat Linux 7.3.
- Added the %{?_smp_mflags} expansion.

* Tue Apr 30 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 1.4.1.

* Mon Oct 22 2001 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial RPM release.

