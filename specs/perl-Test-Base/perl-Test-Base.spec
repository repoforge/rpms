# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Base

Summary: Data driven testing framework for perl
Name: perl-Test-Base
Version: 0.58
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Base/

Source: http://www.cpan.org/modules/by-module/Test/Test-Base-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 1:5.6.1

%description
A data driven testing framework.

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
%doc %{_mandir}/man3/Module::Install::TestBase.3pm*
%doc %{_mandir}/man3/Test::Base.3pm*
%doc %{_mandir}/man3/Test::Base::Filter.3pm*
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
%{perl_vendorlib}/Module/Install/TestBase.pm
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Base.pm
%{perl_vendorlib}/Test/Base/

%changelog
* Fri Jun 12 2009 Christoph Maser <cmr@financial.com> - 0.58-1
- Updated to version 0.58.

* Wed Nov 14 2007 Dag Wieers <dag@wieers.com> - 0.54-1
- Updated to release 0.54.

* Wed Jan 03 2007 Dries Verachtert <dries@ulyssis.org> - 0.53-1
- Updated to release 0.53.

* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.52-1
- Updated to release 0.52.

* Mon Apr 24 2006 Dag Wieers <dag@wieers.com> - 0.50-1
- Initial package.
