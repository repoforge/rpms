# $Id$
# Authority: dries
# Upstream: Tim Jenness <t,jenness$jach,hawaii,edu>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_sitelib %(eval "`perl -V:installsitelib`"; echo $installsitelib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-PassGen

Summary: Generate a random password that looks like a real word
Name: perl-Crypt-PassGen
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-PassGen/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-PassGen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: words

%description
This module provides a single command for generating random password
that is close enough to a real word that it is easy to remember.
It does this by using the frequency of letter combinations in
a language (the frequency table is generated during installation
although multiple tables can be generated and used for different
languages).

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%{__install} -d %{buildroot}%{perl_sitelib}/Crypt/PassGenWordFreq.dat
%{__mv} %{buildroot}%{perl_vendorlib}/Crypt/PassGenWordFreq.dat %{buildroot}%{perl_sitelib}/Crypt/PassGenWordFreq.dat

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST META.yml README
%doc %{_mandir}/man3/Crypt::PassGen.3pm*
%dir %{perl_vendorlib}/Crypt/
#%{perl_vendorlib}/Crypt/PassGen/
%{perl_vendorlib}/Crypt/PassGen.pm
#%{perl_vendorlib}/Crypt/PassGenWordFreq.dat
%{perl_sitelib}/Crypt/PassGenWordFreq.dat

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Fri Apr 07 2006 Dries Verachtert <dries@ulyssis.org> - 0.04-2
- Fix so the dat file is found, thanks to Chris Croome.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.04-1
- Initial package.
