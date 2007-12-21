# $Id$
# Authority: dag
# Upstream: Benjamin Trott <ben$rhumba.pair,com>
# Upstream: Tels <nospam-abuse@$loodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BigInt-Pari

Summary: Use Math::Pari for Math::BigInt routines
Name: perl-Math-BigInt-Pari
Version: 1.13
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BigInt-Pari/

Source: http://www.cpan.org/modules/by-module/Math/Math-BigInt-Pari-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.2, perl(ExtUtils::MakeMaker)
#BuildRequires: perl(Test::More) >= 0.62
Requires: perl >= 1:5.6.2

%description
Use Math::Pari for Math::BigInt routines.

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
%doc CHANGES LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/Math::BigInt::Pari.3pm*
%dir %{perl_vendorlib}/Math/
%dir %{perl_vendorlib}/Math/BigInt/
%{perl_vendorlib}/Math/BigInt/Pari.pm

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 1.13-1
- Updated to release 1.13.

* Thu May 31 2007 Dag Wieers <dag@wieers.com> - 1.12-1
- Initial package. (using DAR)
