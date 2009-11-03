# $Id$
# Authority: dag
# Upstream: Hildo Biersma <Hildo,Biersma$MorganStanley,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MQSeries

Summary: Perl module named MQSeries
Name: perl-MQSeries
Version: 1.25
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MQSeries/

Source: http://www.cpan.org/modules/by-module/MQSeries/MQSeries-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-MQSeries is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYRIGHT LICENSE MANIFEST README
%doc %{_mandir}/man3/MQSeries.3pm*
#%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/MQSeries.pm
%{perl_vendorarch}/auto/MQSeries/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.25-1
- Initial package. (using DAR)
