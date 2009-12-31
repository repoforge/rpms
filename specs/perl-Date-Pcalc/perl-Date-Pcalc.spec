# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Date-Pcalc

Summary: Gregorian calendar date calculations
Name: perl-Date-Pcalc
Version: 6.1
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Date-Pcalc/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Date-Pcalc-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(Bit::Vector) >= 7.1
BuildRequires: perl(Carp::Clan) >= 5.3
Requires: perl(Bit::Vector) >= 7.1
Requires: perl(Carp::Clan) >= 5.3

%filter_from_requires /^perl*/d
%filter_setup

%description
Gregorian calendar date calculations

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
%doc *.txt
%doc %{_mandir}/man3/Date::Pcalc.3pm*
%doc %{_mandir}/man3/Date::Pcalc::Object.3pm.gz
%doc %{_mandir}/man3/Date::Pcalendar.3pm.gz
%doc %{_mandir}/man3/Date::Pcalendar::Profiles.3pm.gz
%doc %{_mandir}/man3/Date::Pcalendar::Year.3pm.gz
%{perl_vendorarch}/
%{perl_vendorarch}/Date/Pcalc.pm
%{perl_vendorarch}/Date/Pcalc.pod
%{perl_vendorarch}/Date/Pcalc/Object.pm
%{perl_vendorarch}/Date/Pcalc/Object.pod
%{perl_vendorarch}/Date/Pcalendar.pm
%{perl_vendorarch}/Date/Pcalendar.pod
%{perl_vendorarch}/Date/Pcalendar/Profiles.pm
%{perl_vendorarch}/Date/Pcalendar/Profiles.pod
%{perl_vendorarch}/Date/Pcalendar/Year.pm
%{perl_vendorarch}/Date/Pcalendar/Year.pod
%{perl_vendorarch}/auto/Date/Pcalc/Pcalc.bs
%{perl_vendorarch}/auto/Date/Pcalc/Pcalc.bs

%changelog
* Thu Dec 31 2009 Christoph Maser <cmr@financial.com> - 6.1-1
- Updated to version 6.1.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2-1.2
- Rebuild for Fedora Core 5.

* Sat Aug 07 2004 Dag Wieers <dag@wieers.com> - 1.2-1
- Initial package. (using DAR)
