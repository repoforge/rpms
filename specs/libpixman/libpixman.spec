# $Id$

# Authority: dag

Summary: A merge of libpixregion and libic.
Name: libpixman
Version: 0.1.0
Release: 0
License: MIT
Group: System Environment/Libraries
URL: http://www.cairographics.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cairographics.org/snapshots/libpixman-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: pkgconfig
Obsoletes: slim, libic, libpixregion

%description
libpixman is a merge of libpixregion and libic.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libpixman-devel, XFree86-devel

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

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc
#%{_libdir}/*.la

%changelog
* Wed Feb 25 2004 Dag Wieers <dag@wieers.com> - 0.1.0-0
- Initial package. (using DAR)
