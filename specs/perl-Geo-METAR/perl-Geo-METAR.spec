# $Id$
# Authority: dries
# Upstream: Koos van den Hout <koos$kzdoos,xs4all,nl>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Geo-METAR

Summary: Accesses Aviation Weather Information
Name: perl-Geo-METAR
Version: 1.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Geo-METAR/

Source: http://www.cpan.org/modules/by-module/Geo/Geo-METAR-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
With this module, you can access Aviation Weather Information.

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
%doc MANIFEST README TODO examples/
%doc %{_mandir}/man3/Geo::METAR.3pm*
%dir %{perl_vendorlib}/Geo/
#%{perl_vendorlib}/Geo/METAR/
%{perl_vendorlib}/Geo/METAR.pm

%changelog
* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 1.15-1
- Updated to release 1.15.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
