# $Id: $

# Authority: dries
# Upstream:

Summary: Single master,query based,synchronous replication server
Name: pgpool
Version: 1.0
Release: 1
License: BSD
Group: Applications/Databases
URL: http://www2b.biglobe.ne.jp/~caco/pgpool/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: ftp://ftp.sra.co.jp/pub/cmd/postgres/pgpool/pgpool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
pgpool is a single master/query based/synchronous replication
server. It acts as a proxy server between PostgreSQL client and
PostgreSQL server. No application change is needed to use pgpool.
pgpool's features include:

* connection pooling. This will reduce the connection establishing
  overhead.

* pre-forking child processes. Like Apache, pgpool pre-forks child
  processes to provide faster service startup.

* degeneration. In the replication mode, if one of PostgreSQL goes
  down, it detaches the broken server and continues operation with the
  surviving server.

* fail over. In the connection pool server mode, if master PostgreSQL
  goes down, it detaches the broken server and continues operation
  with the stand-by server.

pgpool can work with PostgreSQL 7.0 to 7.4.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root, 0755)
%doc

%changelog
* Mon Apr 26 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- Initial package
