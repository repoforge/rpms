# $Id$
# Authority: dag

Summary: Meta-data extraction library 
Name: libextractor
Version: 0.3.7
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://www.ovmj.org/libextractor/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ovmj.org/libextractor/download/libextractor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libvorbis-devel, libogg-devel, zlib-devel, gcc-c++

%description
libextractor is a simple library for meta-data extraction.
libextractor uses a plugin-mechanism that makes it easy to add support
for more file formats, allowing anybody to add new extractors quickly.

libextractor currently features meta-data extractors for  HTML, PDF, PS, 
MP3, OGG, JPEG, GIF, PNG, TIFF, RPM, ZIP, REAL, RIFF (AVI), MPEG, QT 
and ASF. It also detects many more MIME-types in a fashion similar to 
the well-known "file" tool.  Furthermore, a generic extractor that 
extracts dictionary words from binaries is included.  Supported 
dictionaries are currently da, en, de, it and no.

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
%find_lang %{name}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/extract.1*
%{_bindir}/extract
%{_libdir}/libextractor.so.*
%{_libdir}/libextractor_*.so*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/libextractor.3*
%{_includedir}/extractor.h
%{_libdir}/libextractor.a
%exclude %{_libdir}/libextractor.la
%{_libdir}/libextractor.so
%exclude %{_libdir}/libextractor_*.a
%exclude %{_libdir}/libextractor_*.la

%changelog
* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 0.3.7-1
- Updated to release 0.3.7.

* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 0.3.6-1
- Updated to release 0.3.6.

* Sat Jul 24 2004 Dag Wieers <dag@wieers.com> - 0.3.3-1
- Initial package. (using DAR)
