# $Id$
# Authority: rudolf
# Upstream: <physfs$icculus,org>

Summary: Library to provide abstract access to various archives
Name: physfs
Version: 1.0.0
Release: 0%{?dist}
License: zlib License
Group: System Environment/Libraries
URL: http://www.icculus.org/physfs/

Source: http://www.icculus.org/physfs/downloads/physfs-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel, readline-devel, zlib-devel

%description
A library to provide abstract access to various archives.
It is intended for use in video games.
The programmer defines a "write directory" on the physical filesystem.
No file writing done through the PhysicsFS API can leave that write directory.

%package devel
Summary: Headers for developing programs that will use physfs
Group: Development/Libraries
Requires: %{name} = %{version}, zlib-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use physfs

%prep
%setup

%build
%configure \
	--program-prefix="%{?_program_prefix}" \

%install
%{__rm} -rf %{buildroot}
%{__make} install \
	DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG CREDITS INSTALL LICENSE TODO
%{_libdir}/libphysfs-*.so.*

%files -n %{name}-devel
%defattr(-, root, root, 0755)
%{_bindir}/test_physfs
%{_includedir}/physfs.h
%{_libdir}/libphysfs.a
%exclude %{_libdir}/libphysfs.la
%{_libdir}/libphysfs.so

%changelog
* Wed Dec 29 2004 Dag Wieers <dag@wieers.com> - 1.0.0-0
- Added x86_64 fix.

* Sun Oct 12 2003 Che
- initial rpm release
