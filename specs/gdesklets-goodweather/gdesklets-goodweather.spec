# $Id$
# Authority: dag

%define real_name GoodWeather

Summary: GoodWeather sensor and display for gdesklets
Name: gdesklets-goodweather
Version: 0.4
Release: 1
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://gdesklets.gnomedesktop.org/files/GoodWeather-%{version}.tar.bz2
Source1: Makefile_install_scripts.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: gdesklets
Requires: gdesklets, gnome-python2-gnomevfs

%description
GoodWeather (sensor/display) shows the current temperature, humidity,
sky, windchill temperature and a forecast of the next 4 days on your
desktop. The data is retrieved from Weather XML Data Feed project at
weather.com.

To add the display, use :

	gdesklets-add-GoodWeather-display

%prep
%setup -n %{real_name} -a 1

%build
%{__make} \
	PACKAGE_NAME="GoodWeather"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PACKAGE_NAME="GoodWeather"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/gdesklets-add-GoodWeather-display
%{_datadir}/gdesklets/Displays/GoodWeather/
%{_datadir}/gdesklets/Sensors/GoodWeather/

%changelog
* Thu Aug 19 2004 Dag Wieers <dag@wieers.com> - 0.4-1
- Updated to release 0.4.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.3-0
- Initial package. (using DAR)
