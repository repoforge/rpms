# $Id$
# Authority: cmr
# Upstream: Ivan Tubert-Brohman <itub$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Chemistry-Ring

Summary: Perl module named Chemistry-Ring
Name: perl-Chemistry-Ring
Version: 0.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Chemistry-Ring/

Source: http://www.cpan.org/modules/by-module/Chemistry/Chemistry-Ring-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Chemistry::Mol) >= 0.24
BuildRequires: perl(Statistics::Regression) >= 0.15

%description
perl-Chemistry-Ring is a Perl module.

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Chemistry::Ring.3pm*
%doc %{_mandir}/man3/Chemistry::Ring::Find.3pm*
%dir %{perl_vendorlib}/Chemistry/
%{perl_vendorlib}/Chemistry/Ring/Find.pm
%{perl_vendorlib}/Chemistry/Ring.pm

%changelog
* Thu Jul 16 2009 Unknown - 0.20-1
- Initial package. (using DAR)
