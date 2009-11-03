# $Id$
# Authority: cmr
# Upstream: Adam Kennedy <adamk$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-CPAN-Meta

Summary: Parse META.yml and other similar CPAN metadata files
Name: perl-Parse-CPAN-Meta
Version: 1.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-CPAN-Meta/

Source: http://www.cpan.org/modules/by-module/Parse/Parse-CPAN-Meta-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(File::Spec) >= 0.80
BuildRequires: perl(Test::More) >= 0.47


%description
Parse META.yml and other similar CPAN metadata files.

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
%doc Changes MANIFEST META.yml 
%doc %{_mandir}/man3/Parse::CPAN::Meta.3pm*
%dir %{perl_vendorlib}/Parse/
%dir %{perl_vendorlib}/Parse/CPAN/
#%{perl_vendorlib}/Parse/CPAN/Meta/
%{perl_vendorlib}/Parse/CPAN/Meta.pm

%changelog
* Wed Aug  5 2009 Christoph Maser <cmr@financial.com> - 1.40-1
- Updated to version 1.40.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 1.39-1
- Initial package. (using DAR)
