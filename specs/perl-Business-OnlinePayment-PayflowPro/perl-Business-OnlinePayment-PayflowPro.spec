# $Id$
# Authority: shuff
# Upstream: Phil Pearl (Lobbes) <phil$perkpartners,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-OnlinePayment-PayflowPro

Summary: Payflow Pro backend for Business::OnlinePayment
Name: perl-%{real_name}
Version: 1.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-OnlinePayment-PayflowPro/

Source: http://search.cpan.org/CPAN/authors/id/P/PL/PLOBBES/Business-OnlinePayment-PayflowPro-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Business::OnlinePayment) >= 3
BuildRequires: perl(Business::OnlinePayment::HTTPS) >= 0.06
BuildRequires: perl(CGI)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: rpm-macros-rpmforge
Requires: perl
BuildRequires: perl(Business::OnlinePayment) >= 3
BuildRequires: perl(Business::OnlinePayment::HTTPS) >= 0.06
BuildRequires: perl(CGI)
BuildRequires: perl(Digest::MD5)
Requires: rpm-macros-rpmforge


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module is a back end driver that implements the interface specified by
Business::OnlinePayment to support payment handling via the PayPal's Payflow
Pro Internet payment solution.

See Business::OnlinePayment for details on the interface this modules supports.

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
%dir %{perl_vendorlib}/Business/
%{perl_vendorlib}/Business/*

%changelog
* Tue Nov 17 2009 Steve Huff <shuff@vecna.org> - 1.01-1
- Initial package.

