# $Id: torcs-data.spec,v 1.3 2004/02/27 00:11:30 thias Exp $

Summary: The Open Racing Car Simulator data files
Name: torcs-data
Version: 1.2.2
Release: 1.fr
License: GPL
Group: Amusements/Games
URL: http://torcs.org/
Source0: http://dl.sf.net/torcs/TORCS-%{version}-data.tgz
Source1: http://dl.sf.net/torcs/TORCS-%{version}-data-tracks-dirt.tgz
Source2: http://dl.sf.net/torcs/TORCS-%{version}-data-tracks-oval.tgz
Source3: http://dl.sf.net/torcs/TORCS-%{version}-data-tracks-road.tgz
Source4: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-extra.tgz
Source5: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-kcendra-gt.tgz
Source6: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-kcendra-roadsters.tgz
Source7: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-kcendra-sport.tgz
Source8: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-nascar.tgz
Source9: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-Patwo-Design.tgz
Source10: http://dl.sf.net/torcs/TORCS-%{version}-data-cars-VM.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: torcs, %{name}-tracks = %{version}
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
Provides: %{name}-tracks = %{version}-%{release}

%description tracks-dirt
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional tracks for the game.


%package tracks-oval
Summary: The Open Racing Car Simulator additional oval tracks
Group: Amusements/Games
Requires: torcs
Provides: %{name}-tracks = %{version}-%{release}

%description tracks-oval
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional tracks for the game.


%package tracks-road
Summary: The Open Racing Car Simulator additional road tracks
Group: Amusements/Games
Requires: torcs
Provides: %{name}-tracks = %{version}-%{release}

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


%package cars-kcendra-gt
Summary: The Open Racing Car Simulator additional kcendra GT cars
Group: Amusements/Games
Requires: torcs

%description cars-kcendra-gt
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional cars for the game.


%package cars-kcendra-roadsters
Summary: The Open Racing Car Simulator additional kcendra roadsters
Group: Amusements/Games
Requires: torcs

%description cars-kcendra-roadsters
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional cars for the game.


%package cars-kcendra-sport
Summary: The Open Racing Car Simulator additional kcendra sport cars
Group: Amusements/Games
Requires: torcs

%description cars-kcendra-sport
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


%package cars-Patwo-Design
Summary: The Open Racing Car Simulator addition Patwo Design cars
Group: Amusements/Games
License: Other
Requires: torcs

%description cars-Patwo-Design
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional Patwo Design cars (non free!!!).


%package cars-VM
Summary: The Open Racing Car Simulator additional VM cars
Group: Amusements/Games
Requires: torcs

%description cars-VM
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains additional cars for the game.


%prep
%setup -q -T -c %{name}-%{version}
# Uncompress all packages in a separate tree
for source in %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE6} %{SOURCE7} %{SOURCE8} %{SOURCE9} %{SOURCE10}; do
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
rm -rf %{buildroot}
# Install all trees into the main build root
mkdir -p %{buildroot}
for package in `cat package.list`; do
    cp -a ${package}/* %{buildroot}/
done


%clean
rm -rf %{buildroot}


%files -f data.files
%defattr(-, root, root)


%files tracks-dirt -f data-tracks-dirt.files
%defattr(-, root, root)


%files tracks-oval -f data-tracks-oval.files
%defattr(-, root, root)


%files tracks-road -f data-tracks-road.files
%defattr(-, root, root)


%files cars-extra -f data-cars-extra.files
%defattr(-, root, root)


%files cars-kcendra-gt -f data-cars-kcendra-gt.files
%defattr(-, root, root)


%files cars-kcendra-roadsters -f data-cars-kcendra-roadsters.files
%defattr(-, root, root)


%files cars-kcendra-sport -f data-cars-kcendra-sport.files
%defattr(-, root, root)


%files cars-nascar -f data-cars-nascar.files
%defattr(-, root, root)


%files cars-Patwo-Design -f data-cars-Patwo-Design.files
%defattr(-, root, root)


%files cars-VM -f data-cars-VM.files
%defattr(-, root, root)


%changelog
* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1.fr
- Update to 1.2.1
- Added all new tracks : dirt, oval and road.
- Added all new cars : kcendra-gt, kcendra-roadsters, kcendra-sport, nascar
  and VM.
- Updated the %%setup and %%build sections to make them even more flexible.

* Tue Nov 11 2003 Matthias Saou <http://freshrpms.net/> 1.2.1-4.fr
- Rebuild for Fedora Core 1.

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added a requires on torcs for all packages.

* Mon Apr 28 2003 Matthias Saou <http://freshrpms.net/>
- Fixed the defattr problem, doh!

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

