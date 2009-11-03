# $Id$
# Authority: dries
# Upstream: Hagen Mobius <hangen,moebius$starschiffchen,de>

Summary: Library for accessing ARX archives
Name: libarxx
Version: 0.7.9
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://libarxx.sourceforge.net

Source: http://dl.sf.net/libarxx/libarxx-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
libarxx is a C++ implementation for accessing ARX archives. ARX archives are 
compressed and structured collections of data items with advanced features 
like data synchronization, references for external data items, and merging 
multiple archives.

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
%{__perl} -pi -e "s|Arxx\:\:ItemHeader\:\:ItemHeader|ItemHeader|g;" Source/ArchiveFile.h

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%{__rm} -Rf %{buildroot}/usr/doc/libarxx

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libarxx.so.*

%files devel
%{_includedir}/libarxx/
%exclude %{_libdir}/libarxx.a
%{_libdir}/libarxx.so
%{_libdir}/pkgconfig/libarxx.pc
%exclude %{_libdir}/*.la

%changelog
* Tue Apr  7 2009 Dries Verachtert <dries@ulyssis.org> - 0.7.9-1
- Updated to release 0.7.9.

* Fri Jun 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.8-1
- Updated to release 0.7.8.

* Mon Apr 16 2007 Dries Verachtert <dries@ulyssis.org> - 0.7.5-1
- Updated to release 0.7.5.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.1-1
- Updated to release 0.7.1.

* Wed Aug 09 2006 Dries Verachtert <dries@ulyssis.org> - 0.7.0-1
- Initial package.
