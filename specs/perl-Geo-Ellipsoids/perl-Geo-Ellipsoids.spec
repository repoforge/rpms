# $Id$
# Authority: dag
# Upstream: Michael R. Davis <account=>perl,tld=>com,domain=>michaelrdavis>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-Ellipsoids

Summary: Perl module with standard Geo:: ellipsoid a, b, f and 1/f values
Name: perl-Geo-Ellipsoids
Version: 0.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-Ellipsoids/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-Ellipsoids-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Geo-Ellipsoids is a Perl module with standard Geo::
ellipsoid a, b, f and 1/f values.

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
%doc %{_mandir}/man3/Geo::Ellipsoids.3pm*
%dir %{perl_vendorlib}/Geo/
%{perl_vendorlib}/Geo/Ellipsoids.pm

%changelog
* Mon Jun 23 2008 Dag Wieers <dag@wieers.com> - 0.16-1
- Updated to release 0.16.

* Tue May 01 2007 Dag Wieers <dag@wieers.com> - 0.14-1
- Initial package. (using DAR)
