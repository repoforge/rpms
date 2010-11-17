# $Id$
# Authority: dries
# Upstream: Brian Ingerson <ingy$cpan,org>

### EL6 ships with perl-YAML-0.70-4.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML

Summary: Machine parseable data serialization format
Name: perl-YAML
Version: 0.71
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/YAML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl >= 5.8.1
Requires: perl(Filter::Util::Call)
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup

%description
YAML is an abbreviation of YAML Ain't Markup Language. It's a straightforward
machine-parseable data serialization format.

%prep
%setup -n %{real_name}-%{version}

%build
echo "y" | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
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
%doc %{_mandir}/man3/Test::YAML.3pm*
%doc %{_mandir}/man3/YAML.3pm*
%doc %{_mandir}/man3/YAML::*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/YAML.pm
%{perl_vendorlib}/YAML/
%{perl_vendorlib}/YAML.pm

%changelog
* Mon Jan  4 2010 Christoph Maser <cmr@financial.com> - 0.71-1
- Updated to version 0.71.

* Sat Aug 29 2009 Christoph Maser <cmr@financial.com> - 0.70-1
- Updated to version 0.70.

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.68-1
- Updated to version 0.68.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.66-1
- Updated to release 0.66.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.62-1
- Updated to release 0.62.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.58-1
- Updated to release 0.58.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.39-1
- Updated to release 0.39.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 0.36-1
- Updated to release 0.36.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.35-1
- Initial package.
