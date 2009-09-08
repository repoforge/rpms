# $Id$
# Authority: dries
# Upstream: Struan Donald <struan$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-Validator-HTML-W3C

Summary: Access the W3Cs online HTML validator
Name: perl-WebService-Validator-HTML-W3C
Version: 0.26
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-Validator-HTML-W3C/

Source: http://www.cpan.org/modules/by-module/WebService/WebService-Validator-HTML-W3C-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP)
BuildRequires: perl(Test::More)

%description
Access the W3Cs online HTML validator.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/WebService::Validator::HTML::W3C.3pm*
%doc %{_mandir}/man3/WebService::Validator::HTML::W3C::*.3pm*
%dir %{perl_vendorlib}/WebService/
%dir %{perl_vendorlib}/WebService/Validator/
%dir %{perl_vendorlib}/WebService/Validator/HTML/
%{perl_vendorlib}/WebService/Validator/HTML/W3C/
%{perl_vendorlib}/WebService/Validator/HTML/W3C.pm

%changelog
* Tue Sep  8 2009 Christoph Maser <cmr@financial.com> - 0.26-1
- Updated to version 0.26.

* Wed Jul 29 2009 Christoph Maser <cmr@financial.com> - 0.25-1
- Updated to version 0.25.

* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.24-1
- Updated to version 0.24.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.22-1
- Updated to release 0.22.

* Wed May 02 2007 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Updated to release 0.19.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.16-1
- Initial package.
