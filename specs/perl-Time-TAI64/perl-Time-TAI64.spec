# $Id$
# Authority: dag
# Upstream: Jorge Valdes <jorge$joval,info>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-TAI64

Summary: Perl extension for converting TAI64 strings into standard unix timestamps
Name: perl-Time-TAI64
Version: 2.11
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-TAI64/

Source: http://www.cpan.org/modules/by-module/Time/Time-TAI64-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Perl extension for converting TAI64 strings into standard unix timestamps.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man3/Time::TAI64.3pm*
%dir %{perl_vendorlib}/Time/
#%{perl_vendorlib}/Time/TAI64/
%{perl_vendorlib}/Time/TAI64.pm

%changelog
* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 2.11-1
- Initial package. (using DAR)
