# $Id$
# Authority: dries
# Upstream: Tarek Ahmed <luke,lubbock$gmx,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-Trigram

Summary: Find similar strings by trigram (or 1, 2, 4, etc.-gram) method
Name: perl-String-Trigram
Version: 0.1
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-Trigram/

Source: http://search.cpan.org/CPAN/authors/id/T/TA/TAREKA/String-Trigram-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/String/Trigram.pm
%{perl_vendorarch}/auto/String/Trigram

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.1-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.1-1
- Initial package.
