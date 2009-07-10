# $Id$
# Authority: dag
# Upstream: Matt S. Trout <mst$shadowcatsystems,co,uk>
# perl-Carp-Clan >= 6 not available on el4
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Class

Summary: Extensible and flexible object <-> relational mapper
Name: perl-DBIx-Class
Version: 0.08108
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Class/

Source: http://www.cpan.org/modules/by-module/DBIx/DBIx-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 1:5.6.1
BuildRequires: perl(Carp::Clan) >= 6
BuildRequires: perl(Class::Accessor::Grouped) >= 0.08003
BuildRequires: perl(Class::C3::Componentised) >= 1.0005
BuildRequires: perl(Class::Inspector) >= 1.24
BuildRequires: perl(DBD::SQLite) >= 1.25
BuildRequires: perl(DBI) >= 1.605
BuildRequires: perl(Data::Page) >= 2
BuildRequires: perl(JSON::Any) >= 1.18
BuildRequires: perl(List::Util)
BuildRequires: perl(MRO::Compat) >= 0.09
BuildRequires: perl(Module::Find) >= 0.06
BuildRequires: perl(Path::Class) >= 0.16
BuildRequires: perl(SQL::Abstract) >= 1.56
BuildRequires: perl(SQL::Abstract::Limit) >= 0.13
BuildRequires: perl(SQL::Translator) >= 0.09004
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Scope::Guard) >= 0.03
BuildRequires: perl(Sub::Name) >= 0.04
BuildRequires: perl(Storable)
#BuildRequires: perl(Test::Builder) >= 0.33
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::Warn)
Requires: perl >= 1:5.6.1
Requires: perl(Carp::Clan) >= 6
Requires: perl(Class::Accessor::Grouped) >= 0.08003
Requires: perl(Class::C3::Componentised) >= 1.0005
Requires: perl(Class::Inspector) >= 1.24
Requires: perl(DBD::SQLite) >= 1.25
Requires: perl(DBI) >= 1.605
Requires: perl(Data::Page) >= 2
Requires: perl(JSON::Any) >=  1.18
Requires: perl(List::Util)
Requires: perl(MRO::Compat) >= 0.09
Requires: perl(Module::Find) >= 0.06
Requires: perl(Path::Class) >= 0.16
Requires: perl(SQL::Abstract) >= 1.56
Requires: perl(SQL::Abstract::Limit) >= 0.13
Requires: perl(SQL::Translator) >= 0.09004
Requires: perl(Scalar::Util)
Requires: perl(Scope::Guard) >= 0.03
Requires: perl(Storable)
Requires: perl(Sub::Name) >= 0.04

AutoReq: no

%description
Extensible and flexible object <-> relational mapper.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc %{_mandir}/man3/DBIx::Class*.3pm*
%doc %{_mandir}/man3/SQL::Translator::Parser::DBIx::Class.3pm*
%doc %{_mandir}/man3/SQL::Translator::Producer::DBIx::Class::File.3pm*
%doc %{_mandir}/man1/dbicadmin.1*
%{_bindir}/dbicadmin
%dir %{perl_vendorlib}/DBIx/
%dir %{perl_vendorlib}/SQL/Translator/Parser/DBIx/Class.pm
%dir %{perl_vendorlib}/SQL/Translator/Producer/DBIx/Class/File.pm
%{perl_vendorlib}/DBIx/Class/
%{perl_vendorlib}/DBIx/Class.pm

%changelog
* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.08108-1
- Updated to version 0.08108.

* Wed Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.08107-2
- Manually set dependencies.

* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 0.08107-1
- Updated to version 0.08107.

* Sun Mar 02 2008 Dag Wieers <dag@wieers.com> - 0.08010-1
- Updated to release 0.08010.

* Sat Jan 26 2008 Dag Wieers <dag@wieers.com> - 0.08009-1
- Updated to release 0.08009.

* Sat Nov 24 2007 Dag Wieers <dag@wieers.com> - 0.08008-1
- Switch to upstream version.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.8.8-1
- Initial package. (using DAR)
