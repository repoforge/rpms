# $Id$

Summary: Fast Fourier Transform library.
Name: fftw
Version: 2.1.5
Release: 3.fr
License: GPL
Group: System Environment/Libraries
Source: http://www.fftw.org/fftw-%{version}.tar.gz
URL: http://www.fftw.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: /sbin/ldconfig

%description
FFTW is a C subroutine library for computing the Discrete Fourier Transform
(DFT) in one or more dimensions, of both real and complex data, and of
arbitrary input size. We believe that FFTW, which is free software, should
become the FFT library of choice for most applications. Our benchmarks,
performed on on a variety of platforms, show that FFTW's performance is
typically superior to that of other publicly available FFT software.


%package devel
Summary: Headers, libraries and docs for the FFTW library.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
FFTW is a C subroutine library for computing the Discrete Fourier Transform
(DFT) in one or more dimensions, of both real and complex data, and of
arbitrary input size. We believe that FFTW, which is free software, should
become the FFT library of choice for most applications. Our benchmarks,
performed on on a variety of platforms, show that FFTW's performance is
typically superior to that of other publicly available FFT software.

This package contains header files and development libraries needed to
develop programs using the FFTW fast Fourier transform library.


%prep
%setup -q

%build
# Build double precision
%configure \
%ifarch %ix86
    --enable-i386-hacks \
%endif
    --enable-shared \
    --enable-threads
make %{?_smp_mflags}

# Install double precision, yes this is hack-ish
rm -rf %{buildroot}
%makeinstall

# Build single precision (prefixed)
%configure \
%ifarch %ix86
    --enable-i386-hacks \
%endif
    --enable-shared \
    --enable-threads \
    --enable-type-prefix \
    --enable-float
make %{?_smp_mflags}

%install
# Don't remove previously installed double precision
#rm -rf %{buildroot}

# Install single precision
%makeinstall

# Clean up docs
rm -f doc/Makefile*

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%doc FAQ/fftw-faq.html/ doc/
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_infodir}/*
%exclude %{_libdir}/*.la

%changelog
* Fri Jan 16 2004 Matthias Saou <http://freshrpms.net/> 2.1.5-3.fr
- Re-enable build of both single and double precision libraries.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.1.5-2.fr
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.5.
- Rebuilt for Red Hat Linux 9.

* Tue Mar 18 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.1.4.
- Exclude .la files.

* Tue Oct 22 2002 Matthias Saou <http://freshrpms.net/>
- Removed the original single/double build to be "compatible" with the
  gstreamer build :-/

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

