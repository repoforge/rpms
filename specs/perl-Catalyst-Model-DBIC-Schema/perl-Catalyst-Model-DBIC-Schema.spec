# $Id$
# Authority: dag
# Upstream: Brandon L Black <blblack$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Model-DBIC-Schema

Summary: DBIx::Class::Schema Model Class
Name: perl-Catalyst-Model-DBIC-Schema
Version: 0.21
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Model-DBIC-Schema/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Model-DBIC-Schema-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(DBIx::Class) >= 0.07006
BuildRequires: perl(DBIx::Class::Schema::Loader) >= 0.03012
BuildRequires: perl(Catalyst::Devel) >= 1.0
BuildRequires: perl(Catalyst::Runtime) >= 5.70
BuildRequires: perl(Class::Accessor::Fast) >= 0.22
BuildRequires: perl(Class::Data::Accessor) >= 0.02
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require) >= 0.10

%description
DBIx::Class::Schema Model Class.

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
%doc %{_mandir}/man3/Catalyst::Helper::Model::DBIC::Schema.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Model/
%dir %{perl_vendorlib}/Catalyst/Model/DBIC/
#%{perl_vendorlib}/Catalyst/Model/DBIC/Schema/
%{perl_vendorlib}/Catalyst/Model/DBIC/Schema.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.21-1
- Updated to release 0.21.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.20-1
- Initial package. (using DAR)
