# $Id$
# Authority: dries
# Upstream: Martin Hamilton <m$martinh,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Thesaurus-ISO

Summary: Class to handle ISO thesaurii
Name: perl-Text-Thesaurus-ISO
Version: 1.0
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Thesaurus-ISO/

Source: http://www.cpan.org/modules/by-module/Text/Text-Thesaurus-ISO-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module is intended to support the using of ISO thesaurus files
from Perl scripts.  It allows rapid access to individual thesaurus
records based on the terms that they cover and also provides routines
to allow individual items in the thesaurus record to be retrieved.  This
code has been developed as part of the ROADS project but is being made
available separately as it is felt that it may be more widely applicable.

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
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Text/Thesaurus/ISO.pm
%{perl_vendorlib}/auto/Text/Thesaurus/ISO

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
