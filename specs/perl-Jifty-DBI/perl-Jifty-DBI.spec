# $Id$
# Authority: dag
# Upstream: Shawn M Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Jifty-DBI

Summary: Perl module that implements an object-relational persistence framework
Name: perl-Jifty-DBI
Version: 0.49
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jifty-DBI/

Source: http://www.cpan.org/modules/by-module/Jifty/Jifty-DBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.3
BuildRequires: perl(Cache::Memcached)
BuildRequires: perl(Cache::Simple::TimedExpiry) >= 0.21
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::ReturnValue) >= 0.4
BuildRequires: perl(Class::Trigger) >= 0.12
BuildRequires: perl(Clone)
BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBI)
BuildRequires: perl(DBIx::DBSchema) >= 0.34
BuildRequires: perl(Data::Page)
BuildRequires: perl(DateTime) >= 0.34
BuildRequires: perl(DateTime::Format::ISO8601)
BuildRequires: perl(DateTime::Format::Strptime)
BuildRequires: perl(Encode) >= 2.1
BuildRequires: perl(Exporter::Lite)
BuildRequires: perl(Hash::Merge)
BuildRequires: perl(Lingua::EN::Inflect)
BuildRequires: perl(Object::Declare) >= 0.22
BuildRequires: perl(Scalar::Defer) >= 0.1
BuildRequires: perl(Test::More) >= 0.52
BuildRequires: perl(Test::Warn) >= 0.1
BuildRequires: perl(Time::Duration)
BuildRequires: perl(Time::Duration::Parse) >= 0.05
BuildRequires: perl(UNIVERSAL::require) >= 0.11
BuildRequires: perl(version)
BuildRequires: perl(YAML::Syck)
Requires: perl >= 2:5.8.3

%description
perl-Jifty-DBI is a Perl module that implements an object-relational
persistence framework.

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
