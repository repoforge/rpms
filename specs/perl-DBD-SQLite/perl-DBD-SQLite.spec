# $Id$
# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-SQLite

Summary: Small fast embedded SQL database engine
Name: perl-DBD-SQLite
Version: 1.09
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-SQLite/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/DBD-SQLite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl-DBI, sqlite-devel

%description
SQLite is a small fast embedded SQL database engine.

DBD::SQLite embeds that database engine into a DBD driver, so
if you want a relational database for your project, but don't
want to install a large RDBMS system like MySQL or PostgreSQL,
then DBD::SQLite may be just what you need.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/DBD/SQLite.pm
%{perl_vendorarch}/auto/DBD/SQLite

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
