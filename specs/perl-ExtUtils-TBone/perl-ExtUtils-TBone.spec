# $Id$
# Authority: dries
# Upstream: Eryq <eryq$zeegee,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name ExtUtils-TBone

Summary:  Skeleton for writing "t/*.t" test files
Name: perl-ExtUtils-TBone
Version: 1.124
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/ExtUtils-TBone/

Source: http://search.cpan.org/CPAN/authors/id/E/ER/ERYQ/ExtUtils-TBone-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This module is intended for folks who release CPAN modules with "t/*.t"
tests. It makes it easy for you to output syntactically correct test-
output while at the same time logging all test activity to a log file.
Hopefully, bug reports which include the contents of this file will be
easier for you to investigate.
	
%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/ExtUtils/TBone.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.124-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.124-1
- Initial package.

