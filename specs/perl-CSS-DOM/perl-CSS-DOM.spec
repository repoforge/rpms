# $Id$
# Authority: shuff
# Upstream: Father Chrysostomos <sprout$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CSS-DOM

Summary: Document Object Model for Cascading Style Sheets
Name: perl-%{real_name}
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS-DOM/

Source: http://search.cpan.org/CPAN/authors/id/S/SP/SPROUT/CSS-DOM-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Carp) >= 1.01
BuildRequires: perl(Clone) >= 0.09
BuildRequires: perl(constant) >= 1.03
BuildRequires: perl(constant::lexical)
BuildRequires: perl(Encode) >= 2.1
BuildRequires: perl(Exporter) >= 5.57
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Graphics::ColorNames::SVG)
BuildRequires: perl(overload)
BuildRequires: perl(re)
BuildRequires: perl(Scalar::Util) >= 1.09
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tie::Util)
BuildRequires: perl(warnings)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp) >= 1.01
Requires: perl(Clone) >= 0.09
Requires: perl(constant) >= 1.03
Requires: perl(constant::lexical)
Requires: perl(Encode) >= 2.1
Requires: perl(Exporter) >= 5.57
Requires: perl(Graphics::ColorNames::SVG)
Requires: perl(overload)
Requires: perl(re)
Requires: perl(Scalar::Util) >= 1.09
Requires: perl(strict)
Requires: perl(Tie::Util)
Requires: perl(warnings)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This set of modules provides the CSS-specific interfaces described in the W3C
DOM recommendation.

The CSS::DOM class itself implements the StyleSheet and CSSStyleSheet DOM
interfaces.

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
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/CSS/
%{perl_vendorlib}/CSS/*

%changelog
* Wed May 05 2010 Steve Huff <shuff@vecna.org> - 0.10-1
- Initial package.
