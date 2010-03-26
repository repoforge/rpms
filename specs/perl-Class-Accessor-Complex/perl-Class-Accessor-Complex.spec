# $Id$
# Upstream: Marcel Gruenauer == hanekomu <marcel@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Class-Accessor-Complex

Summary: Arrays, hashes, booleans, integers, sets and more
Name: perl-Class-Accessor-Complex
Version: 1.100820
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Complex

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Class-Accessor-Complex-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Carp)
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(Class::Accessor::Installer)
BuildRequires: perl(Data::Miscellany)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Scalar::Util)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(parent)
BuildRequires: perl >= 5.008
Requires: perl(Carp)
Requires: perl(Class::Accessor)
Requires: perl(Class::Accessor::Installer)
Requires: perl(Data::Miscellany)
Requires: perl(English)
Requires: perl(File::Find)
Requires: perl(File::Temp)
Requires: perl(List::MoreUtils)
Requires: perl(Scalar::Util)
#Requires: perl(Test::More) >= 0.88
Requires: perl(Test::More)
Requires: perl(constant)
Requires: perl(parent)
Requires: perl >= 5.008

%filter_from_requires /^perl*/d
%filter_setup


%description
s module generates accessors for your class in the same spirit as Class::Accessor does. While the latter deals with accessors for scalar values, this module provides accessor makers for arrays, hashes, integers, booleans, sets and more.

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
%doc %{_mandir}/man3/Class::Accessor::Complex.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Class/Accessor/Complex.pm

%changelog
* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 1.100820-1
- initial package

