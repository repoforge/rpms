# $Id$
# Authority: dries
# Upstream: David Shao Lin Zhuo <dzhuo$google,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Google-Checkout

Summary: Interface to Google Checkout
Name: perl-Google-Checkout
Version: 1.1.1
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Google-Checkout/

Source: http://www.cpan.org/modules/by-module/Google/Google-Checkout-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Interface to Google Checkout.

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
%doc Changes MANIFEST README examples/
%doc %{_mandir}/man3/Google::Checkout::*.3pm*
%dir %{perl_vendorlib}/Google/
%{perl_vendorlib}/Google/Checkout/
#%{perl_vendorlib}/Google/Checkout.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 1.1.1-1
- Updated to release 1.1.1.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.0.4-1
- Initial package.
