# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-IRC-Service

Summary: Event driven IRC Services module for POE
Name: perl-POE-Component-IRC-Service
Version: 0.994
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-IRC-Service/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-IRC-Service-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
POE::Component::IRC::Service is a POE (Perl Object Environment) component 
which provides a convenient way for POE applications to create an IRC Service.

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
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/IRC/
%{perl_vendorlib}/POE/Component/IRC/Service.pm
%{perl_vendorlib}/POE/Component/IRC/Service/
%dir %{perl_vendorlib}/POE/Filter/
%{perl_vendorlib}/POE/Filter/CTCP/
%{perl_vendorlib}/POE/Filter/IRC/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.994-1
- Updated to version 0.994.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.993-1
- Updated to release 0.993.

* Thu Jul 5 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 0.991-1
- Updated to latest upstream version { old source not available }

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.99-1
- Initial package.
