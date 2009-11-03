%define rname RDGBorder

Summary: Resizable border sensor, designed to replace LTVBorder.
Name: gdesklets-rdgborder
Version: 0.2
Release: 0%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Source0: %{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gdesklets, gnome-python2-gnomevfs

%description
A resizable border sensor, designed to replace LTVBorder.

%prep
%setup -n %{rname}-%{version}

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_datadir}/gdesklets/RDGThemes
%{__mkdir} -p %{buildroot}%{_datadir}/gdesklets/Sensors
%{__mkdir} -p %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}
./Install_RDGBorder_Sensor.bin %{buildroot}%{_datadir}/gdesklets/Sensors
./Install_bluegrey_RDGTheme.bin %{buildroot}%{_datadir}/gdesklets/RDGThemes
./Install_scooby_RDGTheme.bin %{buildroot}%{_datadir}/gdesklets/RDGThemes
%{__install} -p -m0644 *.display %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_datadir}/gdesklets/RDGThemes/*
%{_datadir}/gdesklets/Sensors/*
%{_datadir}/gdesklets/Displays/*

%changelog
* Sun Apr 25 2004 Andre Costa <acosta@ar.microlink.com.br>
- Initial RPM release.
