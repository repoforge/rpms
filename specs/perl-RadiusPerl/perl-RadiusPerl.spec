# $Id$
# Authority: dag
# Upstream: Andrew Zhilenko <andrew$ti,cz>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name RadiusPerl

Summary: Provide simple Radius client facilities
Name: perl-RadiusPerl
Version: 0.15
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/RadiusPerl/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MANOWAR/RadiusPerl-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

Provides: perl-Authen-Radius = %{version}-%{release}
Obsoletes: perl-Authen-Radius <= %{version}-%{release}

%description
Provide simple Radius client facilities.

%prep
%setup -n Authen-Radius-%{version}

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
%doc Changes INSTALL MANIFEST README install-radius-db.PL
%doc %{_mandir}/man3/Authen::Radius.3pm*
%dir %{perl_vendorlib}/Authen/
#%{perl_vendorlib}/Authen/Radius/
%{perl_vendorlib}/Authen/Radius.pm

%changelog
* Thu Jan 07 2010 Christoph Maser <cmr@financial.com> - 0.15-1
- Upgrade to version 0.15.

* Mon Nov 26 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Initial package. (using DAR)
