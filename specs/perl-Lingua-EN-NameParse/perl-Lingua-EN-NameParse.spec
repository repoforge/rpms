# $Id$
# Authority: dries
# Upstream: Kim Ryan <kimryan%20nospam$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Lingua-EN-NameParse

Summary: Manipulate peoples names, titles and initials
Name: perl-Lingua-EN-NameParse
Version: 1.24
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Lingua-EN-NameParse/

Source: http://www.cpan.org/modules/by-module/Lingua/Lingua-EN-NameParse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module takes as input a person or persons name in
free format text and attempts to parse it. If successful,
the name is broken down into components.

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

%{__perl} -pi -e 's|/usr/local/bin/perl|%{_bindir}/perl|g;' %{buildroot}%{perl_vendorlib}/Lingua/EN/*

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README surname_prefs.txt examples/
%doc %{_mandir}/man3/Lingua::EN::NameGrammar.3pm*
%doc %{_mandir}/man3/Lingua::EN::NameParse.3pm*
%dir %{perl_vendorlib}/Lingua/
%dir %{perl_vendorlib}/Lingua/EN/
#%{perl_vendorlib}/Lingua/EN/NameParse/
%{perl_vendorlib}/Lingua/EN/NameGrammar.pm
%{perl_vendorlib}/Lingua/EN/NameParse.pm
#%{perl_vendorlib}/Lingua/EN/demo.pl

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.24-1
- Updated to release 1.24.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.23-1
- Updated to release 1.23.

* Mon Nov  7 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-2
- Fix the script which tries to use perl in /usr/local.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.22-1
- Updated to release 1.22.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Updated to release 1.21.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Initial package.
