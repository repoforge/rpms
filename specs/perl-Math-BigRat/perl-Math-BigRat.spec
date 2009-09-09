# $Id$
# Authority: dag
# Upstream: Tels <nospam-abuse$bloodgate,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-BigRat

Summary: Arbitrary big rational numbers
Name: perl-Math-BigRat
Version: 0.23
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-BigRat/

Source: http://www.cpan.org/modules/by-module/Math/Math-BigRat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Math::BigInt) >= 1.88
Requires: perl >= 0:5.6.0

%description
Arbitrary big rational numbers.

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
%doc BUGS CHANGES INSTALL LICENSE MANIFEST MANIFEST.SKIP META.yml README SIGNATURE TODO
%doc %{_mandir}/man3/Math::BigRat.3pm*
%dir %{perl_vendorlib}/Math/
#%{perl_vendorlib}/Math/BigRat/
%{perl_vendorlib}/Math/BigRat.pm

%changelog
* Wed Sep  9 2009 Christoph Maser <cmr@financial.com> - 0.23-1
- Updated to version 0.23.

* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.22-1
- Initial package. (using DAR)
