# $Id$
# Authority: shuff
# Upstream: Father Chrysostomos <sprout$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Sub-Delete

Summary: Perl module enabling one to delete subroutines
Name: perl-%{real_name}
Version: 1.00002
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Sub-Delete/

Source: http://search.cpan.org/CPAN/authors/id/S/SP/SPROUT/Sub-Delete-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(constant)
BuildRequires: perl(Exporter) >= 5.57
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(constant)
Requires: perl(Exporter) >= 5.57
Requires: perl(strict)
Requires: perl(warnings)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module provides one function, delete_sub, that deletes the subroutine
whose name is passed to it. (To load the module without importing the function,
write use Sub::Delete();.)

This does more than simply undefine the subroutine in the manner of undef &foo,
which leaves a stub that can trigger AUTOLOAD (and, consequently, won't work
for deleting methods). The subroutine is completely obliterated from the symbol
table (though there may be references to it elsewhere, including in compiled
code).

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Sub/
%{perl_vendorlib}/Sub/*

%changelog
* Wed May 05 2010 Steve Huff <shuff@vecna.org> - 1.00002-1
- Initial package.
