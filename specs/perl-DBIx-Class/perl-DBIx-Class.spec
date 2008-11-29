# $Id$
# Authority: dag
# Upstream: Matt S. Trout <mst$shadowcatsystems,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Class

Summary: Extensible and flexible object <-> relational mapper
Name: perl-DBIx-Class
Version: 0.08010
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Class/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Carp::Clan) >= 5.9
BuildRequires: perl(Class::Accessor::Grouped) >= 0.05002
BuildRequires: perl(Class::C3) >= 0.13
BuildRequires: perl(Class::C3::Componentised)
BuildRequires: perl(Class::Inspector) >= 1.18
BuildRequires: perl(Class::Trigger)
BuildRequires: perl(Data::Page) >= 2.00
BuildRequires: perl(DBD::SQLite) >= 1.13
BuildRequires: perl(DBI) >= 1.4
BuildRequires: perl(DBIx::ContextualFetch)
BuildRequires: perl(JSON::Any) >= 1
BuildRequires: perl(Module::Find)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Scope::Guard) >= 0.03
BuildRequires: perl(SQL::Abstract) >= 1.2
BuildRequires: perl(SQL::Abstract::Limit) >= 0.10
BuildRequires: perl(Storable)
#BuildRequires: perl(Test::Builder) >= 0.33
Requires: perl >= 1:5.6.1

%description
Extensible and flexible object <-> relational mapper.

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
%doc %{_mandir}/man3/DBIx::Class.3pm*
%dir %{perl_vendorlib}/DBIx/
#%{perl_vendorlib}/DBIx/Class/
%{perl_vendorlib}/DBIx/Class.pm

%changelog
* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 0.08010-1
- Updated to release 0.08010.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.08009-1
- Updated to release 0.08009.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.08008-1
- Switch to upstream version.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.8.8-1
- Initial package. (using DAR)
