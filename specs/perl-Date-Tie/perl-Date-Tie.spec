# $Id$
# Authority: dries
# Upstream: Flávio Soibelmann Glock <fglock$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Tie

Summary: Perlish interface to dates
Name: perl-Date-Tie
Version: 0.18
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Tie/

Source: http://www.cpan.org/modules/by-module/Date/Date-Tie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Date::Tie is an attempt to simplify date operations syntax.

Date::Tie manages a hash containing the keys:
epoch, utc_epoch, year, month, day, hour, minute, second,
yearday, week, weekday, weekyear, tz, tzhour, tzminute.

Whenever a new value is stored in a key, it will change
the other keys following the common (ISO) date rules.

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES MANIFEST META.yml README TODO eg/
%doc %{_mandir}/man3/Date::Tie.3pm*
%dir %{perl_vendorlib}/Date/
#%{perl_vendorlib}/Date/Tie/
%{perl_vendorlib}/Date/Tie.pm

%changelog
* Wed Jan 23 2008 Dag Wieers <dag@wieers.com> - 0.18-1
- Updated to release 0.18.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
