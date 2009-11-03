%define rname diskmount

Summary: Disk mounter gdesklet.
Name: gdesklets-diskmount
Version: 0.3.1
Release: 0%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Source0: %{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gdesklets, gnome-python2-gnomevfs
Requires: gdesklets-rdgborder

%description
Allows a user to mount/unmount a drive using gdesklets.

%prep
%setup -n %{rname}-%{version}

%build
%{__cat} << EOF > gdesklets-add-%{rname}-display
#!/bin/sh

gdesklets %{_datadir}/gdesklets/Displays/%{rname}/RDGdiskmount.display
EOF

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/gdesklets/Sensors
%{__mkdir} -p %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}
./Install_diskmount_Sensor.bin %{buildroot}%{_datadir}/gdesklets/Sensors
%{__install} -m 644 *.display %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}
%{__cp} -ap gfx %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}
%{__install} -m 755 gdesklets-add-%{rname}-display %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%{_bindir}/*
%{_datadir}/gdesklets/Sensors/*
%{_datadir}/gdesklets/Displays/*

%changelog
* Sun Apr 25 2004 Andre Costa <acosta@ar.microlink.com.br>
- Initial RPM release.
