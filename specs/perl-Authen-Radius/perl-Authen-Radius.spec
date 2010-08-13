# $Id$
# Authority: dag
# Upstream: Andrew Zhilenko <andrew$ti,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Authen-Radius

Summary: Perl module that provides simple Radius client facilities
Name: perl-Authen-Radius
Version: 0.13
Release: 1%{?dist}
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Authen-Radius/

#Source: http://www.cpan.org/modules/by-module/Authen/Authen-Radius-%{version}.tar.gz
Source: http://www.cpan.org/modules/by-module/Authen/RadiusPerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Authen::Radius is a perl module that provides simple Radius client facilities.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Authen::Radius.3pm*
%dir %{perl_vendorlib}/Authen/
#%{perl_vendorlib}/Authen/Radius/
%{perl_vendorlib}/Authen/Radius.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
