# $Id$
# Authority: dag
# Upstream: Stevan Little <stevan$iinteractive,com>
# ExcludeDist: el4 

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Moose-Policy

Summary: Moose-Policy module for perl
Name: perl-Moose-Policy
Version: 0.04
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Moose-Policy/

Source: http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/Moose-Policy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose) >= 0.84
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::More) >= 0.62
Requires: perl(Moose) >= 0.84

%filter_from_requires /^perl*/d
%filter_setup


%description
Moose-Policy module for perl.

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Moose/
%{perl_vendorlib}/Moose/Policy/
%{perl_vendorlib}/Moose/Policy.pm

%changelog
* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.03-1
- Initial package. (using DAR)
