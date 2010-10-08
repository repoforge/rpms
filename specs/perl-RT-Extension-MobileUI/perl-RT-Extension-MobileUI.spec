# $Id$
# Authority: shuff
# Upstream: Jesse Vincent <jesse$bestpractical,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name RT-Extension-MobileUI

Summary: A phone friendly web interface for RT
Name: perl-RT-Extension-MobileUI
Version: 0.97
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RT-Extension-MobileUI/

Source: http://search.cpan.org/CPAN/authors/id/J/JE/JESSE/RT-Extension-MobileUI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(RT) >= 3.8.3

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This RT extension adds a mobile interface for RT.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install DESTDIR="%{buildroot}"
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/RT/Extension/MobileUI.pm
#%{perl_vendorlib}/RT/Extension/MobileUI/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Tue Sep 28 2010 Steve Huff <shuff@vecna.org> - 0.97-1
- Initial package.
