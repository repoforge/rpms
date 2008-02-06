# $Id$
# Authority: dries
# Upstream: Sam Tregar <sam$tregar,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-Validator-Schema

Summary: Validate XML against a subset of W3C XML Schema
Name: perl-XML-Validator-Schema
Version: 1.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Validator-Schema/

Source: http://www.cpan.org/modules/by-module/XML/XML-Validator-Schema-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module allows you to validate XML documents against a W3C XML
Schema. This module does not implement the full W3C XML Schema
recommendation (http://www.w3.org/XML/Schema), but a useful subset. See
the SCHEMA SUPPORT section in the module documention.

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
%doc Changes README
%doc ANNOUNCE Changes MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/XML::Validator::Schema.3pm*
%doc %{_mandir}/man3/XML::Validator::Schema::*.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/Validator/
%{perl_vendorlib}/XML/Validator/Schema/
%{perl_vendorlib}/XML/Validator/Schema.pm

%changelog
* Mon Feb 04 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Thu Jan 31 2008 Dries Verachtert <dries@ulyssis.org> - 1.09-1
- Updated to release 1.09.

* Fri Nov 05 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Initial package.
