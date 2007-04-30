# $Id$
# Authority: dag
# Upstream: Tony Bowden <tony$tmtm,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-DBI
%define real_version 3.000016

Summary: Perl module that implements a simple database abstraction  
Name: perl-Class-DBI
Version: 3.0.16
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-DBI/

Source: http://www.cpan.org/authors/id/T/TM/TMTM/Class-DBI-v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
Requires: perl

%description
Class-DBI is a Perl module that implements a simple database abstraction.

%prep
%setup -n %{real_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Class/
%{perl_vendorlib}/Class/DBI/
%{perl_vendorlib}/Class/DBI.pm

%changelog
* Mon Apr 30 2007 Dag Wieers <dag@wieers.com> - 3.000016-1
- Initial package. (using DAR)
