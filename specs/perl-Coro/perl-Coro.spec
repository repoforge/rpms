# $Id$
# Authority: shuff
# Upstream: Marc Lehmann <pcg$goof,com>
# ExcludeDist: el2 el3 el4

### perl-AnyEvent is RFX in el5
%{?el5:# Tag: rfx}


%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Coro

Summary: Coroutine process abstraction
Name: perl-Coro
### FIXME: Versions >= 4.31 require perl-BDB and db4 >= 4.4
Version: 6.06
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Coro/

Source: http://www.cpan.org/modules/by-module/Coro/Coro-%{version}.tar.gz
#Patch0: Coro-3.63-noprompt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 5.8.2
BuildRequires: perl(AnyEvent) >= 5
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Guard) >= 0.5
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable) >= 2.15
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(common::sense)
# BuildRequires: perl(AnyEvent::AIO) >= 1
# BuildRequires: perl(AnyEvent::BDB) >= 1
# BuildRequires: perl(BDB)
BuildRequires: perl(EV) >= 3
BuildRequires: perl(Event)
# BuildRequires: perl(IO::AIO) >= 3.1
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.2
Requires: perl(AnyEvent) >= 4.81
# Requires: perl(AnyEvent::AIO) >= 1
# Requires: perl(AnyEvent::BDB) >= 1
# Requires: perl(BDB)
Requires: perl(EV) >= 3
Requires: perl(Event)
Requires: perl(Guard) >= 0.5
# Requires: perl(IO::AIO) >= 3.1
Requires: perl(Scalar::Util)
Requires: perl(Storable) >= 2.15
Requires: perl(Time::HiRes)
Requires: perl(common::sense)

# don't scan the examples for autoreq/prov
%filter_requires_in %{_docdir}
%filter_provides_in %{_docdir}

# remove some bogus autoreq
%filter_from_requires /^perl.*/d

%filter_setup

%description
This module collection manages coroutines.
Coroutines are similar to threads but don't run in parallel.


%prep
%setup -n %{real_name}-%{version}
#%patch0 -p1 -b .noprompt

# fix the shebangs
%{__perl} -pi -e 's|^#!/opt/bin/perl|#!%{__perl}|;' Coro/jit*.pl eg/myhttpd

%build
PERL_MM_USE_DEFAULT="1" CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ eg/ -type f -exec %{__chmod} a-x {} \;

# fix for stupid strip issue
%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes INSTALL MANIFEST META.json README README.linux-glibc doc/ eg/
%doc %{_mandir}/man3/Coro.3pm*
%doc %{_mandir}/man3/Coro::*.3pm*
%{perl_vendorarch}/auto/Coro/
%{perl_vendorarch}/Coro/
%{perl_vendorarch}/Coro.pm

%changelog
* Thu Aug 25 2011 Steve Huff <shuff@vecna.org> - 6.06-1
- Updated to version 6.06.

* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 5.1.62-1
- Updated to version 5.162.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 5.1.51-1
- Updated to version 5.151.

* Thu Dec 18 2008 Dag Wieers <dag@wieers.com> - 5.1-1
- Updated to release 5.1.

* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 4.37-1
- Updated to release 4.37.

* Fri Dec 28 2007 Dag Wieers <dag@wieers.com> - 4.34-1
- Updated to release 4.34.

* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 4.31-1
- Updated to release 4.31.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 4.22-1
- Updated to release 4.22.

* Thu Nov 08 2007 Dag Wieers <dag@wieers.com> - 4.13-1
- Updated to release 4.13.

* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 3.63-1
- Update to 3.63.
- Build require perl(ExtUtils::MakeMaker) for F7.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.9-1
- Initial RPM release, patch to use the ucontext method since the Linux
  specific one doesn't compile on FC5.
