# Authority: dag

# Upstream: Jean-Michel POURE <jm@poure.com>

Summary: Graphical client for PostgreSQL.
Name: pgadmin3
Version: 0.9.2
Release: 0
License: Artistic
Group: Applications/Databases
URL: http://www.pgadmin.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://ftp.postgresql.org/postgresql/pgadmin3/beta/src/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: wxGTK2-devel >= 2.5

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

%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
%{__install} -m0644 src/include/images/elephant48.xpm %{buildroot}%{_datadir}/pgadmin3/pgadmin3.xpm

desktop-file-install --vendor net                  \
	--add-category X-Red-Hat-Base              \
	--add-category Application                 \
	--add-category Development                 \
	--dir %{buildroot}%{_datadir}/applications \
	pkg/redhat/pgadmin3.desktop

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/pgadmin3/

%changelog
* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 0.9.2-0
- Initial package. (using DAR)
