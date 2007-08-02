# $Id$
# Authority: dries
# Upstream: Martin 'Kingpin' Thurn <mthurn$verizon,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Alphabet-Phonetic

Summary: Map ABC to phonetic alphabets
Name: perl-Lingua-Alphabet-Phonetic
Version: 0.053
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Alphabet-Phonetic/

Source: http://search.cpan.org//CPAN/authors/id/M/MT/MTHURN/Lingua-Alphabet-Phonetic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Map ABC to phonetic alphabets.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/Lingua::Alphabet::Phonetic*
%doc %{_mandir}/man1/phonetize*
%{_bindir}/phonetize
%{perl_vendorlib}/Lingua/Alphabet/Phonetic.pm
%{perl_vendorlib}/Lingua/Alphabet/Phonetic/

%changelog
* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.053-1
- Initial package.
