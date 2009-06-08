# $Id$
# Authority: dries
# Upstream: Derek Price <derek$ximbiot,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Wiki-Toolkit-Formatter-Mediawiki

Summary: Mediawiki-style formatter for Wiki::Toolkit
Name: perl-Wiki-Toolkit-Formatter-Mediawiki
Version: 0.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Wiki-Toolkit-Formatter-Mediawiki/

Source: http://www.cpan.org/modules/by-module/Wiki/Wiki-Toolkit-Formatter-Mediawiki-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
A Mediawiki-style formatter for Wiki::Toolkit.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Wiki::Toolkit::Formatter::Mediawiki.3pm*
%doc %{_mandir}/man3/Wiki::Toolkit::Formatter::Mediawiki::Link.3pm*
%dir %{perl_vendorlib}/Wiki/
%dir %{perl_vendorlib}/Wiki/Toolkit/
%dir %{perl_vendorlib}/Wiki/Toolkit/Formatter/
%{perl_vendorlib}/Wiki/Toolkit/Formatter/Mediawiki/Link.pm
%{perl_vendorlib}/Wiki/Toolkit/Formatter/Mediawiki.pm

%changelog
* Mon Jun  8 2009 Christoph Maser <cmr@financial.com> - 0.04-1
- Updated to version 0.04.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
