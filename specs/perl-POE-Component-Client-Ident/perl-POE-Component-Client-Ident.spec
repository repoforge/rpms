# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-Client-Ident

Summary: Component that provides non-blocking ident lookups to your sessions
Name: perl-POE-Component-Client-Ident
Version: 1.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-Client-Ident/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-Client-Ident-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
POE::Component::Client::Ident is a POE (Perl Object Environment) component which
provides a convenient way for POE applications to perform non-blocking Ident (auth/tap)
protocol remote username lookups.

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
%doc %{_mandir}/man3/POE::Component::Client::Ident.3pm*
%doc %{_mandir}/man3/POE::Component::Client::Ident::*.3pm*
%doc %{_mandir}/man3/POE::Filter::Ident.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%dir %{perl_vendorlib}/POE/Component/Client/
%{perl_vendorlib}/POE/Component/Client/Ident/
%{perl_vendorlib}/POE/Component/Client/Ident.pm
%{perl_vendorlib}/POE/Filter/Ident.pm

%changelog
* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.08-1
- Updated to release 1.08.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 1.07-1
- Updated to release 1.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Updated to release 1.05.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.03-1
- Updated to release 1.03.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Updated to release 1.02.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.9-1
- Updated to release 0.9.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.8-1
- Initial package.
