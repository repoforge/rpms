# $Id$
# Authority: dries
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Ima-DBI

Summary: Database connection caching and organization
Name: perl-Ima-DBI
Version: 0.34
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Ima-DBI/

Source: http://search.cpan.org/CPAN/authors/id/T/TM/TMTM/Ima-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Database connection caching and organization.

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
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Ima/DBI.pm

%changelog
* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.34-1
- Updated to release 0.34.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.33-1
- Initial package.
