# $Id$
# Authority: dag

%define date 20050322
%define inv_date 22032005
%define mon_version 3.1
%define desktop_vendor rpmforge

%{?dist: %{expand: %%define %dist 1}}
%{!?dist:%define _with_banks 1}
%{?fc4:  %define _with_banks 1}
%{?el4:  %define _with_banks 1}
%{?fc3:  %define _with_banks 1}

Summary: 68k Macintosh emulator
Name: BasiliskII
Version: 1.0
Release: 0.%{date}
License: GPL
Group: Applications/Emulators
URL: http://gwenole.beauchesne.online.fr/basilisk2/

Source0: http://gwenole.beauchesne.online.fr/basilisk2/files/BasiliskII_src_%{inv_date}.tar.bz2
Source1: http://wwwthep.physik.uni-mainz.de/~cbauer/cxmon-%{mon_version}.tar.gz
Source2: BasiliskII.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, gtk+-devel >= 1.2, esound-devel >= 0.2.8
BuildRequires: desktop-file-utils, readline-devel
#BuildRequires: SDL-devel

%description
Basilisk II is an Open Source 68k Macintosh emulator. That is, it enables
you to run 68k MacOS software on you computer, even if you are using a
different operating system. However, you still need a copy of MacOS and
a Macintosh ROM image to use Basilisk II.


%prep
%setup -a 1


%build
pushd src/Unix
%configure \
    --datadir=%{_sysconfdir} \
    %{?_with_banks:--enable-addressing="banks"} \
    %{!?_with_banks:--enable-jit-compiler} \
    %{!?_without_mon: --with-mon=../../cxmon-%{mon_version}/src}
#   --enable-sdl-video \
#   --enable-sdl-audio
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
* Fri Apr  1 2005 Matthias Saou <http://freshrpms.net/> 1.0-0.20050322
- Update to latest snapshot.
- Add a menu entry.
- Addressing of "banks" type is still required.
- SDL still doesn't display properly.
- Add cxmon support, can be disabled with --without mon.
- Add readline-devel build dependency.

* Mon Dec 13 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.20041109
- Update to latest BasilikII JIT snapshot.
- Override datadir to sysconfdir as it makes more sense to have configuration
  files there.
- Force addressing to older "banks" on FC3 as other don't work :-(

* Sat Feb 15 2003 Dag Wieers <dag@wieers.com> - 0.9.20020115-0
- Initial package. (using DAR)

