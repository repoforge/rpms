# $Id$
# Authority: dag
# Upstream: Stephen Kennedy <steve9000$users,sf,net>

%define desktop_vendor rpmforge

Summary: Graphical visual diff and merge tool
Name: meld
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Text
URL: http://meld.sourceforge.net/

Source: http://ftp.gnome.org/pub/gnome/sources/meld/1.2/meld-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pygtk2-devel >= 2.12, gnome-python2 >= 1.99.14
BuildRequires: pyorbit-devel >= 1.99, desktop-file-utils

BuildArch: noarch
Requires: pygtk2 >= 2.12, gnome-python2 >= 1.99, gnome-python2-canvas
Requires: pygtk2-libglade, gnome-python2-gconf >= 1.99

%description
Meld is a GNOME2 visual diff and merge tool. It integrates especially
well with CVS. The diff viewer lets you edit files in place (diffs
update dynamically), and a middle column shows detailed changes and
allows merges.

%prep
%setup

%{__cat} <<'EOF' >meld.sh
#!/bin/sh
exec %{_datadir}/meld/meld $@
EOF

%{__cat} <<EOF >meld.desktop
[Desktop Entry]
Name=Meld Diff Viewer
Comment=Compare and merge multiple files
Exec=meld
Icon=meld.png
Type=Application
Terminal=false
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;Development;
X-GNOME-Bugzilla-Bugzilla=GNOME
X-GNOME-Bugzilla-Product=meld
X-GNOME-Bugzilla-Component=general
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 meld.sh %{buildroot}%{_bindir}/meld
%{__install} -Dp -m0644 glade2/pixmaps/icon.png %{buildroot}%{_datadir}/pixmaps/meld.png
%{__install} -Dp -m0755 meld %{buildroot}%{_datadir}/meld/meld

%{__install} -d -m0755 %{buildroot}%{_datadir}/meld/glade2/pixmaps/
%{__install} -p -m0644 *.py %{buildroot}%{_datadir}/meld/
%{__install} -d -m0755 %{buildroot}%{_datadir}/meld/vc/
%{__install} -p -m0644 vc/* %{buildroot}%{_datadir}/meld/vc/
%{__install} -p -m0644 glade2/*.glade* %{buildroot}%{_datadir}/meld/glade2/
%{__install} -p -m0644 glade2/pixmaps/* %{buildroot}%{_datadir}/meld/glade2/pixmaps/

%{__install} -d -m0755 %{buildroot}%{_datadir}/meld/po/
%{__install} -p -m0644 po/*.po %{buildroot}%{_datadir}/meld/po/

%{__install} -d -m0755 %{buildroot}%{_datadir}/meld/help/C/figures
%{__install} -p -m0644 help/C/meld* %{buildroot}%{_datadir}/meld/help/C/
%{__install} -p -m0644 help/C/figures/*.png %{buildroot}%{_datadir}/meld/help/C/figures/


%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --add-category X-Red-Hat-Base               \
    --dir %{buildroot}%{_datadir}/applications  \
    meld.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
#%doc AUTHORS changelog COPYING INSTALL TODO.txt manual/manual.html manual/stylesheet.css
%doc AUTHORS changelog COPYING INSTALL
%{_bindir}/meld
%{_datadir}/applications/%{desktop_vendor}-meld.desktop
%{_datadir}/meld/
%{_datadir}/pixmaps/meld.png

%changelog
* Mon Jun 30 2008 Dag Wieers <dag@wieers.com> - 1.2-1
- Updated to release 1.2.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> - 1.1.5-1
- Updated to release 1.1.5.

* Mon Jun 12 2006 Dag Wieers <dag@wieers.com> - 1.1.4-1
- Updated to release 1.1.4.

* Tue Feb 28 2006 Dag Wieers <dag@wieers.com> - 1.1.3-1
- Updated to release 1.1.3.

* Wed Dec 07 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.2-2
- Fixes: vc/* and help/* subdirectories added. (James Begley)

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Updated to release 1.1.2.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 1.0.0-1
- Updated to release 1.0.0.

* Wed May 18 2005 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Sun Feb 06 2005 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Fri Nov 19 2004 Dag Wieers <dag@wieers.com> - 0.9.4.1-2
- Moved desktop entry from Utilities to Development. (Rudolf Kastl)

* Sun Jul 18 2004 Dag Wieers <dag@wieers.com> - 0.9.4.1-1
- Updated to release 0.9.4.1.

* Fri Jul 16 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Wed May 26 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 0.9.2.1-1
- Updated to release 0.9.2.1.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Updated to release 0.9.2.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Updated to release 0.9.1.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.9.0-0
- Updated to release 0.9.0.

* Thu Oct 09 2003 Dag Wieers <dag@wieers.com> - 0.8.5-1
- Fixed meld.sh to accept arguments. (Sinisa Segvic)

* Sun Aug 31 2003 Dag Wieers <dag@wieers.com> - 0.8.5-0
- Updated to release 0.8.5.

* Tue Jul 29 2003 Dag Wieers <dag@wieers.com> - 0.8.4-0
- Updated to release 0.8.4.

* Fri Jul 25 2003 Dag Wieers <dag@wieers.com> - 0.8.3-0
- Updated to release 0.8.3.

* Sun Jun 22 2003 Dag Wieers <dag@wieers.com> - 0.8.2-0
- Updated to release 0.8.2.

* Fri Jun 06 2003 Dag Wieers <dag@wieers.com> - 0.8.1-1
- Added gnome-python2-gconf requirement. (Rudolf Kastl)

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 0.8.1-0
- Updated to release 0.8.1.

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 0.7.1-0
- Updated to release 0.7.1.

* Mon Apr 07 2003 Dag Wieers <dag@wieers.com> - 0.7.0-0
- Updated to release 0.7.0.

* Wed Feb 12 2003 Dag Wieers <dag@wieers.com> - 0.6.6-0
- Initial package. (using DAR)
