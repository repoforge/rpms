# Authority: dag

Name: smjpeg
Version: 0.2.1
Release: 0
Summary: SMJPEG library for SDL.
License: LGPL
Group: System Environment/Libraries
URL: http://icculus.org/smjpeg/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://sunsite.dk/pub/os/linux/loki/open-source/smjpeg/%{name}-%{version}.tar.gz
Patch: smjpeg-0.2.1-fixes.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: SDL-devel

%description
SMJPEG is a custom Motion JPEG format used by Loki Entertainment
Software in the games that they port.

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
%patch0 -p0 -b .fixes

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/*.la

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
%{_libdir}/*.so
#exclude %{_libdir}/*.la

%changelog
* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 0.2.1-0
- Initial package. (using DAR)
