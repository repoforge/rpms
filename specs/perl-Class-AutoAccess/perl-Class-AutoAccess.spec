# $Id:$
# Authority: cmr
# Upstream: Jerome Eteve <jeromeAteteveDotnet>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-AutoAccess

Summary: Perl module named Class-AutoAccess
Name: perl-Class-AutoAccess
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-AutoAccess/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JETEVE/Class-AutoAccess-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl(Test::More)

%filter_from_requires /^perl*/d
%filter_setup

%description
perl-Class-AutoAccess is a Perl module.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Class::AutoAccess.3pm*
%dir %{perl_vendorlib}/Class/
#%{perl_vendorlib}/Class/AutoAccess/
%{perl_vendorlib}/Class/AutoAccess.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.03-1
- Updated to version 0.03.

* Wed Dec 09 2009 Christoph Maser <cmr@financial.com> - 0.02-1
- Initial package. (using DAR)
