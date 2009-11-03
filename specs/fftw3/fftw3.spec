# $Id$
# Authority: dag

%define real_name fftw

Summary: Fast Fourier Transform library
Name: fftw3
Version: 3.2.2
Release: 1%{?dist}
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
%setup -n %{real_name}-%{version}

%build
%configure \
    --disable-static \
    --enable-shared \
    --enable-threads \
    --enable-i386-hacks
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up docs
%{__rm} -f doc/Makefile*

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
        %{buildroot}%{_infodir}/dir

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun devel
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT NEWS README* TODO
%{_libdir}/libfftw3.so.*
%{_libdir}/libfftw3_threads.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.pdf doc/FAQ/fftw-faq.html/ doc/html/
%doc %{_infodir}/fftw3.info*
%doc %{_mandir}/man1/fftw-wisdom.1*
%doc %{_mandir}/man1/fftw-wisdom-to-conf.1*
%{_bindir}/fftw-wisdom
%{_bindir}/fftw-wisdom-to-conf
%{_includedir}/fftw3.f
%{_includedir}/fftw3.h
%{_libdir}/libfftw3.so
%{_libdir}/libfftw3_threads.so
%{_libdir}/pkgconfig/fftw3.pc
#exclude %{_libdir}/fftw3.la
#exclude %{_libdir}/fftw3_threads.la

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 3.2.2-1
- Updated to release 3.2.2.

* Sun Mar 19 2006 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Updated to release 3.1.1.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 3.0.1-0
- Updated to release 3.0.1.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 2.1.5-0
- Updated to release 2.1.5.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 2.1.4-0
- Initial package. (using DAR)
