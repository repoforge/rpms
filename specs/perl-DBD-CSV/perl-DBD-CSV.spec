# $Id$

# Authority: dries
# Upstream: Jeff Zucker <jeff$vpservices,com>

%define real_name DBD-CSV
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: DBI driver for CSV files
Name: perl-DBD-CSV
Version: 0.21
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-CSV/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/DBD-CSV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The DBD::CSV module is yet another driver for the DBI (Database
independent interface for Perl). This one is based on the SQL
"engine" SQL::Statement and the abstract DBI driver DBD::File
and implements access to so-called CSV files (Comma separated
values). Such files are mostly used for exporting MS Access and
MS Excel data.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS="vendor" \
	PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_vendorarch} \
	%{buildroot}%{perl_archlib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBD/CSV.pm
%{perl_vendorlib}/Bundle/DBD/CSV.pm

%changelog
* Tue Mar  1 2005 Dries Verachtert <dries@ulyssis.org> - 0.21-1
- Initial package.
