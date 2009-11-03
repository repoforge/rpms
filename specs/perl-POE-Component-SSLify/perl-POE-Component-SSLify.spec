# $Id$
# Authority: dries
# Upstream: Apocalypse <perl$0ne,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-SSLify

Summary: Use SSL in POE
Name: perl-POE-Component-SSLify
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-SSLify/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-SSLify-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module makes Net::SSLeay's SSL sockets behave with POE.

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
%doc %{_mandir}/man3/POE::Component::SSLify.3pm*
%doc %{_mandir}/man3/POE::Component::SSLify::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/SSLify/
%{perl_vendorlib}/POE/Component/SSLify.pm

%changelog
* Fri Jul  3 2009 Christoph Maser <cmr@financial.com> - 0.15-1
- Updated to version 0.15.

* Fri Dec 14 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Updated to release 0.08.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Initial package.
