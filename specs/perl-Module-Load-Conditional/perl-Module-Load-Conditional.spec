# $Id$

# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define real_name Module-Load-Conditional
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Looking up module information / loading at runtime
Name: perl-Module-Load-Conditional
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Module-Load-Conditional/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KANE/Module-Load-Conditional-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Allows you to query the state of modules on your system. It can 
tell you if you have certain modules installed without attempting 
to C<use> them and can do smart loading of modules.
Also it can tell you what *other* modules a certain module 
requires.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
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
%{perl_vendorlib}/Module/Load/Conditional.pm

%changelog
* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
