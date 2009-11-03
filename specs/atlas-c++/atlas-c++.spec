# $Id$
# Authority: dries

Summary: Implements the WorldForge Atlas protocol
Name: atlas-c++
Version: 0.6.1
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: https://sourceforge.net/projects/worldforge/

Source: http://dl.sf.net/worldforge/Atlas-C++-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, zlib-devel, bzip2-devel

%description
Atlas-C++ is the standard implementation of the WorldForge Atlas protocol.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n Atlas-C++-%{version}

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
#%doc %{_mandir}/man?/*
%{_bindir}/atlas_convert
%{_libdir}/libAtlas*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/Atlas-C++*/
%{_libdir}/libAtlas*.so
%{_libdir}/pkgconfig/atlascpp*.pc
%exclude %{_libdir}/*.la

%changelog
* Sat Dec  1 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.1-1
- Updated to release 0.6.1.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.0-1
- Updated to release 0.6.0.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.98-1.2
- Rebuild for Fedora Core 5.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.98-1
- Initial package.
