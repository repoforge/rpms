# $Id$
# Authority: dries
# Upstream: Hogeist <mahito$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-GoogleAccount

Summary: Simple Authentication with Google Account
Name: perl-Authen-GoogleAccount
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-GoogleAccount/

Source: http://www.cpan.org/modules/by-module/Authen/Authen-GoogleAccount-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Simple Authentication with Google Account.

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
%doc %{_mandir}/man3/Authen::GoogleAccount.3pm*
%dir %{perl_vendorlib}/Authen/
#%{perl_vendorlib}/Authen/GoogleAccount/
%{perl_vendorlib}/Authen/GoogleAccount.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Updated to release 0.02.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.01-1
- Initial package.
