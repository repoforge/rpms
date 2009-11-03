# $Id$
# Authority: dries
# Upstream: Marius L. Jøhndal <mariuslj$ifi,uio,no>

Summary: Command line-based RSS enclosure downloader
Name: castget
Version: 1.0.1
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.nongnu.org/castget/

Source: http://savannah.nongnu.org/download/castget/castget-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel, libxml2-devel, id3lib-devel, glib2-devel

%description
castget is a simple, command line-based RSS enclosure downloader. It is 
primarily intended for automatic, unattended downloading of podcasts. 

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
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/castget*.1*
%doc %{_mandir}/man5/castgetrc*.5*
%{_bindir}/castget
%{_libdir}/libcastget.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libcastget.h
%exclude %{_libdir}/libcastget.a
%{_libdir}/libcastget.so
%exclude %{_libdir}/*.la

%changelog
* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Mon Sep 24 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.0-1
- Updated to release 1.0.0.

* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Initial package.
