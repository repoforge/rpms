# $Id$
# Authority: shuff
# Upstream: Jean Forget <j2n-forget$wanadoo,fr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Acme-MetaSyntactic-soviet

Summary: NATO codenames for Soviet-designed equipment
Name: perl-%{real_name}
Version: 0.01
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Acme-MetaSyntactic-soviet/

Source: http://search.cpan.org/CPAN/authors/id/J/JF/JFORGET/Acme-MetaSyntactic-soviet-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Acme::MetaSyntactic::MultiList)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Acme::MetaSyntactic::MultiList)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Some codenames given by NATO to Soviet-designed aircraft, missiles, radars and other electronic systems. The various categories and sub-categories are

* electronic
* electronic/radars
* electronic/misc
* vehicles
* vehicles/aircraft
* vehicles/helicopters
* vehicles/missiles
* vehicles/error

The default category is 'electronic'.

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
%dir %{perl_vendorlib}/Acme/MetaSyntactic/
%{perl_vendorlib}/Acme/MetaSyntactic/*

%changelog
* Mon Nov 16 2009 Steve Huff <shuff@vecna.org> - 0.01-1
- Initial package.
