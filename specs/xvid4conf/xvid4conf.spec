# $Id$
# Authority: matthias

%define desktop_vendor rpmforge

Summary: Tool to create XviD configuration files
Name: xvid4conf
Version: 1.12
Release: 2%{?dist}
License: GPL
Group: Applications/Multimedia
URL: http://www.exit1.org/archive/dvdrip-users/2005-07/msg00007.html
Source0: http://nexus.tfh-berlin.de/~t2/source/2.1/x/xvid4conf-%{version}.tar.bz2
Source1: xvid4conf.png
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel, desktop-file-utils

%description
This tool creates XviD configuration files. The generated configuration file
is meant to be read by transcode's xvid4 export module. This module (and so
the configuration file) is intended to be used with at least XviD 1.0.


%prep
%setup
# Create the desktop file
%{__cat} > xvid4conf.desktop << EOF
[Desktop Entry]
Name=XviD Configurator
Comment=Create XviD configuration files to use with transcode and dvd::rip
Exec=xvid4conf
Icon=xvid4conf.png
Terminal=false
Type=Application
Categories=Application;AudioVideo;
EOF


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall

# Install the desktop file
desktop-file-install \
    --vendor %{desktop_vendor} \
    --dir %{buildroot}%{_datadir}/applications \
    xvid4conf.desktop

# Icon for the desktop file
%{__install} -D -p -m 0644 %{SOURCE1} \
    %{buildroot}%{_datadir}/pixmaps/xvid4conf.png


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/xvid4conf
%{_datadir}/applications/%{desktop_vendor}-xvid4conf.desktop
%{_datadir}/pixmaps/xvid4conf.png


%changelog
* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.12-2
- Release bump to drop the disttag number in FC5 build.

* Mon Jan  9 2006 Matthias Saou <http://freshrpms.net/> 1.12-1
- Initial RPM release.

