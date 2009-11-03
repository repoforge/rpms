# $Id$
# Authority: dag

Summary: Audio Processing library for changing Tempo, Pitch and Playback Rates
Name: soundtouch
Version: 1.3.1
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://sky.prohosting.com/oparviai/soundtouch/

Source: http://www.surina.net/soundtouch/soundtouch-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, libtool

%description
SoundTouch is a LGPL-licensed open-source audio processing library for
changing the Tempo, Pitch and Playback Rates of audio streams or
files. The SoundTouch library is suited for application developers
writing sound processing tools that require tempo/pitch control
functionality, or just for playing around with the sound effects.

The SoundTouch library source kit includes an example utility
SoundStretch which allows processing .wav audio files from a
command-line interface.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking \
	--enable-shared
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/soundtouch/

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING.TXT README.html
%{_bindir}/soundstretch
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_datadir}/aclocal/soundtouch.m4
%{_includedir}/soundtouch/
%{_libdir}/lib*.a
%exclude %{_libdir}/lib*.la
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Sun Mar 25 2007 Dag Wieers <dag@wieers.com> - 1.3.1-1
- Initial package. (using DAR)
