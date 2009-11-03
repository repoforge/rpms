# $Id$
# Authority: dries
# Upstream: Randy J. Ray <rjray$blackperl,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name WebService-ISBNDB

Summary: Data and communication classes for talking to isbndb.com
Name: perl-WebService-ISBNDB
Version: 0.34
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/WebService-ISBNDB/

Source: http://www.cpan.org/modules/by-module/WebService/WebService-ISBNDB-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0 
BuildRequires: perl(Module::Build)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0 

%description
Data and communication classes for talking to isbndb.com.

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
%doc ChangeLog ChangeLog.xml MANIFEST MANIFEST.SKIP META.yml README SIGNATURE
%doc %{_mandir}/man3/WebService::ISBNDB.3pm*
%doc %{_mandir}/man3/WebService::ISBNDB::*.3pm*
%dir %{perl_vendorlib}/WebService/
%{perl_vendorlib}/WebService/ISBNDB/
%{perl_vendorlib}/WebService/ISBNDB.pm

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 0.34-1
- Updated to release 0.34.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 0.33-1
- Updated to release 0.33.

* Sun Nov 19 2006 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Initial package.
