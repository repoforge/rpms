# $Id$
# Authority: shuff

Summary: NeMeSi - RTSP/RSP client library
Name: libnemesi
Version: 0.6
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://lscube.org/projects/libnemesi

Source: http://cgit.lscube.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc >= 3.4, make >= 3.80, libtool >= 1.5.20
BuildRequires: netembryo-devel >= 0.0.4
BuildRequires: autoconf >= 2.61, automake >= 1.9

Requires: netembryo >= 0.0.4

%description
Libnemesi let you add multimedia streaming playback in your applications in a
quick and straightforward way. This software, derived from the experience
matured with NeMeSi is fully compliant with IETF's standards for real-time
streaming of multimedia contents over Internet. libnemesi implements RTSP –
Real-Time Streaming Protocol (RFC2326) and RTP/RTCP – Real-Time Transport
Protocol/RTP Control Protocol (RFC3550) supporting the RTP Profile for Audio
and Video Conferences with Minimal Control (RFC3551).

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
autoreconf -i

%build
%configure --disable-static --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc README
%{_libdir}/libnemesi.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libnemesi/libnemesi.h
%exclude %{_libdir}/libnemesi.la
%{_libdir}/libnemesi.so
%{_libdir}/pkgconfig/libnemesi.pc

%changelog
* Wed Sep 09 2009 Steve Huff <shuff@vecna.org> - 0.6-1
- initial package
- DOES NOT BUILD (needs autoconf >= 2.61)
