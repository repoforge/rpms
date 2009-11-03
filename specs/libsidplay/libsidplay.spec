# $Id$
# Authority: dag

Summary: Commodore 64 music player and SID chip emulator library
Name: libsidplay
Version: 1.36.59
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.geocities.com/SiliconValley/Lakes/5147/
Source: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/libsidplay-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# libtool, sigh
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
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc DEVELOPER src/fastforward.txt src/format.txt src/mixing.txt src/mpu.txt src/panning.txt
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/sidplay/
#exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.36.59-1.2
- Rebuild for Fedora Core 5.

* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 1.36.59-1
- Updated to release 1.36.59.

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 1.36.57-0
- Initial package. (using DAR)

