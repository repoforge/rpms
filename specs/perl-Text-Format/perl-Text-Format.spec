# $Id$
# Authority: dries
# Upstream: Shlomi Fish <shlomif@iglu.org.il>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Format

Summary: Various subroutines to format text
Name: perl-Text-Format
Version: 0.53
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Format/

Source: http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/Text-Format-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
BuildRequires: perl(strict)
BuildRequires: perl(vars)
BuildRequires: perl(warnings)
Requires: perl(Carp)
Requires: perl(strict)
Requires: perl(vars)
Requires: perl(warnings)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Various subroutines to format text.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes 
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Format.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.53-1
- Updated to version 0.53.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Initial package.
