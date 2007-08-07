# $Id$
# Authority: dag
# Upstream: Andy Lester <andy$petdance,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Harness

Summary: Perl module to run Perl standard test scripts with statistics
Name: perl-Test-Harness
Version: 2.64
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Harness/

Source: http://www.cpan.org/modules/by-module/Test/Test-Harness-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Test-Harness is a Perl module to run Perl standard test scripts
with statistics.

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
%doc Changes MANIFEST META.yml NOTES examples/
%doc %{_mandir}/man1/prove.1*
%doc %{_mandir}/man3/*.3pm*
%{_bindir}/prove
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Harness/
%{perl_vendorlib}/Test/Harness.pm

%changelog
* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 2.64-1
- Initial package. (using DAR)
