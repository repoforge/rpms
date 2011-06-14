# $Id:$
# Authority: cmr
# Upstream: Marc Lehmann <schmorp@schmorp.de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name EV

Summary: Perl interface to libev
Name: perl-EV
Version: 4.03
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/EV/

Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/EV-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(common::sense)
Requires: perl(common::sense)

%filter_from_requires /^perl*/d
%filter_setup

%description
This module provides an interface to libev
(http://software.schmorp.de/pkg/libev.html).

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" PERL_MM_USE_DEFAULT="1" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes MANIFEST META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorarch}/auto/EV/
%{perl_vendorarch}/EV.pm
%{perl_vendorarch}/EV

%changelog
* Tue Jun 14 2011 Steve Huff <shuff@vecna.org> - 4.03-1
- Updated to version 4.03.
- Split off 3.9 specfile for convenience.

* Tue Jan  5 2010 Christoph Maser <cmr@financial.com> - 3.9-1
- Updated to version 3.9.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 3.8-1
- Updated to version 3.8.

* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 3.7-1
- Updated to version 3.7.

* Wed Jul 08 2009 Christoph Maser <cmr@financial.com> - 3.6-1
- Initial package. (using DAR)
