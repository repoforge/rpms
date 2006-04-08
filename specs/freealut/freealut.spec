# $Id$
# Authority: dries

Summary: OpenAL Utility Toolkit
Name: freealut
Version: 1.0.1
Release: 1.2
License: LGPL
Group: Development/Libraries
URL: http://openal.org/

Source: http://openal.org/openal_webstf/downloads/freealut-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, openal-devel

%description
Freealut is the OpenAL Utility Toolkit.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_bindir}/freealut-config
%{_libdir}/libalut.so.*

%files devel
%defattr(-, root, root, 0755)
%dir %{_includedir}/AL/
%{_includedir}/AL/alut.h
%{_libdir}/libalut.a
%{_libdir}/libalut.so
%exclude %{_libdir}/libalut.la
%{_libdir}/pkgconfig/freealut.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1.2
- Rebuild for Fedora Core 5.

* Sat Feb 04 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Initial package.
