# $Id$

# Authority: dag
# Upstream: Anthony Tekatch <anthony@unihedron.com>

Summary: Units conversion utility.
Name: gonvert
Version: 0.1.10
Release: 1
License: GPL
Group: Applications/Engineering
URL: http://unihedron.com/projects/gonvert/gonvert.php

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.unihedron.com/projects/gonvert/downloads/gonvert-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: python >= 1.5, pygtk2-devel >= 2.0, libglade >= 0.13, gnome-libs >= 1.2.4
Requires: python >= 1.5, pygtk2 >= 2.0, libglade >= 0.13, gnome-libs >= 1.2.4

%description
gonvert is a conversion utility that allows conversion between many units 
like CGS, Ancient, Imperial with many categories like length, mass, numbers, 
etc. All units converted values shown at once as you type. Easy to add/change 
your own units.

%prep 
%setup

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=Gonvert Unit Conversion
Comment=Convert various units
Exec=gonvert
Terminal=false
Type=Application
Icon=gonvert_icon.png
Categories=GNOME;Application;Utility
EOF

%build 
%{__make} %{?_smp_mflags}

%install 
%{__rm} -rf %{buildroot}
%makeinstall \
	DESTDIR="%{buildroot}"

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-, root, root, 0755) 
%doc doc/*
%{_bindir}/*
%{_libdir}/*
%{_datadir}/gnome/apps/Utilities/*.desktop
%{_datadir}/pixmaps/*

%changelog 
* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 0.1.10-1
- Updated to release 0.1.10.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 0.1.7-1
- Swapped pygtk requirement by pygtk2. (Paolo Dona)

* Mon Jan 26 2004 Dag Wieers <dag@wieers.com> - 0.1.7-0
- Updated to release 0.1.7.

* Sat Jun 29 2003 Dag Wieers <dag@wieers.com> - 0.1.6-0
- Updated to release 0.1.6.

* Wed Feb 26 2003 Dag Wieers <dag@wieers.com> - 0.1.5-0
- Initial package. (using DAR)
