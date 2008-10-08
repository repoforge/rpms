# $Id$
# Authority: dries
# Upstream: Matthew McGillis <mmcgillis$cpan,org>
# Upstream: Phil Lobbes <phil$perkpartners,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Finance-QIF

Summary: Parse and create Quicken Interchange Format files
Name: perl-Finance-QIF
Version: 3.00
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Finance-QIF/

Source: http://www.cpan.org/modules/by-module/Finance/Finance-QIF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Parse and create Quicken Interchange Format files.

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
%doc Changes MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Finance::QIF.3pm*
%dir %{perl_vendorlib}/Finance/
#%{perl_vendorlib}/Finance/QIF/
%{perl_vendorlib}/Finance/QIF.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 3.00-1
- Updated to release 3.00.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 2.07-1
- Updated to release 2.07.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 2.06-1
- Initial package.
