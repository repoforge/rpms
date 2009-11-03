# $Id$
# Authority: dag

Summary: Library for reading and converting WordPerfect(tm) documents
Name: libwpd
Version: 0.8.14
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://libwpd.sourceforge.net/

Source: http://dl.sf.net/libwpd/libwpd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel >= 2.0.0, libgsf-devel >= 1.6.0, gcc-c++, libstdc++-devel
Requires: glib2 >= 2.0.0, libgsf >= 1.6.0

%description
libwpd is a library for reading and converting WordPerfect(tm) documents.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel >= 2.0.0, libgsf-devel >= 1.6.0

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package tools
Summary: Tools to transform WordPerfect Documents into other formats
Group: Applications/Publishing

%description tools
Tools to transform WordPerfect Documents into other formats.
Currently supported: html, raw, text.

%prep
%setup

%build
%configure \
    --disable-static \
    --without-docs
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
%doc CHANGES COPYING CREDITS HACKING README TODO
%{_libdir}/libwpd-0.8.so.*
%{_libdir}/libwpd-stream-0.8.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libwpd-0.8/
%{_libdir}/libwpd-0.8.so
%{_libdir}/libwpd-stream-0.8.so
%{_libdir}/pkgconfig/libwpd-0.8.pc
%{_libdir}/pkgconfig/libwpd-stream-0.8.pc
%exclude %{_libdir}/libwpd-0.8.la
%exclude %{_libdir}/libwpd-stream-0.8.la

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/wpd2html
%{_bindir}/wpd2raw
%{_bindir}/wpd2text

%changelog
* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 0.8.14-1
- Initial package. (using DAR)
