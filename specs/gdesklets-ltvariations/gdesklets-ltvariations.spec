# Authority: dag

%define rname LTVariations

Summary: A set of different sensors and displays for gdesklets.
Name: gdesklets-ltvariations
Version: 0.21
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.pycage.de/download/gdesklets/%{rname}-%{version}.tgz
Source1: Makefile_install_scripts.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: gdesklets
Requires: gdesklets, gnome-python2-gnomevfs

%description
LTVariations is set of different sensors and displays for gdesklets.

To add the display, use :

	gdesklets-add-GoodWeather-display

%prep
%setup -c %{rname} -a 1

%build
%{__make} \
	PACKAGE_NAME="LTVariations"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PACKAGE_NAME="LTVariations"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_datadir}/gdesklets/Displays/*
%{_datadir}/gdesklets/Sensors/*

%changelog
* Fri Dec 05 2003 Dag Wieers <dag@wieers.com> - 0.21-0
- Initial package. (using DAR)
