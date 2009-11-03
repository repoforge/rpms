# Authority: dries
# Upstream: Bruno 'Beosil' Heidelberger <beosil$swileys,com>

%define real_name cal3d

Summary: Skeletal based character animation library
Name: cal3d
Version: 0.11.0
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://home.gna.org/cal3d/

Source: http://download.gna.org/cal3d/sources/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, docbook-utils, doxygen, autoconf, automake

%description
Cal3D is a skeletal based 3d character animation library written in C++ in a
platform/graphic API-independent way.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package guide
Summary: Guide for %{name}.
Group: Documentation
Requires: %{name}-devel = %{version}-%{release}

%description guide
This package contains the HTML guide for development with Cal3D.

%prep
%setup -n %{real_name}-%{version}

%build
%configure --enable-static
%{__make} %{?_smp_mflags}
( cd docs && %{__make} doc-guide && %{__make} doc-api )

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING fileformats.txt README TODO
%{_bindir}/cal3d_converter
%{_mandir}/man1/cal3d_converter.1.gz
%{_libdir}/libcal3d.so*

%files devel
%defattr(-, root, root, 0755)
%doc docs/api/html/*
%{_includedir}/cal3d/
%{_libdir}/pkgconfig/cal3d.pc
%{_libdir}/libcal3d.a
%exclude %{_libdir}/*.la

%files guide
%defattr(-, root, root, 0755)
%doc docs/guide/*

%changelog
* Mon Jul 24 2006 Vincent Knecht <vknecht@users.sourceforge.net> - 0.11.0-1
- Updated for Cal3D 0.11.0 and new location at gna.
- Added API documentation and guide.

* Thu Oct 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.9.1-1
- Initial package.
