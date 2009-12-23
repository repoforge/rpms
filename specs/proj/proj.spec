# $Id$
# Authority: dag
# Upstream: PROJ.4 <proj$lists,maptools,org>

%define datumgrid_version 1.5

Summary: Cartographic projection software (PROJ.4)
Name:    proj
Version: 4.7.0
Release: 1%{?dist}
License: MIT
Group:   Applications/Engineering
URL:     http://trac.osgeo.org/proj/
Source0: http://download.osgeo.org/proj/proj-%{version}.tar.gz
Source1: http://download.osgeo.org/proj/proj-datumgrid-%{datumgrid_version}.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Proj and invproj perform respective forward and inverse transformation of
cartographic data to or from cartesian data with a wide range of selectable
projection functions.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package nad
Summary: US and Canadian datum shift grids for PROJ.4
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}

%description nad
This package contains additional US and Canadian datum shift grids.

%prep
%setup
unzip -d nad %{SOURCE1}

%build
%configure \
    --disable-static
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 nad/pj_out27.dist %{buildroot}%{_datadir}/proj/pj_out27.dist
%{__install} -Dp -m0644 nad/pj_out83.dist %{buildroot}%{_datadir}/proj/pj_out83.dist
%{__install} -Dp -m0644 nad/td_out.dist %{buildroot}%{_datadir}/proj/td_out.dist
%{__install} -Dp -m0755 nad/test27 %{buildroot}%{_datadir}/proj/test27
%{__install} -Dp -m0755 nad/test83 %{buildroot}%{_datadir}/proj/test83
%{__install} -Dp -m0755 nad/testvarious %{buildroot}%{_datadir}/proj/testvarious

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%doc %{_mandir}/man1/cs2cs.1*
%doc %{_mandir}/man1/geod.1*
%doc %{_mandir}/man1/nad2nad.1*
%doc %{_mandir}/man1/proj.1*
%{_bindir}/cs2cs
%{_bindir}/geod
%{_bindir}/invgeod
%{_bindir}/invproj
%{_bindir}/nad2bin
%{_bindir}/nad2nad
%{_bindir}/proj
%{_libdir}/libproj.so.*

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/pj_init.3*
%{_includedir}/nad_list.h
%{_includedir}/org_proj4_Projections.h
%{_includedir}/proj_api.h
%{_includedir}/projects.h
%{_libdir}/libproj.so
%exclude %{_libdir}/libproj.la

%files nad
%defattr(-, root, root, 0755)
%doc nad/README
%{_datadir}/proj/

%changelog
* Wed Dec 23 2009 Yury V. Zaytsev <yury@shurup.com> - 4.7.0-1
- Minor updates.

* Tue Dec 22 2009 Nico Kadel-Garcia <nkadel@gmail.com> - 4.7.0-0
- Updated proj to 4.7.0.
- Updated source URLs.
- Updated proj-datumgrid to 1.5.

* Sun Aug 19 2007 Dag Wieers <dag@wieers.com> - 4.5.0-1 - +/
- Initial package. (using DAR)
