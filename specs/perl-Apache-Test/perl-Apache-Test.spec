# $Id$
# Authority: dag
# Upstream: Fred Moyer <fred$redhotpenguin,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Apache-Test

Summary: Perl module contains a Test.pm wrapper with helpers for testing Apache
Name: perl-Apache-Test
Version: 1.30
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Apache-Test/

Source: http://www.cpan.org/modules/by-module/Apache/Apache-Test-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Apache-Test is a Perl module contains a Test.pm wrapper with helpers
for testing Apache.

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
%doc Changes INSTALL LICENSE MANIFEST META.yml README ToDo install-pl
%doc %{_mandir}/man3/Apache::*.3pm*
%doc %{_mandir}/man3/Bundle::ApacheTest.3pm*
%{perl_vendorlib}/Apache/
%dir %{perl_vendorlib}/Bundle/
%{perl_vendorlib}/Bundle/ApacheTest.pm

%changelog
* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.29-1
- Initial package. (using DAR)
