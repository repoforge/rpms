# $Id$
# Authority: dag
# Upstream: Erik de Castro Lopo <erikd$mega-nerd,com>
# Upstream: <src$mega-nerd,com>

Summary: Library for performing sample rate conversion on audio
Name: libsamplerate
Version: 0.1.7
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.mega-nerd.com/SRC/

Source: http://www.mega-nerd.com/SRC/libsamplerate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: fftw-devel
BuildRequires: gcc-c++
BuildRequires: libsndfile-devel >= 1.0.2
BuildRequires: pkgconfig

%description
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.

%package devel
Summary: Header files, libraries and development docs for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using
%{name}, you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/sndfile-resample
%{_libdir}/libsamplerate.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.css doc/*.html doc/*.png
%{_includedir}/samplerate.h
%{_libdir}/libsamplerate.so
%{_libdir}/pkgconfig/samplerate.pc
%exclude %{_libdir}/libsamplerate.la

%changelog
* Mon Jul 27 2009 Dag Wieers <dag@wieers.com> - 0.1.7-1
- Updated to release 0.1.7.

* Fri Sep 17 2004 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Update to 0.1.2.

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.0.15-1
- Initial package. (using DAR)

