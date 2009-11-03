# $Id$
# Authority: dag
# Upstream: Aymeric Moizard <jack$atosc,org>
# Upstream: <osip$atosc,org>.

Summary: SIP implementation
Name: libosip2
Version: 2.2.0
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/osip/osip.html

Source: http://ftp.gnu.org/gnu/osip/libosip2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /sbin/ldconfig
BuildRequires: gcc-c++, autoconf, automake

%description
oSIP is an implementation of the Session Initiation Protocol as described
by the rfc3261 (wich deprecates rfc2543). This library aims to provide
multimedia and telecom software developers an easy and powerful interface
to initiate and control SIP based sessions in their applications. SIP is
an open standard replacement from IETF for H323.

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

%{__mv} -f %{buildroot}%{_mandir}/man1/osip.1  %{buildroot}%{_mandir}/man1/osip2.1

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/osip2.1*
%{_libdir}/libosip2.so.*
%{_libdir}/libosipparser2.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/osip2/
%{_includedir}/osipparser2/
%{_libdir}/libosip2.a
%{_libdir}/libosipparser2.a
%exclude %{_libdir}/libosip2.la
%exclude %{_libdir}/libosipparser2.la
%{_libdir}/libosip2.so
%{_libdir}/libosipparser2.so
%{_libdir}/pkgconfig/libosip2.pc

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.2.0-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 23 2005 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Initial package. (using DAR)
