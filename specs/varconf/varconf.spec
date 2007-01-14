# $Id$
# Authority: dries

Summary: Configuration handling library
Name: varconf
Version: 0.6.5
Release: 1
License: LGPL
Group: Development/Libraries
URL: http://www.worldforge.org/dev/eng/libraries/varconf

Source: http://dl.sf.net/worldforge/varconf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, pkgconfig, libsigc++20-devel

%description
Varconf is configuration handling library required by many WorldForge
components. It supports the loading and saving of config files, handling
of complex command line arguments, and signals to notify the application
of configuration changes.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_libdir}/libvarconf*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/varconf-*/
%{_libdir}/libvarconf*.so
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/varconf*.pc

%changelog
* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1
- Updated to release 0.6.5.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.4-1.2
- Rebuild for Fedora Core 5.

* Mon Jan 16 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.4-1
- Updated to release 0.6.4.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Initial package.
