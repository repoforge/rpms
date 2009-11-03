# $Id: loudmouth.spec 4303 2006-04-18 22:05:03Z dries $
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh7:%define _without_gnutls 1}
%{?el2:%define _without_gnutls 1}

%{?rh7:%define _without_gtkdoc 1}
%{?el2:%define _without_gtkdoc 1}

Summary: Jabber programming library written in C
Name: loudmouth
Version: 0.16
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.loudmouth-project.org/

Source: http://ftp.imendio.com/pub/imendio/loudmouth/src/loudmouth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: glib2-devel >= 2.0, libidn-devel, check-devel
%{!?_without_gtkdoc:BuildRequires: gtk-doc >= 0.10}
%{!?_without_gnutls:BuildRequires: gnutls-devel}
%{?_without_gnutls:BuildRequires: openssl-devel}

%description
Loudmouth is a lightweight and easy-to-use C library for programming with
the Jabber protocol. It's designed to be easy to get started with and yet
extensible to let you do anything the Jabber protocol allows.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel, libidn-devel
%{!?_without_gnutls:Requires: gnutls-devel}
%{?_without_gnutls:Requires: openssl-devel}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure \
%{!?_without_gtkdoc:--enable-gtk-doc} \
	--enable-static="no" \
%{!?_without_gnutls:--with-ssl="gnutls"} \
%{?_without_gnutls:--with-ssl="openssl"}
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
%doc ChangeLog COPYING NEWS README
%{_libdir}/libloudmouth-1.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_datadir}/gtk-doc/html/loudmouth/
%{_libdir}/libloudmouth-1.so
%{_libdir}/pkgconfig/loudmouth-1.0.pc
%{_includedir}/loudmouth-1.0/
%exclude %{_libdir}/libloudmouth-1.la

%changelog
* Thu Apr 29 2004 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 0.15.1-1
- Initial packahe. (using DAR)
