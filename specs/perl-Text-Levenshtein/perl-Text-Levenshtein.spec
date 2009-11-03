# $Id$
# Authority: dag
# Upstream: Josh Goldberg <josh at 3io<d_o t>com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Levenshtein
%define real_version 0.04

Summary: Perl module implements the Levenshtein edit distance
Name: perl-Text-Levenshtein
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Levenshtein/

Source: http://www.cpan.org/modules/by-module/Text/Text-Levenshtein-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Text-Levenshtein is a Perl module implements the Levenshtein edit distance.

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
%doc %{_mandir}/man3/Text::Levenshtein.3pm*
%dir %{perl_vendorlib}/Text/
%{perl_vendorlib}/Text/Levenshtein.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
