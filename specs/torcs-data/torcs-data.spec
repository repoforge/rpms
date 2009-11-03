# $Id$
# Authority: matthias
# Dist: nodist

Summary: The Open Racing Car Simulator data files
Name: torcs-data
Version: 1.2.4
Release: 1%{?dist}
License: GPL and Free Art License
Group: Amusements/Games
URL: http://torcs.org/
Source0: http://dl.sf.net/torcs/TORCS-%{version}-data.tgz
Source1: http://dl.sf.net/torcs/TORCS-%{version}-data-tracks-dirt.tgz
Source2: http://dl.sf.net/torcs/TORCS-%{version}-data-tracks-oval.tgz
Source3: http://dl.sf.net/torcs/TORCS-%{version}-data-tracks-road.tgz
Source4: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-extra.tgz
Source5: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-nascar.tgz
Source90: Free-Art-License
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: torcs, %{name}-tracks-road = %{version}
BuildArch: noarch

%description
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains the data files needed to run the game.


%package tracks-dirt
Summary: The Open Racing Car Simulator additional dirt tracks
Group: Amusements/Games
Requires: torcs

%description tracks-dirt
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional tracks for the game.


%package tracks-oval
Summary: The Open Racing Car Simulator additional oval tracks
Group: Amusements/Games
Requires: torcs

%description tracks-oval
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional tracks for the game.


%package tracks-road
Summary: The Open Racing Car Simulator additional road tracks
Group: Amusements/Games
Requires: torcs

%description tracks-road
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional tracks for the game.


%package cars-extra
Summary: The Open Racing Car Simulator additional cars
Group: Amusements/Games
Requires: torcs

%description cars-extra
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional cars for the game.


%package cars-nascar
Summary: The Open Racing Car Simulator additional NASCAR cars
Group: Amusements/Games
Requires: torcs

%description cars-nascar
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional cars for the game.


%prep
%setup -T -c %{name}-%{version}
# Uncompress all packages in a separate tree
for source in %{SOURCE0} %{SOURCE1} %{SOURCE2} \
              %{SOURCE3} %{SOURCE4} %{SOURCE5}; do
    package="`basename ${source} .tgz | sed 's/TORCS-%{version}-//g'`"
    mkdir -p ${package}%{_datadir}/games/torcs/
    ( cd ${package}%{_datadir}/games/torcs/
        tar xzf %{_sourcedir}/TORCS-%{version}-${package}.tgz )
    echo ${package} >> package.list
done


%build
# List each package's files
for package in `cat package.list`; do
    ( cd ${package}
      find .%{_datadir}/games/torcs -type d \
          | sed s/^./\%dir\ / > ../${package}.files
      find .%{_datadir}/games/torcs -type f \
          | sed s/^.// >> ../${package}.files )
done


%install
%{__rm} -rf %{buildroot}
# Install all trees into the main build root
mkdir -p %{buildroot}
for package in `cat package.list`; do
    cp -a ${package}/* %{buildroot}/
done
# Prepare Free-Art-License for doc inclusion
%{__install} -m 0644 %{SOURCE90} .


%clean
%{__rm} -rf %{buildroot}


%files -f data.files
%defattr(-, root, root, 0755)
%doc Free-Art-License


%files tracks-dirt -f data-tracks-dirt.files
%defattr(-, root, root, 0755)
%doc Free-Art-License


%files tracks-oval -f data-tracks-oval.files
%defattr(-, root, root, 0755)
%doc Free-Art-License


%files tracks-road -f data-tracks-road.files
%defattr(-, root, root, 0755)
%doc Free-Art-License


%files cars-extra -f data-cars-extra.files
%defattr(-, root, root, 0755)
%doc Free-Art-License


%files cars-nascar -f data-cars-nascar.files
%defattr(-, root, root, 0755)
%doc Free-Art-License


%changelog
* Wed Oct 12 2005 Matthias Saou <http://freshrpms.net/> 1.2.4-1
- Update to 1.2.4.

* Wed Aug  3 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-3
- Replace default tracks requirement (provided by all 3 tracks sub-packages)
  by tracks-road since those are the ones required for a quick race, and yum
  was installing the first available (alphabetically?) package, tracks-dirt.
- Remove now unused virtual provides of tracks sub-packages.

* Mon Feb 28 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-2
- Change %%doc and %%defattr order to fix wrong ownership of doc files.

* Fri Feb 11 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Change License: to "GPL and Free Art License" (#147681).
- Include Free-Art-License and add a copy to each sub-package.

* Mon Feb  7 2005 Matthias Saou <http://freshrpms.net/> 1.2.3-1
- Update to 1.2.3.
- Removed "non-free" cars (kcendra ones, Patwo-Design and VM).

* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1
- Update to 1.2.2
- Added all new tracks : dirt, oval and road.
- Added all new cars : kcendra-gt, kcendra-roadsters, kcendra-sport, nascar
  and VM.
- Updated the %%setup and %%build sections to make them even more flexible.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.2.1-4
- Rebuild for Fedora Core 1.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added a requires on torcs for all packages.

* Mon Apr 28 2003 Matthias Saou <http://freshrpms.net/>
- Fixed the defattr problem, doh!

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

