# $Id$
# Authority: dries
# Upstream: Matt Sergeant <msergeant$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Piece

Summary: Object Oriented time objects
Name: perl-Time-Piece
Version: 1.14
Release: 1
Epoch: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Piece/

Source: http://www.cpan.org/modules/by-module/Time/Time-Piece-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module contains Object Oriented time objects.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Time::Piece.3pm*
%doc %{_mandir}/man3/Time::Seconds.3pm*
%dir %{perl_vendorarch}/auto/Time/
%{perl_vendorarch}/auto/Time/Piece/
%dir %{perl_vendorarch}/Time/
#%{perl_vendorarch}/Time/Piece/
%{perl_vendorarch}/Time/Piece.pm
%{perl_vendorarch}/Time/Seconds.pm

%changelog
* Wed Jun 10 2009 Christoph Maser <cmr@financial.com> - 1.14-1
- Updated to version 1.14.

* Fri Mar 07 2008 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Thu Nov 22 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 1.11-1
- Updated to release 1.11.

* Tue Aug 22 2006 Dag Wieers <dag@wieers.com> - 1:1.09-1
- Revert back to non-developer release 1.09. (Aaron Scamehorn)

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.00_01-1
- Updated to release 2.00_01.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
