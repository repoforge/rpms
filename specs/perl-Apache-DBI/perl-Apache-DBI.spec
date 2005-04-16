# $Id$
# Authority: dries
# Upstream: Ask Bj&#248;rn Hansen <ask$perl,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-DBI

Summary: Persistent database connections and basic authentication support
Name: perl-Apache-DBI
Version: 0.94
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-DBI/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABH/Apache-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is supposed to be used with the Apache server together with 
an embedded perl interpreter like mod_perl. It provides support for basic 
authentication and authorization as well as support for persistent database 
connections via Perl's Database Independent Interface (DBI).

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
%{perl_vendorlib}/Apache/DBI.pm
%{perl_vendorlib}/Apache/AuthDBI.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
