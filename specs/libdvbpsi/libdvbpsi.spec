# $Id$

%define real_name libdvbpsi3

Summary: A library for decoding and generating MPEG TS and DVB PSI tables.
Name: libdvbpsi
Version: 0.1.4
Release: 1.fr
License: GPL
Group: System Environment/Libraries
Source: http://download.videolan.org/pub/%{name}/%{version}/%{real_name}-%{version}.tar.bz2
URL: http://developers.videolan.org/libdvbpsi/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The libdvbpsi is part of the VideoLAN project, a full MPEG2 client/server
solution. The libdvbpsi can also be used with extra programs that need DVB
and PSI decoders and generators.
 
The VideoLAN team decided to write the libdvbpsi to make the VideoLAN Client
and the VideoLAN Server capable of demultiplexing a satellite DVB stream.
The library aims at making it easy to decode PSI tables (such as PAT, PMT
etc.) present in a TS/DVB stream.


%package devel
Summary: Development files from the libdvbpsi library.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
The libdvbpsi is part of the VideoLAN project, a full MPEG2 client/server
solution. The libdvbpsi can also be used with extra programs that need DVB
and PSI decoders and generators.

You will need to install these development files if you intend to rebuild
programs with libdvbpsi support.


%prep
%setup -q -n %{real_name}-%{version}

%build
%configure --enable-release
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%makeinstall

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/%{name}.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/%{name}.a
%exclude %{_libdir}/%{name}.la
%{_libdir}/%{name}.so

%changelog
* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.1.4-1.fr
- Update to 0.1.4.
- Added %%{real_name} since it changed to libdvbpsi3.
- Updated the Source URL to reflect new download location.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 0.1.3-2.fr
- Rebuild for Fedora Core 1.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.1.3.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Tue Feb  4 2003 Matthias Saou <http://freshrpms.net/>
- Initial rpm release, 0.1.2.

