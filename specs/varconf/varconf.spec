# $Id$
# Authority: dries

Summary: Configuration handling library
Name: varconf
Version: 0.6.7
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://www.worldforge.org/dev/eng/libraries/varconf

Source: http://downloads.sourceforge.net/worldforge/varconf-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: pkgconfig
BuildRequires: libsigc++20-devel

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
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_libdir}/libvarconf-1.0.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/varconf-1.0/
%{_libdir}/libvarconf-1.0.so
%exclude %{_libdir}/libvarconf-1.0.la
%{_libdir}/pkgconfig/varconf-1.0.pc

%changelog
* Fri Apr 19 2013 Dries Verachtert <dries.verachtert@dries.eu> - 0.6.7-1
- Updated to release 0.6.7.

* Mon Mar 23 2009 Dries Verachtert <dries@ulyssis.org> - 0.6.6-1
- Updated to release 0.6.6.

* Sun Jan 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.6.5-1
- Updated to release 0.6.5.

* Mon Jan 16 2006 Dries Verachtert <dries@ulyssis.org> - 0.6.4-1
- Updated to release 0.6.4.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 0.6.3-1
- Initial package.
