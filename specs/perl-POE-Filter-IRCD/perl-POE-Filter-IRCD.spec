# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Filter-IRCD

Summary: POE filter for the IRC protocol
Name: perl-POE-Filter-IRCD
Version: 2.35
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Filter-IRCD/

Source: http://www.cpan.org/modules/by-module/POE/POE-Filter-IRCD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
This module implements a POE filter for the IRC protocol.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/POE::Filter::IRCD.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Filter/
#%{perl_vendorlib}/POE/Filter/IRCD/
%{perl_vendorlib}/POE/Filter/IRCD.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 2.35-1
- Updated to release 2.35.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 2.34-1
- Updated to release 2.34.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 2.32-1
- Updated to release 2.32.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 2.2-1
- Updated to release 2.2.

* Fri Sep 29 2006 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Updated to release 2.1.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.7-1
- Updated to release 1.7.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.5-1
- Updated to release 1.5.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Initial package.
