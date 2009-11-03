# $Id$
# Authority: dries
# Upstream: <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Locale-Maketext-Fuzzy

Summary: Maketext from already interpolated strings
Name: perl-Locale-Maketext-Fuzzy
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Locale-Maketext-Fuzzy/

Source: http://www.cpan.org/modules/by-module/Locale/Locale-Maketext-Fuzzy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is the README file for Locale::Maketext::Fuzzy, a subclass of
Locale::Maketext with additional support for localizing messages that
already contains interpolated variables.

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
%doc Changes MANIFEST README SIGNATURE
%doc %{_mandir}/man3/Locale::Maketext::Fuzzy.3pm*
%dir %{perl_vendorlib}/Locale/
%dir %{perl_vendorlib}/Locale/Maketext/
#%{perl_vendorlib}/Locale/Maketext/Fuzzy/
%{perl_vendorlib}/Locale/Maketext/Fuzzy.pm

%changelog
* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.10-1
- Updated to release 0.10.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
