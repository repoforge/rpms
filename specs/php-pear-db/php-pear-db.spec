# $Id$
# Authority: dag

%define pear_dir %{_datadir}/pear
%define real_name DB

Summary: PEAR: Database Abstraction Layer
Name: php-pear-db
Version: 1.7.13
Release: 2
License: PHP
Group: Development/Libraries
URL: http://pear.php.net/package/DB

Source: http://pear.php.net/get/%{real_name}-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: php >= 4.2.0
BuildRequires: php-pear
Requires(post): /usr/bin/pear
Requires(postun): /usr/bin/pear
Requires: php >= 4.2.0
Requires: php-pear

Provides: php-pear(DB) = %{version}

Obsoletes: php-pear-DB <= %{version}-%{release}
Provides: php-pear-DB = %{version}-%{release}

%description
DB is a database abstraction layer providing:
* an OO-style query API
* portability features that make programs written for one DBMS work with
  other DBMS's
* a DSN (data source name) format for specifying database servers
* prepare/execute (bind) emulation for databases that don't support it natively
* a result object for each query response
* portable error codes
* sequence emulation
* sequential and non-sequential row fetching as well as bulk fetching
* formats fetched rows as associative arrays, ordered arrays or objects
* row limit support
* transactions support
* table information interface
* DocBook and phpDocumentor API documentation

DB layers itself on top of PHP's existing database extensions.

%prep

%build

%install
%{__rm} -rf %{buildroot}
/usr/bin/pear install --packagingroot="%{buildroot}" --nodeps %{SOURCE0}

### Clean up buildroot
%{__rm} -f %{buildroot}%{pear_dir}/{.filemap,.lock}
%{__rm} -Rf %{buildroot}%{pear_dir}/{.channels,.depdb*,.registry}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%{pear_dir}/DB.php
%{pear_dir}/DB/
%{pear_dir}/doc/DB/
%{pear_dir}/test/DB/

%changelog
* Mon Jul 28 2008 Dries Verachtert <dries@ulyssis.org> - 1.7.13-2
- Fix file conflicts with php-pear, thanks to Hugo van der Kooij and Brandon Amaro.

* Thu Dec 20 2007 Dag Wieers <dag@wieers.com> - 1.7.13-1
- Initial package. (using DAR)
