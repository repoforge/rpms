# $Id$
# Authority: dries
# Upstream: Michel Rodriguez <xmltwig$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-TreeBuilder-XPath

Summary: Add XPath support for HTML::TreeBuilder
Name: perl-HTML-TreeBuilder-XPath
Version: 0.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-TreeBuilder-XPath/

Source: http://www.cpan.org/modules/by-module/HTML/HTML-TreeBuilder-XPath-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
XPath support for HTML::TreeBuilder.

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
%doc %{_mandir}/man3/HTML::TreeBuilder::XPath.3pm*
%dir %{perl_vendorlib}/HTML/
%dir %{perl_vendorlib}/HTML/TreeBuilder/
#%{perl_vendorlib}/HTML/TreeBuilder/XPath/
%{perl_vendorlib}/HTML/TreeBuilder/XPath.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Updated to version 0.11.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Updated to release 0.09.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Updated to release 0.08.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.07-1
- Initial package.
