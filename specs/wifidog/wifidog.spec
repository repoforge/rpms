# $Id$
# Authority: dag

Summary: Captive portal solution for wireless hotspots
Name: wifidog
Version: 1.1.2
Release: 1.2%{?dist}
License: GPL
Group: Applications/System
Source: http://dl.sf.net/wifidog/wifidog-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++

%description
The WiFi Guard Dog project is a complete and embeedable captive portal
solution for wireless community groups or individuals who wish to open
a free HotSpot while still preventing abuse of their Internet connection.

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
%{__make} install DESTDIR="%{buildroot}"

%{__install} -D -m0644 wifidog.conf %{buildroot}%{_sysconfdir}/wifidog.conf
%{__install} -D -m0755 scripts/init.d/wifidog %{buildroot}%{_initrddir}/wifidog

### FIXME: Register wifidog using chkconfig and (re)start, check sysv script
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README doc/html
%config(noreplace) %{_sysconfdir}/wifidog.conf
%config %{_initrddir}/wifidog
%{_bindir}/wdctl
%{_bindir}/wifidog
%{_libdir}/libhttpd.so.*
%{_includedir}/wifidog/

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libhttpd.a
%exclude %{_libdir}/libhttpd.la
%{_libdir}/libhttpd.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1.2-1.2
- Rebuild for Fedora Core 5.

* Tue Jan 31 2006 Dag Wieers <dag@wieers.com> - 1.1.2-1
- Initial package. (using DAR)
