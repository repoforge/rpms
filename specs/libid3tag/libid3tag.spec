# $Id$

Summary: Library for reading and writing ID3v1 and ID3v2 tags
Name: libid3tag
Version: 0.15.1b
Release: 1.fr
License: GPL
Group: System Environment/Libraries
URL: http://www.underbit.com/products/mad/
Source: ftp://ftp.mars.org/pub/mpeg/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel, gcc-c++
Conflicts: libmad < 0.15.1b

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.


%package devel
Summary: Header and library for developing programs that will use libid3tag.
Group: Development/Libraries
Requires: %{name} = %{version}, zlib-devel

%description devel
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

This package contains the header file as well as the static library needed
to develop programs that will use libid3tag for ID3 tar reading and writing.


%prep
%setup -q

%build
%configure
make %{_smp_mflags}

cat << EOF > id3tag.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: id3tag
Description: ID3 tag library
Requires:
Version: %{version}
Libs: -L%{_libdir} -lid3tag -lz
Cflags: -I%{_includedir}
EOF

%install
rm -rf %{buildroot}
%makeinstall
install -m 644 -D id3tag.pc %{buildroot}%{_libdir}/pkgconfig/id3tag.pc

%clean
rm -rf %{buildroot}

%files 
%defattr(-, root, root)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
* Thu Feb 19 2004 Matthias Saou <http://freshrpms.net/> 0.15.1b-1.fr
- Update to 0.15.1b.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.15.0b-4.fr
- Rebuild for Fedora Core 1.

* Wed Sep  3 2003 Matthias Saou <http://freshrpms.net/>
- Fixed the -I in the pkgconfig file, thanks to Michael A. Peters.

* Thu Aug 28 2003 Matthias Saou <http://freshrpms.net/>
- Added id3tag.pc required by gstreamer-plugins.
- Added zlib-devel dep to the devel package.

* Mon Jul 21 2003 Matthias Saou <http://freshrpms.net/>
- Added zlib-devel build dep.

* Wed Jun 25 2003 Matthias Saou <http://freshrpms.net/>
- Initial release of 0.15.0b.

