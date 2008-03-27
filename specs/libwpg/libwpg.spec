# $Id$
# Authority: dag

Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images
Name: libwpg
Version: 0.1.2
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://libwpg.sourceforge.net/

Source: http://dl.sf.net/libwpg/libwpg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libwpd-devel >= 0.8.0, gcc-c++, libstdc++-devel, pkgconfig

%description
libwpg is a library for importing and converting Corel WordPerfect(tm)
Graphics images.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: libwpd-devel >= 0.8.0

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package tools
Summary: Tools to transform WordPerfect Graphics into other formats
Group: Applications/Publishing

%description tools
Tools to transform WordPerfect Graphics into other formats.

%prep
%setup

%build
%configure \
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
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libwpg-0.1.so.*
%{_libdir}/libwpg-stream-0.1.so.*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/wpg2raw
%{_bindir}/wpg2svg
%{_bindir}/wpg2svgbatch.pl

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libwpg-0.1/
%{_libdir}/libwpg-0.1.so
%{_libdir}/libwpg-stream-0.1.so
%{_libdir}/pkgconfig/libwpg-0.1.pc
%{_libdir}/pkgconfig/libwpg-stream-0.1.pc
%exclude %{_libdir}/libwpg-0.1.la
%exclude %{_libdir}/libwpg-stream-0.1.la

%changelog
* Wed Mar 26 2008 Dag Wieers <dag@wieers.com> - 0.1.2-1
- Initial package. (using DAR)
