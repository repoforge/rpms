# Authority: dag

Summary: GtkSQL is a graphical database query tool for MySQL and PostgreSQL.
Name: gtksql
Version: 0.4
Release: 0
License: GPL
Group: Applications/Databases
URL: http://gtksql.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/gtksql/gtksql-%{version}.tar.gz
Patch: %{name}-%{version}.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: mysql-devel, postgresql-devel, lua-devel

%description
GtkSQL is a graphical database query tool for the PostgreSQL and MySQL
databases.

It is similar to PostgreSQL's psql, or the Microsoft Query Analyser. It
is a free tool released under the GNU GPL license.

Its main features are :

* multiple SQL buffers
* SQL keywords, table names and fields auto-completion
* displays table definition
* PostgreSQL and MySQL support (and easy addition of other databases)

%prep
%setup
#%patch -p1

%{__cat} <<EOF >%{name}.desktop
[Desktop Entry]
Name=GtkSql SQL Client
Comment=A SQL database query interface.
Exec=gtksql
Icon=gtksql_gnome_icon.png
Terminal=false
Type=Application
StartupNotify=true
Categories=GNOME;Application;Development;
EOF

%build
%configure
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_datadir}/pixmaps/
%{__install} -m0644 pixmaps/gtksql_gnome_icon.png %{buildroot}%{_datadir}/pixmaps/

desktop-file-install --vendor gnome                \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	%{name}.desktop

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/gtksql/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%changelog
* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
