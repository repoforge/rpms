# $Id$
# Authority: dag
# Upstream: Dave Cross <dave$mag-sol,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Calendar-Simple

Summary: Perl extension to create simple calendars
Name: perl-Calendar-Simple
Version: 1.20
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Calendar-Simple/

Source: http://www.cpan.org/modules/by-module/Calendar/Calendar-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
Requires: perl >= 0:5.6.0

%description
Perl extension to create simple calendars.

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
%doc %{_mandir}/man3/Calendar::Simple.3pm*
%{_bindir}/pcal
%dir %{perl_vendorlib}/Calendar/
#%{perl_vendorlib}/Calendar/Simple/
%{perl_vendorlib}/Calendar/Simple.pm

%changelog
* Sat May 03 2008 Dag Wieers <dag@wieers.com> - 1.20-1
- Updated to release 1.20.

* Tue Mar 11 2008 Dag Wieers <dag@wieers.com> - 1.19-1
- Updated to release 1.19.

* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 1.17-1
- Initial package. (using DAR)
