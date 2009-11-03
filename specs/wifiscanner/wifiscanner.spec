# $Id$
# Authority: dag


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

%define real_name WifiScanner

Summary: Discover wireless clients and access points
Name: wifiscanner
Version: 1.0.2a
Release: 1%{?dist}
License: GPL
Group: Applications/Internet
URL: http://wifiscanner.sourceforge.net/

Source: http://dl.sf.net/wifiscanner/WifiScanner-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libpcap, glib-devel, gcc-c++, bison, flex, glib2-devel
BuildRequires: ncurses-devel
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}

%description
WifiScanner is a tool to discover wireless clients and access points.

%prep
%setup -n %{real_name}-%{version}

%build
%configure \
	--disable-dependency-tracking \
#	--with-linux-wlan-ng="%{_builddir}/linux-wlan-ng-0.2.0"
#	--with-linux="/lib/modules/2.4.20-19.9/build"
#	--with-linux-include="/lib/modules/2.4.20-19.9/build/include"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUG-REPORT-ADDRESS ChangeLog COPYING FAQ NEWS README THANKS TODO
%doc %{_mandir}/man1/wifiscanner.1*
%{_sbindir}/wifiscanner
%exclude %{_libdir}/libwiretap.a
%exclude %{_libdir}/libwiretap.la

%changelog
* Fri Feb 16 2007 Dag Wieers <dag@wieers.com> - 1.0.2a-1
- Updated to release 1.0.2a.

* Thu Nov 04 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.1-1
- Updated to release 1.0.1.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.9.6-1
- Updated to release 0.9.6.

* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Fri May 28 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Initial package. (using DAR)
