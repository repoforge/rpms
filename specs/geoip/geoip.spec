# $Id$
# Authority: dag

%define real_name GeoIP

Summary: C library for country/city/organization to IP address or hostname mapping
Name: geoip
Version: 1.4.6
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://www.maxmind.com/app/c

Source: http://www.maxmind.com/download/geoip/api/c/GeoIP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel
Obsoletes: GeoIP < %{version}-%{release}
Provides: GeoIP = %{version}-%{release}

%description
GeoIP is a C library that enables the user to find the country that any IP
address or hostname originates from. It uses a file based database that is
accurate as of February 2009. This database simply contains IP blocks as keys,
and countries as values. This database should be more complete and accurate
than using reverse DNS lookups.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: GeoIP-devel < %{version}-%{release}
Provides: GeoIP-devel = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
%configure --disable-static --disable-dependency-tracking
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
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/GeoIP.conf.default
%config(noreplace) %{_sysconfdir}/GeoIP.conf
%{_bindir}/geoiplookup
%{_bindir}/geoiplookup6
%{_bindir}/geoipupdate
%{_datadir}/GeoIP/
%{_libdir}/libGeoIP.so.*
%{_libdir}/libGeoIPUpdate.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/GeoIP.h
%{_includedir}/GeoIPCity.h
%{_includedir}/GeoIPUpdate.h
%{_libdir}/libGeoIP.so
%{_libdir}/libGeoIPUpdate.so
%exclude %{_libdir}/libGeoIP.la
%exclude %{_libdir}/libGeoIPUpdate.la

%changelog
* Tue Feb 02 2010 Steve Huff <shuff@vecna.org> - 1.4.6-1
- Updated to release 1.4.6.

* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 1.4.5-1
- Updated to release 1.4.5.

* Fri Nov 24 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.0-1
- Updated to release 1.4.0.

* Sun Aug 06 2006 Dag Wieers <dag@wieers.com> - 1.3.17-1
- Initial package. (using DAR)
