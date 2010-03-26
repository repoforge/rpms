# $Id$
# Upstream: Marcel Gruenauer == hanekomu <marcel@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Data-Miscellany

Summary: Collection of miscellaneous subroutines
Name: perl-Data-Miscellany
Version: 0.04
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-Miscellany

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Data-Miscellany-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.70
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.8.0
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup


%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/Data::Miscellany.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Data/Miscellany.pm

%changelog
* Fri Mar 26 2010 Christoph Maser <cmr.financial.com> - 0.04-1
- initial package

