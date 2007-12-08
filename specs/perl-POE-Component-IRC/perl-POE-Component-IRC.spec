# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-IRC

Summary: POE component for IRC
Name: perl-POE-Component-IRC
Version: 5.38
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-IRC/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-IRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More) >= 0.47

%description
POE::Component::IRC is a POE (Perl Object Environment) component
which provides a convenient way for POE applications to create a tiny
IRC client session and send and receive IRC events through it. If that
first sentence was a bit too much, go read the POE documentation over
and over until it makes some sense.

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
find docs/ examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README docs/ examples/
%doc %{_mandir}/man3/POE::Component::IRC.3pm*
%doc %{_mandir}/man3/POE::Component::IRC::*.3pm*
%doc %{_mandir}/man3/POE::Filter::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/IRC/
%{perl_vendorlib}/POE/Component/IRC.pm
%{perl_vendorlib}/POE/Filter/

%changelog
* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 5.38-1
- Updated to release 5.38.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 5.36-1
- Updated to release 5.36.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 5.32-1
- Updated to release 5.32.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 5.24-1
- Updated to release 5.24.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 5.18-1
- Updated to release 5.18.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 5.11-1
- Updated to release 5.11.

* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 5.04-1
- Updated to release 5.04.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 5.03-1
- Updated to release 5.03.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 4.91-1
- Updated to release 4.91.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 4.80-1
- Updated to release 4.80.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 4.77-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 4.77-1
- Updated to release 4.77.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 4.75-1
- Initial package.
