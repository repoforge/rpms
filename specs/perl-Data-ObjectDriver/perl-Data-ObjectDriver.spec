# $Id$
# Authority: dag
# Upstream: Six Apart <cpan$sixapart,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-ObjectDriver

Summary: Simple, transparent data interface, with caching
Name: perl-Data-ObjectDriver
Version: 0.06
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-ObjectDriver/

Source: http://www.cpan.org/modules/by-module/Data/Data-ObjectDriver-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Class::Accessor::Fast)
BuildRequires: perl(Class::Data::Inheritable)
BuildRequires: perl(Class::Trigger)
BuildRequires: perl(DBI)
BuildRequires: perl(List::Util)
BuildRequires: perl(Test::Exception)
Requires: perl(Class::Accessor::Fast)
Requires: perl(Class::Data::Inheritable)
Requires: perl(Class::Trigger)
Requires: perl(DBI)
Requires: perl(List::Util)
AutoReq: no



%description
Simple, transparent data interface, with caching.

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
%doc %{_mandir}/man3/Data::ObjectDriver.3pm*
%doc %{_mandir}/man3/Data::ObjectDriver::*.3pm*
%dir %{perl_vendorlib}/Data/
%{perl_vendorlib}/Data/ObjectDriver/
%{perl_vendorlib}/Data/ObjectDriver.pm

%changelog
* Sun Jul 28 2009 Christoph Maser <cmr@financial.com> - 0.06-2
- Turn off AutoReq to get rid of DBD::Oracle dep

* Sun Jul 19 2009 Dag Wieers <dag@wieers.com> - 0.06-1
- Initial package. (using DAR)
