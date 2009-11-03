# $Id$
# Authority: dag
# Upstream: 

Summary: C++ High Performance Arbitrary Precision Arithmetic Package
Name: apfloat
%define real_version 241
Version: 2.41
Release: 1%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://www.apfloat.org/apfloat/

Source: http://www.apfloat.org/apfloat/%{version}/apf%{real_version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Apfloat is a C++ arbitrary precision arithmetic package. Multiplications are
done using Fast Fourier Transforms for O(n log n) complexity. The transforms
are done as Number Theoretic Transforms to avoid round-off problems. Three
different moduli are used for optimal memory usage. The final result is
achieved using the Chinese Remainder Theorem. The algorithms are optimized
for very high precision (more than 100 000 digits). The package is written to
be easily portable, but also includes assembler optimization in critical parts
for various processors for maximum performance. The software is released as
freeware and is free for non-commercial use.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -c

%build
%{__make} %{?_smp_mflags} lib OPTS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
%{__install} -Dp -m0755 apfloat.a %{buildroot}%{_libdir}/apfloat.a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

#%files
#%defattr(-, root, root, 0755)
#%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc bases.txt filelist.txt legal.txt readme.1st tapfloat.txt apfloat.ini
#%{_includedir}/*.h
#%{_libdir}/*.so
%{_libdir}/apfloat.a

%changelog
* Fri Feb 20 2009 Dag Wieers <dag@wieers.com> - 2.41-1
- Initial package. (using DAR)
