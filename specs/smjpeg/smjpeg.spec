# $Id$
# Authority: dag

Name: smjpeg
Version: 0.2.1
Release: 0.2%{?dist}
Summary: SMJPEG library for SDL
License: LGPL
Group: System Environment/Libraries
URL: http://icculus.org/smjpeg/

Source: ftp://sunsite.dk/pub/os/linux/loki/open-source/smjpeg/smjpeg-%{version}.tar.gz
Patch: smjpeg-0.2.1-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: SDL-devel, libtool, autoconf, automake

%description
SMJPEG is a custom Motion JPEG format used by Loki Entertainment
Software in the games that they port.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch0 -p0 -b .fixes

%build
%{__libtoolize} --force --copy
%configure
%{__make} %{?_smp_mflags} SED=sed

%install
%{__rm} -rf %{buildroot}
%makeinstall SED=sed

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README SMJPEG.txt TODO
%{_bindir}/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/smjpeg/
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2.1-0.2
- Rebuild for Fedora Core 5.

* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
