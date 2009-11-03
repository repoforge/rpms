# $Id$
# Authority: dag
# Upstream: <vls-devel$videolan,org>

%define real_name vls

Summary: MPEG, DVD, and DVB server for Unix/Linux
Name: videolan-server
Version: 0.5.6
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.videolan.org/streaming/

Source: http://download.videolan.org/pub/videolan/vls/%{version}/vls-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libdvdread-devel, libdvbpsi-devel, linuxdoc-tools, gcc-c++
Provides: vls = %{version}-%{release}

%description
The VideoLAN Server (VLS) can stream MPEG-1, MPEG-2, and MPEG-4 files,
DVDs, digital satellite channels, digital terrestial television
channels, and live videos on a network in unicast or multicast. A
VideoLAN Client (VLC) or a set top box can receive the stream, decode,
and display

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

### Disable default passwords.
%{__perl} -pi.orig -e '
		s|^(  monitor)|#$1|;
		s|^(  bozo)|#$1|;
	' vls.cfg

%build
%configure \
	--enable-v4l \
	--enable-daemon \
	--enable-syslog \
	--enable-dvd
#	--enable-dvb
%{__make} %{?_smp_mflags}
#%{__make} -C doc/developer/

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO vls.cfg
%config(noreplace) %{_sysconfdir}/videolan/
%{_bindir}/*
%{_libdir}/videolan/

#%files devel
#%defattr(-, root, root, 0755)
#%doc doc/developer/*.html

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.6-1.2
- Rebuild for Fedora Core 5.

* Sun May 02 2004 Dag Wieers <dag@wieers.com>  0.5.6-1
- Initial package. (using DAR)
