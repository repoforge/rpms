# $Id$
# Authority: dag

Summary: C library for reading, creating, and modifying zip archives
Name: libzip
Version: 0.9
Release: 1%{?dist}
License: BSD
Group: System Environment/Libraries
URL: http://www.nih.at/libzip/

Source: http://www.nih.at/libzip/libzip-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: zlib-devel
#BuildRequires: zlib-devel >= 1.2.2

%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from 
other zip archives. Changes made without closing the archive can be reverted. 
The API is documented by man pages.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
#autoreconf -f -i
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" INSTALL="%{__install} -p"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS NEWS README THANKS TODO
%doc %{_mandir}/man1/zipcmp.1*
%doc %{_mandir}/man1/zipmerge.1*
%doc %{_mandir}/man1/ziptorrent.1*
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptorrent
%{_libdir}/libzip.so.1*

%files devel
%defattr(-, root, root, 0755)
%{_mandir}/man3/libzip.3*
%{_mandir}/man3/zip_*.3*
%{_includedir}/zip.h
%{_libdir}/libzip.so
%{_libdir}/pkgconfig/libzip.pc
%exclude %{_libdir}/libzip.la

%changelog
* Mon Jan 11 2010 Dag Wieers <dag@wieers.com> - 0.9-1
- Initial package. (using DAR)
