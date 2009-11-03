# $Id$
# Authority: dag

Summary: UCL compression library
Name: ucl
Version: 1.03
Release: 2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.oberhumer.com/opensource/ucl/

Source: http://www.oberhumer.com/opensource/ucl/download/ucl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
UCL is a portable lossless data compression library written in ANSI C.
UCL implements a number of compression algorithms that achieve an
excellent compression ratio while allowing *very* fast decompression.
Decompression requires no additional memory.

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
%configure --enable-shared
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
%doc COPYING NEWS README THANKS TODO
%{_libdir}/libucl.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ucl/
%{_libdir}/libucl.a
%exclude %{_libdir}/libucl.la
%{_libdir}/libucl.so

%changelog
* Wed Oct 11 2006 Dag Wieers <dag@wieers.com> - 1.03-2
- Fix include directory location.

* Fri Oct 01 2004 Dag Wieers <dag@wieers.com> - 1.03-1
- Updated to release 1.03.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 1.02-1
- Updated to release 1.02.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
