# $Id$
# Authority: matthias
# Dist: nodist

Summary: Additional maps for Xplanet, the planet image rendering program
Name: xplanet-maps
Version: 1.0
Release: 2%{?dist}
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
%setup -c %{name}-%{version} -a 1 -a 2 -a 3 -a 4 -a 5 -a 6


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_datadir}
# Already included with xplanet
%{__rm} -f usr/local/share/xplanet/images/earth.jpg
%{__cp} -a usr/local/share/xplanet %{buildroot}%{_datadir}/


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(0644, root, root, 0755)
%{_datadir}/xplanet/


%changelog
* Tue Mar 16 2004 Matthias Saou <http://freshrpms.net> 1.0-2
- Remove conflicting earth.jpg file.

* Thu Mar  4 2004 Matthias Saou <http://freshrpms.net> 1.0-1
- Initial spec file.

