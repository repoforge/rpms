# $Id$
# Authority: rudolf

Summary: Open Audio Library
Name: openal
Version: 0.0.8
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.openal.org/

Source0: http://www.openal.org/openal_webstf/downloads/openal-%{version}.tar.gz
Source1: openalrc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, arts-devel, esound-devel, libogg-devel, libvorbis-devel
BuildRequires: texinfo, alsa-lib-devel

%description
OpenAL is an audio library designed in the spirit of OpenGL--machine
independent, cross platform, and data format neutral, with a clean,
simple C-based API.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --enable-arts \
           --enable-esd \
           --enable-vorbis \
           --enable-sdl \
           --disable-smpeg \
           --enable-capture \
           --enable-alsa
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/openalrc

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NOTES PLATFORM README
%config(noreplace) %{_sysconfdir}/openalrc
%{_libdir}/libopenal.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libopenal.a
%{_libdir}/libopenal.so
%{_includedir}/AL/
%{_libdir}/pkgconfig/openal.pc
%{_bindir}/openal-config
%exclude %{_libdir}/libopenal.la

%changelog
* Sat Dec 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.0.8-1
- Updated to release 0.0.8.
- Source doesn't contain an openal.info file anymore.
- --enable-alsa added.
- Spec cleanup.

* Mon Feb 09 2004 Dag Wieers <dag@wieers.com> - 0.0.0-0.20031006
- Initial package. (using DAR)
