# $Id$
# Authority: dag

%define real_name starterbar-desklet

Summary: Starterbar sensor and display for gdesklets
Name: gdesklets-starterbar
Version: 0.31.2
Release: 1.2%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Source: http://gdesklets.gnomedesktop.org/files/starterbar-desklet-%{version}.tar.bz2
#Source: http://www.pycage.de/download/gdesklets/starterbar-desklet-%{version}.tar.bz2
Source1: Makefile_install_scripts.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: gdesklets
Requires: gdesklets, gnome-python2-gnomevfs

%description
An icon bar for GNOME where you can put starters into. Yes, you can do
the same with the GNOME panel, but this one is pure eye candy!

To add the display, use :

	gdesklets-add-starterbar-display

%prep
%setup -n %{real_name}-%{version} -a 1

%build
%{__make} \
	PACKAGE_NAME="StarterBar"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	PACKAGE_NAME="StarterBar"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_datadir}/gdesklets/Displays/*
#%{_datadir}/gdesklets/Sensors/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.31.2-1.2
- Rebuild for Fedora Core 5.

* Sun Jan 02 2005 Dag Wieers <dag@wieers.com> - 0.31.2-1
- Updated to release 0.31.2.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 0.22.1-0
- Initial package. (using DAR)
