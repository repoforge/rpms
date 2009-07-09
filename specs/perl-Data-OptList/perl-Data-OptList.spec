# $Id$
# Authority: dag
# Upstream: Ricardo SIGNES <rjbs$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-OptList

Summary: Perl module to parse and validate simple name/value option pairs
Name: perl-Data-OptList
Version: 0.104
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-OptList/

Source: http://www.cpan.org/modules/by-module/Data/Data-OptList-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Data-OptList is a Perl module to parse and validate simple
name/value option pairs.

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
%doc Changes LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Data::OptList.3pm*
%dir %{perl_vendorlib}/Data/
#%{perl_vendorlib}/Data/OptList/
%{perl_vendorlib}/Data/OptList.pm

%changelog
* Thu Jul  9 2009 Christoph Maser <cmr@financial.com> - 0.104-1
- Updated to version 0.104.

* Tue Nov 06 2007 Dag Wieers <dag@wieers.com> - 0.103-1
- Updated to release 0.103.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 0.101-1
- Initial package. (using DAR)
