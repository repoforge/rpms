# $Id$
# Authority: dries
# Upstream: Aaron James Trevena <TeeJay-cpan$droogs,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name XML-DOM-BagOfTricks

Summary: Functions for dealing with DOM trees
Name: perl-XML-DOM-BagOfTricks
Version: 0.05
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-DOM-BagOfTricks/

Source: http://www.cpan.org/modules/by-module/XML/XML-DOM-BagOfTricks-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
XML::DOM::BagOfTricks provides a bundle, or bag, of functions that make
dealing with and creating DOM objects easier.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/XML/
%dir %{perl_vendorlib}/XML/DOM/
%{perl_vendorlib}/XML/DOM/BagOfTricks.pm
%dir %{perl_vendorlib}/auto/XML/
%dir %{perl_vendorlib}/auto/XML/DOM/
%{perl_vendorlib}/auto/XML/DOM/BagOfTricks/

%changelog
* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
