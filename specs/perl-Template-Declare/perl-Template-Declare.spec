# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Declare

Summary: Perlish declarative templates
Name: perl-Template-Declare
Version: 0.44
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Declare/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/Template-Declare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::ISA)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(HTML::Lint)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(String::BufferStack) >= 1.1
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn) >= 0.11
BuildRequires: perl >= 5.8.2
Requires: perl(Class::Accessor::Fast)
Requires: perl(Class::Data::Inheritable)
Requires: perl(Class::ISA)
Requires: perl(HTML::Lint)
Requires: perl(String::BufferStack) >= 1.1
Requires: perl >= 5.8.2

%filter_from_requires /^perl*/d
%filter_setup

%description
Perlish declarative templates.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Template::Declare.3pm*
%doc %{_mandir}/man3/Template::Declare::*.3pm*
%dir %{perl_vendorlib}/Template/
%{perl_vendorlib}/Template/Declare/
%{perl_vendorlib}/Template/Declare.pm

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 0.44-1
- Updated to version 0.44.

* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.43-1
- Updated to version 0.43.

* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.40-1
- Updated to version 0.40.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.39-1
- Updated to version 0.39.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 0.28-1
- Updated to release 0.28.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.27-1
- Updated to release 0.27.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.26-1
- Updated to release 0.26.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
