# $Id$
# Authority: dries
# Upstream: Joshua Nathaniel Pritikin <jpritikin$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Event

Summary: Generic Perl Event Loop
Name: perl-Event
Version: 1.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Event/

Source: http://search.cpan.org/CPAN/authors/id/J/JP/JPRIT/Event-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test) >= 1
Requires: perl(Test) >= 1

%filter_from_requires /^perl*/d
%filter_setup


%description
This extension aims to provide an simple and optimized event loop for
a broad class of applications.

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

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCE ChangeLog INSTALL MANIFEST MANIFEST.SKIP META.yml README TODO
%doc %{_mandir}/man3/Event.3pm*
%doc %{_mandir}/man3/Event::*.3pm*
%{perl_vendorarch}/auto/Event/
%{perl_vendorarch}/Event/
%{perl_vendorarch}/Event.pm
%{perl_vendorarch}/Event.pod

%changelog
* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 1.13-1
- Updated to version 1.13.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 1.12-1
- Updated to version 1.12.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.11-1
- Updated to release 1.11.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 1.10-1
- Updated to release 1.10.

* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.09-1
- Updated to release 1.09.

* Tue Nov 14 2006 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Updated to release 1.08.

* Fri Mar 17 2006 Matthias Saou <http://freshrpms.net/> 1.0.6-2
- Release bump to drop the disttag number in FC5 build.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.06-1
- Updated to release 1.06.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Initial package.
