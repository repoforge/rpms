# $Id$
# Authority: dries
# Upstream: Chris Williams <chris$bingosnet,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-IRC

Summary: Fully event-driven IRC client module
Name: perl-POE-Component-IRC
Version: 6.18
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-IRC/

Source: http://search.cpan.org/CPAN/authors/id/H/HI/HINRIK/POE-Component-IRC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Encode)
BuildRequires: perl(Encode::Guess)
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(POE) >= 0.3202
BuildRequires: perl(POE::Component::Pluggable) >= 1.24
BuildRequires: perl(POE::Driver::SysRW)
BuildRequires: perl(POE::Filter::IRCD) >= 2.42
BuildRequires: perl(POE::Filter::Line)
BuildRequires: perl(POE::Filter::Stackable)
BuildRequires: perl(POE::Filter::Stream)
BuildRequires: perl(POE::Wheel::ReadWrite)
BuildRequires: perl(POE::Wheel::SocketFactory)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl >= 5.8.0
Requires: perl(Encode)
Requires: perl(Encode::Guess)
Requires: perl(POE) >= 0.3202
Requires: perl(POE::Component::Pluggable) >= 1.24
Requires: perl(POE::Driver::SysRW)
Requires: perl(POE::Filter::IRCD) >= 2.42
Requires: perl(POE::Filter::Line)
Requires: perl(POE::Filter::Stackable)
Requires: perl(POE::Filter::Stream)
Requires: perl(POE::Wheel::ReadWrite)
Requires: perl(POE::Wheel::SocketFactory)
Requires: perl >= 5.8.0

%filter_from_requires /^perl*/d
%filter_setup

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
%doc Changes LICENSE MANIFEST META.yml README docs/ examples/
%doc %{_mandir}/man3/POE::Component::IRC.3pm*
%doc %{_mandir}/man3/POE::Component::IRC::*.3pm*
%doc %{_mandir}/man3/POE::Filter::*.3pm*
%dir %{perl_vendorlib}/POE/
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/IRC/
%{perl_vendorlib}/POE/Component/IRC.pm
%{perl_vendorlib}/POE/Filter/

%changelog
* Tue Dec 15 2009 Christoph Maser <cmr@financial.com> - 6.18-1
- Updated to version 6.18.

* Thu Dec 10 2009 Christoph Maser <cmr@financial.com> - 6.16-1
- Updated to version 6.16.

* Thu Sep 10 2009 Christoph Maser <cmr@financial.com> - 6.12-1
- Updated to version 6.12.

* Mon Sep  7 2009 Christoph Maser <cmr@financial.com> - 6.10-1
- Updated to version 6.10.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 6.08-1
- Updated to version 6.08.

* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 5.76-1
- Updated to release 5.76.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 5.70-1
- Updated to release 5.70.

* Thu Feb 21 2008 Dag Wieers <dag@wieers.com> - 5.68-1
- Updated to release 5.68.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 5.52-1
- Updated to release 5.52.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 5.46-1
- Updated to release 5.46.

* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 5.40-1
- Updated to release 5.40.

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
