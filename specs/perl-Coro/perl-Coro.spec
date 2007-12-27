# $Id$
# Authority: matthias
# Upstream: Marc Lehmann <pcg$goof,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Coro

Summary: Coroutine process abstraction
Name: perl-Coro
Version: 4.34
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Coro/

Source: http://www.cpan.org/modules/by-module/Coro/Coro-%{version}.tar.gz
Patch0: Coro-3.63-noprompt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Event) >= 0.86
BuildRequires: perl(IO::AIO) >= 1.6
# This would introduce a circular dependency since AnyEvent requires Coro...
#BuildRequires: perl(AnyEvent)
# Provided by either perl or perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module collection manages coroutines.
Coroutines are similar to threads but don't run in parallel.


%prep
%setup -n %{real_name}-%{version}
%patch0 -p1 -b .noprompt

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
* Thu Dec 27 2007 Dag Wieers <dag@wieers.com> - 4.34-1
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
