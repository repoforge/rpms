# $Id$
# Authority: dries
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Template-Declare

Summary: Perlish declarative templates
Name: perl-Template-Declare
Version: 0.40
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Template-Declare/

Source: http://www.cpan.org/modules/by-module/Template/Template-Declare-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTML::Lint)
BuildRequires: perl(String::BufferStack) >= 1.1
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::Warn)
Requires: perl >= 0:5.6.0

%description
Perlish declarative templates.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Template::Declare.3pm*
%doc %{_mandir}/man3/Template::Declare::*.3pm*
%dir %{perl_vendorlib}/Template/
%{perl_vendorlib}/Template/Declare/
%{perl_vendorlib}/Template/Declare.pm

%changelog
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
