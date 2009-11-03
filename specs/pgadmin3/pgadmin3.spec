# $Id$
# Authority: dag
# Upstream: Jean-Michel POURE <jm$poure,com>

%define desktop_vendor rpmforge

Summary: Graphical client for PostgreSQL
Name: pgadmin3
Version: 1.8.4
Release: 1%{?dist}
License: Artistic
Group: Applications/Databases
URL: http://www.pgadmin.org/

Source: ftp://ftp.postgresql.org/pub/pgadmin3/release/v%{version}/src/pgadmin3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: wxGTK-devel >= 2.6, postgresql-devel, wxGTK-stc, wxGTK-xrc
BuildRequires: desktop-file-utils, gcc-c++

%description
pgAdmin III is a comprehensive PostgreSQL database design and management
system. It is freely available under the terms of the Artistic Licence
and may be redistributed provided the terms of the licence are adhered to.

pgAdmin III uses the PostgreSQL ODBC Driver (psqlODBC) to communicate with
a PostgreSQL server. The software allows the entire server to be managed
by using 'DSN-less' connections that are made and managed by the pgSchema
object library. All PostgreSQL object types are supported and may be
created, dropped and edited to the extent supported by the database.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 pgadmin/include/images/elephant48.xpm %{buildroot}%{_datadir}/pgadmin3/pgadmin3.xpm

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor} \
    --add-category X-Red-Hat-Base               \
    --add-category Application                  \
    --add-category Development                  \
    --dir %{buildroot}%{_datadir}/applications  \
    pkg/pgadmin3.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/pgadmin3
%{_bindir}/pgagent
%{_datadir}/applications/%{desktop_vendor}-pgadmin3.desktop
%{_datadir}/pgadmin3/

%changelog
* Mon Sep 22 2008 Dag Wieers <dag@wieers.com> - 1.8.4-1
- Updated to release 1.8.4.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.3-1
- Updated to release 1.4.3.

* Sun Mar 12 2006 Dries Verachtert <dries@ulyssis.org> - 1.4.2-1
- Updated to release 1.4.2.

* Mon Dec 19 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.1-1
- Updated to release 1.4.1.

* Fri Nov 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.4.0-1
- Updated to release 1.4.0.

* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-0
- Update.

* Wed Aug 18 2004 Bert de Bruijn <bert@debruijn.be> - 1.0.2-0
- update.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Initial package. (using DAR)
