# $Id$
# Authority: dag
# Upstream: Shawn M Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jifty-DBI

Summary: Perl module that implements an object-relational persistence framework
Name: perl-Jifty-DBI
Version: 0.58
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty-DBI/

Source: http://www.cpan.org/modules/by-module/Jifty/Jifty-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.3
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::ReturnValue) >= 0.4
BuildRequires: perl(Class::Trigger) >= 0.12
BuildRequires: perl(Clone)
BuildRequires: perl(DBI)
BuildRequires: perl(DBIx::DBSchema) >= 0.34
BuildRequires: perl(Data::Page) >= 2.0
BuildRequires: perl(DateTime) >= 0.34
BuildRequires: perl(DateTime::Format::ISO8601)
BuildRequires: perl(DateTime::Format::Strptime)
BuildRequires: perl(Encode) >= 2.1
BuildRequires: perl(Exporter::Lite)
BuildRequires: perl(Hash::Merge)
BuildRequires: perl(Lingua::EN::Inflect)
BuildRequires: perl(Object::Declare) >= 0.22
BuildRequires: perl(Scalar::Defer) >= 0.1
BuildRequires: perl(UNIVERSAL::require) >= 0.11
BuildRequires: perl(YAML::Syck)
BuildRequires: perl(version)

Requires: perl(Class::Accessor::Fast)
Requires: perl(Class::Data::Inheritable)
Requires: perl(Class::ReturnValue) >= 0.4
Requires: perl(Class::Trigger) >= 0.12
Requires: perl(Clone)
Requires: perl(DBI)
Requires: perl(DBIx::DBSchema) >= 0.34
Requires: perl(Data::Page) >= 2.0
Requires: perl(DateTime) >= 0.34
Requires: perl(DateTime::Format::ISO8601)
Requires: perl(DateTime::Format::Strptime)
Requires: perl(Encode) >= 2.1
Requires: perl(Exporter::Lite)
Requires: perl(Hash::Merge)
Requires: perl(Lingua::EN::Inflect)
Requires: perl(Object::Declare) >= 0.22
Requires: perl(Scalar::Defer) >= 0.1
Requires: perl(UNIVERSAL::require) >= 0.11
Requires: perl(YAML::Syck)
Requires: perl(version)
Requires: perl >= 2:5.8.3

AutoReq: no

%description
perl-Jifty-DBI is a Perl module that implements an object-relational
persistence framework.

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

### Clean up docs
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README ROADMAP SIGNATURE doc/
%doc %{_mandir}/man3/Jifty::DBI.3pm*
%doc %{_mandir}/man3/Jifty::DBI::*.3pm*
%dir %{perl_vendorlib}/Jifty/
%{perl_vendorlib}/Jifty/DBI/
%{perl_vendorlib}/Jifty/DBI.pm

%changelog
* Thu Jul 23 2009 Christoph Maser <cmr@financial.com> - 0.58-1
- Updated to version 0.58.

* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.57-1
- Updated to version 0.57.

* Mon May 05 2008 Dag Wieers <dag@wieers.com> - 0.49-1
- Updated to release 0.49.

* Tue Dec 04 2007 Dag Wieers <dag@wieers.com> - 0.48-1
- Updated to release 0.48.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.47-1
- Updated to release 0.47.

* Tue Nov 13 2007 Dag Wieers <dag@wieers.com> - 0.46-1
- Updated to release 0.46.

* Mon Nov 05 2007 Dag Wieers <dag@wieers.com> - 0.43-1
- Initial package. (using DAR)
