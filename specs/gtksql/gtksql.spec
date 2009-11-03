# $Id$
# Authority: dag
# Upstream: Darryl Luff <djluff$users,sf,net>

%define desktop_vendor rpmforge

Summary: Graphical database query tool for MySQL and PostgreSQL
Name: gtksql
Version: 0.4.2
Release: 2.2%{?dist}
License: GPL
Group: Applications/Databases
URL: http://gtksql.sourceforge.net/

Source: http://dl.sf.net/gtksql/gtksql-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel, lua-devel, postgresql-devel, gtk+-devel
BuildRequires: automake, autoconf, desktop-file-utils

%description
GtkSQL is a graphical database query tool for the PostgreSQL and MySQL
databases.

It is similar to PostgreSQL's psql, or the Microsoft Query Analyser. It
is a free tool released under the GNU GPL license.

Its main features are:

	multiple SQL buffers,
	SQL keywords, table names and fields auto-completion,
	displays table definition
and	PostgreSQL and MySQL support (and easy addition of other databases)

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure Makefile.in

%{__cat} <<EOF >gtksql.desktop
[Desktop Entry]
Name=GtkSql SQL Client
Comment=Query SQL databases
Exec=gtksql
Icon=gtksql.png
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

%{__install} -Dp -m0644 pixmaps/gtksql_gnome_icon.png %{buildroot}%{_datadir}/pixmaps/gtksql.png

desktop-file-install --vendor %{desktop_vendor}    \
	--add-category X-Red-Hat-Base              \
	--dir %{buildroot}%{_datadir}/applications \
	gtksql.desktop

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
%exclude %{_prefix}/doc/

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.4.2-2.2
- Rebuild for Fedora Core 5.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 0.4.2-2
- Fixed mysql support in x86_64 build. (Preet Khalsa)

* Thu May 13 2004 Dag Wieers <dag@wieers.com> - 0.4.2-1
- Updated to release 0.4.2.

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 0.4.1-1
- Updated to release 0.4.1.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 0.4-0
- Initial package. (using DAR)
