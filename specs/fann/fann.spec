# $Id$

# Authority: dries

Summary: a fast artificial neural network library
Name: fann
Version: 1.0.5
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://fann.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/fann/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc, make

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
sed -i "s/^DESTDIR =.*//" $(find . -type f | egrep "Makefile$")
export DESTDIR=$RPM_BUILD_ROOT
make install

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
/usr/lib/libfloatfann.so.1
/usr/lib/libdoublefann.so.1
/usr/lib/libfixedfann.so.1
/usr/lib/libfann.so.1
/usr/lib/libdoublefann.so.1.0.5
/usr/lib/libfann.so.1.0.5
/usr/lib/libfixedfann.so.1.0.5
/usr/lib/libfloatfann.so.1.0.5

%files devel
/usr/lib/libfloatfann.so
/usr/lib/libdoublefann.so
/usr/lib/libfann.so
/usr/lib/libfann.so
/usr/lib/libfann.a
/usr/lib/libfann.la
/usr/include/compat_time.h
/usr/include/doublefann.h
/usr/include/fann.h
/usr/include/fann_data.h
/usr/include/fann_internal.h
/usr/include/fixedfann.h
/usr/include/floatfann.h
/usr/lib/libdoublefann.a
/usr/lib/libdoublefann.la
/usr/lib/libfixedfann.a
/usr/lib/libfixedfann.la
/usr/lib/libfloatfann.a
/usr/lib/libfloatfann.la


%changelog
* Sun Jan 11 2004 Dries Verachtert <dries@ulyssis.org> 1.0.5-1
- cleanup of spec file
- update from 1.0.4 to 1.0.5

* Sun Dec 13 2003 Dries Verachtert <dries@ulyssis.org> 1.0.4-2
- first packaging for Fedora Core 1
