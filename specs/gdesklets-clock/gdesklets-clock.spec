# $Id$
# Authority: dag

%define real_name clock-desklet

Summary: Clock sensor and display for gdesklets
Name: gdesklets-clock
Version: 0.40
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Source: http://gdesklets.gnomedesktop.org/files/clock-desklet-%{version}.tar.gz
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
%setup -n %{real_name}-%{version} -a 1

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
#%{_datadir}/gdesklets/Sensors/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.40-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.40-1
- Updated to release 0.40.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.32-0
- Initial package. (using DAR)
