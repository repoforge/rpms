# $Id: perl-IP-Country.spec 171 2004-03-28 01:43:07Z dag $
# Authority: dag
# Upstream: Ronan Oger <ronan$cpan,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name SVG

Summary: Perl extension for generating Scalable Vector Graphics (SVG) documents
Name: perl-SVG
Version: 2.50
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVG/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/RONAN/SVG-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
Requires: perl(Scalar::Util)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Perl extension for generating Scalable Vector Graphics (SVG) documents.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/SVG.3pm*
%doc %{_mandir}/man3/SVG::*.3pm*
%{perl_vendorlib}/SVG/
%{perl_vendorlib}/SVG.pm

%changelog
* Thu Feb 10 2011 Christoph Maser <cmaser@gmx.de> - 2.50-1
- Updated to version 2.50.

* Wed Jun 17 2009 Christoph Maser <cmr@financial.com> - 2.49-1
- Updated to version 2.49.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 2.44-1
- Updated to release 2.44.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 2.37-1
- Updated to release 2.37.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.36-1
- Updated to release 2.36.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.33-2
- Disabled auto-requires for examples/.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.33-1
- Updated to release 2.33.

* Tue Apr 13 2004 Dag Wieers <dag@wieers.com> - 2.28-1
- Initial package. (using DAR)
