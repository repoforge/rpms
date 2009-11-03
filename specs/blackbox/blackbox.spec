# $Id$
# Authority: matthias


%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}

Summary: Very small and fast Window Manager
Name: blackbox
Version: 0.70.1
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://blackboxwm.sourceforge.net/
Source0: http://dl.sf.net/blackboxwm/blackbox-%{version}.tar.bz2
Source1: blackbox.desktop
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel, libXext-devel, libXt-devel}

%description
Blackbox is a window manager for the X Window environment, which is
almost completely compliant with ICCCM specified operation policies.
It features nice and fast interface with multiple workspaces and
simple menus. Fast built-in graphics code that can render solids,
gradients and bevels is used to draw window decorations. Remaining
small in size, blackbox preserves memory and CPU.


%package devel
Summary: Blackbox Toolbox library for writing small applications
Group: Development/Libraries
Requires: gcc-c++, pkgconfig

%description devel
This package contains the Blackbox Toolbox files, headers and static library
of the utility class library for writing small applications.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Install GDM session filee
%{__mkdir_p} %{buildroot}/etc/X11/gdm/Sessions
%{__cat} > %{buildroot}/etc/X11/gdm/Sessions/Blackbox << EOF
#!/bin/sh
exec /etc/X11/xdm/Xsession %{name}
EOF

# Install the desktop entry
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog* COMPLIANCE LICENSE README* RELNOTES TODO
%attr(755, root, root) /etc/X11/gdm/Sessions/Blackbox
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/bt/
%{_libdir}/libbt.a
%exclude %{_libdir}/libbt.la
%{_libdir}/pkgconfig/libbt.pc


%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.70.1-1
- Updated to release 0.70.1.

* Sat Mar 12 2005 Mattthias Saou <http://freshrpms.net/> 0.70.0-1
- Update to 0.70.0.
- Use bz2 source instead of gz.
- Add devel sub-package for the libbt stuff.

* Mon Nov 15 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-9
- Added gcc 3.4 patch from Arch Linux.

* Thu May  6 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-8
- Removed switchdesk file, it doesn't work because of hardcoded stuff.

* Wed Mar 24 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-8
- Removed explicit XFree86 dependency.

* Mon Feb 23 2004 Mattthias Saou <http://freshrpms.net/> 0.65.0-7
- Added blackbox.desktop file for xsessions based on the GNOME one.

* Tue Feb 10 2004 Scott R. Godin <nospam@webdragon.net> 0.65.0-6
- Patch for #include <cassert> in Window.cc
- Fixed nls problem, left in --disable just in case. Smile, Matthias. :-)

* Fri Nov 14 2003 Mattthias Saou <http://freshrpms.net/> 0.65.0-5
- Rebuild for Fedora Core 1.

* Wed May 14 2003 Matthias Saou <http://freshrpms.net/>
- Added --without nls to enable rebuilding on Red Hat Linux 9 :-(

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Fri Sep 20 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.65.0 final.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

