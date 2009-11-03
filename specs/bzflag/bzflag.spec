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
%{?rh6:%define _without_modxorg 1}
%{?yd3:%define _without_modxorg 1}

%define desktop_vendor rpmforge
%define date           20050318

Summary: 3D multi-player tank battle game
Name: bzflag
Version: 2.0.2
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://bzflag.org/
Source: http://dl.sf.net/bzflag/bzflag-%{version}.%{date}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, desktop-file-utils
BuildRequires: ncurses-devel, curl-devel, SDL-devel
# This one should have been required by curl-devel
%{!?dtag:BuildRequires: libidn-devel}
%{?fc3:BuildRequires: libidn-devel}
%{?_without_modxorg:BuildRequires: XFree86-devel}
%{!?_without_modxorg:BuildRequires: libX11-devel}

%description
BZFlag is a 3D multi-player tank battle game  that  allows users to play
against each other in a networked environment.  There are five teams: red,
green, blue, purple and rogue (rogue tanks are black).  Destroying a player
on another team  scores a win, while being destroyed or destroying a teammate
scores a loss.  Rogues have no teammates (not even other rogues), so they
cannot shoot teammates and they do not have a team score.
There are two main styles of play: capture-the-flag and free-for-all.


%prep
%setup -n %{name}-%{version}.%{date}


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m 644 data/bzflag-48x48.png \
    %{buildroot}%{_datadir}/pixmaps/bzflag.png

# Desktop menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Categories=Game;ArcadeGame
Name=BZFlag
Comment=3D multi-player tank battle game
Exec=bzflag
Icon=bzflag.png
Terminal=false
Type=Application
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README README.Linux
%{_bindir}/bzadmin
%{_bindir}/bzflag
%{_bindir}/bzfs
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/bzflag/
%{_datadir}/pixmaps/bzflag.png
%{_mandir}/man?/*


%changelog
* Tue Apr  5 2005 Matthias Saou <http://freshrpms.net/> 2.0.2-1
- Update to 2.0.2.

* Fri Jan 21 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-1
- Update to 2.0.0.
- Added ncurses, curl, SDL and libidn devel build requirements.
- Replace xpm "BZFlag" image by a nicer png tank image.

* Tue Aug 10 2004 Alan Cox <alan@redhat.com> 1.10.6-2
- Adopted for FC3 core from Matthias Saou's freshrpms package. Thanks
  to Matthias for doing all the work.

* Tue May 18 2004 Matthias Saou <http://freshrpms.net/> 1.10.6-1
- Update to 1.10.6.
- First rebuild for Fedora Core 2.

* Thu Mar 25 2004 Matthias Saou <http://freshrpms.net/> 1.10.4-2
- Removed explicit XFree86 dependency.

* Mon Feb 16 2004 Matthias Saou <http://freshrpms.net/> 1.10.4-1
- Update to 1.10.4.20040125, update the included docs.
- Removed no longer existing bzfls file and added bzadmin.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.7g2-2
- Rebuild for Fedora Core 1.
- Added missing gcc-c++ build dependency.

* Sun Jun 22 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7g2.
- Major spec changes for the new build method.

* Tue Apr  1 2003 Matthias Saou <http://freshrpms.net/>
- Fix the Xfree86 dependency, doh!
- Clean up the confusing build.
- Add a system menu entry.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7g0.
- Rebuilt for Red Hat Linux 9.

* Mon Nov  4 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Wed Jun 19 2002 Matthias Saou <http://freshrpms.net/>
- Update to 1.7e6.

* Wed Feb 13 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

