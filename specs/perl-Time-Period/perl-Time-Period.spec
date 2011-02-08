# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Period

Summary: Perl module to deal with time periods.
Name: perl-Time-Period
Version: 1.21
Release: 1%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Period/

Source: http://search.cpan.org/CPAN/authors/id/P/PB/PBOYD/Time-Period-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)
BuildRequires: perl >= 5.001
Requires: perl(Exporter)
Requires: perl >= 5.001
Provides: perl-Period

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Perl module to deal with time periods.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/Time::Period.3pm*
%dir %{perl_vendorlib}/Time/
%{perl_vendorlib}/Time/Period.pm

%changelog
* Tue Feb  8 2011 Christoph Maser <cmaser@gmx.de> - 1.21-1
- Updated to version 1.21.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.20-2
- Initial package. (using DAR)
