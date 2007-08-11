# $Id$
# Authority: matthias

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Coro

Summary: Coroutine process abstraction
Name: perl-Coro
Version: 3.63
Release: 1
License: Artistic or GPL
Group: Development/Libraries
URL: http://search.cpan.org/~mlehmann/Coro/
Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/Coro-%{version}.tar.gz
Patch0: Coro-3.63-noprompt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: perl(Event) >= 0.86, perl(IO::AIO) >= 1.6
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
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod \
           %{buildroot}%{perl_vendorarch}/auto/*/.packlist


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changes COPYING README
%{perl_vendorarch}/auto/Coro/
%{perl_vendorarch}/Coro/
%{perl_vendorarch}/Coro.pm
%{_mandir}/man3/*


%changelog
* Thu May 31 2007 Matthias Saou <http://freshrpms.net/> 3.63-1
- Update to 3.63.
- Build require perl(ExtUtils::MakeMaker) for F7.

* Wed Apr 19 2006 Matthias Saou <http://freshrpms.net/> 1.9-1
- Initial RPM release, patch to use the ucontext method since the Linux
  specific one doesn't compile on FC5.
