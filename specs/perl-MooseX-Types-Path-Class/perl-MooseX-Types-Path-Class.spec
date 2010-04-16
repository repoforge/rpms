# $Id$
# Upstream: Todd Hepler <CENSORED>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name MooseX-Types-Path-Class

Summary: A Path::Class type library for Moose
Name: perl-MooseX-Types-Path-Class
Version: 0.05
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Types-Path-Class

Source: http://search.cpan.org/CPAN/authors/id/T/TH/THEPLER/MooseX-Types-Path-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Class::MOP)
BuildRequires: perl(Moose) >= 0.39
BuildRequires: perl(MooseX::Types) >= 0.04
BuildRequires: perl(Path::Class) >= 0.16
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More) 
Requires: perl(Class::MOP)
Requires: perl(Moose) >= 0.39
Requires: perl(MooseX::Types) >= 0.04
Requires: perl(Path::Class) >= 0.16

%filter_from_requires /^perl*/d
%filter_setup


%description

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

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
%doc %{_mandir}/man3/MooseX::Types::Path::Class.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/MooseX/Types/Path/Class.pm

%changelog
* Fri Apr 16 2010 Christoph Maser <cmr.financial.com> - 0.05-1
- initial package
