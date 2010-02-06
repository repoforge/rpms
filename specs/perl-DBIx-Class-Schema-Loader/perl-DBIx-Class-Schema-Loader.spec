# $Id$
# Authority: dag
# Upstream: Rafael Kitover <rkitover@io.com>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-Class-Schema-Loader

Summary: Dynamic definition of a DBIx::Class::Schema
Name: perl-DBIx-Class-Schema-Loader
Version: 0.05001
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-Class-Schema-Loader/

Source: http://search.cpan.org/CPAN/authors/id/R/RK/RKITOVER/DBIx-Class-Schema-Loader-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(Carp::Clan)
BuildRequires: perl(Class::Accessor::Grouped) >= 0.09002
BuildRequires: perl(Class::C3) >= 0.18
BuildRequires: perl(Class::C3::Componentised) >= 1.0005
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Class::Unload)
BuildRequires: perl(DBD::SQLite) >= 1.12
BuildRequires: perl(DBI) >= 1.56
BuildRequires: perl(DBIx::Class) >= 0.08114
BuildRequires: perl(Data::Dump) >= 1.06
BuildRequires: perl(Digest::MD5) >= 2.36
#BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Copy)
#BuildRequires: perl(File::Path) >= 2.07
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Slurp) >= 9999.13
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp) >= 0.16
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Lingua::EN::Inflect::Number) >= 1.1
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Exception)
#BuildRequires: perl(Test::More) >= 0.94
BuildRequires: perl(Test::More) 
BuildRequires: perl(Text::Balanced)
Requires: perl(Carp::Clan)
Requires: perl(Class::Accessor::Grouped) >= 0.09002
Requires: perl(Class::C3) >= 0.18
Requires: perl(Class::C3::Componentised) >= 1.0005
Requires: perl(Class::Inspector)
Requires: perl(Class::Unload)
Requires: perl(DBIx::Class) >= 0.08114
Requires: perl(Data::Dump) >= 1.06
Requires: perl(Digest::MD5) >= 2.36
Requires: perl(File::Slurp) >= 9999.13
Requires: perl(File::Spec)
Requires: perl(Lingua::EN::Inflect::Number) >= 1.1
Requires: perl(Scalar::Util)
Requires: perl(Text::Balanced)

%filter_from_requires /^perl*/d
%filter_setup


%description
Dynamic definition of a DBIx::Class::Schema.

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
%doc %{_mandir}/man3/DBIx::Class::Schema::Loader*.3pm*
%doc %{_mandir}/man1/dbicdump.1*
%{_bindir}/dbicdump
%dir %{perl_vendorlib}/DBIx/
%dir %{perl_vendorlib}/DBIx/Class/
%dir %{perl_vendorlib}/DBIx/Class/Schema/
%{perl_vendorlib}/DBIx/Class/Schema/Loader/
%{perl_vendorlib}/DBIx/Class/Schema/Loader.pm

%changelog
* Sat Feb  6 2010 Christoph Maser <cmr@financial.com> - 0.05001-1
- Updated to version 0.05001.

* Wed Feb  3 2010 Christoph Maser <cmr@financial.com> - 0.05000-1
- Updated to version 0.05000.

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.04006-2
- Update dependencies

* Fri Jul 10 2009 Christoph Maser <cmr@financial.com> - 0.04006-1
- Updated to version 0.04006.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.04005-1
- Updated to release 0.04005.

* Sun Dec 30 2007 Dag Wieers <dag@wieers.com> - 0.04004-1
- Initial package. (using DAR)
