# Authority: freshrpms
Summary: A portable abstraction library for DVD decryption.
Name: libdvdcss
Version: 1.2.8
Release: 0
License: GPL
Group: System Environment/Libraries
URL: http://www.videolan.org/libdvdcss/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.videolan.org/pub/videolan/libdvdcss/%{version}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
This is a portable abstraction library for DVD decryption which is used by
the VideoLAN project, a full MPEG2 client/server solution.  You will need
to install this package in order to have encrypted DVD playback with the
VideoLAN client and the Xine navigation plugin.

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

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig &>/dev/null

%postun
/sbin/ldconfig &>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/dvdcss/
%{_libdir}/*.a
%{_libdir}/*.so
#exclude %{_libdir}/*.la

%changelog
* Tue Sep 30 2003 Dag Wieers <dag@wieers.com> - 1.2.8-0
- Updated to release 1.2.8.
- Resync with Matthias Saou (FreshRPMS).

* Tue Mar 11 2003 Dag Wieers <dag@wieers.com> - 1.2.6-0
- Updated to release 1.2.6.

* Wed Feb 05 2003 Dag Wieers <dag@wieers.com> - 1.2.5-0
- Initial package. (using DAR)
