# $Id$
# Authority: dag

%{?dtag: %{expand: %%define %dtag 1}}

%{?el4:%define _without_sqlite3 1}
%{?el3:%define _without_sqlite3 1}
%{?rh9:%define _without_sqlite3 1}
%{?rh7:%define _without_sqlite3 1}
%{?el2:%define _without_sqlite3 1}

%define logmsg logger -t %{name}/rpm

Summary: Advanced and high performance authoritative-only nameserver
Name: pdns
Version: 2.9.21.1
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://powerdns.com/

Source: http://downloads.powerdns.com/releases/pdns-%{version}.tar.gz
Patch0: pdns-2.9.21-fixinit.patch
Patch1: pdns-2.9.21-avoid-version.patch
Patch2: pdns-2.9.21.1-compile-fixes.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: boost-devel
BuildRequires: mysql-devel
BuildRequires: postgresql-devel
%{!?_without_sqlite3:BuildRequires: sqlite-devel >= 3.0}
Requires: %{_sbindir}/useradd, /sbin/chkconfig, /sbin/service
Provides: powerdns = %{version}-%{release}

Provides: pdns-backend-geo = %{version}-%{release}
Obsoletes: pdns-backend-geo <= %{version}-%{release}
Provides: pdns-backend-ldap = %{version}-%{release}
Obsoletes: pdns-backend-ldap <= %{version}-%{release}
Provides: pdns-backend-mysql = %{version}-%{release}
Obsoletes: pdns-backend-mysql <= %{version}-%{release}
Provides: pdns-backend-pipe = %{version}-%{release}
Obsoletes: pdns-backend-pipe <= %{version}-%{release}
Provides: pdns-backend-postgresql = %{version}-%{release}
Obsoletes: pdns-backend-postgresql <= %{version}-%{release}
%{!?_without_sqlite3:Provides: pdns-backend-sqlite = %{version}-%{release}}
%{!?_without_sqlite3:Obsoletes: pdns-backend-sqlite <= %{version}-%{release}}

%description
The PowerDNS Nameserver is a modern, advanced and high performance
authoritative-only nameserver. It is written from scratch and conforms
to all relevant DNS standards documents.
Furthermore, PowerDNS interfaces with almost any database.

%prep
%setup
%patch0 -p1 -b .fixinit
%patch1 -p1 -b .avoid-version
%patch2 -p1 -b .compile-fixes

%build
export CPPFLAGS="-DLDAP_DEPRECATED %{optflags}"
%configure \
    --disable-static \
    --libdir="%{_libdir}/pdns" \
    --sysconfdir="%{_sysconfdir}/pdns" \
    --with-dynmodules="geo gmysql gpgsql %{!?_without_sqlite3:gsqlite3} ldap pipe" \
    --with-modules="" \
    --with-mysql-lib="%{_libdir}/mysql" \
    --with-pgsql-lib="%{_libdir}" \
%{!?_without_sqlite3:--with-sqlite3-lib="%{_libdir}"}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0755 pdns/pdns %{buildroot}%{_initrddir}/pdns

%{__cat} <<EOF %{buildroot}%{_sysconfdir}/pdns/pdns.conf-dist >%{buildroot}%{_sysconfdir}/pdns/pdns.conf
setuid=pdns
setgid=pdns
EOF

%{__rm} -f %{buildroot}%{_sysconfdir}/pdns/pdns.conf-dist

%pre
if ! /usr/bin/getent group pdns &>/dev/null; then
    /usr/sbin/groupadd pdns &>/dev/null || \
        %logmsg "Unexpected error adding group \"pdns\". Aborting installation."
fi
if ! /usr/bin/id pdns &>/dev/null; then
    /usr/sbin/useradd -r -d / -s /sbin/nologin -c "PowerDNS user" -g pdns pdns || \
        %logmsg "Unexpected error adding user \"nagios\". Aborting installation."
fi

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add pdns
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service pdns stop &>/dev/null || :
    /sbin/chkconfig --del pdns
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog TODO pdns/COPYING
%doc %{_mandir}/man8/pdns_control.8*
%doc %{_mandir}/man8/pdns_server.8*
%doc %{_mandir}/man8/zone2sql.8*
%config(noreplace) %{_sysconfdir}/pdns/
%config %{_initrddir}/pdns
%{_bindir}/pdns_control
%{_bindir}/zone2ldap
%{_bindir}/zone2sql
%{_libdir}/pdns/
%{_sbindir}/pdns_server
%exclude %{_libdir}/pdns/*.la

%changelog
* Fri Sep 12 2008 Dries Verachtert <dries@ulyssis.org> - 2.9.21.1-1
- Updated to release 2.9.21.1.

* Wed Nov 21 2007 Dag Wieers <dag@wieers.com> - 2.9.21-1
- Initial package. (using DAR)
