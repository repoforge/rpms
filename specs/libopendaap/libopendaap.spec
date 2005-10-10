# $Id$
# Authority: dries

Summary: Library for connection to iTunes music shares
Name: libopendaap
Version: 0.4.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://crazney.net/programs/itunes/libopendaap.html

Source: http://crazney.net/programs/itunes/files/libopendaap-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
Libopendaap is a library written in C which enables applications to
discover, and connect to, iTunes music shares. 

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
%{_libdir}/libopendaap.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%{_includedir}/daap
%{_libdir}/libopendaap.a
%exclude %{_libdir}/libopendaap.la
%{_libdir}/libopendaap.so
%{_libdir}/pkgconfig/opendaap.pc

%changelog
* Mon May 16 2005 Dag Wieers <dag@wieers.com> - 0.4.0-1
- Updated to release 0.4.0.

* Thu Jan 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.0
- Initial package.
