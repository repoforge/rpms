# $Id$
# Authority: dag
# Upstream: Michael R. Davis <account=>perl,tld=>com,domain=>michaelrdavis>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-GPSD

Summary: Perl module that provides an object client interface to the gpsd server daemon
Name: perl-Net-GPSD
Version: 0.37
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-GPSD/

Source: http://www.cpan.org/modules/by-module/Net/Net-GPSD-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
perl-Net-GPSD is a Perl module that provides an object client interface
to the gpsd server daemon.

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
find doc/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES LICENSE MANIFEST META.yml README doc/
%doc %{_mandir}/man3/Net::GPSD.3pm*
%doc %{_mandir}/man3/Net::GPSD::*.3pm*
%dir %{perl_vendorlib}/Net/
%{perl_vendorlib}/Net/GPSD/
%{perl_vendorlib}/Net/GPSD.pm

%changelog
* Sat Jul  4 2009 Christoph Maser <cmr@financial.com> - 0.37-1
- Updated to version 0.37.

* Thu Nov 15 2007 Dag Wieers <dag@wieers.com> - 0.36-1
- Updated to release 0.36.

* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 0.35-1
- Initial package. (using DAR)
