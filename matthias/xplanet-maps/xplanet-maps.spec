# $Id$

Summary: Additional maps for Xplanet, the planet image rendering program
Name: xplanet-maps
Version: 1.0
Release: 1.fr
License: Distributable
Group: Amusements/Graphics
URL: http://flatplanet.sourceforge.net/maps/
Source0: http://dl.sf.net/flatplanet/maps_abstract-1.0.tar.gz
Source1: http://dl.sf.net/flatplanet/maps_alien-1.0.tar.gz
Source2: http://dl.sf.net/flatplanet/maps_data-1.0.tar.gz
Source3: http://dl.sf.net/flatplanet/maps_historical-1.0.tar.gz
Source4: http://dl.sf.net/flatplanet/maps_natural-1.0.tar.gz
Source5: http://dl.sf.net/flatplanet/maps_night-1.0.tar.gz
Source6: http://dl.sf.net/flatplanet/maps_topo-1.0.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

%description
Additional maps (surfaces) to use with Xplanet.


%prep
%setup -q -c %{name}-%{version} -a 1 -a 2 -a 3 -a 4 -a 5 -a 6


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/
cp -a usr/local/share/xplanet %{buildroot}%{_datadir}/


%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%{_datadir}/xplanet


%changelog
* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net> 1.0-1.fr
- Initial spec file.

