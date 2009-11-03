# $Id$
# Authority: dag
# Upstream: Jiro Nishiguchi <jiro$cpan,org> Jason Levitt <jlevitt$yahoo-inc,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Yahoo-BBAuth

Summary: Perl module to interface with the Yahoo! Browser-Based Authentication
Name: perl-Yahoo-BBAuth
Version: 0.50
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Yahoo-BBAuth/

Source: http://www.cpan.org/modules/by-module/Yahoo/Yahoo-BBAuth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Yahoo-BBAuth is a Perl module to interface with the Yahoo!
Browser-Based Authentication.

This package contains the following Perl module:

    Yahoo::BBAuth

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
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README eg/
%doc %{_mandir}/man3/Yahoo::BBAuth.3pm*
%dir %{perl_vendorlib}/Yahoo/
%{perl_vendorlib}/Yahoo/BBAuth.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 0.50-1
- Initial package. (using DAR)
