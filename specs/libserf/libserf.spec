# $Id$
# Authority: cmr
# Upstream: serf-dev@googlegroups.com

Summary: HTTP client library written in C using apr
Name: libserf
Version: 0.3.0
Release: 1
License: Apache License 2.0
Group: Development/Libraries
URL: http://code.google.com/p/serf/

Source: serf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: apr-devel apr-util-devel openssl-devel
Requires: apr apr-util openssl

%description

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n serf-%{version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post
/sbin/ldconfig 2>/dev/null

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/libserf-0.so.0
%{_libdir}/libserf-0.so.0.0.0

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/serf.h
%{_includedir}/serf_bucket_types.h
%{_includedir}/serf_bucket_util.h
%{_includedir}/serf_declare.h
%{_libdir}/libserf-0.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la


%changelog
* Fri May 08 2009 Christoph Maser <cmr@financial.com> - 0.3.0-1
- Initial package.
