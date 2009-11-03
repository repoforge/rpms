# $Id$
# Authority: dag
# Upstream: David A, Golden <dagolden$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Number-Delta

Summary: Compare the difference between numbers against a given tolerance
Name: perl-Test-Number-Delta
Version: 1.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Number-Delta/

Source: http://www.cpan.org/modules/by-module/Test/Test-Number-Delta-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.004
Requires: perl >= 0:5.004

%description
Compare the difference between numbers against a given tolerance.

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
%doc Changes INSTALL LICENSE MANIFEST META.yml README Todo
%doc %{_mandir}/man3/Test::Number::Delta.3pm*
%dir %{perl_vendorlib}/Test/
%dir %{perl_vendorlib}/Test/Number/
#%{perl_vendorlib}/Test/Number/Delta/
%{perl_vendorlib}/Test/Number/Delta.pm

%changelog
* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 1.03-1
- Initial package. (using DAR)
