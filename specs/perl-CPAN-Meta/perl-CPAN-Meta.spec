# $Id$
# Upstream: David Golden <dagolden@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name CPAN-Meta

Summary: the distribution metadata for a CPAN dist
Name: perl-CPAN-Meta
Version: 2.101670
Release: 1%{?dist}
License: ARRAY(0x90fb408)
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CPAN-Meta

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAGOLDEN/CPAN-Meta-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch


BuildRequires: perl(Carp)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(JSON) >= 2
BuildRequires: perl(Parse::CPAN::Meta)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable)
BuildRequires: perl(Version::Requirements)
BuildRequires: perl(autodie)
BuildRequires: perl >= 5.6.0
BuildRequires: perl(version) >= 0.82
Requires: perl(Carp)
Requires: perl(JSON) >= 2
Requires: perl(Parse::CPAN::Meta)
Requires: perl(Scalar::Util)
Requires: perl(Storable)
Requires: perl(Version::Requirements)
Requires: perl(autodie)
Requires: perl >= 5.6.0
Requires: perl(version) >= 0.82

%filter_from_requires /^perl*/d
%filter_setup


%description
Software distributions released to the CPAN include a META.json  or, for older distributions, META.yml, which describes the distribution, its contents, and the requirements for building and installing the distribution. The data structure stored in the META.json  file is described in CPAN::Meta::Spec.

CPAN::Meta provides a simple class to represent this distribution metadata (or distmeta), along with some helpful methods for interrogating that data.


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
%doc %{_mandir}/man3/CPAN::Meta.3pm*
%doc %{_mandir}/man3/CPAN::Meta::Converter.3pm*
%doc %{_mandir}/man3/CPAN::Meta::Feature.3pm*
%doc %{_mandir}/man3/CPAN::Meta::History.3pm*
%doc %{_mandir}/man3/CPAN::Meta::Prereqs.3pm*
%doc %{_mandir}/man3/CPAN::Meta::Spec.3pm*
%doc %{_mandir}/man3/CPAN::Meta::Validator.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/CPAN/Meta.pm
%{perl_vendorlib}/CPAN/Meta/Converter.pm
%{perl_vendorlib}/CPAN/Meta/Feature.pm
%{perl_vendorlib}/CPAN/Meta/History.pm
%{perl_vendorlib}/CPAN/Meta/Prereqs.pm
%{perl_vendorlib}/CPAN/Meta/Spec.pm
%{perl_vendorlib}/CPAN/Meta/Validator.pm

%changelog
* Fri Jul 09 2010 Christoph Maser <cmaser.gmx.de> - 2.101670-1
- initial package
