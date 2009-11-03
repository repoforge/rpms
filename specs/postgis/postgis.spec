# $Id$
# Authority: dag

Summary: Geographic Information Systems Extensions to PostgreSQL
Name: postgis
Version: 1.3.6
Release: 1%{?dist}
License: GPL
Group: Applications/Databases
URL: http://postgis.refractions.net/

Source: http://postgis.refractions.net/download/postgis-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildrequires: bison
#BuildRequires: docbook-utils
#BuildRequires: docbook-utils-pdf
BuildRequires: flex
BuildRequires: geos-devel >= 2.1.1
#BuildRequires: libxslt
BuildRequires: perl
BuildRequires: postgresql-devel
BuildRequires: proj-devel
#Buildrequires: xmltex

%description
PostGIS adds support for geographic objects to the PostgreSQL object-relational
database. In effect, PostGIS "spatially enables" the PostgreSQL server,
allowing it to be used as a backend spatial database for geographic information
systems (GIS), much like ESRI's SDE or Oracle's Spatial extension. PostGIS
follows the OpenGIS "Simple Features Specification for SQL" and will be
submitted for conformance testing at version 1.0.

%package utils
Summary: PostGIS utilities
Group: Applications/System
Requires: %{name} = %{version}-%{release}
Requires: perl(DBD::Pg)

%description utils
The postgis-utils package provides the utilities for PostGIS.

%prep
%setup
%{__perl} -pi.orig -e "s|^SCRIPT_DOLINK=rm.*|SCRIPT_DOLINK=echo \\\\|g;" extras/template_gis/Makefile

%build
%{__make} %{?_smp_mflags} \
    PGXS="1" \
    PGSQL_SRC="/usr/lib/pgsql/pgxs" \
    shlib="postgis.so"
#    LPATH="\$\(pkglibdir\)" \
#    CFLAGS="%{optflags} -Wno-pointer-sign"
%{__make} %{?_smp_mflags} templategis
%{__make} -C utils

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    PGXS="1" \
    PGSQL_SRC="/usr/lib/pgsql/pgxs"

%{__make} templategis-install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 lwgeom/liblwgeom.so %{buildroot}%{_libdir}/pgsql/liblwgeom.so
%{__install} -Dp -m0755 lwgeom/postgis.so %{buildroot}%{_libdir}/pgsql/postgis.so

%{__install} -d -m0755 %{buildroot}%{_datadir}/pgsql/postgresql/contrib/
%{__install} -Dp -m0644 *.sql %{buildroot}%{_datadir}/pgsql/postgresql/contrib/

%{__install} -d -m0755 %{buildroot}%{_datadir}/postgis/
%{__install} -p -m0755 utils/*.pl %{buildroot}%{_datadir}/postgis/

### Clean up buildroot
%{__rm} -f %{buildroot}%{_datadir}/*.sql

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING CREDITS README.postgis TODO doc/html/ loader/README.* *.sql doc/postgis.xml  doc/ZMSgeoms.txt 
%doc %{_mandir}/man1/createdb.postgis.1*
%doc %{_mandir}/man1/mktemplate_gis.1*
%doc %{_mandir}/man1/rmtemplate_gis.1*
%config(noreplace) %{_datadir}/default/postgis
%{_bindir}/createdb.postgis
%{_bindir}/mktemplate_gis
%{_bindir}/mktemplate_gis.sh
%{_bindir}/pgsql2shp
%{_bindir}/postgis_env.sh
%{_bindir}/postgres_lib.sh
%{_bindir}/rmtemplate_gis
%{_bindir}/rmtemplate_gis.sh
%{_bindir}/shp2pgsql
%dir %{_libdir}/pgsql/
%{_libdir}/pgsql/liblwgeom.so
%{_libdir}/pgsql/postgis.so
%dir %{_datadir}/pgsql/
%dir %{_datadir}/pgsql/postgresql/
%dir %{_datadir}/pgsql/postgresql/contrib/
%{_datadir}/pgsql/postgresql/contrib/*.sql
%exclude %{_libdir}/pgsql/liblwgeom.so.*

%files utils
%defattr(-, root, root, 0755)
%doc utils/README
%{_datadir}/postgis/

%changelog
* Wed Jul  8 2009 Christoph Maser <cmr@financial.com> - 1.3.6-1
- Updated to version 1.3.6.

* Tue Jan 22 2008 Dries Verachtert <dries@ulyssis.org> - 1.3.2-1
- Updated to release 1.3.2.

* Sun Aug 19 2007 Dag Wieers <dag@wieers.com> - 1.2.1-1
- Initial package. (using DAR)
