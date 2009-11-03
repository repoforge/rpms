# $Id$
# Authority: dag

%define real_name SysInfo

Summary: SysInfo sensor and display for gdesklets
Name: gdesklets-sysinfo
Version: 0.26
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Source: http://www.pycage.de/download/gdesklets/SysInfo-%{version}.tar.gz
Source1: Makefile_install_scripts.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gdesklets
Requires: gdesklets

%description
SysInfo for gDeskletes shows various system informations.

To add the display, use :

	gdesklets-add-sysinfo-display

%prep
%setup -n %{real_name}

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
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.26-1.2
- Rebuild for Fedora Core 5.

* Thu May 27 2004 Dag Wieers <dag@wieers.com> - 0.26.2-1
- Updated to release 0.26.2.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.22.1-0
- Initial package. (using DAR)
