# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name YAML-Tests

Summary: Common Test Suite for Perl YAML Implementations
Name: perl-YAML-Tests
Version: 0.06
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/YAML-Tests/

Source: http://www.cpan.org/modules/by-module/YAML/YAML-Tests-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.5.3
Requires: perl >= 0:5.5.3

%description
Common Test Suite for Perl YAML Implementations.

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
%doc %{_mandir}/man1/yt.1*
%doc %{_mandir}/man3/Module::Install::YAML::Tests.3pm*
%doc %{_mandir}/man3/YAML::Tests.3pm*
%{_bindir}/yt
%dir %{perl_vendorlib}/Module/
%dir %{perl_vendorlib}/Module/Install/
%dir %{perl_vendorlib}/Module/Install/YAML/
%{perl_vendorlib}/Module/Install/YAML/Tests.pm
%dir %{perl_vendorlib}/YAML/
%{perl_vendorlib}/YAML/Tests/
%{perl_vendorlib}/YAML/Tests.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
