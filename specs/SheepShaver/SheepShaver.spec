# $Id$
# Authority: matthias

%define date 20050315
%define mon_version 3.1
%define desktop_vendor rpmforge

Summary: Power Macintosh emulator
Name: SheepShaver
Version: 2.2
Release: 0.%{date}
License: GPL
Group: Applications/Emulators
URL: http://gwenole.beauchesne.free.fr/sheepshaver/
Source0: http://gwenole.beauchesne.free.fr/sheepshaver/files/SheepShaver-%{version}-%{date}.tar.bz2
Source1: http://wwwthep.physik.uni-mainz.de/~cbauer/cxmon-%{mon_version}.tar.gz
Source2: SheepShaver.png
Patch0: SheepShaver-2.2-misc.patch
Patch1: SheepShaver-2.2-stats.patch
Patch2: SheepShaver-2.2-nostrip.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, gtk+-devel >= 1.2, esound-devel >= 0.2.8
BuildRequires: desktop-file-utils, readline-devel
#BuildRequires: SDL-devel
# Other archs need an instruction skipper on well-known invalid
# memory references (e.g. illegal writes to ROM).
ExclusiveArch: %{ix86} ppc x86_64

%description
SheepShaver is a MacOS run-time environment that allows you to run classic
MacOS applications. This means that both Linux and MacOS applications can
run at the same time (usually in a window on the Linux desktop).

If you are using a PowerPC-based system, applications will run at native
speed (i.e. with no emulation involved). There is also a built-in PowerPC
G4 emulator, without MMU support, for non-PowerPC systems.


%prep
%setup -a 1
%patch0 -p1 -b .misc
%patch1 -p1 -b .stats
%patch2 -p1 -b .nostrip


%build
pushd src/Unix
%configure \
    --datadir=%{_sysconfdir} \
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
Name=Sheep Shaver
Comment=Power Macintosh Emulator
Exec=SheepShaver
Icon=SheepShaver.png
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
    %{buildroot}%{_datadir}/pixmaps/SheepShaver.png


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc COPYING NEWS doc/Linux/*
%dir %{_sysconfdir}/SheepShaver/
%{_sysconfdir}/SheepShaver/keycodes
%{_sysconfdir}/SheepShaver/tunconfig
%{_bindir}/SheepShaver
%{_datadir}/pixmaps/SheepShaver.png
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%{_mandir}/man1/SheepShaver.1*


%changelog
* Sat Apr 21 2005 Matthias Saou <http://freshrpms.net/> 2.2-0.20050315
- Spec file cleanup, based on the .src.rpm from the SheepShaver website.
- Make cxmon support optionnal with --without mon.
- Add menu entry.
- Disable binary stripping on make install to get a useful debuginfo package.

