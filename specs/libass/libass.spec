# $Id$
# Authority: dag

Summary: Portable library for SSA/ASS subtitles rendering
Name: libass
Version: 0.9.11
Release: 1%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: http://code.google.com/p/libass/

Source0: http://libass.googlecode.com/files/libass-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: enca-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libpng-devel

%description
Libass is a portable library for SSA/ASS subtitles rendering.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING
%{_libdir}/libass.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ass/
%{_libdir}/libass.so
%{_libdir}/pkgconfig/libass.pc
%exclude %{_libdir}/libass.la

%changelog
* Mon Dec 06 2010 Dag Wieers <dag@wieers.com> - 0.9.11-1
- Initial package. (using DAR)
