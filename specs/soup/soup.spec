# $Id$
# Authority: matthias

Summary: SOAP (Simple Object Access Protocol) implementation
Name: soup
Version: 0.7.11
Release: 1%{?dist}
License: GPL/LGPL
Group: System Environment/Libraries
URL: http://www.gnome.org/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/soup/0.7/soup-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libxml2-devel, glib2-devel, openssl-devel, popt, zlib-devel
BuildRequires: gtk-doc

%description
Soup is a SOAP (Simple Object Access Protocol) implementation in C.

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.


%package devel
Summary: Development libraries, header files and utilities for soup
Group: Development/Libraries
Requires: %{name} = %{version}, libxml2-devel, glib2-devel

%description devel
Soup is a SOAP (Simple Object Access Protocol) implementation in C.

It provides an queued asynchronous callback-based mechanism for sending and
servicing SOAP requests, and a WSDL (Web Service Definition Language) to C
compiler which generates client stubs and server skeletons for easily calling
and implementing SOAP methods.

This package contains the files necessary to develop applications with soup.


%prep
%setup

%build
%configure --enable-glib2
# Parallel compilation is broken (From the Mandrake spec file)
%{__make}


%install
%{__rm} -rf %{buildroot}
%makeinstall


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/soup-httpd
%{_bindir}/soup-ssl-proxy
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/*
%{_bindir}/soup-config
%{_bindir}/soup-wsdl
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.sh
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*


%changelog
* Mon May 10 2004 Matthias Saou <http://freshrpms.net/> 0.7.11-1
- Spec file changes for Fedora Core.

* Wed May  7 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 0.7.11-2mdk
- fix BuildRequires
- mklibnamification

* Fri Feb  7 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.11-1mdk
- Release 0.7.11

* Thu Jan 16 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.10-2mdk
- Rebuild against latest openssl

* Mon Dec 16 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.10-1mdk
- Release 0.7.10

* Thu Nov 14 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.9-1mdk
- Release 0.7.9

* Wed Nov  6 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.4-1mdk
- Initial Mandrake package

