# $Id$
# Authority: dries
# Upstream: Kevin Meltzer <perlguy$perlguy,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-PageIndex

Summary: Create HTML page index objects
Name: perl-HTML-PageIndex
Version: 0.3
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-PageIndex/

Source: http://search.cpan.org/CPAN/authors/id/K/KM/KMELTZ/HTML-PageIndex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Create HTML page index objects.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/HTML/PageIndex.pm

%changelog
* Sun Apr  3 2005 Dries Verachtert <dries@ulyssis.org> - 0.3-1
- Initial package.
