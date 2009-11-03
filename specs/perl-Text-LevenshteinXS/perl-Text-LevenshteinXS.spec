# $Id$
# Authority: dag
# Upstream: Josh Goldberg <josh at 3io<d_o t>com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-LevenshteinXS

Summary: Perl module provides an XS implementation of the Levenshtein edit distance
Name: perl-Text-LevenshteinXS
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-LevenshteinXS/

Source: http://www.cpan.org/modules/by-module/Text/Text-LevenshteinXS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-Text-LevenshteinXS is a Perl module provides an XS implementation
of the Levenshtein edit distance.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Text::LevenshteinXS.3pm*
%dir %{perl_vendorarch}/Text/
%{perl_vendorarch}/Text/LevenshteinXS.pm
%dir %{perl_vendorarch}/auto/Text/
%{perl_vendorarch}/auto/Text/LevenshteinXS/

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
