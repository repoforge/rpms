# $Id$
# Authority: dag

%define real_name WifiScanner

Summary: Discover wireless clients and access points
Name: wifiscanner
Version: 0.9.5
Release: 1
License: GPL
Group: Applications/Internet
URL: http://wifiscanner.sf.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source:  http://dl.sf.net/wifiscanner/WifiScanner-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
%find_lang %{name}

#%{__install} -d -m0755 %{buildroot}%{_datadir}/applications
#desktop-file-install --vendor gnome                \
#	--add-category X-Red-Hat-Base              \
#	--add-category Application                 \
#	--add-category AudioVideo                  \
#	--dir %{buildroot}%{_datadir}/applications \
#	gnome-%{name}.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUG-REPORT-ADDRESS ChangeLog COPYING FAQ NEWS README THANKS TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop

%changelog
* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 0.9.5-1
- Updated to release 0.9.5.

* Fri May 28 2004 Dag Wieers <dag@wieers.com> - 0.9.4-1
- Updated to release 0.9.4.

* Mon Mar 22 2004 Dag Wieers <dag@wieers.com> - 0.9.3-1
- Updated to release 0.9.3.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 0.9.1-0
- Initial package. (using DAR)
