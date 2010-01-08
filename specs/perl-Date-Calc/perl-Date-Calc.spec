# $Id$
# Authority: dag
# Upstream: Steffen Beyer <sb$engelschall,com>

# ExclusiveDist: el3

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Calc

Summary: Gregorian calendar date calculations
Name: perl-Date-Calc
Version: 6.3
Release: 1%{?dist}
License: Artistic/GPL/LGPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Calc/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Date-Calc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Bit::Vector) >= 7.1
BuildRequires: perl(Carp::Clan) >= 6.04
Requires: perl(Bit::Vector) >= 7.1
Requires: perl(Carp::Clan) >= 6.04

%filter_from_requires /^perl*/d
%filter_setup



%description
Gregorian calendar date calculations

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

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
%doc Artistic.txt CHANGES.txt CREDITS.txt EXAMPLES.txt GNU_GPL.txt GNU_LGPL.txt INSTALL.txt MANIFEST README.txt TOOLS.txt examples/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/auto/Date/
%{perl_vendorarch}/Date/

%changelog
* Fri Jan  8 2010 Christoph Maser <cmr@financial.com> - 6.3-1
- Updated to version 6.3.

* Fri Oct 16 2009 Christoph Maser <cmr@financial.com> - 6.0-1
- Updated to version 6.0.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 5.8-1
- Updated to version 5.8.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 5.6-1
- Updated to version 5.6.

* Tue Sep 13 2005 Dag Wieers <dag@wieers.com> - 5.4-1
- Initial package. (using DAR)
