# $Id$
# Authority: cmr

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Statistics-Basic

Summary: Perl module named Statistics-Basic
Name: perl-Statistics-Basic
Version: 1.6601
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-Basic/

Source: http://www.cpan.org/modules/by-module/Statistics/Statistics-Basic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
BuildRequires: perl(ExtUtils::MakeMaker)
# From yaml requires
BuildRequires: perl(Number::Format) >= 1.61
BuildRequires: perl(Scalar::Util)
Requires: perl >= 0:5.006

%description
perl-Statistics-Basic is a Perl module.

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
%doc %{_mandir}/man3/Statistics::Basic*.3pm*
%dir %{perl_vendorlib}/Statistics/
%{perl_vendorlib}/Statistics/Basic/
%{perl_vendorlib}/Statistics/Basic.pm
%{perl_vendorlib}/Statistics/Basic.pod

%changelog
* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 1.6601-1
- Initial package. (using DAR)
