# $Id$
# Authority: dries

Summary: OpenAL Utility Toolkit
Name: freealut
Version: 1.1.0
Release: 1%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://openal.org/

Source: http://openal.org/openal_webstf/downloads/freealut-%{version}.tar.gz
Patch0: freealut-1.1.0-openal.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, automake >= 1.9, openal-devel

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
%patch0 -p0

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libalut.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/freealut-config
%{_includedir}/AL/
%{_libdir}/libalut.a
%exclude %{_libdir}/libalut.la
%{_libdir}/libalut.so
%{_libdir}/pkgconfig/freealut.pc

%changelog
* Tue Feb 20 2007 Dag Wieers <dag@wieers.com> - 1.1.0-1
- Updated to release 1.1.0.

* Sat Feb 04 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Initial package.
