# $Id$

# Authority: dag

%define real_name LTVariations

Summary: set of different sensors and displays for gdesklets
Name: gdesklets-ltvariations
Version: 0.21
Release: 0.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Source: http://www.pycage.de/download/gdesklets/%{real_name}-%{version}.tgz
Source1: Makefile_install_scripts.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: gdesklets
Requires: gdesklets, gnome-python2-gnomevfs

%description
LTVariations is set of different sensors and displays for gdesklets.

To add the display, use :

	gdesklets-add-GoodWeather-display

%prep
%setup -c %{real_name} -a 1

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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.21-0.2
- Rebuild for Fedora Core 5.

* Fri Dec 05 2003 Dag Wieers <dag@wieers.com> - 0.21-0
- Initial package. (using DAR)
