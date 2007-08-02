# $Id$
# Authority: dries
# Upstream: Fl&#225;vio Soibelmann Glock <fglock$pucrs,br>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Tie

Summary: Perlish interface to dates
Name: perl-Date-Tie
Version: 0.17
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Tie/

Source: http://search.cpan.org/CPAN/authors/id/F/FG/FGLOCK/Date-Tie-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Date/Tie.pm

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.17-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.17-1
- Initial package.
