# Authority: freshrpms
Summary: DVD menu navigation library
Name: libdvdnav
Version: 0.1.9
Release: 0
Group: System Environment/Libraries
License: GPL
URL: http://dvd.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://prdownloads.sourceforge.net/dvd/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: automake >= 1.7, doxygen

%description
The libdvdnav library provides support to applications wishing to make use
of advanced DVD features.

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

%build
#{__aclocal}
#{__autoconf}
#{__autoheader}
#{__automake}
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/*.la

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/dvdnav-config
%{_libdir}/*.so
%{_includedir}/dvdnav/
%{_datadir}/aclocal/*
#exclude %{_libdir}/*.la

%changelog
* Tue Jun 10 2003 Dag Wieers <dag@wieers.com> - 0.1.9-0
- Updated to release 0.1.9.
- Updated to release 0.1.7.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 0.1.4note2-1
- Use %makeinstall macro.
- Added automake macros so it builds on older systems.

* Mon Feb 17 2003 Dag Wieers <dag@wieers.com> - 0.1.4note2-0
- Initial package. (using DAR)
