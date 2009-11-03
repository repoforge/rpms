# $Id$
# Authority: dag

Summary: MSWord 6/7/8/9 binary file format to HTML converter
Name: wv
Version: 1.0.3
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://wvware.sourceforge.net/

Source: http://dl.sf.net/wvware/wv-%{version}.tar.gz
Patch5: wv-1.0.0-rhbug150461.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib2-devel
BuildRequires: ImageMagick-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libole2-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig

Provides: wvware = %{version}-%{release}

%description
wv is a program that understands the Microsoft Word 6/7/8/9 binary file
format and is able to convert Word documents into HTML, which can then
be read with a browser.

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
%patch5 -p1 -b .printf-rhbug150461

%build
%configure \
    --disable-static \
    --with-exporter \
    --with-libxml2
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man1/wv*.1*
%{_bindir}/wv*
%{_datadir}/wv/
%{_libdir}/libwv-1.0.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/wv/
%{_libdir}/libwv.so
%{_libdir}/pkgconfig/wv-1.0.pc
%exclude %{_libdir}/libwv.la

%changelog
* Mon Mar 17 2008 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Initial package. (using DAR)
