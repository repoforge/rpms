# $Id$
# Authority: dries

Summary: Simple multi-channel audio mixer
Name: SDL_mixer
Version: 1.2.7
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.libsdl.org/projects/SDL_mixer/

Source: http://www.libsdl.org/projects/SDL_mixer/release/SDL_mixer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, SDL-devel >= 1.2.10, libvorbis-devel, smpeg-devel, mikmod-devel

%description
SDL_mixer is a simple multi-channel audio mixer. It supports 8 channels of 16
bit stereo audio, plus a single channel of music, mixed by the popular MikMod
MOD, Timidity MIDI, Ogg Vorbis, and SMPEG MP3 libraries.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__install} -D build/playmus %{buildroot}%{_bindir}/playmus
%{__install} -D build/playwave %{buildroot}%{_bindir}/playwave

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_bindir}/playmus
%{_bindir}/playwave
%{_libdir}/libSDL_mixer-*.so.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/SDL/
%{_includedir}/SDL/SDL_mixer.h
%{_libdir}/libSDL_mixer.a
%{_libdir}/libSDL_mixer.so
%exclude %{_libdir}/*.la

%changelog
* Sat Mar 10 2007 Dag Wieers <dag@wieers.com> - 1.2.7-1
- Updated to release 1.2.7.

* Mon Jan 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.6-1
- Initial package, based on the spec file provided by the PLD Linux Distribution.
