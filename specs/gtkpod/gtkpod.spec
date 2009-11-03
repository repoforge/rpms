# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Graphical song management program for Apple's iPod
Name: gtkpod
Version: 0.99.8
Release: 3%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.gtkpod.org/
Source: http://dl.sf.net/gtkpod/gtkpod-%{version}.tar.gz
Patch0: http://heanet.dl.sf.net/gtkpod/gtkpod-0.99.8_libgpod-0.4.2.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libgpod-devel, gtk2-devel, libglade2-devel
BuildRequires: libid3tag-devel, libmp4v2-devel, gettext, flex
%{!?_without_freedesktop:BuildRequires: desktop-file-utils}

%description
gtkpod is a platform independent Graphical User Interface for Apple's iPod
using GTK2. It supports the first to fifth Generation including the iPod
mini, iPod Photo, iPod Shuffle, iPod nano, and iPod Video..


%prep
%setup
%patch0 -p1 -b .libgpod-0.4.2
# Create a desktop menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=iPod Song Manager
Comment=Manage songs on your Apple iPod
Exec=gtkpod
Icon=gtkpod.png
Terminal=false
Type=Application
Categories=GNOME;Application;AudioVideo;X-Red-Hat-Base;
Encoding=UTF-8
EOF


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Install menu icon
%{__install} -D -p -m 0644 pixmaps/gtkpod-icon-48x48.png \
    %{buildroot}%{_datadir}/pixmaps/gtkpod.png

# Install menu entry
%if %{!?_without_freedesktop:1}0
%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop
%else
%{__install} -D -p -m 0644 %{name}.desktop \
    %{buildroot}%{_sysconfdir}/X11/applnk/Multimedia/%{name}.desktop
%endif


%clean
%{__rm} -rf %{buildroot}


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODOandBUGS.txt TROUBLESHOOTING
%{_bindir}/gtkpod
%{_datadir}/gtkpod/
%{_datadir}/pixmaps/gtkpod.png
%if %{!?_without_freedesktop:1}0
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%else
%{_sysconfdir}/X11/applnk/Multimedia/%{name}.desktop
%endif


%changelog
* Wed Jan 24 2007 Matthias Saou <http://freshrpms.net/> 0.99.8-3
- Rebuild against new libgpod 0.4.2.

* Fri Dec 15 2006 Matthias Saou <http://freshrpms.net/> 0.99.8-2
- Rebuild against simple libmp4v2 instead of full faac2, it seems like this
  package could go into Extras now!

* Mon Sep 25 2006 Matthias Saou <http://freshrpms.net/> 0.99.8-1
- Update to 0.99.8.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-2
- Release bump to drop the disttag number in FC5 build.

* Tue Mar 14 2006 Matthias Saou <http://freshrpms.net/> 0.99.4-1
- Update to 0.99.4.

* Mon Dec 19 2005 Matthias Saou <http://freshrpms.net/> 0.99.2-1
- Update to 0.99.2.
- Now depend on split-off libgpod.
- Remove no longer needed gcc4 patch.
- Remove no longer needed workaround for the absolute symlinks.

* Mon Jul 18 2005 Matthias Saou <http://freshrpms.net/> 0.94.0-1
- Update to 0.94.0.

* Mon Jun 27 2005 Matthias Saou <http://freshrpms.net/> 0.93.1-1
- Update to 0.93.1.
- Add libglade2-devel build dependency.
- Remove gtk2.4-gtk2.0.diff patch.
- Add workaround for absolute symlinks of glade files.

* Wed Apr 20 2005 Matthias Saou <http://freshrpms.net/> 0.88.2-2
- Add patch to fix building with gcc4.

* Fri Apr  1 2005 Matthias Saou <http://freshrpms.net/> 0.88.2-1
- Update to 0.88.2.

* Fri Mar 11 2005 Dag Wieers <dag@wieers.com> - 0.88-1
- Updated to release 0.88.0.

* Mon Nov 22 2004 Matthias Saou <http://freshrpms.net/> 0.85.0-1
- Update to 0.85.0.

* Fri Aug 27 2004 Matthias Saou <http://freshrpms.net/> 0.80-0
- Update to 0.80-2.
- Added AAC support through faad2.
- Spec file cleanup, use included pixmap, use find_lang macro, fix files.

* Sat Mar 21 2004 Casper Pedersen <cpedersen [at] c-note.dk> 0.72-2.3
- BuildRequires:  gtk2-devel >= 2.2.4
- BuildRequires:  glib2-devel >= 2.2.3

* Tue Mar 16 2004 Casper Pedersen <cpedersen [at] c-note.dk> 0.72-2.1
- Follow Fedora specs
- add .desktop file
- add icon

* Mon Mar 24 2003 Mike Gerber <mike@sprachgewalt.de> 0.50-1
- Initial spec file

