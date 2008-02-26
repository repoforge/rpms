# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

%define desktop_vendor rpmforge

Summary: Chess board interface for ICS and engines
Name: eboard
Version: 1.1.1
Release: 1
License: GPL
Group: Amusements/Games
URL: http://eboard.sourceforge.net/

Source: http://dl.sf.net/eboard/eboard-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
eboard is a GTK+ chess board interface for ICS (Internet
Chess Servers) and chess engines (GNU Chess, Crafty, etc.).
It also displays games in PGN (Portable Game Notation)
format.

%prep
%setup

%{__cat} <<EOF >eboard.desktop
[Desktop Entry]
Name=Eboard Chess Client
Comment=Play chess against an engine, on a LAN or on the Internet
Exec=eboard
Icon=redhat-games.png
Terminal=false
Type=Application
Categories=Application;Game;
EOF

%build
./configure --prefix="%{_prefix}" --man-prefix="%{_mandir}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

#chmod 644 $RPM_BUILD_ROOT/%prefix/man/*/*

%if %{?_without_freedesktop:1}0
    %{__install} -Dp -m0644 eboard.desktop %{buildroot}%{_datadir}/gnome/apps/Games/eboard.desktop
%else
    %{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
    desktop-file-install --vendor %{desktop_vendor}    \
        --add-category X-Red-Hat-Base              \
        --dir %{buildroot}%{_datadir}/applications \
        eboard.desktop
%endif

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README TODO Documentation/*.txt
%doc %{_mandir}/man1/eboard-addtheme.1*
%doc %{_mandir}/man1/eboard-config.1*
%doc %{_mandir}/man6/eboard.6*
%{_bindir}/eboard
%{_bindir}/eboard-addtheme
%{_bindir}/eboard-config
%{_datadir}/eboard/
%{?_without_freedesktop:%{_datadir}/gnome/apps/Games/eboard.desktop}
%{!?_without_freedesktop:%{_datadir}/applications/%{desktop_vendor}-eboard.desktop}

%changelog
* Tue Feb 26 2008 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Tue Nov 27 2007 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Initial package. (using DAR)
