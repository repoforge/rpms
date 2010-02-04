# $Id$
# Authority: shuff
# Upstream: Cal Henderson <cal$iamcal,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name CSS

Summary: Object-oriented access to Cascading Style Sheets (CSS)
Name: perl-%{real_name}
Version: 1.08
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS/

Source: http://search.cpan.org/CPAN/authors/id/I/IA/IAMCAL/CSS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Parse::RecDescent) >= 1.0
BuildRequires: perl(Test::Simple)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Parse::RecDescent) >= 1.0
Requires: perl(Test::Simple)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module can be used, along with a CSS::Parse::* module, to parse CSS data
and represent it as a tree of objects. Using a CSS::Adaptor::* module, the CSS
data tree can then be transformed into other formats.

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
%{perl_vendorlib}/CSS.pm

%changelog
* Tue Nov 03 2009 Steve Huff <shuff@vecna.org> - 1.08-1
- Initial package.
