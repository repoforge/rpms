# $Id$

Summary: A software codec for DV video, used by most digital camcorders.
Name: libdv
Version: 0.101
Release: 2.fr
License: GPL
Group: System Environment/Libraries
Source: http://dl.sf.net/libdv/%{name}-%{version}.tar.gz
URL: http://libdv.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk+-devel >= 1.2.4, pkgconfig >= 0.9.0

%description 
The Quasar DV codec (libdv) is a software codec for DV video, the encoding
format used by most digital camcorders, typically those that support the
IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was developed
according to the official standards for DV video: IEC 61834 and SMPTE 314M. 


%package devel
Summary: Development file for programs which use the libdv library.
Group: Development/Libraries
Requires: %{name} = %{version}, gtk+-devel >= 1.2.4, pkgconfig >= 0.9.0

%description devel
The Quasar DV codec (libdv) is a software codec for DV video, the encoding
format used by most digital camcorders, typically those that support the
IEEE 1394 (a.k.a. FireWire or i.Link) interface. Libdv was developed
according to the official standards for DV video: IEC 61834 and SMPTE 314M. 

This is the libraries, include files and other resources that are used to
incorporate libdv into applications.


%prep
%setup -q

%build
%configure
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
%doc AUTHORS ChangeLog COPY* NEWS README* TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.101-2.fr
- Add missing gtk+-devel dependency on the devel package.

* Tue Feb 24 2004 Matthias Saou <http://freshrpms.net/> 0.101-1.fr
- Update to 0.101.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.99-3.fr
- Rebuild for Fedora Core 1.

* Tue Aug 12 2003 Matthias Saou <http://freshrpms.net/>
- Added gtk+-devel build dep.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Exclude .la files.

* Thu Jan 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.99.

* Thu Sep 26 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.

* Thu Aug  1 2002 Matthias Saou <http://freshrpms.net/>
- Spec file rewrite from the one included with the sources.

