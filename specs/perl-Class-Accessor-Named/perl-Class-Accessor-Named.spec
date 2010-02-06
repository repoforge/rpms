# $Id$
# Authority: shuff
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Accessor-Named

Summary: Better profiling output for Class::Accessor
Name: perl-%{real_name}
Version: 0.009
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Accessor-Named/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/Class-Accessor-Named-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Class::Accessor)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Hook::LexWrap)
BuildRequires: perl(Sub::Name)
BuildRequires: perl(UNIVERSAL::require)
Requires: perl(Class::Accessor)
Requires: perl(Hook::LexWrap)
Requires: perl(Sub::Name)
Requires: perl(UNIVERSAL::require)

%filter_from_requires /^perl*/d
%filter_setup

%description
Class::Accessor is a great way to automate the tedious task of generating
accessors and mutators. One small drawback is that due to the details of the
implemenetation, you only get one __ANON__ entry in profiling output. That
entry contains all your accessors, which can be a real pain if you're
attempting to figure out which of your accessors is being called six billion
times. This module is a development aid which uses Hook::LexWrap and Sub::Name
to talk your accessors into identifying themselves. While it shouldn't add much
additional runtime overhead (as it acts only Class::Accessor's generator
functions), it has not been designed for production deployment.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Class/Accessor/
%{perl_vendorlib}/Class/Accessor/*

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.009-1
- Updated to version 0.009.

* Tue Dec 22 2009 Steve Huff <shuff@vecna.org> - 0.008-1
- Initial package.
