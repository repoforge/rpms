# $Id:$
# Authority: cmr
# Upstream: Paul Miller <jettero@cpan.org>

%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Statistics-Basic

Summary: Perl module named Statistics-Basic
Name: perl-Statistics-Basic
Version: 1.6602
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Statistics-Basic/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JETTERO/Statistics-Basic-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Number::Format) >= 1.61
BuildRequires: perl(Scalar::Util)
BuildRequires: perl >= 5.006
Requires: perl(Number::Format) >= 1.61
Requires: perl(Scalar::Util)
Requires: perl >= 5.006

%filter_from_requires /^perl*/d
%filter_setup


%description
perl-Statistics-Basic is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Statistics::Basic*.3pm*
%dir %{perl_vendorlib}/Statistics/
%{perl_vendorlib}/Statistics/Basic/
%{perl_vendorlib}/Statistics/Basic.pm
%{perl_vendorlib}/Statistics/Basic.pod

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 1.6602-1
- Updated to version 1.6602.

* Sat Feb 06 2010 Christoph Maser <cmr@financial.com> - 1.6601-2
- Cleanup, trigger rebuild

* Tue Sep 29 2009 Christoph Maser <cmr@financial.com> - 1.6601-1
- Initial package. (using DAR)
