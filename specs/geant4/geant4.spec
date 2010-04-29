# $Id$
# Authority: shuff
# Upstream: Albert De Roeck <Albert.de.Roeck$cern,ch>

%define superdir %{_usr}/%{name}

%define G4ABLA_version 3.0
%define G4EMLOW_version 6.9
%define G4NDL_version 3.13
%define G4RadioactiveDecay_version 3.2
%define PhotonEvaporation_version 2.0
%define RealSurface_version 1.0

Summary: Toolkit for the simulation of the passage of particles through matter
Name: geant4
Version: 9.3
Release: 2%{?dist}
License: FLOSS/Other
Group: Applications/Engineering
URL: http://geant4.web.cern.ch/geant4/

Source0: http://geant4.cern.ch/support/source/%{name}.%{version}.tar.gz
Source1: http://geant4.cern.ch/support/source/G4NDL.%{G4NDL_version}.tar.gz
Source2: http://geant4.cern.ch/support/source/G4EMLOW.%{G4EMLOW_version}.tar.gz
Source3: http://geant4.cern.ch/support/source/PhotonEvaporation.%{PhotonEvaporation_version}.tar.gz
Source4: http://geant4.cern.ch/support/source/G4RadioactiveDecay.%{G4RadioactiveDecay_version}.tar.gz
Source5: http://geant4.cern.ch/support/source/G4ABLA.%{G4ABLA_version}.tar.gz
Source6: http://geant4.cern.ch/support/source/RealSurface.%{RealSurface_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#Buildarch: noarch
BuildRequires: binutils, gcc-c++, make
BuildRequires: clhep-devel >= 2.0.4.5
BuildRequires: expat-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: libdrm-devel
BuildRequires: libICE-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libSM-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXau-devel
BuildRequires: libXaw-devel
BuildRequires: libXdmcp-devel
BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: libXp-devel
BuildRequires: libXpm-devel
BuildRequires: libXrender-devel
BuildRequires: libXt-devel
BuildRequires: libXxf86vm-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: openmotif-devel
BuildRequires: setup
BuildRequires: rpm-macros-rpmforge
BuildRequires: xerces-c-devel
BuildRequires: zlib-devel
Requires: clhep >= 2.0.4.5
Requires: clhep-devel >= 2.0.4.5
Requires: expat-devel
Requires: fontconfig-devel
Requires: freetype-devel
Requires: libdrm-devel
Requires: libICE-devel
Requires: libjpeg-devel
Requires: libpng-devel
Requires: libSM-devel
Requires: libstdc++-devel
Requires: libX11-devel
Requires: libXau-devel
Requires: libXaw-devel
Requires: libXdmcp-devel
Requires: libXext-devel
Requires: libXft-devel
Requires: libXi-devel
Requires: libXmu-devel
Requires: libXp-devel
Requires: libXpm-devel
Requires: libXrender-devel
Requires: libXt-devel
Requires: libXxf86vm-devel
Requires: mesa-libGL-devel
Requires: mesa-libGLU-devel
Requires: openmotif-devel
Requires: setup
Requires: xerces-c-devel
Requires: zlib-devel

%description
Geant4 is a toolkit for the simulation of the passage of particles through
matter. Its areas of application include high energy, nuclear and accelerator
physics, as well as studies in medical and space science.

%package data
Summary: Additional data files for use with Geant4.
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}

%description data
For specific, optional physics processes some of the files in this package are
required.

%prep
%setup -n %{name}.%{version}
%{__mkdir} data
pushd data
%{__gzip} -dc %{_sourcedir}/G4NDL.%{G4NDL_version}.tar.gz | %{__tar} -xvvf -
%{__gzip} -dc %{_sourcedir}/G4EMLOW.%{G4EMLOW_version}.tar.gz | %{__tar} -xvvf -
%{__gzip} -dc %{_sourcedir}/PhotonEvaporation.%{PhotonEvaporation_version}.tar.gz | %{__tar} -xvvf -
%{__gzip} -dc %{_sourcedir}/G4RadioactiveDecay.%{G4RadioactiveDecay_version}.tar.gz | %{__tar} -xvvf -
%{__gzip} -dc %{_sourcedir}/G4ABLA.%{G4ABLA_version}.tar.gz | %{__tar} -xvvf -
%{__gzip} -dc %{_sourcedir}/RealSurface.%{RealSurface_version}.tar.gz | %{__tar} -xvvf -
popd

%build
%define config_args -d -e -r -s -O
./Configure -build %{config_args} \
    -D g4final_install=%{buildroot}%{_usr} \
    -D g4includes_flag=y \
    -D g4clhep_base_dir=%{_usr} \
    -D g4clhep_include_dir=%{_includedir} \
    -D g4clhep_lib_dir=%{_libdir} \
    -D g4clhep_lib=%{_libdir}/libCLHEP.so \
    -D g4ui_build_xaw_session=y \
    -D g4ui_build_xm_session=y \
    -D g4vis_build_openglx_driver=y \
    -D g4vis_build_openglxm_driver=y \
    -D g4vis_build_raytracerx_driver=y \
    -D g4vis_build_vrml_driver=y \
    -D g4lib_build_gdml=y 

%install
%{__rm} -rf %{buildroot}
./Configure -install %{config_args} \
    -D g4final_install=%{buildroot}%{_usr} \
    -D g4includes_flag=y \
    -D g4clhep_base_dir=%{_usr} \
    -D g4clhep_include_dir=%{_includedir} \
    -D g4clhep_lib_dir=%{_libdir} \
    -D g4clhep_lib=%{_libdir}/libCLHEP.so \
    -D g4ui_build_xaw_session=y \
    -D g4ui_build_xm_session=y \
    -D g4vis_build_openglx_driver=y \
    -D g4vis_build_openglxm_driver=y \
    -D g4vis_build_raytracerx_driver=y \
    -D g4vis_build_vrml_driver=y \
    -D g4lib_build_gdml=y \
    || true

# move things to reasonable places
%{__install} -m0755 -d %{buildroot}%{_datadir}/%{name}/src
%{__mv} %{buildroot}/%{_usr}/src/%{name}/* %{buildroot}/%{_datadir}/%{name}/src/ || true
%{__mv} data/ %{buildroot}/%{_datadir}/%{name}/ || true

# make the ldconfig snippet
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/ld.so.conf.d
cat > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf <<LDSOCONF
%{_usr}/lib/%{name}/Linux-g++
LDSOCONF

# make the shell environment snippets
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh <<'BOURNE'
export G4SYSTEM='Linux-g++'
export G4INSTALL='%{_datadir}/%{name}/src'
export G4INCLUDE='%{_includedir}/%{name}'
export G4LIB='%{_usr}/lib/%{name}'
export CLHEP_BASE_DIR='%{_usr}'
export CLHEP_INCLUDE_DIR='%{_includedir}'
export CLHEP_LIB_DIR='%{_libdir}'
export CLHEP_LIB='CLHEP'
export G4DEBUG=0
export G4UI_USE_TCSH=1
export G4UI_BUILD_XAW_SESSION=1
export G4UI_USE_XAW=1
export G4UI_BUILD_XM_SESSION=1
export G4UI_USE_XM=1
export G4VIS_BUILD_OPENGLX_DRIVER=1
export G4VIS_USE_OPENGLX=1
export G4VIS_BUILD_OPENGLXM_DRIVER=1
export G4VIS_USE_OPENGLXM=1
export G4VIS_BUILD_RAYTRACER_DRIVER=1
export G4VIS_USE_RAYTRACER=1
export G4VIS_USE_VRML=1
export XMLIBS=' -lXm -lXpm '
export XMFLAGS=''
export XAWLIBS=' -lXaw '
export XAWFLAGS=''
export G4LIB_BUILD_GDML=1
export XERCESROOT=''
export G4LIB_BUILD_SHARED=1
export G4WORKDIR=${HOME}/%{name}

export PATH=${PATH}:${G4WORKDIR}/bin/${G4SYSTEM}
BOURNE

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}-data.sh <<BOURNEDATA
export G4LEVELGAMMADATA='%{_datadir}/%{name}/data/PhotonEvaporation%{PhotonEvaporation_version}'
export G4RADIOACTIVEDATA='%{_datadir}/%{name}/data/RadioactiveDecay%{G4RadioactiveDecay_version}'
export G4LEDATA='%{_datadir}/%{name}/data/EMLOW%{G4EMLOW_version}'
export G4NEUTRONHPDATA='%{_datadir}/%{name}/data/G4NDL%{G4NDL_version}'
export G4ABLADATA='%{_datadir}/%{name}/data/G4ABLA%{G4ABLA_version}'
export G4REALSURFACEDATA='%{_datadir}/%{name}/data/RealSurface%{RealSurface_version}'
BOURNEDATA

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh <<'CSH'
setenv G4SYSTEM 'Linux-g++'
setenv G4INSTALL '%{_datadir}/%{name}/src'
setenv G4INCLUDE '%{_includedir}/%{name}'
setenv G4LIB '%{_usr}/lib/%{name}'
setenv CLHEP_BASE_DIR '%{_usr}'
setenv CLHEP_INCLUDE_DIR '%{_includedir}'
setenv CLHEP_LIB_DIR '%{_libdir}'
setenv CLHEP_LIB 'CLHEP'
setenv G4DEBUG 0
setenv G4UI_USE_TCSH 1
setenv G4UI_BUILD_XAW_SESSION 1
setenv G4UI_USE_XAW 1
setenv G4UI_BUILD_XM_SESSION 1
setenv G4UI_USE_XM 1
setenv G4VIS_BUILD_OPENGLX_DRIVER 1
setenv G4VIS_USE_OPENGLX 1
setenv G4VIS_BUILD_OPENGLXM_DRIVER 1
setenv G4VIS_USE_OPENGLXM 1
setenv G4VIS_BUILD_RAYTRACER_DRIVER 1
setenv G4VIS_USE_RAYTRACER 1
setenv G4VIS_USE_VRML 1
setenv XMLIBS " -lXm -lXpm "
setenv XMFLAGS ""
setenv XAWLIBS " -lXaw "
setenv XAWFLAGS ""
setenv G4LIB_BUILD_GDML 1
setenv XERCESROOT ""
setenv G4LIB_BUILD_SHARED 1
setenv G4WORKDIR ${HOME}/%{name}

setenv PATH ${PATH}:${G4WORKDIR}/bin/${G4SYSTEM}
CSH

cat > %{buildroot}%{_sysconfdir}/profile.d/%{name}-data.csh <<CSHDATA
setenv G4LEVELGAMMADATA '%{_datadir}/%{name}/data/PhotonEvaporation%{PhotonEvaporation_version}'
setenv G4RADIOACTIVEDATA '%{_datadir}/%{name}/data/RadioactiveDecay%{G4RadioactiveDecay_version}'
setenv G4LEDATA '%{_datadir}/%{name}/data/EMLOW%{G4EMLOW_version}'
setenv G4NEUTRONHPDATA '%{_datadir}/%{name}/data/G4NDL%{G4NDL_version}'
setenv G4ABLADATA '%{_datadir}/%{name}/data/G4ABLA%{G4ABLA_version}'
setenv G4REALSURFACEDATA '%{_datadir}/%{name}/data/RealSurface%{RealSurface_version}'
CSHDATA

%post
/sbin/ldconfig 2>/dev/null

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENSE ReleaseNotes/
%{_includedir}/*
%{_usr}/lib/*
%{_sysconfdir}/ld.so.conf.d/*
%{_sysconfdir}/profile.d/%{name}.*sh
%{_datadir}/%{name}/src
%exclude %{_usr}/src

%files data
%defattr(-, root, root, 0755)
%{_datadir}/%{name}/data
%{_sysconfdir}/profile.d/%{name}-data.*sh

%changelog
* Tue Apr 06 2010 Steve Huff <shuff@vecna.org> - 9.3-2
- Fixed bug in profile scripts (undesired variable interpolation).

* Fri Mar 05 2010 Steve Huff <shuff@vecna.org> - 9.3-1
- Initial package.
