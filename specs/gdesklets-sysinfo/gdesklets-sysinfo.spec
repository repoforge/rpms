# $Id$

# Authority: dag

%define rname SysInfo

Summary: SysInfo sensor and display for gdesklets.
Name: gdesklets-sysinfo
Version: 0.21.2
Release: 0
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.pycage.de/download/gdesklets/%{rname}-%{version}.tar.bz2
Source1: Makefile_install_scripts.tar.bz2
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: gdesklets
Requires: gdesklets

%description
SysInfo for gDeskletes shows various system informations.

To add the display, use :

	gdesklets-add-sysinfo-display

%prep
%setup -n %{rname}-%{version} -a 1

%build
%{__make} \
	PACKAGE_NAME="SysInfo"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PACKAGE_NAME="SysInfo"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_datadir}/gdesklets/Displays/*
%{_datadir}/gdesklets/Sensors/*

%changelog
* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.22.1-0
- Initial package. (using DAR)
