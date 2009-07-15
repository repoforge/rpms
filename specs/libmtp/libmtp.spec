# $Id$
# Authority: dag

Summary: Library for MTP media players
Name: libmtp
Version: 0.3.7
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://libmtp.sourceforge.net/

Source: http://dl.sf.net/libmtp/libmtp-%{version}.tar.gz
Patch: libmtp-0.2.6.1-simpler-rules.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libusb-devel
BuildRequires: doxygen
Requires: hal
Requires: udev

%description
This package provides a software library for communicating with MTP
(Media Transfer Protocol) media players, typically audio players, video
players etc.

%package utils
Summary: MTP media player utilities
Group: Applications/Multimedia
Requires: %{name} = %{version}-%{release}
Obsoletes: mtp-examples <= %{version}-%{release}
Provides: mtp-examples = %{version}-%{release}

%description utils
This package provides example programs for communicating with MTP
devices.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libusb-devel
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p1 -b .rules

%build
%configure \
    --disable-static \
    --program-prefix="mtp-"
%{__make} %{?_smp_mflags}

### Remove permissions from symlink in udev script, we use
### hald rules to fix the permissions instead.
examples/hotplug -a"SYMLINK+=\"libmtp-%k\"" > libmtp.rules

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 libmtp.rules %{buildroot}%{_sysconfdir}/udev/rules.d/60-libmtp.rules
%{__install} -Dp -m0644 libmtp.fdi %{buildroot}%{_datadir}/hal/fdi/information/10freedesktop/10-usb-music-players-libmtp.fdi

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%config(noreplace) %{_sysconfdir}/udev/rules.d/*
%config(noreplace) %{_datadir}/hal/fdi/information/10freedesktop/10-usb-music-players-libmtp.fdi
%{_libdir}/libmtp.so.*

%files utils
%defattr(-, root, root, 0755)
%{_bindir}/mtp-*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmtp.h
%{_libdir}/libmtp.so
%{_libdir}/pkgconfig/libmtp.pc
%exclude %{_libdir}/libmtp.la

%changelog
* Wed Jul 15 2009 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Initial package. (using DAR)
