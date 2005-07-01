# $Id$
# Authority: dag
# Upstream: Jean-Michel POURE <jm$poure,com>

%define desktop-vendor rpmforge

Summary: Graphical client for PostgreSQL
Name: pgadmin3
Version: 1.2.2
Release: 0
License: Artistic
Group: Applications/Databases
URL: http://www.pgadmin.org/

Source: ftp://ftp.postgresql.org/pub/pgadmin3/release/v1.2.2/src/pgadmin3-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildRequires: wxGTK-devel >= 2.4.2, postgresql-devel, wxGTK-stc, wxGTK-xrc
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
%makeinstall

%{__install} -Dp -m0644 src/include/images/elephant48.xpm %{buildroot}%{_datadir}/pgadmin3/pgadmin3.xpm

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--add-category Application                 \
	--add-category Development                 \
	--dir %{buildroot}%{_datadir}/applications \
	pkg/pgadmin3.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pgadmin3/

%changelogA
* Sat Jun 18 2005 Dries Verachtert <dries@ulyssis.org> - 1.2.2-0
- Update.

* Wed Aug 18 2004 Bert de Bruijn <bert@debruijn.be> - 1.0.2-0
- update.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Initial package. (using DAR)
