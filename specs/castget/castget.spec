# $Id$
# Authority: dries
# Upstream: Marius L. Jøhndal <mariuslj$ifi,uio,no>

Summary: Command line-based RSS enclosure downloader
Name: castget
Version: 0.9.6
Release: 1
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
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/castget*
%doc %{_mandir}/man5/castgetrc*
%{_bindir}/castget
%{_libdir}/libcastget.so.*

%files devel
#%defattr(-, root, root, 0755)
%{_includedir}/libcastget.h
%exclude %{_libdir}/libcastget.a
%{_libdir}/libcastget.so
%exclude %{_libdir}/*.la

%changelog
* Tue Apr 17 2007 Dries Verachtert <dries@ulyssis.org> - 0.9.6-1
- Updated to release 0.9.6.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.5-1
- Initial package.
