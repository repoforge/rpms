# $Id$
# Authority: dries
# Upstream: Matthew Simon Cavalletto <simonm$cavalletto,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-MakeMethods

Summary: Generate common types of methods
Name: perl-Class-MakeMethods
Version: 1.01
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-MakeMethods/

Source: http://search.cpan.org/CPAN/authors/id/E/EV/EVO/Class-MakeMethods-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
Generate common types of methods.

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Class/MakeMethods.pm
%{perl_vendorlib}/Class/MakeMethods
%{perl_vendorlib}/Class/benchmark.pl

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Initial package.
