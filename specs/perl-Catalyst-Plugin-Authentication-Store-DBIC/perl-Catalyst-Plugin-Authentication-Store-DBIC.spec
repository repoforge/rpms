# $Id$
# Authority: dag
# Upstream: David Kamholz <dkamholz$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Catalyst-Plugin-Authentication-Store-DBIC

Summary: Authentication and authorization against a DBIx::Class or Class::DBI model
Name: perl-Catalyst-Plugin-Authentication-Store-DBIC
Version: 0.11
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Catalyst-Plugin-Authentication-Store-DBIC/

Source: http://www.cpan.org/modules/by-module/Catalyst/Catalyst-Plugin-Authentication-Store-DBIC-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Catalyst::Model::DBIC::Schema)
BuildRequires: perl(Catalyst::Plugin::Authentication) >= 0.06
BuildRequires: perl(Catalyst::Plugin::Authorization::Roles) >= 0.03
BuildRequires: perl(Catalyst::Plugin::Session::State::Cookie) >= 0.02
BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(Set::Object) >= 1.14

%description
Authentication and authorization against a DBIx::Class or Class::DBI model.

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
%doc %{_mandir}/man3/Catalyst::Plugin::Authentication::Store::DBIC.3pm*
%dir %{perl_vendorlib}/Catalyst/
%dir %{perl_vendorlib}/Catalyst/Plugin/
%dir %{perl_vendorlib}/Catalyst/Plugin/Authentication/
%dir %{perl_vendorlib}/Catalyst/Plugin/Authentication/Store/
#%{perl_vendorlib}/Catalyst/Plugin/Authentication/Store/DBIC/
%{perl_vendorlib}/Catalyst/Plugin/Authentication/Store/DBIC.pm

%changelog
* Tue Oct 07 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.09-1
- Initial package. (using DAR)
