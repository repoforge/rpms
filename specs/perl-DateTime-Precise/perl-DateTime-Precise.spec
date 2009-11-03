# $Id$
# Authority: dag
# Upstream: Blair Zajac <blair$orcaware,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DateTime-Precise

Summary: Perform common time and date operations with additional GPS operations
Name: perl-DateTime-Precise
Version: 1.05
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Precise/

Source: http://www.cpan.org/modules/by-module/DateTime/DateTime-Precise-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

### Provides required by package itself
Provides: perl(DateTime::Math/bigfloat.pl)
Provides: perl(DateTime::Math/bigint.pl)

%description
Perform common time and date operations with additional GPS operations.

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
%doc CHANGES MANIFEST README
%doc %{_mandir}/man3/DateTime::Precise.3pm*
%dir %{perl_vendorlib}/DateTime/
#%{perl_vendorlib}/DateTime/Precise/
%{perl_vendorlib}/DateTime/Precise.pm
%dir %{perl_vendorlib}/DateTime/Math/
%{perl_vendorlib}/DateTime/Math/bigfloat.pl
%{perl_vendorlib}/DateTime/Math/bigint.pl

%changelog
* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 1.05-2
- Added selfcontained provides.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 1.05-1
- Initial package. (using DAR)
