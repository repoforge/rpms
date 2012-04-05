# $Id$
# Authority: dag

%define _default_patch_fuzz 2

%define real_name live
%define real_version 2012.02.04
%define live_soversion 0

Summary: Live555.com streaming libraries
Name: live555
Version: 0
Release: 0.27.%{real_version}%{?dist}
License: LGPLv2+ and GPLv2+
Group: System Environment/Libraries
URL: http://live555.com/liveMedia/

Source0: http://live555.com/liveMedia/public/live.%{real_version}.tar.gz
Patch0: live.2010.01.16-shared.patch
Patch1: live-getaddrinfo.patch
Patch2: live-inet_ntop.patch
Patch3: live-uselocale.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

%package devel
Summary: Development files for live555.com streaming libraries
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: live-devel < 0-0.19.2008.04.03
Provides: live-devel = %{version}-%{release}

%description devel
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

%package tools
Summary: RTSP streaming tools using live555.com streaming libraries
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Obsoletes: live-tools < 0-0.19.2008.04.03
Provides: live-tools = %{version}-%{release}

%description tools
This code forms a set of C++ libraries for multimedia streaming, 
using open standard protocols (RTP/RTCP, RTSP, SIP). These 
libraries - which can be compiled for Unix (including Linux and Mac OS X), 
Windows, and QNX (and other POSIX-compliant systems) - can be used 
to build streaming applications.
The libraries can also be used to stream, receive, and process MPEG, 
H.263+ or JPEG video, and several audio codecs. They can easily be 
extended to support additional (audio and/or video) codecs, and can 
also be used to build basic RTSP or SIP clients and servers, and have 
been used to add streaming support to existing media player applications.

This package contains the live555.com streaming server
(live555MediaServer), the example programs (openRTSP, playSIP, sapWatch,
vobStreamer) and a variety of test tools.

%package static
Summary: Static libraries for %{name}
Group: Development/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for
developing applications that use %{name}.

%prep
%setup -n %{real_name}
%{__install} -Dp -m0644 config.linux config.linux.static
%patch0 -p1 -b .shared
#patch1 -p1 -b .vlc1
#patch2 -p1 -b .vlc2
#patch3 -p1 -b .vlc3

%build
./genMakefiles %{_target_os}.static
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"
%{__mv} $(find BasicUsageEnvironment groupsock liveMedia UsageEnvironment -name "*.a" ) $(pwd)
%{__make} clean

./genMakefiles %{_target_os}
%{__make} CFLAGS="%{optflags} -fPIC -DPIC" SO_VERSION="%{live_soversion}"

%install
%{__rm} -rf %{buildroot}
for base in BasicUsageEnvironment groupsock liveMedia UsageEnvironment ; do
    %{__install} -d -m0755 %{buildroot}%{_includedir}/$base/
    %{__install} -p -m0644 $base/include/*.h* %{buildroot}%{_includedir}/$base/
    %{__install} -Dp -m0644 lib$base.a %{buildroot}%{_libdir}/lib$base.a
    %{__install} -Dp -m0755 $base/lib$base.so %{buildroot}%{_libdir}/lib$base.so.%{date}
    %{__ln_s} -f lib$base.so.%{date} %{buildroot}%{_libdir}/lib$base.so.%{live_soversion}
    %{__ln_s} -f lib$base.so.%{date} %{buildroot}%{_libdir}/lib$base.so
done

%{__install} -Dp -m0755 mediaServer/live555MediaServer %{buildroot}%{_bindir}/live555MediaServer

pushd testProgs
for bin in \
  MPEG2TransportStreamIndexer \
  openRTSP \
  playSIP \
  sapWatch \
  testAMRAudioStreamer \
  testMP3Receiver \
  testMP3Streamer \
  testMPEG1or2AudioVideoStreamer \
  testMPEG1or2AudioVideoToDarwin \
  testMPEG1or2ProgramToTransportStream \
  testMPEG1or2Splitter \
  testMPEG1or2VideoReceiver \
  testMPEG1or2VideoStreamer \
  testMPEG2TransportStreamTrickPlay \
  testMPEG2TransportStreamer \
  testMPEG4VideoStreamer \
  testMPEG4VideoToDarwin \
  testOnDemandRTSPServer \
  testRelay \
  testWAVAudioStreamer \
  vobStreamer \
; do
    %{__install} -Dp -m0755 $bin %{buildroot}%{_bindir}/$bin
done
popd

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_libdir}/libBasicUsageEnvironment.so.*
%{_libdir}/libgroupsock.so.*
%{_libdir}/libliveMedia.so.*
%{_libdir}/libUsageEnvironment.so.*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libBasicUsageEnvironment.so
%{_libdir}/libgroupsock.so
%{_libdir}/libliveMedia.so
%{_libdir}/libUsageEnvironment.so
%{_includedir}/BasicUsageEnvironment/
%{_includedir}/groupsock/
%{_includedir}/liveMedia/
%{_includedir}/UsageEnvironment/

%files static
%defattr(-, root, root, 0755)
%{_libdir}/libBasicUsageEnvironment*.a
%{_libdir}/libgroupsock*.a
%{_libdir}/libliveMedia*.a
%{_libdir}/libUsageEnvironment*.a

%changelog
* Tue Feb 21 2012 Dag Wieers <dag@wieers.com> - 0-0.27.2012.02.04
- Updated to release 2012.02.04.

* Sun Dec 05 2010 Dag Wieers <dag@wieers.com> - 0-0.27.2010.04.09
- Initial package. (based on fedora)
