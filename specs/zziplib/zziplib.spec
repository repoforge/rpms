# $Id$
# Authority: matthias

Summary: Lightweight library to easily extract data from zip files
Name: zziplib
Version: 0.13.45
Release: 1%{?dist}
License: LGPL/MPL
Group: Applications/Archiving
URL: http://zziplib.sourceforge.net/
Source: http://dl.sf.net/zziplib/zziplib-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, zlib-devel, zip, python, SDL-devel, xmlto, pkgconfig

%description
The zziplib library is intentionally lightweight, it offers the ability to
easily extract data from files archived in a single zip file. Applications
can bundle files into a single zip archive and access them. The implementation
is based only on the (free) subset of compression with the  zlib algorithm
which is actually used by the zip/unzip tools.


%package devel
Summary: Development files for the zziplib library
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig, zlib-devel, SDL-devel

%description devel
The zziplib library is intentionally lightweight, it offers the ability to
easily extract data from files archived in a single zip file. Applications
can bundle files into a single zip archive and access them. The implementation
is based only on the (free) subset of compression with the  zlib algorithm
which is actually used by the zip/unzip tools.

This package contains files required to build applications that will use the
zziplib library.


%prep
%setup


%build
%configure --enable-sdl
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc ChangeLog docs/COPYING* README TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc docs/*.htm docs/README.SDL
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
%{_datadir}/zziplib/


%changelog
* Tue Dec 20 2005 Matthias Saou <http://freshrpms.net/> 0.13.45-1
- Update to 0.13.45.

* Tue Apr  5 2005 Matthias Saou <http://freshrpms.net/> 0.13.38-1
- Update to 0.13.38, fixes gcc4 compile issues (Adrian Reber).

* Tue Jun  8 2004 Matthias Saou <http://freshrpms.net/> 0.13.36-1
- Initial RPM release.

