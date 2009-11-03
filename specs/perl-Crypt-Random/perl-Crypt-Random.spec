# $Id$
# Authority: dries
# Upstream: Vipul Ved Prakash <mail$vipul,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Crypt-Random

Summary: Cryptographically Secure, True Random Number Generator
Name: perl-Crypt-Random
Version: 1.25
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Random/

Source: http://www.cpan.org/modules/by-module/Crypt/Crypt-Random-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Crypt::Random is an interface module to the /dev/random device found on most
modern Unix systems. The /dev/random driver gathers environmental noise from
various non-deterministic sources including inter-keyboard timings and
inter-interrupt timings that occur within the operating system environment.

The /dev/random driver maintains an estimate of true randomness in the pool and
decreases it every time random strings are requested for use. When the estimate
goes down to zero, the routine blocks and waits for the occurrence of
non-deterministic events to refresh the pool.

The /dev/random kernel module also provides another interface, /dev/urandom,
that does not wait for the entropy-pool to recharge and returns as many bytes
as requested. /dev/urandom is considerably faster at generation compared to
/dev/random, which should be used only when very high quality randomness is
desired.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{_bindir}/makerandom
%{perl_vendorlib}/Crypt/Random.pm
%{perl_vendorlib}/Crypt/Random

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.25-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Initial package.
