# $Id$
# Authority: dag
# Upstream: Vedran Sego <vsego$math,hr>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Linux-stat

Summary: Perl module to parse /proc/stat
Name: perl-Linux-stat
Version: 1.00
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Linux-stat/

Source: http://www.cpan.org/modules/by-module/Linux/Linux-stat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Linux-stat is a Perl module to parse /proc/stat.

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
%doc %{_mandir}/man3/Linux::stat.3pm*
%dir %{perl_vendorlib}/Linux/
%{perl_vendorlib}/Linux/example.pl
%{perl_vendorlib}/Linux/stat.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 1.00-1
- Initial package. (using DAR)
