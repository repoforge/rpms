# $Id$
# Authority: dag
# Upstream: Erik de Castro Lopo <erikd$mega-nerd,com>
# Upstream: <src$mega-nerd,com>

# Distcc: 0

Summary: Library for performing sample rate conversion on audio
Name: libsamplerate
Version: 0.1.2
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.mega-nerd.com/SRC/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.mega-nerd.com/SRC/libsamplerate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libsndfile-devel >= 1.0.2
BuildRequires: pkgconfig, fftw-devel, gcc-c++

%description
Secret Rabbit Code is a sample rate converter for audio. It is capable
of arbitrary and time varying conversions. It can downsample by a
factor of 12 and upsample by the same factor. The ratio of input and
output sample rates can be a real number. The conversion ratio can
also vary with time for speeding up and slowing down effects.

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
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.css doc/*.html doc/*.png
%{_includedir}/samplerate.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Fri Sep 17 2004 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Update to 0.1.2.

* Sun Apr 11 2004 Dag Wieers <dag@wieers.com> - 0.0.15-1
- Initial package. (using DAR)

