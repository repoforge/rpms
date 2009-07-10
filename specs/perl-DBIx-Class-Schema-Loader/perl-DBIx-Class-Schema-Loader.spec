# $Id$
# Authority: dag
# Upstream: Brandon Black <blblack$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Class-Schema-Loader

Summary: Dynamic definition of a DBIx::Class::Schema
Name: perl-DBIx-Class-Schema-Loader
Version: 0.04006
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Class-Schema-Loader/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-Class-Schema-Loader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Class::Accessor::Fast) >= 0.30
BuildRequires: perl(Class::C3) >= 0.18
BuildRequires: perl(Class::Data::Accessor) >= 0.03
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(DBD::SQLite) >= 1.12
BuildRequires: perl(DBI) >= 1.56
BuildRequires: perl(DBIx::Class) >= 0.07006
BuildRequires: perl(Data::Dump) >= 1.06
BuildRequires: perl(Date::Calc)
BuildRequires: perl(Digest::MD5) >= 2.36
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Lingua::EN::Inflect::Number) >= 1.1
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::More) >= 0.47
BuildRequires: perl(Text::Balanced)
BuildRequires: perl(UNIVERSAL::require) >= 0.11

%description
Dynamic definition of a DBIx::Class::Schema.

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
%doc %{_mandir}/man3/DBIx::Class::Schema::Loader.3pm*
%dir %{perl_vendorlib}/DBIx/
%dir %{perl_vendorlib}/DBIx/Class/
%dir %{perl_vendorlib}/DBIx/Class/Schema/
#%{perl_vendorlib}/DBIx/Class/Schema/Loader/
%{perl_vendorlib}/DBIx/Class/Schema/Loader.pm

%changelog
* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.04006-1
- Updated to version 0.04006.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.04005-1
- Updated to release 0.04005.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.04004-1
- Initial package. (using DAR)
