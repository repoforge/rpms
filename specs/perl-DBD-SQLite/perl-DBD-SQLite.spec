# $Id$
# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

### EL5 ships with perl-DBI-1.52
%{?el5:# Tag: rfx}
### EL6 ships with perl-DBD-SQLite-1.27-3.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-SQLite

Summary: Small fast embedded SQL database engine
Name: perl-DBD-SQLite
Version: 1.29
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-SQLite/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/DBD-SQLite-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(DBI) >= 1.57
BuildRequires: perl(File::Spec) >= 0.82
BuildRequires: perl(Test::More) >= 0.42
BuildRequires: perl(Tie::Hash)
Requires: perl(DBI) >= 1.57
Requires: perl(Tie::Hash)

%filter_from_requires /^perl*/d
%filter_setup

%description
SQLite is a small fast embedded SQL database engine.

DBD::SQLite embeds that database engine into a DBD driver, so
if you want a relational database for your project, but don't
want to install a large RDBMS system like MySQL or PostgreSQL,
then DBD::SQLite may be just what you need.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/DBD::SQLite.3pm*
%doc %{_mandir}/man3/DBD::SQLite::Cookbook.3pm*
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/SQLite.pm
%{perl_vendorarch}/DBD/SQLite/Cookbook.pod
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/SQLite/

%changelog
* Fri Aug 05 2011 Steve Huff <shuff@vecna.org> - 1.29-2
- RFX for el5 as well as el6, due to perl-DBI version requirement.

* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 1.29-1
- Updated to version 1.29.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.27-1
- Updated to version 1.27.

* Tue Jun 03 2009 Christoph Maser <cmr@financial.com> - 1.25-2
- Add dependency for perl-DBI >= 1.57

* Tue Apr 28 2009 Christoph Maser <cmr@financial.com> - 1.25-1
- Updated to release 1.25.

* Tue Apr 21 2009 Christoph Maser <cmr@financial.com> - 1.23-1
- Updated to release 1.23.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.14-1
- Updated to release 1.14.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Updated to release 1.12.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
