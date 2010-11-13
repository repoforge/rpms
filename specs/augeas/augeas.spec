# $Id$
# Authority: dag

### EL6 ships with augeas-0.7.2-3.el6
# ExclusiveDist: el2 el3 el4 el5

Summary: Configuration API and editing tool
Name: augeas
Version: 0.2.2
Release: 1%{?dist}
License: LGPL
Group: System Environment/Base
URL: http://augeas.net/

Source: http://augeas.net/download/augeas-%{version}.tar.gz
Patch0: augeas-0.2.2-const.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel
Requires: augeas-libs = %{version}-%{release}

%description
Augeas is a configuration API and editing tool. It parses common configuration
files like /etc/hosts or /etc/grub.conf in their native formats and transforms
them into a tree. Configuration changes are made by manipulating this tree and
saving it back into native configuration files. 

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
%patch0 -p0

%build
%configure --disable-static
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
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man1/augtool.1*
%doc %{_mandir}/man1/augparse.1*
%{_bindir}/augtool
%{_bindir}/augparse
%{_datadir}/augeas/
%{_libdir}/libaugeas.so.*
%{_libdir}/libfa.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/augeas.h
%{_includedir}/fa.h
%{_libdir}/libaugeas.so
%{_libdir}/libfa.so
%{_libdir}/pkgconfig/augeas.pc
%exclude %{_libdir}/libaugeas.la
%exclude %{_libdir}/libfa.la

%changelog
* Sun Jul 20 2008 Dag Wieers <dag@wieers.com> - 0.2.2-1
- Initial package. (using DAR)
