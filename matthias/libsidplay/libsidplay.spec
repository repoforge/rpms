# $Id$
# Authority: dag

Summary: A Commodore 64 music player and SID chip emulator library
Name: libsidplay
Version: 1.36.57
Release: 0.1
License: GPL
Group: System Environment/Libraries
URL: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/
Source: http://www.geocities.com/SiliconValley/Lakes/5147/sidplay/packages/%{name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This library provides the Sound Interface Device (SID) chip emulator
engine that is used by music player programs like SIDPLAY. With it
you can play musics from Commodore 64 (or compatible) programs.


%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup -q


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root, 0755)
%doc DEVELOPER src/fastforward.txt src/format.txt 
%doc src/mixing.txt src/mpu.txt src/panning.txt
%{_libdir}/*.a
%{_libdir}/*.so
%{_includedir}/sidplay/


%changelog 
* Fri Mar  5 2003 Matthias Saou <http://freshrpms.net/> 1.36.57-0.1
- Branch off to build gstreamer07-plugins.

* Thu Aug 28 2003 Dag Wieers <dag@wieers.com> - 1.36.57-0
- Initial package. (using DAR)

