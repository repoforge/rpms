# $Id$
# Authority: dag
# Upstream: Ilya Zakharevich <cpan$ilyaz,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name FreezeThaw

Summary: FreezeThaw module for perl
Name: perl-FreezeThaw
Version: 0.45
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/FreezeThaw/

Source: http://www.cpan.org/modules/by-module/FreezeThaw/FreezeThaw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 2:5.8.0

%description
FreezeThaw module for perl.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/FreezeThaw.3pm*
#%{perl_vendorlib}/FreezeThaw/
%{perl_vendorlib}/FreezeThaw.pm

%changelog
* Sun Jul  5 2009 Christoph Maser <cmr@financial.com> - 0.45-1
- Updated to version 0.45.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 0.43-1
- Cosmetic cleanup.

* Fri Jul 18 2003 Dag Wieers <dag@wieers.com> - 0.43-0
- Initial package. (using DAR)
