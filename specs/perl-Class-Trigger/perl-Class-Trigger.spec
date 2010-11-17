# $Id$
# Authority: dries
# Upstream: Tatsuhiko Miyagawa <miyagawa$bulknews,net>

### EL6 ships with perl-Class-Trigger-0.13-2.1.el6
%{?el6:# Tag: rfx}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Trigger

Summary: Mixin to add / call inheritable triggers
Name: perl-Class-Trigger
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Trigger/

Source: http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Class-Trigger-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Filter::Util::Call)
BuildRequires: perl(IO::Scalar)
BuildRequires: perl(IO::WrapTie)
BuildRequires: perl(Test::More) >= 0.32
BuildRequires: perl >= 5.8.1
Requires: perl(Filter::Util::Call)
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup


%description
Class::Trigger is a mixin class to add / call triggers (or hooks) that
get called at some points you specify.

This package contains the following Perl module:

    Class::Trigger

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
%doc %{_mandir}/man3/Class::Trigger.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/Trigger.pm

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 0.14-1
- Updated to version 0.14.

* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.12-1
- Updated to release 0.12.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.11-1
- Updated to release 0.11.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
