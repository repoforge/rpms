# $Id$
# Authority: dries
# Upstream: Tommi Maekitalo <tommi$maekitalo,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Cursor

Summary: Easy DBI-access to a single table
Name: perl-DBIx-Cursor
Version: 0.14
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Cursor/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-Cursor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
The class DBIx::Cursor represents a cursor for a single Database-table.
You can select, update, insert or delete entries in a table easier than
creating SQL-statements. It does not use any specific features of any
database, so it should work with every DBD-driver.

DBIx::Cursor is not a replacement for DBI, but a add-on. You can use
DBI as usual and use SQL-statements as you need.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBIx/Cursor.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
