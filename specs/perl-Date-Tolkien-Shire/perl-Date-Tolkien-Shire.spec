# $Id$
# Authority: dries
# Upstream: Tom Braun <tbraun$pobox,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Tolkien-Shire

Summary: Tolkien dates
Name: perl-Date-Tolkien-Shire
Version: 1.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Tolkien-Shire/

Source: http://www.cpan.org/modules/by-module/Date/Date-Tolkien-Shire-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is an object-oriented module to convert dates into
the Shire Calender as presented in the Lord of the Rings
by J. R. R. Tolkien.  It includes converting epoch time to
the Shire Calendar (you can also get epoch time back),
comparison operators, and a method to print a formatted
string containing that does something to the effect of on
this date in history -- pulling events from the Lord of
the Rings.

The biggest use I can see in this thing is in a startup
script or possible to keep yourself entertained in an
otherwise boring app that includes a date.  If you have
any other ideas/suggestions/uses, etc., please let me
know.  I am curious to see how this gets used (if it gets
used that is).

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
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Date/Tolkien/Shire.pm

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.13-1
- Updated to release 1.13.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.12-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.12-1
- Initial package.
