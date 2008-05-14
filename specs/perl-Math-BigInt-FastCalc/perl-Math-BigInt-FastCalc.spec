# $Id$
# Authority: dag
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BigInt-FastCalc

Summary: Math::BigInt::Calc with some XS for more speed
Name: perl-Math-BigInt-FastCalc
Version: 0.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BigInt-FastCalc/

Source: http://www.cpan.org/modules/by-module/Math/Math-BigInt-FastCalc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 1:5.6.2
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.62
Requires: perl >= 1:5.6.2

%description
Math::BigInt::Calc with some XS for more speed.

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
%doc CHANGES CREDITS MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Math::BigInt::FastCalc.3pm*
%dir %{perl_vendorarch}/auto/Math/
%dir %{perl_vendorarch}/auto/Math/BigInt/
%{perl_vendorarch}/auto/Math/BigInt/FastCalc/
%dir %{perl_vendorarch}/Math/
%dir %{perl_vendorarch}/Math/BigInt/
%{perl_vendorarch}/Math/BigInt/FastCalc.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.19-1
- Updated to release 0.19.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.15-1
- Updated to release 0.15.

* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
