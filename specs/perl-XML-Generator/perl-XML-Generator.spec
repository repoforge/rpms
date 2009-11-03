# $Id$
# Authority: dries
# Upstream: Benjamin Holzman <bholzman$earthlink,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Generator

Summary: Perl extension for generating XML
Name: perl-XML-Generator
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Generator/

Source: http://www.cpan.org/modules/by-module/XML/XML-Generator-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module allows you to generate XML documents.

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
%doc %{_mandir}/man3/XML::Generator.3*
%doc %{_mandir}/man3/XML::Generator::*.3*
%dir %{perl_vendorlib}/XML/
%{perl_vendorlib}/XML/Generator/
%{perl_vendorlib}/XML/Generator.pm

%changelog
* Mon Aug  3 2009 Christoph Maser <cmr@financial.com> - 1.03-1
- Updated to version 1.03.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 1.01-1
- Updated to release 1.01.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 0.99_02-1
- Updated to release 0.99_02.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 0.99_02-1
- Initial package.
