# $Id$
# Authority: dries
# Upstream: Apocalypse <perl$0ne,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name POE-Component-SimpleDBI

Summary: Asynchronous non-blocking DBI calls in POE
Name: perl-POE-Component-SimpleDBI
Version: 1.16
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/POE-Component-SimpleDBI/

Source: http://www.cpan.org/modules/by-module/POE/POE-Component-SimpleDBI-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module simplifies DBI usage in POE's multitasking world.

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
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorlib}/POE/Component/
%{perl_vendorlib}/POE/Component/SimpleDBI.pm
%{perl_vendorlib}/POE/Component/SimpleDBI/

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Updated to release 1.16.

* Sat Sep 30 2006 Dries Verachtert <dries@ulyssis.org> - 1.15-1
- Updated to release 1.15.

* Tue Sep 19 2006 Dries Verachtert <dries@ulyssis.org> - 1.14-1
- Initial package.
