# $Id$
# Authority: dag

%define real_name fftw

Summary: Fast Fourier Transform library
Name: fftw3
Version: 3.0.1
Release: 0
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
	--enable-shared \
	--enable-threads \
	--enable-i386-hacks
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up docs
%{__rm} -f doc/Makefile*

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la \
		%{buildroot}%{_infodir}/dir

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%post devel
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir

%preun devel
/sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYRIGHT NEWS README* TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.pdf doc/FAQ/fftw-faq.html/ doc/html/
%doc %{_mandir}/man?/*
%doc %{_infodir}/*.info*
%{_bindir}/*
%{_includedir}/*.h
%{_includedir}/*.f
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
#exclude %{_libdir}/*.la

%changelog
* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 3.0.1-0
- Updated to release 3.0.1.

* Thu Apr 17 2003 Dag Wieers <dag@wieers.com> - 2.1.5-0
- Updated to release 2.1.5.

* Sun Mar 30 2003 Dag Wieers <dag@wieers.com> - 2.1.4-0
- Initial package. (using DAR)
