# $Id: xplanet.spec,v 1.1 2004/03/01 20:08:05 driesve Exp $

# Authority: dries

# todo: figure out what to do with the extra maps
# nice to have, but the src rpm gets really big
# rpm is not uploaded yet

# NeedsCleanup

Summary: todo
Name: xplanet
Version: 1.0.3
Release: 1
License: GPL
Group: Amusements/Graphics
URL: http://xplanet.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://prdownloads.sourceforge.net/xplanet/%{name}-%{version}.tar.gz
# from http://flatplanet.sourceforge.net/maps/
Source1: http://prdownloads.sourceforge.net/flatplanet/maps_abstract-1.0.tar.gz
Source2: http://prdownloads.sourceforge.net/flatplanet/maps_alien-1.0.tar.gz
Source3: http://prdownloads.sourceforge.net/flatplanet/maps_data-1.0.tar.gz
Source4: http://prdownloads.sourceforge.net/flatplanet/maps_historical-1.0.tar.gz
Source5: http://prdownloads.sourceforge.net/flatplanet/maps_natural-1.0.tar.gz
Source6: http://prdownloads.sourceforge.net/flatplanet/maps_night-1.0.tar.gz
Source7: http://prdownloads.sourceforge.net/flatplanet/maps_topo-1.0.tar.gz


BuildRoot: %{_tmppath}/root-%{name}-%{version}
BuildRequires: netpbm-devel

#(d) primscreenshot: todo
#(d) screenshotsurl: todo

%description
todo

%prep
%{__rm} -rf "${RPM_BUILD_ROOT}"
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
export DESTDIR=$RPM_BUILD_ROOT
%{__make} install-strip

%files
%defattr(-,root,root, 0755)
%doc README AUTHORS README.config NEWS TODO
%{_bindir}/xplanet
/usr/share/man/man1/xplanet.1.gz
/usr/share/xplanet/arcs/constellations
/usr/share/xplanet/config/default
/usr/share/xplanet/config/earth_markers
/usr/share/xplanet/config/moon_orbit
/usr/share/xplanet/config/overlay_clouds
/usr/share/xplanet/ephemeris/README
/usr/share/xplanet/fonts/FreeMonoBold.ttf
/usr/share/xplanet/fonts/README
/usr/share/xplanet/images/README
/usr/share/xplanet/images/earth.jpg
/usr/share/xplanet/images/hubble.png
/usr/share/xplanet/images/iss.png
/usr/share/xplanet/images/night.jpg
/usr/share/xplanet/images/shuttle.png
/usr/share/xplanet/images/smile.png
/usr/share/xplanet/images/sublunar.png
/usr/share/xplanet/images/subsolar.png
/usr/share/xplanet/markers/brightStars
/usr/share/xplanet/markers/earth
/usr/share/xplanet/markers/mars
/usr/share/xplanet/markers/moon
/usr/share/xplanet/origin/README
/usr/share/xplanet/origin/cassini
/usr/share/xplanet/origin/galileo
/usr/share/xplanet/rgb.txt
/usr/share/xplanet/satellites/iss
/usr/share/xplanet/satellites/iss.tle
/usr/share/xplanet/scripts/convertCassini.perl
/usr/share/xplanet/scripts/convertCassini2.perl
/usr/share/xplanet/stars/BSC


%changelog
* Wed Jan 28 2004 Dries Verachtert <dries@ulyssis.org> 1.0.3-1
- first packaging for Fedora Core 1

