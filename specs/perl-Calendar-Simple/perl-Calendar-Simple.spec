# $Id$
# Authority: dag
# Upstream: Dave Cross <dave$dave,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Calendar-Simple

Summary: Perl module to create simple calendars  
Name: perl-Calendar-Simple
Version: 1.17
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Calendar-Simple/

Source: http://www.cpan.org/modules/by-module/Calendar/Calendar-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl

%description
Calendar-Simple is a Perl module to create simple calendars.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Calendar::Simple.3pm*
%{_bindir}/pcal
%dir %{perl_vendorlib}/Calendar/
%{perl_vendorlib}/Calendar/Simple.pm

%changelog
* Sun Apr 29 2007 Dag Wieers <dag@wieers.com> - 1.17-1
- Initial package. (using DAR)
