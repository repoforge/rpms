# $Id$
# Authority: dries
# Upstream: Apocalypse <perl$0ne,us>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-SimpleDBI

Summary: Asynchronous non-blocking DBI calls in POE
Name: perl-POE-Component-SimpleDBI
Version: 1.15
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-SimpleDBI/

Source: http://search.cpan.org//CPAN/authors/id/A/AP/APOCAL/POE-Component-SimpleDBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module simplifies DBI usage in POE's multitasking world.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/SimpleDBI.pm
%{perl_vendorlib}/POE/Component/SimpleDBI/

%changelog
* Sat Sep 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
