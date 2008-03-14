# $Id$
# Authority: dries
# Upstream: Martin 'Kingpin' Thurn <mthurn$verizon,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Alphabet-Phonetic

Summary: Map ABC to phonetic alphabets
Name: perl-Lingua-Alphabet-Phonetic
Version: 0.056
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Alphabet-Phonetic/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Alphabet-Phonetic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Map ABC to phonetic alphabets.

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
%doc Changes
%doc %{_mandir}/man1/phonetize.1*
%doc %{_mandir}/man3/Lingua::Alphabet::Phonetic.3pm*
%doc %{_mandir}/man3/Lingua::Alphabet::Phonetic::*.3pm*
%{_bindir}/phonetize
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/Alphabet/
%{perl_vendorlib}/Lingua/Alphabet/Phonetic/
%{perl_vendorlib}/Lingua/Alphabet/Phonetic.pm

%changelog
* Fri Mar 14 2008 Dag Wieers <dag@wieers.com> - 0.056-1
- Updated to release 0.056.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.054-1
- Updated to release 0.054.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.053-1
- Initial package.
