# $Id$
# Authority: dries
# Upstream: Ivan Kohler <ivan-pause$420,am>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-DataSource

Summary: Database-independant create and drop functions
Name: perl-DBIx-DataSource
Version: 0.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-DataSource/

Source: http://search.cpan.org/CPAN/authors/id/I/IV/IVAN/DBIx-DataSource-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Database-independant create and drop functions.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBIx/DataSource.pm
%{perl_vendorlib}/DBIx/DataSource

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
