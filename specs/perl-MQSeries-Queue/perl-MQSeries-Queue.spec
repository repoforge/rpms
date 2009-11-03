# $Id$
# Authority: dag
# Upstream: Hildo Biersma <Hildo,Biersma$MorganStanley,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MQSeries-Queue

Summary: Perl module named MQSeries-Queue
Name: perl-MQSeries-Queue
Version: 1.25
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MQSeries-Queue/

Source: http://www.cpan.org/modules/by-module/MQSeries/MQSeries-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-MQSeries-Queue is a Perl module.

%prep
%setup -n MQSeries-%{version}

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
%doc %{_mandir}/man3/MQSeries::Queue.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/MQSeries/
%{perl_vendorarch}/MQSeries/Queue.pm
%dir %{perl_vendorarch}/auto/MQSeries/
%{perl_vendorarch}/auto/MQSeries/Queue/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.25-1
- Initial package. (using DAR)
