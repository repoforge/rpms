# $Id$
# Authority: dries
# Upstream: Alberto Manuel Brandao Simoes <ambs@perl-hackers.net>

%define debug_package %{nil}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Ngram

Summary: Ngram analysis of text
Name: perl-Text-Ngram
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Ngram/

Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMBS/Text/Text-Ngram-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Ngram analysis of text.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
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
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/Ngram.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/Ngram/

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 0.13-1
- Updated to version 0.13.

* Thu Jun 11 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Updated to release 0.09.

* Wed Dec 21 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
