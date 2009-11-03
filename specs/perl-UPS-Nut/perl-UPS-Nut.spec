# $Id$
# Authority: dag
# Upstream: Kit Peters <perl$clownswilleatyou,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name UPS-Nut

Summary: Perl module to talk to a UPS via Network UPS Tools (NUT) upsd
Name: perl-UPS-Nut
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/UPS-Nut/

Source: http://www.cpan.org/authors/id/K/KP/KPETERS/UPS-Nut-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-UPS-Nut is a Perl module to talk to a UPS via NUT (Network UPS Tools) upsd.

This package contains the following Perl module:

    UPS::Nut

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
%doc Changes LICENSE MANIFEST README
%doc %{_mandir}/man3/UPS::Nut.3pm*
%dir %{perl_vendorlib}/UPS/
#%{perl_vendorlib}/UPS/Nut/
%{perl_vendorlib}/UPS/Nut.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.04-1
- Initial package. (using DAR)
