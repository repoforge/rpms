# $Id$
# Authority: dag
# Upstream: Peter Rabbitson <devel@rabbit.us>
# perl-Carp-Clan >= 6 not available on el4
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Class

Summary: Extensible and flexible object <-> relational mapper
Name: perl-DBIx-Class
Version: 0.08118
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Class/

Source: http://search.cpan.org/CPAN/authors/id/R/RI/RIBASUSHI/DBIx-Class-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp::Clan) >= 6.0
BuildRequires: perl(Class::Accessor::Grouped) >= 0.09002
BuildRequires: perl(Class::C3::Componentised) >= 1.0005
BuildRequires: perl(Class::Inspector) >= 1.24
BuildRequires: perl(DBD::SQLite) >= 1.25
BuildRequires: perl(DBI) >= 1.609
BuildRequires: perl(Data::Dumper::Concise) >= 1.000
BuildRequires: perl(Data::Page) >= 2.00
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
#BuildRequires: perl(File::Temp) >= 0.22
BuildRequires: perl(File::Temp)
BuildRequires: perl(JSON::Any) >= 1.18
BuildRequires: perl(List::Util)
BuildRequires: perl(MRO::Compat) >= 0.09
BuildRequires: perl(Module::Find) >= 0.06
BuildRequires: perl(Path::Class) >= 0.16
BuildRequires: perl(SQL::Abstract) >= 1.61
BuildRequires: perl(SQL::Abstract::Limit) >= 0.13
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Scope::Guard) >= 0.03
BuildRequires: perl(Storable)
BuildRequires: perl(Sub::Name) >= 0.04
#BuildRequires: perl(Test::Builder) >= 0.33
#BuildRequires: perl(Test::Deep)
BuildRequires: perl(Test::Exception)
#BuildRequires: perl(Test::More) >= 0.92
BuildRequires: perl(Test::Warn) >= 0.21
BuildRequires: perl >= 5.8.1
Requires: perl(Carp::Clan) >= 6.0
Requires: perl(Class::Accessor::Grouped) >= 0.09002
Requires: perl(Class::C3::Componentised) >= 1.0005
Requires: perl(Class::Inspector) >= 1.24
Requires: perl(DBD::SQLite) >= 1.25
Requires: perl(DBI) >= 1.609
Requires: perl(Data::Dumper::Concise) >= 1.000
Requires: perl(Data::Page) >= 2.00
Requires: perl(JSON::Any) >= 1.18
Requires: perl(List::Util)
Requires: perl(MRO::Compat) >= 0.09
Requires: perl(Module::Find) >= 0.06
Requires: perl(Path::Class) >= 0.16
Requires: perl(SQL::Abstract) >= 1.61
Requires: perl(SQL::Abstract::Limit) >= 0.13
Requires: perl(Scalar::Util)
Requires: perl(Scope::Guard) >= 0.03
Requires: perl(Storable)
Requires: perl(Sub::Name) >= 0.04
Requires: perl >= 5.8.1

%filter_from_requires /^perl*/d
%filter_setup

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
%{perl_vendorlib}/SQL/Translator/Parser/DBIx/Class.pm
%{perl_vendorlib}/SQL/Translator/Producer/DBIx/Class/File.pm
%{perl_vendorlib}/DBIx/Class/
%{perl_vendorlib}/DBIx/Class.pm

%changelog
* Mon Feb 08 2010 Steve Huff <shuff@vecna.org> - 0.08118-1
- Updated to version 0.08118.

* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.08117-1
- Updated to version 0.08117.

* Wed Dec 30 2009 Christoph Maser <cmr@financial.com> - 0.08115-1
- Updated to version 0.08115.

* Mon Sep 14 2009 Christoph Maser <cmr@financial.com> - 0.08111-1
- Updated to version 0.08111.

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
