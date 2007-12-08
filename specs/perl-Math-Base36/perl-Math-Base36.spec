# $Id$
# Authority: dries
# Upstream: Rune Henssel <perl$henssel,dk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Base36

Summary: Encoding and decoding of base36 strings
Name: perl-Math-Base36
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Base36/

Source: http://www.cpan.org/modules/by-module/Math/Math-Base36-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
Encoding and decoding of base36 strings.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Math::Base36.3pm*
%dir %{perl_vendorlib}/Math/
#%{perl_vendorlib}/Math/Base36/
%{perl_vendorlib}/Math/Base36.pm

%changelog
* Sat Dec 08 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Updated to release 0.05.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Updated to release 0.04.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
