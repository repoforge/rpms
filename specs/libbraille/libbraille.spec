# $Id$
# Authority: dries
# Upstream: Sébastien Sablé <sable$users,sf,net>

Summary: Easy access to Braille displays and terminals
Name: libbraille
Version: 0.19.0
Release: 1.2%{?dist}
License: LGPL
Group: Development/Libraries
URL: http://libbraille.sourceforge.net/

Source: http://dl.sf.net/libbraille/libbraille-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++, libusb-devel >= 0.1.8

%description
This library makes it possible to easily access Braille displays and
terminals : you can write text on the braille display, directly draw braille
dots, or get the value of pressed keys. It is compatible with a wide range
of braille displays.

The features contain:
* usable from C, C++, Python and Java
* supports over 10 braille displays (including some recent models)
* easy configuration of the braille table
* distributed under the LGPL Free Software Licence
* portable (currently linux and win32)
* packages available
* easy to incorporate in any application wanting to use braille displays
(simple shared library)
* uses autoconf, automake and libtool for easier installation and portability
* contains a virtual graphical terminal made with Gtk+ for developers testing

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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%config(noreplace) %{_sysconfdir}/libbraille.conf
%{_bindir}/*
%{_libdir}/*.so.*
%{_libdir}/libbraille/*.so.*
%{_datadir}/libbraille

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/libbraille/*.a
%{_libdir}/*.so
%{_libdir}/libbraille/*.so
%exclude %{_libdir}/*.la
%exclude %{_libdir}/libbraille/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.19.0-1.2
- Rebuild for Fedora Core 5.

* Tue Mar 14 2006 Dries Verachtert <dries@ulyssis.org> 0.19.0-1
- Update to release 0.19.0.

* Tue Nov 30 2004 Dries Verachtert <dries@ulyssis.org> 0.18.0-1
- Update to release 0.18.0.

* Mon Nov 08 2004 Dries Verachtert <dries@ulyssis.org> 0.17.0-1
- Update to release 0.17.0.

* Mon Oct 25 2004 Dries Verachtert <dries@ulyssis.org> 0.16.0-1
- Update to release 0.16.0.

* Wed Sep 01 2004 Dries Verachtert <dries@ulyssis.org> 0.15.0-1
- Update to version 0.15.0.

* Fri Jul 30 2004 Dries Verachtert <dries@ulyssis.org> 0.14.1-1
- Update to version 0.14.1

* Sat Apr 24 2004 Dries Verachtert <dries@ulyssis.org> 0.12.0-1
- initial package
