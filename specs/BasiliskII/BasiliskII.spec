# $Id$
# Authority: dag

%define date 20060501
%define inv_date 01052006
%define cxmon_version 3.2
%define desktop_vendor rpmforge

%{?dtag: %{expand: %%define %dtag 1}}
%{?fedora: %{expand: %%define fc%{fedora} 1}}

%{!?dtag:%define _with_banks 1}
%{?el5:  %define _with_banks 1}
%{?fc7:  %define _with_banks 1}
%{?fc6:  %define _with_banks 1}
%{?fc5:  %define _with_banks 1}
%{?fc4:  %define _with_banks 1}
%{?el4:  %define _with_banks 1}
%{?fc3:  %define _with_banks 1}

%{?el4:%define _without_modxorg 1}
%{?el3:%define _without_modxorg 1}

Summary: 68k Macintosh emulator
Name: BasiliskII
Version: 1.0
Release: 0.%{date}.2
License: GPL
Group: Applications/Emulators
URL: http://gwenole.beauchesne.info/projects/basilisk2/

Source0: http://gwenole.beauchesne.info/projects/basilisk2/files/BasiliskII_src_%{inv_date}.tar.bz2
Source1: http://cxmon.cebix.net/downloads/cxmon-%{cxmon_version}.tar.gz
Source2: BasiliskII.png
Patch: BasiliskII-1.0-nostrip.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gtk2-devel, esound-devel >= 0.2.8
BuildRequires: desktop-file-utils, readline-devel
%{!?_without_modxorg:BuildRequires: libXt-devel, libXxf86dga-devel, libXxf86vm-devel}
%{?_with_sdl:BuildRequires: SDL-devel}

%description
Basilisk II is an Open Source 68k Macintosh emulator. That is, it enables
you to run 68k MacOS software on you computer, even if you are using a
different operating system. However, you still need a copy of MacOS and
a Macintosh ROM image to use Basilisk II.

Available rebuild options :
--with    : sdl banks modxorg
--without : mon

%prep
%setup -a 1
%patch -p1 -b .nostrip

%build
pushd src/Unix
%configure \
    --datadir=%{_sysconfdir} \
    %{?_with_banks:--enable-addressing="banks"} \
    %{!?_with_banks:--enable-jit-compiler} \
    %{!?_without_mon: --with-mon="../../cxmon-%{cxmon_version}/src"} \
    %{?_with_sdl: --enable-sdl-video --enable-sdl-audio}
%{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
%makeinstall -C src/Unix \
    datadir="%{buildroot}%{_sysconfdir}"

# Create the system menu entry
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Basilisk II
Comment=68k Macintosh Emulator
Exec=BasiliskII
Icon=BasiliskII.png
Terminal=false
Type=Application
Categories=Application;Utility;
Encoding=UTF-8
EOF

%{__mkdir_p} %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    %{name}.desktop

%{__install} -D -p -m 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/pixmaps/BasiliskII.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README TECH TODO
%dir %{_sysconfdir}/BasiliskII/
%config %{_sysconfdir}/BasiliskII/fbdevices
%config %{_sysconfdir}/BasiliskII/keycodes
%config %{_sysconfdir}/BasiliskII/tunconfig
%{_bindir}/BasiliskII
%{_datadir}/pixmaps/BasiliskII.png
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_mandir}/man1/BasiliskII.1*

%changelog
* Mon Jun 11 2007 Dag Wieers <dag@wieers.com> - 1.0-0.20060501.2
- Updated release of cxmon.

* Wed Mar  7 2007 Matthias Saou <http://freshrpms.net/> 1.0-0.20060501.1
- Update to 01052006.
- Update URL and source locations.

* Wed Mar 22 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.20051122.5
- Add missing modular X build requirements.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.20051122.4
- Release bump to drop the disttag number in FC5 build.

* Thu Jan 12 2006 Matthias Saou <http://freshrpms.net/> 1.0-0.20051122.3
- Add modular xorg build switch, and make it the default.

* Thu Dec  1 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.20051122
- Update to 20051122 snapshot.
- Add --with sdl rebuild option.
- Switch from gtk1 to new gtk2 GUI.

* Fri Apr  1 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.20050322
- Update to latest snapshot.
- Add a menu entry.
- Addressing of "banks" type is still required.
- SDL still doesn't display properly.
- Add cxmon support, can be disabled with --without mon.
- Add readline-devel build dependency.
- Disable binary stripping on make install to get a useful debuginfo package.

* Mon Dec 13 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.20041109
- Update to latest BasilikII JIT snapshot.
- Override datadir to sysconfdir as it makes more sense to have configuration
  files there.
- Force addressing to older "banks" on FC3 as other don't work :-(

* Sat Feb 15 2003 Dag Wieers <dag@wieers.com> - 0.9.20020115-0
- Initial package. (using DAR)

