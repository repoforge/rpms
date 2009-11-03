# $Id$
# Authority: dries

Summary: Single master,query based,synchronous replication server
Name: pgpool
Version: 2.0.1
Release: 1%{?dist}
License: BSD
Group: Applications/Databases
URL: http://www2b.biglobe.ne.jp/~caco/pgpool/

Source: ftp://ftp.sra.co.jp/pub/cmd/postgres/pgpool/pgpool-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex

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

### Clean up buildroot
%{__mv} -f %{buildroot}%{_sysconfdir}/pgpool.conf.sample %{buildroot}%{_sysconfdir}/pgpool.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README README.euc_jp TODO
%config(noreplace) %{_sysconfdir}/pgpool.conf
%{_bindir}/pgpool

%changelog
* Sat Dec  1 2007 Dries Verachtert <dries@ulyssis.org> - 2.0.1-1
- Updated to release 2.0.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-1.2
- Rebuild for Fedora Core 5.

* Sun Jun 26 2004 Dries Verachtert <dries@ulyssis.org> 2.0-1
- Updated to release 2.0.

* Sun May 02 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Cosmetic changes.
- Updated to release 1.1.

* Mon Apr 26 2004 Dries Verachtert <dries@ulyssis.org> 1.0-1
- Initial package
