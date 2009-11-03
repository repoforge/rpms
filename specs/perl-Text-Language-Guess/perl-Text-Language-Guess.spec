# $Id$
# Authority: dag
# Upstream: Michael Schilli <m$perlmeister,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-Language-Guess

Summary: Perl trained module to guess a document's language
Name: perl-Text-Language-Guess
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-Language-Guess/

Source: http://www.cpan.org/modules/by-module/Text/Text-Language-Guess-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Text-Language-Guess is a Perl trained module to guess
a document's language.

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

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README eg/
%doc %{_mandir}/man1/language-guess.1*
%doc %{_mandir}/man3/Text::Language::Guess.3pm*
%{_bindir}/language-guess
%dir %{perl_vendorlib}/Text/
%dir %{perl_vendorlib}/Text/Language/
%{perl_vendorlib}/Text/Language/Guess.pm

%changelog
* Wed Oct 10 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
