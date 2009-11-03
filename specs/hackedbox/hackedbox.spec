# $Id$
# Authority: matthias

%{?dtag: %{expand: %%define %dtag 1}}

%{?fc4:%define _without_modxorg 1}
%{?el4:%define _without_modxorg 1}
%{?fc3:%define _without_modxorg 1}
%{?fc2:%define _without_modxorg 1}
%{?fc1:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}
%{?rh9:%define _without_modxorg 1}
%{?rh7:%define _without_modxorg 1}
%{?el2:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

Summary: The bastard son of Blackbox, a small and fast Window Manager
Name: hackedbox
Version: 0.8.4
Release: 2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://scrudgeware.org/projects/Hackedbox

Source: http://scrudgeware.org/downloads/hackedbox/hackedbox-%{version}.tar.gz
Source1: hackedbox.desktop
Patch: blackbox-0.65.0-gcc34.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libstdc++-devel, gcc-c++, perl
%{!?_without_modxorg:BuildRequires: libX11-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}

%description
Hackedbox is a stripped down version of Blackbox - The X11 Window Manager.
The toolbar and Slit have been removed. The goal of Hackedbox is to be a
small "feature-set" window manager, with no bloat. There are no plans to
add any functionality, only bugfixes and speed enhancements whenever possible.


%prep
%setup
%patch -p1 -b .gcc34


%build
%configure \
    --x-libraries="%{_prefix}/X11R6/%{_lib}"
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Install Session file
%{__mkdir_p} %{buildroot}/etc/X11/gdm/Sessions
%{__cat} > %{buildroot}/etc/X11/gdm/Sessions/Hackedbox << EOF
#!/bin/sh
exec /etc/X11/xdm/Xsession %{name}
EOF

# Replace the /usr/local stuff
%{__perl} -pi -e 's|/local||g' %{buildroot}%{_datadir}/%{name}/menu

# Install the desktop entry
%{__install} -Dp -m644 %{SOURCE1} \
    %{buildroot}%{_datadir}/xsessions/%{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog README TODO
%attr(755, root, root) /etc/X11/gdm/Sessions/Hackedbox
%{_bindir}/*
%config(noreplace) %{_datadir}/%{name}/bgmenu.mk
%config(noreplace) %{_datadir}/%{name}/menu
%{_datadir}/%{name}/backgrounds
%{_datadir}/%{name}/nls
%{_datadir}/%{name}/styles
%{_datadir}/xsessions/%{name}.desktop
%{_mandir}/man1/*
%lang(fr_FR) %{_mandir}/fr_FR/man1/*
%lang(ja JP) %{_mandir}/ja_JP/man1/*
%lang(nl_NL) %{_mandir}/nl_NL/man1/*
%lang(sl_SI) %{_mandir}/sl_SI/man1/*


%changelog
* Mon Nov 15 2004 Matthias Saou <http://freshrpms.net/> 0.8.4-2
- Added gcc 3.4 patch from Arch Linux (the same as Linux From Scratch).

* Fri Jul 16 2004 Matthias Saou <http://freshrpms.net/> 0.8.4-1
- Update to 0.8.4.
- Remove the NLS workaround, no longer required.

* Mon Feb 23 2004 Matthias Saou <http://freshrpms.net/> 0.8.2-3
- Apply the same nls workaround as for blackbox.
- Add the xsessions desktop file for recent gdm/kdm.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.8.2-2
- Rebuild for Fedora Core 1.
- Added the (currently mandatory) without nls conditional build.

* Sat Apr 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.2.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Jan  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.1.

* Mon Nov  4 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.8.0.

* Sun Oct  6 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Tue Sep 10 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.7.3.

* Mon Aug 12 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

