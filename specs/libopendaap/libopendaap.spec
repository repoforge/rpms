# $Id: $

# Authority: dries
# Upstream: 

# Problem: the lib files don't have an .so extension

Summary: Library for connection to iTunes music shares
Name: libopendaap
Version: 0.3.0
Release: 1
License: GPL
Group: Applications/Internet
URL: http://crazney.net/programs/itunes/libopendaap.html

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://crazney.net/programs/itunes/files/libopendaap-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires: 

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
%doc %{_mandir}/man?/*
%{_libdir}/libopendaap.0*

%files devel
%{_includedir}/daap
%{_libdir}/*.a
%{_libdir}/libopendaap
%{_libdir}/pkgconfig/opendaap.pc
%exclude %{_libdir}/*.la

%changelog
* Thu Jan 06 2005 Dries Verachtert <dries@ulyssis.org> - 0.3.0
- Initial package.
