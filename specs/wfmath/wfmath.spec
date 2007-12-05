# $Id$
# Authority: dries

Summary: Geometric objects and math objects
Name: wfmath
Version: 0.3.7
Release: 1
License: GPL
Group: Development/Libraries
URL: http://www.worldforge.org/dev/eng/libraries/wfmath

Source: http://dl.sf.net/worldforge/wfmath-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
The primary focus of WFMath is geometric objects. Thus, it includes several
shapes (boxes, balls, lines), in addition to the basic math objects that
are used to build these shapes (points, vectors, and matrices).

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

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libwfmath*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/wfmath*/
%{_libdir}/libwfmath*.so
%{_libdir}/pkgconfig/wfmath*.pc
%exclude %{_libdir}/*.la

%changelog
* Mon Dec  3 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.7-1
- Updated to release 0.3.7.

* Mon Jul 23 2007 Dries Verachtert <dries@ulyssis.org> - 0.3.6-1
- Updated to release 0.3.6.

* Thu Aug 24 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.5-1
- Updated to release 0.3.5.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.3.4-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.4-1
- Initial package.
