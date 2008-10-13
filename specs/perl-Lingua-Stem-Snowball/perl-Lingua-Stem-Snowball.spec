# $Id$
# Authority: dries
# Upstream: Marvin Humphrey <marvin$rectangular,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-Stem-Snowball

Summary: Perl interface to Snowball stemmers
Name: perl-Lingua-Stem-Snowball
Version: 0.952
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-Stem-Snowball/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-Stem-Snowball-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.6.2
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(ExtUtils::ParseXS)
#BuildRequires: perl(Module::Build)
Requires: perl >= 1:5.6.2

%description
Perl interface to Snowball stemmers.

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
%{__rm} -f %{buildroot}%{_bindir}/*.plx

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Lingua::Stem::Snowball.3pm*
%dir %{perl_vendorarch}/auto/Lingua/
%dir %{perl_vendorarch}/auto/Lingua/Stem/
%{perl_vendorarch}/auto/Lingua/Stem/Snowball/
%dir %{perl_vendorarch}/Lingua/
%dir %{perl_vendorarch}/Lingua/Stem/
%{perl_vendorarch}/Lingua/Stem/Snowball.pm
#%{_bindir}/add_stemmer.pl
#{_bindir}/benchmark_stemmers.plx
#{_bindir}/generate_tests.plx

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 0.952-1
- Updated to release 0.952.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.941-1
- Updated to release 0.941.

* Sun Jun 04 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-2
- Fix: don't package the test scripts, thanks to Andreas de Pretis.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Updated to release 0.94.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.93-1
- Updated to release 0.93.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.92-1
- Updated to release 0.92.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
