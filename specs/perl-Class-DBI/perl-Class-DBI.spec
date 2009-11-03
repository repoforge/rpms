# $Id$
# Authority: dag
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI
%define real_version 3.000017

Summary: Perl module that implements a simple database abstraction  
Name: perl-Class-DBI
Version: 3.0.17
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI/

Source: http://www.cpan.org/modules/by-module/Class/Class-DBI-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Class-DBI is a Perl module that implements a simple database abstraction.

%prep
%setup -n %{real_name}-v%{version}

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
%doc Changes MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/Class::DBI.3pm*
%doc %{_mandir}/man3/Class::DBI::*.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/DBI/
%{perl_vendorlib}/Class/DBI.pm

%changelog
* Fri Nov 09 2007 Dag Wieers <dag@wieers.com> - 3.0.17-1
- Updated to release 3.000017.

* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 3.0.16-1
- Initial package. (using DAR)
