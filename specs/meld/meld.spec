# $Id$
# Authority: dag
# Upstream: Stephen Kennedy <steve9000@users.sf.net>

Summary: Graphical visual diff and merge tool
Name: meld
Version: 0.9.3
Release: 1
License: GPL
Group: Applications/Text
URL: http://meld.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://ftp.gnome.org/pub/gnome/sources/meld/0.9/meld-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: pygtk2-devel >= 1.99.14, gnome-python2 >= 1.99.14
BuildRequires: pyorbit-devel >= 1.99

BuildArch: noarch
Requires: pygtk2 >= 1.99.14, gnome-python2 >= 1.99, gnome-python2-canvas
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
Categories=GNOME;Application;Utility;
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0755 meld.sh %{buildroot}%{_bindir}/meld
%{__install} -D -m0644 glade2/pixmaps/icon.png %{buildroot}%{_datadir}/pixmaps/meld.png
%{__install} -D -m0755 meld %{buildroot}%{_datadir}/meld/meld

%{__install} -d -m0755 %{buildroot}%{_datadir}/meld/glade2/pixmaps/
%{__install} -m0644 *.py %{buildroot}%{_datadir}/meld/
%{__install} -m0644 glade2/*.glade* %{buildroot}%{_datadir}/meld/glade2/
%{__install} -m0644 glade2/pixmaps/* %{buildroot}%{_datadir}/meld/glade2/pixmaps/

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	meld.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING TODO.txt manual/manual.html manual/stylesheet.css
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/meld/
%{_datadir}/pixmaps/*.png

%changelog
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
