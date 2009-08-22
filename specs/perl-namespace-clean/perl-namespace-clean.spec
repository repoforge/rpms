# $Id$
# Authority: dag
# Upstream: Robert Sedlacek <rs$474,at>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name namespace-clean

Summary: Keep imports and functions out of your namespace
Name: perl-namespace-clean
Version: 0.11
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/namespace-clean/

Source: http://www.cpan.org/modules/by-module/namespace/namespace-clean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
# From yaml build_requires
BuildRequires: perl(FindBin)
BuildRequires: perl(Test::More)
# From yaml requires
BuildRequires: perl(B::Hooks::EndOfScope) >= 0.07
BuildRequires: perl(Symbol)

%description
Keep imports and functions out of your namespace.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/namespace::clean.3pm*
%dir %{perl_vendorlib}/namespace/
#%{perl_vendorlib}/namespace/clean/
%{perl_vendorlib}/namespace/clean.pm

%changelog
* Sat Aug 22 2009 Christoph Maser <cmr@financial.com> - 0.11-2
- Fix dependencies

* Fri May 29 2009 Christoph Maser <cmr@financial.com> - 0.11-1
- Update to version 0.11.

* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
