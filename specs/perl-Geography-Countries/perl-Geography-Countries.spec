# $Id$
# Authority: dag
# Upstream: Nigel Wetters <nigel$wetters,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geography-Countries

Summary: Classes for 2-letter, 3-letter, and numerical codes for countries
Name: perl-Geography-Countries
Version: 2009041301
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geography-Countries/

Source: http://www.cpan.org/modules/by-module/Geography/Geography-Countries-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503
Obsoletes: perl(IP::Country) <= 2.08

%description
This module maps country names, and their 2-letter, 3-letter and
numerical codes, as defined by the ISO-3166 maintenance agency [1],
and defined by the UNSD.

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
%doc MANIFEST
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Geography/
%{perl_vendorlib}/Geography/Countries.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 2009041301-1
- Updated to version 2009041301.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-2.2
- Rebuild for Fedora Core 5.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 1.4-2
- Cosmetic cleanup.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Obsolete older perl-IP-Country package.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
