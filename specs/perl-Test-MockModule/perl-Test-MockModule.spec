# $Id$
# Authority: dag
# Upstream: Simon Flack <sf AT flacks,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-MockModule

Summary: Perl module to override subroutines in a module for unit testing
Name: perl-Test-MockModule
Version: 0.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-MockModule/

Source: http://www.cpan.org/modules/by-module/Test/Test-MockModule-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Test-MockModule is a Perl module to override subroutines in a module
for unit testing.

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
%doc %{_mandir}/man3/Test::MockModule.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/MockModule.pm

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
