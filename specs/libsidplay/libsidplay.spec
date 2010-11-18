# $Id$
# Authority: dag

Summary: Commodore 64 music player and SID chip emulator library
Name: libsidplay
Version: 1.36.60
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.geocities.com/SiliconValley/Lakes/5147/

#Source: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/libsidplay-%{version}.tgz
Source: http://home.arcor.de/ms2002sep/bak/libsidplay-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it
you can play musics from Commodore 64 (or compatible) programs.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%{_libdir}/libsidplay.so.*

%files devel
%defattr(-, root, root, 0755)
%doc DEVELOPER src/fastforward.txt src/mixing.txt src/mpu.txt src/panning.txt
%{_includedir}/sidplay/
%{_libdir}/libsidplay.so
%exclude %{_libdir}/libsidplay.la

%changelog
* Sun Nov 14 2010 Dag Wieers <dag@wieers.com> - 1.36.60-1
- Updated to release 1.36.60.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 1.36.59-1
- Updated to release 1.36.59.

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 1.36.57-0
- Initial package. (using DAR)
