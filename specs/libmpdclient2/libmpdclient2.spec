# $Id$
# Authority: shuff
# Upstream: Max Kellermann <max$duempel,org>

%define real_name libmpdclient

Summary: MPD client API
Name: libmpdclient2
Version: 2.1
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.musicpd.org/doc/libmpdclient/

Source: http://downloads.sourceforge.net/project/musicpd/libmpdclient/%{version}/libmpdclient-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make autoconf, automake
BuildRequires: doxygen
BuildRequires: glibc-devel
BuildRequires: libtool
BuildRequires: pkgconfig

%description
A stable, documented, asynchronous API library for interfacing MPD in the C,
C++ & Objective C languages.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}


%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__mkdir} libmpdclient2-doc
%{__mv} %{buildroot}%{_docdir}/libmpdclient/* libmpdclient2-doc
%{__rm} -rf %{buildroot}/%{_docdir}/libmpdclient

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL NEWS README
%doc libmpdclient2-doc/*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%exclude %{_libdir}/*.la

%changelog
* Thu Mar 25 2010 Steve Huff <shuff@vecna.org> - 2.1-1
- Initial package.
