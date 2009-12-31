# $Id$
# Upstream: Guillermo Roditi <groditi@gmail.com>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name MooseX-Types-Common

Summary: A set of commonly-used type constraints that do not ship with Moose by default.
Name: perl-MooseX-Types-Common
Version: 0.001000
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Types-Common

Source: http://search.cpan.org/CPAN/authors/id/G/GR/GRODITI/MooseX-Types-Common-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Moose) >= 0.39
BuildRequires: perl(MooseX::Types) >= 0.04
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)
Requires: perl(Moose) >= 0.39
Requires: perl(MooseX::Types) >= 0.04

%filter_from_requires /^perl*/d
%filter_setup

%description
A set of commonly-used type constraints that do not ship with Moose by default.

%prep
%setup -n %{real_name}-%{version}

%build 
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" %{perl_vendorlib}
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man3/MooseX::Types::Common.3pm*
%doc %{_mandir}/man3/MooseX::Types::Common::Numeric.3pm*
%doc %{_mandir}/man3/MooseX::Types::Common::String.3pm*
%dir %{perl_vendorlib}/MooseX
%{perl_vendorlib}/MooseX/Types/Common.pm
%{perl_vendorlib}/MooseX/Types/Common/Numeric.pm
%{perl_vendorlib}/MooseX/Types/Common/String.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.001000-1
- Initial package (using mcsfb)
