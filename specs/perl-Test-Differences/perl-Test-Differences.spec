# $Id$
# Authority: dries
# Upstream: Barrie Slaymaker <barries$slaysys,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Differences

Summary: Test strings and data structures and show differences if not ok
Name: perl-Test-Differences
Version: 0.500
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Differences/

Source: http://www.cpan.org/modules/by-module/Test/Test-Differences-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Diff) >= 0.35
Requires: perl(Test::More)
Requires: perl(Text::Diff) >= 0.35

%filter_from_requires /^perl*/d
%filter_setup

%description
Test strings and data structures and show differences if not ok.

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
%doc Changes MANIFEST 
%doc %{_mandir}/man3/Test::Differences.3pm*
%dir %{perl_vendorlib}/Test/
#%{perl_vendorlib}/Test/Differences/
%{perl_vendorlib}/Test/Differences.pm

%changelog
* Thu Oct 22 2009 Christoph Maser <cmr@financial.com> - 0.500-1
- Updated to version 0.500.

* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.4801-1
- Updated to version 0.4801.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.47-1
- Initial package.
