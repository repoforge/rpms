# $Id: $

# Authority: dries
# Upstream: 

Summary: General-purpose video codec
Name: dirac
Version: 0.1.0
Release: 1
License: MPL 1.1
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/dirac

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/dirac/Dirac-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

%description
Dirac is a general-purpose video codec aimed at resolutions from QCIF
(180x144) to HDTV (1920x1080) progressive or interlaced. It uses wavelets,
motion compensation and arithmetic coding and aims to be competitive with
other state of the art codecs.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n Dirac-%{version}

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
%doc AUTHORS ChangeLog COPYING CREDITS INSTALL LICENSE NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Tue May 11 2004 Dries Verachtert <dries@ulyssis.org> - 0.1.0
- Initial package.

