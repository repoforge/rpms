# $Id$
# Upstream: Marcel Gruenauer == hanekomu <marcel@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Class-Accessor-Installer

Summary: Install an accessor subroutine
Name: perl-Class-Accessor-Installer
Version: 1.100820
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Installer

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARCEL/Class-Accessor-Installer-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Name)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl >= 5.006
Requires: perl(Carp)
Requires: perl(English)
Requires: perl(File::Find)
Requires: perl(File::Temp)
Requires: perl(Scalar::Util)
Requires: perl(Sub::Name)
#Requires: perl(Test::More) >= 0.88
Requires: perl(Test::More)
Requires: perl(UNIVERSAL::require)
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup

%description
This mixin class provides a method that will install a coderef. There are other modules that do this, but this one is a bit more specific to the needs of Class::Accessor::Complex and friends.

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
%doc %{_mandir}/man3/Class::Accessor::Installer.3pm*
%dir %{perl_vendorlib}/Class
%{perl_vendorlib}/Class/Accessor/Installer.pm

%changelog
* Fri Mar 26 2010 Christoph Maser <cmr@financial.com> - 1.100820-1
- initial package

