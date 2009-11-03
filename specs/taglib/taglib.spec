# $Id$
# Authority: dag

Summary: Audio Meta-Data Library
Name: taglib
Version: 1.5
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://ktown.kde.org/~wheeler/taglib/

Source: http://developer.kde.org/~wheeler/files/src/taglib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: doxygen, graphviz, gcc-c++

%description
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for
MP3 files, Ogg Vorbis comments and ID3 tags and Vorbis comments in
FLAC files.

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
%configure --disable-rpath

%{__make} %{?_smp_mflags}

pushd doc
doxygen taglib.doxygen
popd

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf examples/{.deps,Makefile*}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING* doc/README
%{_libdir}/libtag.so.*
%{_libdir}/libtag_c.so.*

%files devel
%defattr(-, root, root, 0755)
%doc examples/ doc/html/
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/libtag.so
%exclude %{_libdir}/libtag.la
%{_libdir}/libtag_c.so
%exclude %{_libdir}/libtag_c.la
%{_libdir}/pkgconfig/taglib*.pc

%changelog
* Sat Feb 23 2008 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Tue Feb 14 2006 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
