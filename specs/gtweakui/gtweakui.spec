# $Id$

%define real_name gTweakUI

Summary: Extra configuration dialogus for GNOME
Name: gtweakui
Version: 0.0.6
Release: 2
Group: User Interface/Desktop
License: GPL
URL: http://gtweakui.sourceforge.net/
Source: http://dl.sf.net/gtweakui/%{real_name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libgnomeui-devel >= 2.4.0, GConf2-devel >= 2.4.0, gettext
Obsoletes: gTweakUI <= 0.0.6

%description
gTweakUI Provides extra configuration dialogs for the GNOME 2.0 desktop.


%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >gtweakui-menus.desktop.in
[Desktop Entry]
Name=Menus
Comment=Change extra menu preferences
Exec=gtweakui-menus
Icon=gnome-desktop-config.png
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;Settings
OnlyShowIn=GNOME;
EOF

%{__cat} <<EOF >gtweakui-nautilus.desktop.in
[Desktop Entry]
Name=Nautilus
Comment=Change extra nautilus preferences
Exec=gtweakui-nautilus
Icon=gnome-desktop-config.png
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;Settings
OnlyShowIn=GNOME;
EOF

%{__cat} <<EOF >gtweakui-session.desktop.in
[Desktop Entry]
Name=Session
Comment=Change extra session preferences
Exec=gtweakui-session
Icon=gnome-desktop-config.png
Terminal=false
Type=Application
StartupNotify=true
Encoding=UTF-8
Categories=GNOME;Application;Settings
OnlyShowIn=GNOME;
EOF

%build
%configure
%{__make} %{?_smp_mflags}
  

%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO FAQ
%{_bindir}/*
%{_datadir}/gTweakUI/
%{_datadir}/applications/*.desktop


%changelog
* Fri Jun 11 2004 Dag Wieers <dag@wieers.com> - 0.6.2
- Added improved desktop files.

* Wed Jun  9 2004 Matthias Saou <http://freshrpms.net/> 0.6-1
- Adopted for freshrpms, based on provided source package.
- Changed the name from gTweakUI to gtweakui.

* Sun May 30 2004 Daniel James <daniel@netbreeze.com.au>
- Fixed the issue with the session splash preview not displaying for gnome 2.6
- Updated build system to check for new gtk file chooser dialog
- Use new gtk file chooser dialog if it is available.

* Fri May 28 2004 Daniel James <daniel@netbreeze.com.au>
- Made session.c more usable - second dialog is much nicer now.

* Thu May 27 2004 Daniel James <daniel@netbreeze.com.au>
- Added notice dialog: tells the use which settings require restart
- Added notices to menus.c
- Finished session.c - second dialog completed.
- Added notices to session.c

* Tue May 25 2004 Daniel James <daniel@netbreeze.com.au>
- Better about dialog.

* Mon Feb 24 2003 Daniel James daniel@netbreeze.com.au 0.0.1
- Initial RPM release.

