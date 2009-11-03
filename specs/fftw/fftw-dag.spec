# $Id$
# Authority: matthias

Summary: Fast Fourier Transform library
Name: fftw
Version: 2.1.5
Release: 2%{?dist}
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
### build double
%configure \
	--enable-shared \
	--enable-threads \
	--enable-i386-hacks
%{__make} %{?_smp_mflags}

### install double
%{__rm} -rf %{buildroot}
%makeinstall

### build single
%configure \
	--enable-shared \
	--enable-threads \
	--enable-type-prefix \
	--enable-float \
	--enable-i386-hacks
%{__make} %{?_smp_mflags}

%install
#%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING COPYRIGHT ChangeLog NEWS README* TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.gif doc/*.html doc/*.ps FAQ/fftw-faq.html/
%doc %{_infodir}/*.info*
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Fri Feb 20 2004 Dag Wieers <dag@wieers.com> - 2.1.5-2
- Cleaned up documentation.

* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 2.1.5-1
- Added double and single precision builds.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 2.1.5-0
- Updated to release 2.1.5.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 2.1.4-0
- Initial package. (using DAR)
