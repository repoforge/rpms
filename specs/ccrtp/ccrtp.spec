# $Id$
# Authority: dag

Summary: Common C++ class framework for RTP/RTCP
Name: ccrtp
Version: 1.6.0
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/commoncpp/

Source: http://ftp.gnu.org/pub/gnu/ccrtp/ccrtp-%{version}.tar.gz
Patch0: ccrtp-1.6.0-gcc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: commoncpp2-devel >= 1.6.0
BuildRequires: doxygen
BuildRequires: libgcrypt-devel

%description
ccRTP is a generic, extensible and efficient C++ framework for
developing applications based on the Real-Time Transport Protocol
(RTP) from the IETF. It is based on Common C++ and provides a full
RTP/RTCP stack for sending and receiving of realtime data by the use
of send and receive packet queues. ccRTP supports unicast,
multi-unicast and multicast, manages multiple sources, handles RTCP
automatically, supports different threading models and is generic as
for underlying network and transport protocols.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: commoncpp2-devel
Requires: pkgconfig
Requires: /sbin/install-info

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .gcc
%{__chmod} 0644 src/ccrtp/rtp.h

%build
%configure --disable-static
%{__make} # %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%post devel
/sbin/install-info %{_infodir}/ccrtp.info* %{_infodir}/dir || :

%preun devel
if [ $1 = 0 ]; then
    /sbin/install-info --delete %{_infodir}/ccrtp.info* %{_infodir}/dir || :
fi

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING* README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/html
%doc %{_infodir}/ccrtp.info*
%{_includedir}/ccrtp/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libccrtp1.pc
#%exclude %{_infodir}/dir
%exclude %{_libdir}/*.la

%changelog
* Sun Sep 14 2008 Dag Wieers <dag@wieers.com> - 1.6.0-1
- Initial package. (using DAR)
