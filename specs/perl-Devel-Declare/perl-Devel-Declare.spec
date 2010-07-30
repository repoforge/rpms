# $Id$
# Authority: shuff
# Upstream: Florian Ragwitz <rafl$debian,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Devel-Declare

Summary: Adding keywords to perl, in perl
Name: perl-Devel-Declare
Version: 0.006000
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-Declare/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Devel-Declare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: perl >= 5.8.1
BuildRequires: perl(B::Hooks::OP::Check) >= 0.18
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(B::Hooks::EndOfScope) >= 0.05
Requires: perl(B::Hooks::OP::Check) >= 0.18
Requires: perl(Scalar::Util) >= 1.11
Requires: perl(Sub::Name) >= 0

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Devel::Declare can install subroutines called declarators which locally take
over Perl's parser, allowing the creation of new syntax.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/Devel/Declare.pm
%{perl_vendorarch}/Devel/Declare/*
%{perl_vendorarch}/auto/Devel/Declare/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Jul 30 2010 Steve Huff <shuff@vecna.org> - 0.006000-1
- Initial package.
