# $Id$

# Authority: dag

%define rname clock-desklet

Summary: Clock sensor and display for gdesklets
Name: gdesklets-clock
Version: 0.32
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.pycage.de/download/gdesklets/%{rname}-%{version}.tar.bz2
Source1: Makefile_install_scripts.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: gdesklets
Requires: gdesklets

%description
The clock sensor with various clock displays.

To add the display, use:

	gdesklets-add-[gnomeclock/osXclock/plainclock/pocket-watch/rafclock]-display

%prep
%setup -n %{rname}-%{version} -a 1

%build
%{__make} \
	PACKAGE_NAME="Clock"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PACKAGE_NAME="Clock"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_datadir}/gdesklets/Displays/*
%{_datadir}/gdesklets/Sensors/*

%changelog
* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.32-0
- Initial package. (using DAR)
