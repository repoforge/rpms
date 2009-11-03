# $Id$
# Authority: dag
# Upstream: Michael R. Davis

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Inverse

Summary: Perl module to calculate geographic distance from a lat & lon pair
Name: perl-Geo-Inverse
Version: 0.05
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Inverse/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Inverse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Geo-Inverse is a Perl module to calculate geographic distance
from a lat & lon pair.

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
%doc CHANGES LICENSE MANIFEST META.yml README
%doc %{_mandir}/man3/Geo::Inverse.3pm*
%dir %{perl_vendorlib}/Geo/
%{perl_vendorlib}/Geo/Inverse.pm

%changelog
* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)
