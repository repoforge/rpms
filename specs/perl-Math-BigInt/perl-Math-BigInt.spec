# $Id$
# Authority: dag
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BigInt

Summary: Arbitrary size integer/float math package
Name: perl-Math-BigInt
Version: 1.89
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BigInt/

Source: http://www.cpan.org/modules/by-module/Math/Math-BigInt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.006
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.006

%description
Arbitrary size integer/float math package.

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES CREDITS HISTORY INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO examples/
%doc %{_mandir}/man3/Math::BigFloat.3pm*
%doc %{_mandir}/man3/Math::BigInt.3pm*
%doc %{_mandir}/man3/Math::BigInt::*.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/BigInt/
%{perl_vendorlib}/Math/BigFloat.pm
%{perl_vendorlib}/Math/BigInt.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 1.89-1
- Initial package. (using DAR)
