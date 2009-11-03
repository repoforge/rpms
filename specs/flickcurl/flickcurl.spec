# $Id$
# Authority: dries
# Upstream: Dave Beckett

Summary: C library for the Flickr API and utility programs
Name: flickcurl
Version: 1.3
Release: 1%{?dist}
License: LGPL 2.1 / GPL 2 / Apache 2.0
Group: Development/Libraries
URL: http://librdf.org/flickcurl/

Source: http://download.dajobe.org/flickcurl/flickcurl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: curl-devel, libxml2-devel

%description
Flickcurl is a C library for the Flickr API, handling creating the requests, 
signing, token management, calling the API, marshalling request parameters 
and decoding responses. It uses libcurl to call the REST web service and 
libxml2 to manipulate the XML responses.

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
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%doc %{_mandir}/man1/flick*.1*
%{_bindir}/flickcurl
%{_bindir}/flickrdf
%{_libdir}/libflickcurl.so.*
%{_libdir}/pkgconfig/flickcurl.pc

%files devel
%{_bindir}/flickcurl-config
%{_includedir}/flickcurl.h
%{_libdir}/libflickcurl.so
%{_datadir}/gtk-doc/html/flickcurl/
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%changelog
* Sun Jun  1 2008 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Initial package.
