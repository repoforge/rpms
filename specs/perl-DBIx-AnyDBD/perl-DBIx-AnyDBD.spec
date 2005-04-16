# $Id$
# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBIx-AnyDBD

Summary: DBD independant class
Name: perl-DBIx-AnyDBD
Version: 2.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBIx-AnyDBD/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/DBIx-AnyDBD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This class is an alternative approach to developing database independant
code, which differs from modules that write SQL for you (such as 
DBIx::Recordset). Instead this module provides an OO inheritance
hierarchy for putting methods that do your SQL.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/DBIx/AnyDBD.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Initial package.
