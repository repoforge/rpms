# $Id$
# Authority: matthias

%define desktop_vendor freshrpms
%define date           20040125

Summary: A 3D multi-player tank battle game.
Name: bzflag
Version: 1.10.4
Release: 1
License: GPL
Group: Amusements/Games
Source: http://dl.sourceforge.net/bzflag/%{name}-%{version}.%{date}.tar.bz2
URL: http://bzflag.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: XFree86, libstdc++
BuildRequires: XFree86-devel, libstdc++-devel, gcc-c++, desktop-file-utils

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
%{__make}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -D -m 644 package/rpm/bzflag-m.xpm \
    %{buildroot}%{_datadir}/pixmaps/bzflag.xpm

# Desktop menu entry
cat > %{name}.desktop << EOF
[Desktop Entry]
Name=BZFlag
Comment=%{summary}
Exec=%{name}
Icon=bzflag.xpm
Terminal=0
Type=Application
EOF

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category X-Red-Hat-Extra                \
  --add-category Application                    \
  --add-category Game                           \
  %{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README README.Linux
%{_bindir}/bzadmin
%{_bindir}/bzflag
%{_bindir}/bzfrelay
%{_bindir}/bzfs
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_datadir}/bzflag
%{_datadir}/pixmaps/bzflag.xpm
%{_mandir}/man6/*

%changelog
* Mon Feb 16 2004 Matthias Saou <http://freshrpms.net/> 1.10.4-1.fr
- Update to 1.10.4.20040125, update the included docs.
- Removed no longer existing bzfls file and added bzadmin.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.7g2-2.fr
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

