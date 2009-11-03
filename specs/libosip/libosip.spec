# $Id$
# Authority: dag
# Upstream: Aymeric Moizard <jack$atosc,org>
# Upstream: <osip$atosc,org>.

Summary: SIP implementation
Name: libosip
Version: 0.9.7
Release: 1.2%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.gnu.org/software/osip/osip.html

Source: http://ftp.gnu.org/gnu/osip/libosip-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /sbin/ldconfig

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

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO
%doc %{_mandir}/man1/osip.1*
%{_libdir}/libfsmtl.so.*
%{_libdir}/libosip.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/osip/
%{_libdir}/libfsmtl.a
%{_libdir}/libosip.a
%exclude %{_libdir}/libfsmtl.la
%exclude %{_libdir}/libosip.la
%{_libdir}/libfsmtl.so
%{_libdir}/libosip.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.9.7-1.2
- Rebuild for Fedora Core 5.

* Sun Mar 13 2005 Dag Wieers <dag@wieers.com> - 0.9.7-1
- Initial package. (using DAR)
