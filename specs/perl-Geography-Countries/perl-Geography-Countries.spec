# $Id$
# Authority: dag
# Upstream: Nigel Wetters <nigel$wetters,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geography-Countries

Summary: Classes for 2-letter, 3-letter, and numerical codes for countries
Name: perl-Geography-Countries
Version: 1.4
Release: 2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geography-Countries/

Source: http://search.cpan.org/CPAN/authors/id/A/AB/ABIGAIL/Geography-Countries-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
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
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Geography/
%{perl_vendorlib}/Geography/Countries.pm

%changelog
* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 1.4-2
- Cosmetic cleanup.

* Fri Jan 02 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Obsolete older perl-IP-Country package.

* Wed Dec 03 2003 Dag Wieers <dag@wieers.com> - 1.4-0
- Initial package. (using DAR)
