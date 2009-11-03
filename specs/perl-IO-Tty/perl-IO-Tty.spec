# $Id$
# Authority: dries
# Upstream: Roland Giersig <RGiersig$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Tty

Summary: Interface to pseudo Tty
Name: perl-IO-Tty
Version: 1.08
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Tty/

Source: http://www.cpan.org/modules/by-module/IO/IO-Tty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
IO::Tty and IO::Pty provide an interface to pseudo ttys.

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
%{_mandir}/man3/*
%dir %{perl_vendorarch}/IO/
%{perl_vendorarch}/IO/Pty.pm
%{perl_vendorarch}/IO/Tty.pm
%{perl_vendorarch}/IO/Tty/
%dir %{perl_vendorarch}/auto/IO/
%{perl_vendorarch}/auto/IO/Tty/

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 1.08-1
- Updated to version 1.08.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.07-1
- Updated to release 1.07.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.04-1
- Updated to release 1.04.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.02-1.2
- Rebuild for Fedora Core 5.

* Wed Jun 16 2004 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
