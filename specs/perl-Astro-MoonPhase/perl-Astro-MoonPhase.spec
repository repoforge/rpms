# $Id$
# Authority: dag
# Upstream: Brett Hamilton <open$simple,be>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Astro-MoonPhase

Summary: Information about the phase of the Moon
Name: perl-Astro-MoonPhase
Version: 0.60
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Astro-MoonPhase/

Source: http://www.cpan.org/modules/by-module/Astro/Astro-MoonPhase-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Information about the phase of the Moon.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man3/Astro::MoonPhase.3pm*
%dir %{perl_vendorlib}/Astro/
#%{perl_vendorlib}/Astro/MoonPhase/
%{perl_vendorlib}/Astro/MoonPhase.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.60-1
- Initial package. (using DAR)
