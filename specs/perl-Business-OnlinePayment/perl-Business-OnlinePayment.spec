# $Id$
# Authority: shuff
# Upstream: Ivan Kohler <ivan-pause$420,am>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Business-OnlinePayment

Summary: Perl extension for online payment processing
Name: perl-%{real_name}
Version: 3.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-OnlinePayment/

Source: http://search.cpan.org/CPAN/authors/id/I/IV/IVAN/Business-OnlinePayment-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Tie::IxHash)
BuildRequires: perl(URI::Escape)
BuildRequires: rpm-macros-rpmforge
BuildRequires: %{name}-alternative >= %{version}
Requires: perl
Requires: perl(Tie::IxHash)
Requires: perl(URI::Escape)
Requires: rpm-macros-rpmforge
Requires: %{name}-alternative >= %{version}


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Business::OnlinePayment is a generic module for processing payments through
online credit card processors, electronic cash systems, etc.

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
* Tue Nov 17 2009 Steve Huff <shuff@vecna.org> - 3.00-1
- Initial package.

