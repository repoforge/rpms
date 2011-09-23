# $Id$
# Authority: shuff
# Upstream: Tim Riker <Tim$Rikers,org

%{?el5:%define _with_bundled_cares 1}
%{?el4:%define _with_bundled_cares 1}
%{?el3:%define _with_bundled_cares 1}
%{?el2:%define _with_bundled_cares 1}

%define desktop_vendor RepoForge

%define bzlibdir %{_libdir}/bzflag-%{version}

Summary: 3D multi-player tank battle game
Name: bzflag
Version: 2.4.0
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://bzflag.org/
Source: https://downloads.sourceforge.net/project/bzflag/bzflag%20source/%{version}/bzflag-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
%{!?_with_bundled_cares:BuildRequires: c-ares-devel}
BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++
BuildRequires: libidn-devel
BuildRequires: libtool
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: rpm-macros-rpmforge
BuildRequires: SDL-devel >= 1.2.10
BuildRequires: zlib-devel

%{?_with_bundled_cares:Conflicts: c-ares-devel}

# our libs are not for others
%filter_provides_in %{bzlibdir}
%filter_setup

%description
BZFlag is a 3D multi-player tank battle game  that  allows users to play
against each other in a networked environment.  There are five teams: red,
green, blue, purple and rogue (rogue tanks are black).  Destroying a player
on another team  scores a win, while being destroyed or destroying a teammate
scores a loss.  Rogues have no teammates (not even other rogues), so they
cannot shoot teammates and they do not have a team score.
There are two main styles of play: capture-the-flag and free-for-all.

%prep
%setup


%build
%configure \
    --libdir="%{bzlibdir}" \
    --disable-dependency-tracking \
    --enable-robots
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m 644 data/bzflag-48x48.png \
    %{buildroot}%{_datadir}/pixmaps/bzflag.png

# Desktop menu entry
%{__cat} > %{name}.desktop << DESKTOP
[Desktop Entry]
Categories=Game;ArcadeGame;
Name=BZFlag
Comment=3D multi-player tank battle game
Exec=bzflag
Icon=bzflag
Terminal=false
Type=Application
Encoding=UTF-8
DESKTOP

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

# ld.so.conf.d file
%{__cat} > %{name}-ldso.conf << LDSO
%{bzlibdir}
LDSO

%{__install} -Dp -m 644 bzflag-ldso.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/bzflag.conf

%{__rm} -f %{buildroot}%{bzlibdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

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
%{_sysconfdir}/ld.so.conf.d/*
%{bzlibdir}


%changelog
* Thu Sep 22 2011 Steve Huff <shuff@vecna.org> - 2.4.0-1
- Update to 2.4.0.
- Move messy shared libraries into their own libdir.
- Enforce use of bundled c-ares on <el6.

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

