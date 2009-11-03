# $Id$
# Authority: dag
# Upstream: <portaudio$techweb,rfa,org>


%{?el3:%define _without_alsa 1}

%define real_name pa_stable

Summary: Free, cross platform, open-source, audio I/O library
Name: portaudio
%define real_version v19_20071207
Version: 19
Release: 1.20071207%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.portaudio.com/

Source: http://www.portaudio.com/archives/pa_stable_%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_alsa:BuildRequires: alsa-lib-devel}
BuildRequires: doxygen
BuildRequires: gcc-c++
Requires: pkgconfig

Provides: %{name}-devel = %{version}-%{release}

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

%prep
%setup -n %{name}

%build
%configure \
    --disable-static \
    --enable-cxx
%{__make} %{?_smp_mflags}
doxygen

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE.txt README.txt
%{_includedir}/*
%{_libdir}/libportaudio.so*
%{_libdir}/libportaudiocpp.so*
%{_libdir}/pkgconfig/portaudio-2.0.pc
%{_libdir}/pkgconfig/portaudiocpp.pc
%exclude %{_libdir}/libportaudio.la
%exclude %{_libdir}/libportaudiocpp.la

%changelog
* Wed Jul 22 2009 Dag Wieers <dag@wieers.com> - 19-1.20071207
- Updated to release v19_20071207.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> - 18.1-2
- Add -devel provides.
- Fix .so 644 mode (overidden in defattr).

* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 18.1-1
- Added -fPIC for x86_64.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 18.1-0
- Initial package. (using DAR)
