# $Id$
# Authority: dag

%define date 20041109
%define inv_date 09112004

%{?dist: %{expand: %%define %dist 1}}
%{!?dist:%define _with_banks 1}
%{?el4:  %define _with_banks 1}
%{?fc3:  %define _with_banks 1}

Summary: 68k Macintosh emulator
Name: BasiliskII
Version: 1.0
Release: 0.%{date}
License: GPL
Group: Applications/Emulators
URL: http://gwenole.beauchesne.online.fr/basilisk2/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gwenole.beauchesne.online.fr/basilisk2/files/BasiliskII_src_%{inv_date}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel >= 1.2, esound-devel >= 0.2.8, gcc-c++
BuildRequires: SDL-devel

%description
Basilisk II is an Open Source 68k Macintosh emulator. That is, it enables
you to run 68k MacOS software on you computer, even if you are using a
different operating system. However, you still need a copy of MacOS and
a Macintosh ROM image to use Basilisk II.

%prep
%setup

%build
pushd src/Unix
%configure \
    --datadir=%{_sysconfdir} \
    %{?_with_banks:--enable-addressing="banks"} \
    %{!?_with_banks:--enable-jit-compiler}
#   --enable-sdl-video \
#   --enable-sdl-audio \
%{__make} %{?_smp_mflags}
popd

%install
%{__rm} -rf %{buildroot}
%makeinstall -C src/Unix \
    datadir="%{buildroot}%{_sysconfdir}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README TECH TODO
%dir %{_sysconfdir}/BasiliskII/
%config %{_sysconfdir}/BasiliskII/fbdevices
%config %{_sysconfdir}/BasiliskII/keycodes
%config %{_sysconfdir}/BasiliskII/tunconfig
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Dec 13 2004 Matthias Saou <http://freshrpms.net/> 1.0-0.20041109
- Update to latest BasilikII JIT snapshot.
- Override datadir to sysconfdir as it makes more sense to have configuration
  files there.
- Force addressing to older "banks" on FC3 as other don't work :-(

* Sat Feb 15 2003 Dag Wieers <dag@wieers.com> - 0.9.20020115-0
- Initial package. (using DAR)

