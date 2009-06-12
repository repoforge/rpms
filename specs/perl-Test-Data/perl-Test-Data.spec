# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Data

Summary: Test functions for particular variable types
Name: perl-Test-Data
Version: 1.22
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Data/

Source: http://www.cpan.org/modules/by-module/Test/Test-Data-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Test functions for particular variable types.

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
%doc Changes LICENSE MANIFEST META.yml README examples/
%doc %{_mandir}/man3/Test::Data.3*
%doc %{_mandir}/man3/Test::Data::*.3*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Data/
%{perl_vendorlib}/Test/Data.pm

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 1.22-1
- Updated to version 1.22.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 1.21-1
- Updated to release 1.21.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Initial package.
