# $Id$
# Authority: shuff
# Upstream: Jakub Schroeter <js$camaya,net>

Summary: Full-featured C++ XMPP library
Name: gloox
Version: 1.0
Release: 1%{?dist}
License: Boost
Group: Applications/Internet
URL: http://camaya.net/gloox/

Source: http://camaya.net/download/gloox-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gcc-c++
BuildRequires: libidn-devel >= 0.5
BuildRequires: libtool
BuildRequires: make
BuildRequires: gnutls-devel >= 1.2
BuildRequires: openssl-devel >= 0.9.8
BuildRequires: zlib-devel >= 1.2.3
BuildRequires: rpm-macros-rpmforge

%description
gloox is a rock-solid, full-featured Jabber/XMPP client library, written in
clean ANSI C++. It makes writing spec-compliant clients easy and allows for
hassle-free integration of Jabber/XMPP functionality into existing
applications.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --disable-static
%{__make} %{?_smp_mflags}

# recode file to Unicode
%{__mv} -f AUTHORS AUTHORS.old
/usr/bin/iconv -f iso8859-1 -t UTF-8 AUTHORS.old > AUTHORS

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog LICENSE README TODO UPGRADING
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/*.la

%changelog
* Wed Aug 03 2011 Steve Huff <shuff@vecna.org> - 1.0-1
- Initial package.
