# $Id$

# Authority: dries

Summary: Fast artificial neural network library
Name: fann
Version: 1.1.0
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://fann.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/fann/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make, gcc-c++

%description
Fann is a fast artificial neural network library. More information and a lot
of documentation is available at http://fann.sourceforge.net/ 

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%package devel
Summary: fann devel
Group: Development/Libraries
Requires: fann = %{version}-%{release}

%description devel
Development headers of fann: fast artificial neural network library

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc README AUTHORS COPYING INSTALL NEWS README TODO
%{_libdir}/libfloatfann.so.1
%{_libdir}/libdoublefann.so.1
%{_libdir}/libfixedfann.so.1
%{_libdir}/libfann.so.1
%{_libdir}/libdoublefann.so.1.1.0
%{_libdir}/libfann.so.1.1.0
%{_libdir}/libfixedfann.so.1.1.0
%{_libdir}/libfloatfann.so.1.1.0

%files devel
%{_libdir}/libfloatfann.so
%{_libdir}/libdoublefann.so
%{_libdir}/libfann.so
%{_libdir}/libfann.a
%{_libdir}/libfann.la
%{_includedir}/compat_time.h
%{_includedir}/doublefann.h
%{_includedir}/fann.h
%{_includedir}/fann_data.h
%{_includedir}/fann_internal.h
%{_includedir}/fixedfann.h
%{_includedir}/floatfann.h
%{_libdir}/libdoublefann.a
%{_libdir}/libdoublefann.la
%{_libdir}/libfixedfann.a
%{_libdir}/libfixedfann.la
%{_libdir}/libfloatfann.a
%{_libdir}/libfloatfann.la


%changelog
* Wed Apr 21 2004 Dries Verachtert <dries@ulyssis.org> 1.1.0-1
- update to 1.1.0

* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.0.5-1
- cleanup of spec file
- update from 1.0.4 to 1.0.5

* Sun Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 1.0.4-2
- first packaging for Fedora Core 1
