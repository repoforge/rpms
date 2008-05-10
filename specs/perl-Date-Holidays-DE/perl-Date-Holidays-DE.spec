# $Id$
# Authority: dries
# Upstream: Martin Schmitt <mas$scsy,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Holidays-DE

Summary: Creates a list of german holidays in a given year
Name: perl-Date-Holidays-DE
Version: 1.0.1
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Holidays-DE/

Source: http://www.cpan.org/modules/by-module/Date/Date-Holidays-DE-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module creates a list of German holidays in a given year.

It knows about special holiday regulations for all of Germany's federal
states and also about "semi-holidays" that will be treated as holidays on
request.

Holidays that occur on weekends can be excluded from the generated list.

The generated list can be freely formatted using regular strftime() format
definitions.

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

### Clean up docs
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README example/
%doc %{_mandir}/man3/Date::Holidays::DE.3pm*
%dir %{perl_vendorlib}/Date/
%dir %{perl_vendorlib}/Date/Holidays/
#%{perl_vendorlib}/Date/Holidays/DE/
%{perl_vendorlib}/Date/Holidays/DE.pm

%changelog
* Sat May 10 2008 Dag Wieers <dag@wieers.com> - 1.0.1-1
- Updated to release 1.0.1.

* Sun Dec 11 2005 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Initial package.
