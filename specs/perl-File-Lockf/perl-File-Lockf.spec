# $Id$
# Authority: dries
# Upstream: Paul B. Henson <henson$acm,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name File-Lockf

Summary: Interface to the lockf system call
Name: perl-File-Lockf
Version: 0.20
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/File-Lockf/

Source: http://www.cpan.org/modules/by-module/File/File-Lockf-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
File-Lockf is a wrapper around the lockf system call. Perl supports the
flock system call natively, but that does not acquire network locks. Perl
also supports the fcntl system call, but that is somewhat ugly to
use. There are other locking modules available for Perl, but none of them
provided what I wanted -- a simple, clean interface to the lockf system
call, without any bells or whistles getting in the way.

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
%doc README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/File/
%{perl_vendorarch}/File/lockf.pm
%dir %{perl_vendorarch}/auto/File/
%{perl_vendorarch}/auto/File/lockf/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
