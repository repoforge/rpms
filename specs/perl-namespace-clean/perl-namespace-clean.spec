# $Id$
# Authority: dag
# Upstream: Robert Sedlacek <rs$474,at>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name namespace-clean

Summary: Keep imports and functions out of your namespace
Name: perl-namespace-clean
Version: 0.08
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/namespace-clean/

Source: http://www.cpan.org/modules/by-module/namespace/namespace-clean-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(FindBin)
#BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::More)

%description
Keep imports and functions out of your namespace.

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
%doc %{_mandir}/man3/namespace::clean.3pm*
%dir %{perl_vendorlib}/namespace/
#%{perl_vendorlib}/namespace/clean/
%{perl_vendorlib}/namespace/clean.pm

%changelog
* Thu Oct 09 2008 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
