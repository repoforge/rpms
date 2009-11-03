# $Id$
# Authority: matthias
# Upstream: <libdvbpsi-devel$videolan,org>

Summary: Library for decoding and generating MPEG 2 and DVB PSI sections
Name: libdvbpsi
Version: 0.1.2
Release: 0%{?dist}
License: GPL
URL: http://www.videolan.org/libdvbpsi/
Group: System Environment/Libraries

Source: http://www.videolan.org/pub/videolan/libdvbpsi/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
libdvbpsi is a simple library designed for MPEG 2 TS and DVB PSI tables
decoding and generating. The important features are:
 * PAT decoder and genarator.
 * PMT decoder and generator.

%package devel
Summary: Development tools for programs which will use the libdvbpsi library
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The libdvbpsi-devel package includes the header files and static libraries
necessary for developing programs which will manipulate MPEG 2 and DVB PSI
information using the libdvbpsi library.

%prep
%setup

%build
%configure --enable-release
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc COPYING
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/dvbpsi/
#exclude %{_libdir}/*.la

%changelog
* Wed Feb 19 2003 Dag Wieers <dag@wieers.com> - 0.1.2-0
- Initial package. (using DAR)
