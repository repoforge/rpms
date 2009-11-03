# $Id$
# Authority: matthias

Summary: Fastest Fourier Transform in the West library
Name: fftw
Version: 2.1.5
Release: 4%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.fftw.org/
Source: http://www.fftw.org/fftw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
FFTW is a C subroutine library for computing the Discrete Fourier Transform
(DFT) in one or more dimensions, of both real and complex data, and of
arbitrary input size. We believe that FFTW, which is free software, should
become the FFT library of choice for most applications. Our benchmarks,
performed on on a variety of platforms, show that FFTW's performance is
typically superior to that of other publicly available FFT software.


%package devel
Summary: Headers, development libraries and documentation for the FFTW library
Group: Development/Libraries
#Requires(post): info
#Requires(preun): info
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
%setup


%build
# Build double precision
%configure \
%ifarch %{ix86}
    --enable-i386-hacks \
%endif
    --enable-shared \
    --enable-threads
%{__make} %{?_smp_mflags}

# Install double precision, yes this is rpm build hack-ish
%{__rm} -rf %{buildroot}
%makeinstall

# Build single precision (prefixed)
%configure \
%ifarch %{ix86}
    --enable-i386-hacks \
%endif
    --enable-shared \
    --enable-threads \
    --enable-type-prefix \
    --enable-float
%{__make} %{?_smp_mflags}


%install
# Don't remove previously installed double precision
#%{__rm} -rf %{buildroot}

# Install single precision
%makeinstall

# Clean up docs
%{__rm} -f doc/Makefile*


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


#post devel
# warning: no info dir entry in `/usr/share/info/fftw.info.gz'
#/sbin/install-info %{_infodir}/fftw.info.gz %{_infodir}/dir

#preun devel
#if [ $1 -eq 0]; then
#    /sbin/install-info --delete %{_infodir}/fftw.info.gz %{_infodir}/dir
#fi


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc FAQ/fftw-faq.html/ doc/
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_infodir}/fftw.info*


%changelog
* Mon Aug 30 2004 Matthias Saou <http://freshrpms.net/> 2.1.5-4
- Added install-info calls for the devel sub-package... nope, doesn't work.

* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 2.1.5-4
- Rebuild for Fedora Core 2.

* Fri Jan 16 2004 Matthias Saou <http://freshrpms.net/> 2.1.5-3
- Re-enable build of both single and double precision libraries.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.1.5-2
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

