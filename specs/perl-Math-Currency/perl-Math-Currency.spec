# $Id$
# Authority: dries
# Upstream: John Peacock <jpeacock$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-Currency

Summary: Exact Currency Math with Formatting and Rounding
Name: perl-Math-Currency
Version: 0.46
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Currency/

Source: http://www.cpan.org/modules/by-module/Math/Math-Currency-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Module::Build)

%description
Exact Currency Math with Formatting and Rounding.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Math::Currency.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/Currency/
%{perl_vendorlib}/Math/Currency.pm

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.46-1
- Updated to release 0.46.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.44-1
- Updated to release 0.44.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.43-1
- Updated to release 0.43.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.42-1
- Initial package.
