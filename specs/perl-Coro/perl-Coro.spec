# $Id$
# Authority: matthias
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Coro
%define real_version 5.162

Summary: Coroutine process abstraction
Name: perl-Coro
### FIXME: Versions >= 4.31 require perl-BDB and db4 >= 4.4
Version: 5.1.62
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Coro/

Source: http://www.cpan.org/modules/by-module/Coro/Coro-%{real_version}.tar.gz
#Patch0: Coro-3.63-noprompt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# From yaml requires
BuildRequires: perl(AnyEvent) >= 4.81
BuildRequires: perl(Guard) >= 0.5
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Storable) >= 2.15
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(common::sense)
# From yaml recommends
BuildRequires: perl(AnyEvent::AIO)
BuildRequires: perl(AnyEvent::BDB)
BuildRequires: perl(BDB)
BuildRequires: perl(EV)
BuildRequires: perl(Event)
BuildRequires: perl(IO::AIO)
Requires: perl(AnyEvent) >= 4.81
Requires: perl(Guard) >= 0.5
Requires: perl(Scalar::Util)
Requires: perl(Storable) >= 2.15
Requires: perl(Time::HiRes)
Requires: perl(common::sense)
AutoReq: no

%description
This module collection manages coroutines.
Coroutines are similar to threads but don't run in parallel.


%prep
%setup -n %{real_name}-%{real_version}
#%patch0 -p1 -b .noprompt

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find doc/ eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Changes INSTALL MANIFEST META.yml README README.linux-glibc doc/ eg/
%doc %{_mandir}/man3/Coro.3pm*
%doc %{_mandir}/man3/Coro::*.3pm*
%{perl_vendorarch}/auto/Coro/
%{perl_vendorarch}/Coro/
%{perl_vendorarch}/Coro.pm

%changelog
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
