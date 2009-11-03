# $Id$
# Authority: dries
# Upstream: Tarek Ahmed <luke,lubbock$gmx,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Trigram

Summary: Find similar strings by trigram (or 1, 2, 4, etc.-gram) method
Name: perl-String-Trigram
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Trigram/

Source: http://www.cpan.org/modules/by-module/String/String-Trigram-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module computes the similarity of two strings based on the trigram
method. This consists of splitting some string into triples of
characters and comparing those to the trigrams of some other string. For
example the string kangaroo has the trigrams "{kan ang nga gar aro
roo}". A wrongly typed kanagaroo has the trigrams "{kan ana nag aga gar
aro roo}". To compute the similarity we divide the number of matching
trigrams (tokens not types) by the number of all trigrams (types not
tokens). For our example this means dividing 4 / 9 resulting in 0.44.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%dir %{perl_vendorarch}/String/
%{perl_vendorarch}/String/Trigram.pm
%dir %{perl_vendorarch}/auto/String/
%{perl_vendorarch}/auto/String/Trigram/

%changelog
* Thu Jun 18 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
