# $Id$
# Authority: dries
# Upstream: Chip Turner <cturner$pattern,net>
# Upstream: Tels <tels$bloodgate,com>
# Upstream: Greg Sabino Mullane <greg$turnstep,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-GMP

Summary: High speed arbitrary size integer math
Name: perl-Math-GMP
Version: 2.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-GMP/

Source: http://www.cpan.org/modules/by-module/Math/Math-GMP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.61
BuildRequires: perl(Test::More)
BuildRequires: gmp-devel

%description
Math::GMP gives you access to the fast GMP library for fast
big integer math.

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
%doc COPYING.LIB Changes INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Math::GMP.3pm*
%dir %{perl_vendorarch}/auto/Math/
%{perl_vendorarch}/auto/Math/GMP/
%dir %{perl_vendorarch}/Math/
%{perl_vendorarch}/Math/GMP.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.04-1
- Initial package.
