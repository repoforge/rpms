# $Id$
# Authority: dries
# Upstream: Jeff Zucker <jeff$vpservices,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-AnyData

Summary: Interface to data in many formats and from many sources
Name: perl-DBD-AnyData
Version: 0.08
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-AnyData/

Source: http://search.cpan.org/CPAN/authors/id/J/JZ/JZUCKER/DBD-AnyData-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
The DBD::AnyData module provides a DBI (Perl Database Interface)
and SQL (Structured Query Language) interface to data in many
formats and from many sources.

There are actually two modules DBD::AnyData and AnyData.  The AnyData
module provides most of the same features as DBD::AnyData
through a tied hash interface which does not require or support
DBI and SQL.

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
%{perl_vendorlib}/DBD/AnyData.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.08-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
