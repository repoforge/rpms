# Authority: freshrpms
Summary: A simple foundation for reading DVD video disks.
Name: libdvdread
Version: 0.9.4
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://www.dtek.chalmers.se/groups/dvd/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Requires: libdvdcss >= 1.2.0

%description
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.
It parses IFO files, reads NAV-blocks, and performs CSS authentication
and descrambling. 

%package devel
Summary: Development files from the libdvdread library.
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
libdvdread provides a simple foundation for reading DVD video disks.
It provides the functionality that is required to access many DVDs.
It parses IFO files, reads NAV-blocks, and performs CSS authentication
and descrambling. 

You will need to install these development files if you intend to rebuild
programs that use this library.

%prep
%setup

%build
%configure
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
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/dvdread/
%{_libdir}/*.a
%{_libdir}/*.so
#exclude %{_libdir}/*.la

%changelog
* Wed Feb 05 2003 Dag Wieers <dag@wieers.com> - 0.9.3-0
- Initial package.
