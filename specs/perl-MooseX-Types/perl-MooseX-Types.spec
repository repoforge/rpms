# $Id$
# Authority: cmr
# Upstream: Robert "phaylon" Sedlacek <rs$474,at>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Types

Summary: Organise your Moose types in libraries
Name: perl-MooseX-Types
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Types/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-Types-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(Carp::Clan) >= 6.00
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(FindBin)
BuildRequires: perl(Moose) >= 0.61
BuildRequires: perl(SubInstall) >= 0.924
BuildRequires: perl(Test::More) >= 0.8
BuildRequires: perl(namespace::clean) >= 0.08
Requires: perl >= 2:5.8.0

%description
Organise your Moose types in libraries.

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
%doc %{_mandir}/man3/MooseX::Types.3pm*
%doc %{_mandir}/man3/MooseX::Types*.3pm*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/Types/
%{perl_vendorlib}/MooseX/Types.pm

%changelog
* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Initial package. (using DAR)
