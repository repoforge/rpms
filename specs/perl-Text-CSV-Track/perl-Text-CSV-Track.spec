# $Id$
# Authority: dries
# Upstream: Jozef Kutej <jozef$kutej,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Text-CSV-Track

Summary: Module to work with .csv file that stores some value(s) per identificator
Name: perl-Text-CSV-Track
Version: 0.8
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Text-CSV-Track/

Source: http://www.cpan.org/modules/by-module/Text/Text-CSV-Track-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

%description
Module to work with .csv file that stores some value(s) per identificator.

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
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Text::CSV::Track.3pm*
%doc %{_mandir}/man3/Text::CSV::Track::*.3pm*
%dir %{perl_vendorlib}/Text/
%dir %{perl_vendorlib}/Text/CSV/
%{perl_vendorlib}/Text/CSV/Track/
%{perl_vendorlib}/Text/CSV/Track.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.8-1
- Updated to release 0.8.

* Sun Aug 12 2007 Dries Verachtert <dries@ulyssis.org> - 0.6-1
- Updated to release 0.6.

* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 0.2-1
- Initial package.
