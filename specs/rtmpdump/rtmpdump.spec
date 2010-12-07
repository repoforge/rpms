# $Id$
# Authority: dag

Summary: Toolkit for RTMP streams
Name: rtmpdump
Version: 2.3
Release: 1%{?dist}
License: GPLv2+
Group: Applications/Internet
URL: http://rtmpdump.mplayerhq.hu/

Source0: http://rtmpdump.mplayerhq.hu/download/rtmpdump-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gnutls-devel >= 2.0
BuildRequires: zlib-devel

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://. 

%package -n librtmp
Summary: Support library for RTMP streams
License: LGPLv2+
Group: Applications/Internet

%description -n librtmp
librtmp is a suport library for RTMP streams. All forms of RTMP are supported,
including rtmp://, rtmpt://, rtmpe://, rtmpte://, and rtmps://. 

%package -n librtmp-devel
Summary: Files for librtmp development
License: LGPLv2+
Group: Applications/Internet
Requires: librtmp = %{version}-%{release}

%description -n librtmp-devel
librtmp is a suport library for RTMP streams. The librtmp-devel package
contains include files needed to develop applications using librtmp.

%prep
%setup

%build
%{__make} CRYPTO="GNUTLS" SHARED="yes" OPT="%{optflags}" LIB_GNUTLS="-lgnutls -lgcrypt -ldl" LIBRTMP="librtmp/librtmp.so" LIBS=""

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" CRYPTO="GNUTLS" SHARED="yes" prefix="%{_prefix}" mandir="%{_mandir}" libdir="%{_libdir}"

%clean
%{__rm} -rf %{buildroot}

%post -n librtmp -p /sbin/ldconfig
%postun -n librtmp -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/rtmpdump.1*
%doc %{_mandir}/man8/rtmpgw.8*
%{_bindir}/rtmpdump
%{_sbindir}/rtmpgw
%{_sbindir}/rtmpsrv
%{_sbindir}/rtmpsuck

%files -n librtmp
%defattr(-, root, root, 0755)
%doc librtmp/COPYING
%{_libdir}/librtmp.so.0

%files -n librtmp-devel
%defattr(-, root, root, 0755)
%doc ChangeLog
%doc %{_mandir}/man3/librtmp.3*
%{_includedir}/librtmp/
%{_libdir}/librtmp.so
%{_libdir}/pkgconfig/librtmp.pc
%exclude %{_libdir}/librtmp.a

%changelog
* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 2.3-1
- Initial package. (using DAR)
