# Authority: dag

Summary: UCL compression library.
Name: ucl
Version: 1.01
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://www.oberhumer.com/opensource/ucl/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.oberhumer.com/opensource/ucl/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

%description
UCL is a portable lossless data compression library written in ANSI C.
UCL implements a number of compression algorithms that achieve an
excellent compression ratio while allowing *very* fast decompression.
Decompression requires no additional memory.

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
%configure \
	--enable-shared \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	includedir="%{buildroot}%{_includedir}/ucl/"

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README NEWS THANKS TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ucl/*
%{_libdir}/*.so
%{_libdir}/*.a

%changelog
* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 1.01-0
- Initial package. (using DAR)
