%define rname rssgrab

Summary: RSS feeds gdesklet.
Name: gdesklets-rss-grab
Version: 0.6
Release: 1%{?dist}
License: GPL
Group: User Interface/Desktops
URL: http://gdesklets.gnomedesktop.org/

Source0: %{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
Requires: gdesklets, gnome-python2-gnomevfs
Requires: gdesklets-rdgborder, gnome-python2-gnomevfs

%description
This desklet allows you to viw the contents of an RSS/RDF feed, as
supplied by various news sites and blogs all over the web.

%prep
%setup -n %{rname}-%{version}

%build
%{__cat} << EOF > gdesklets-add-%{rname}-display
#!/bin/sh

gdesklets %{_datadir}/gdesklets/Displays/%{rname}/RDGrssgrab.display
EOF

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/gdesklets/Sensors
%{__mkdir} -p %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}
./Install_rssgrab_Sensor.bin %{buildroot}%{_datadir}/gdesklets/Sensors
%{__install} -p -m0644 *.display %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}
%{__cp} -ap gfx %{buildroot}%{_datadir}/gdesklets/Displays/%{rname}
%{__install} -p -m0755 gdesklets-add-%{rname}-display %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README README.feeds
%{_bindir}/*
%{_datadir}/gdesklets/Sensors/*
%{_datadir}/gdesklets/Displays/*

%changelog
* Sun Apr 25 2004 Andre Costa <acosta@ar.microlink.com.br>
- Added dependency to RDGBorder and provided installation script

* Sun Apr 25 2004 Andre Costa <acosta@ar.microlink.com.br>
- Initial RPM release.
