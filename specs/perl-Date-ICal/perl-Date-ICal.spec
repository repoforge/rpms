# $Id$
# Authority: dries
# Upstream: Rich Bowen <rbowen$rcbowen,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-ICal

Summary: ICalendar date objects
Name: perl-Date-ICal
Version: 1.72
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-ICal/

Source: http://search.cpan.org/CPAN/authors/id/R/RB/RBOW/Date-ICal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Date::ICal talks the ICal date format, and is intended to be a base
class for other date/calendar modules that know about ICal time format
also.

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
%{perl_vendorlib}/Date/ICal.pm
%{perl_vendorlib}/Date/ICal

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.72-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.72-1
- Initial package.
