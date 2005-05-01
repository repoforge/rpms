# $Id$
# Authority: dries
# Upstream: Daniel Koch <dkoch$bizjournals,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-TextIndex

Summary: full-text searching in SQL databases
Name: perl-DBIx-TextIndex
Version: 0.25
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-TextIndex/

Source: http://search.cpan.org/CPAN/authors/id/D/DK/DKOCH/DBIx-TextIndex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
DBIx::TextIndex was developed for doing full-text searches on BLOB
columns stored in a database. Almost any database with BLOB and DBI
support should work with minor adjustments to SQL statements in the
module. MySQL, PostgreSQL, and SQLite are currently supported.
	
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
%{perl_vendorarch}/DBIx/TextIndex.pm
%{perl_vendorarch}/DBIx/TextIndex
%{perl_vendorarch}/auto/DBIx/TextIndex

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.25-1
- Initial package.
