# $Id$
# Upstream: Marcus Holland-Moritz <mhx-cpan@gmx.net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Devel-PPPort

Summary: Portability aid for your XS code
Name: perl-Devel-PPPort
Version: 3.19
Release: 1%{?dist}
License: perl
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Devel-PPPort

Source: http://search.cpan.org/CPAN/authors/id/M/MH/MHX/Devel-PPPort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Perl's API has changed over time, gaining new features, new functions, increasing its flexibility, and reducing the impact on the C namespace environment (reduced pollution). The header file written by this module, typically ppport.h, attempts to bring some of the newer Perl API features to older versions of Perl, so that you can worry less about keeping track of old releases, but users can still reap the benefit.

Devel::PPPort contains a single function, called WriteFile. Its only purpose is to write the ppport.h C header file. This file contains a series of macros and, if explicitly requested, functions that allow XS modules to be built using older versions of Perl. Currently, Perl versions from 5.003 to 5.10.0 are supported.

This module is used by h2xs to write the file ppport.h.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%doc %{_mandir}/man3/Devel::PPPort.3pm*
%{perl_vendorarch}/Devel/PPPort.pm
%{perl_vendorarch}/auto/Devel/PPPort/PPPort.bs
%{perl_vendorarch}/auto/Devel/PPPort/PPPort.so

%changelog
* Wed Feb 03 2010 Christoph Maser <cmr@financial.com> - 3.19-1
- initial package

