# $Id$

# Authority: dries
# Upstream:

Summary: Dutch online dictionary
Name: gnuvd
Version: 1.0beta4
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.djcbsoftware.nl/projecten/gnuvd/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://www.djcbsoftware.nl/projecten/gnuvd/gnuvd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++

# Screenshot: http://www.djcbsoftware.nl/projecten/gnuvd/gnuvd1.png

%description
A program which searches Dutch words in the online dictionary Van Dale.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc README ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS TODO README.nl
%{_bindir}/gnuvd
%doc %{_mandir}/man?/*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libgnuvd/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/*.la

%changelog
* Sat May 5 2004 Dries Verachtert <dries@ulyssis.org> 1.0beta4
- initial package
