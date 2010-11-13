# $Id$
# Authority: dag

### EL6 ships with libfprint-0.1.0-19.pre2.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Tool kit for fingerprint scanner
Name: libfprint
Version: 0.0.6
Release: 1%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://www.reactivated.net/fprint/wiki/Main_Page

Source: http://dl.sf.net/fprint/libfprint-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ImageMagick-devel
BuildRequires: doxygen
BuildRequires: glib2-devel
BuildRequires: libusb-devel
BuildRequires: openssl-devel 

%description
libfprint offers support for consumer fingerprint reader devices.

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
%configure --disable-static 
%{__make} %{?_smp_mflags}
%{__make} -C doc docs

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS TODO THANKS
%{_libdir}/libfprint.so.*

%files devel
%defattr(-, root, root, 0755)
%doc HACKING doc/html/
%{_includedir}/libfprint/
%{_libdir}/libfprint.so
%{_libdir}/pkgconfig/libfprint.pc
%exclude %{_libdir}/libfprint.la

%changelog
* Fri Dec 19 2008 Dag Wieers <dag@wieers.com> - 0.0.6-1
- Initial package. (using DAR)
