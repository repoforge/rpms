# $Id$
# Authority: dag
# Upstream: <lincvs-users$sunsite,dk>

Summary: Graphical frontend to CVS.
Name: lincvs
Version: 1.4.3
Release: 1.2%{?dist}
License: GPL
Group: Development/Tools
URL: http://www.lincvs.org/

Source: http://lincvs.com/download/lincvs-%{version}-0-generic-src.tgz
#http://ppprs1.phy.tu-dresden.de/~trogisch/lincvs/download/20_LinCVS/hn_lincvs-%{version}/lincvs-%{version}-1-generic-src.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: qt-devel >= 3.0.5, gcc-c++, desktop-file-utils

%description
LinCVS is a graphical interface for the cvs client commandline tool.
It allows modules to be loaded (checkout) or created (import) on
the server, as well as checking the state of directories and
individual files or updating them.

Basic operations like add, remove and commit are supported, just like
showing the actual differences between the server version and the local
sandbox, graphical display of the version tree, and manifoldy graphical
support of project maintenance.

%prep
%setup

%{__cat} <<'EOF' >lincvs.sh
#!/bin/sh
exec %{_datadir}/lincvs/AppRun $@
EOF

%{__cat} <<EOF >lincvs.desktop
[Desktop Entry]
Name=LinCVS CVS Client
Comment=Browse and use CVS graphically.
Icon=lincvs.xpm
Exec=lincvs
Terminal=false
Type=Application
Categories=Application;Development;
EOF

%build
source "%{_sysconfdir}/profile.d/qt.sh"

### FIXME: Dirty trick so RH qmake creates Makefile with exceptions enabled (Please fix upstream)
qmake lincvs.pro
%{__perl} -pi -e "s|-fno-exceptions|-fexceptions|g;" Makefile
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
source "%{_sysconfdir}/profile.d/qt.sh"
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/lincvs/
%{__cp} -apv LinCVS/* %{buildroot}%{_datadir}/lincvs/

%{__install} -Dp -m0755 lincvs.sh %{buildroot}%{_bindir}/lincvs
%{__install} -Dp -m0644 LinCVS/AppIcon.xpm %{buildroot}%{_datadir}/pixmaps/lincvs.xpm

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor net                  \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        %{name}.desktop

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/lincvs/lincvs

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING doc/ LICENSE NEWS README THANKS VERSION
%{_bindir}/*
%{_datadir}/lincvs/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.xpm

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.3-1.2
- Rebuild for Fedora Core 5.

* Mon Sep 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.3-1
- Updated to release 1.4.3.

* Tue May 18 2004 Dag Wieers <dag@wieers.com> - 1.3.2-1
- Updated to release 1.3.2.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Small cosmetic changes.
- Added desktop-file and icon.

* Thu Apr 01 2004 Andre Costa <acosta@ar.microlink.com.br>
- upgraded to LinCVS 1.3.1
- fixed yet another RH incompatibility
- removed 'todo.txt' from docs list

* Wed Feb 04 2004 Andre Costa <acosta@ar.microlink.com.br>
- use 'make install'. Now all related files (Messages, Tools, Help) are
  installed)
- fixed startscript and copied it to the right place (thks Tilo)
- tested against root install on install phase

* Mon Feb 02 2004 Andre Costa <acosta@ar.microlink.com.br>
- updated to version 1.3.0

* Mon Mar 10 2003 Andre Costa <acosta@ar.microlink.com.br>
- Initial RPM release.
