# Authority: freshrpms

%define real_version 0.15.1b

Summary: Library for reading and writing ID3v1 and ID3v2 tags
Name: libid3tag
Version: 0.15.1
Release: 0.b
License: GPL
Group: System Environment/Libraries
URL: http://www.underbit.com/products/mad/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.mars.org/pub/mpeg/%{name}-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: zlib-devel
Conflicts: libmad < 0.15.0

%description
A library for reading and (eventually) writing ID3 tags, both ID3v1 and the
various versions of ID3v2.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{name}-%{real_version}

%{__cat} <<EOF >id3tag.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

Name: id3tag
Description: ID3 tag reading library
Requires:
Version: %{real_version}
Libs: -L%{_libdir} -lid3tag -lz
Cflags: -I%{_includedir}
EOF

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0644 id3tag.pc %{buildroot}%{_libdir}/pkgconfig/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755)
%doc CHANGES COPYING COPYRIGHT CREDITS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
#exclude %{_libdir}/*.la

%changelog
* Wed Feb 18 2004 Dag Wieers <dag@wieers.com> - 0.15.1-0.b
- Updated to release 0.15.1b.

* Wed Aug 27 2003 Dag Wieers <dag@wieers.com> - 0.15.0-0.b
- Taken from Matthias Saou (FreshRPMS) for compatibility.
- Added id3tag.pc (needed for gstreamer-plugins).

* Mon Jul 21 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Added zlib-devel build dep.

* Wed Jun 25 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Initial release of 0.15.0b.
