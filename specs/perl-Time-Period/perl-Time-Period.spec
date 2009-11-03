# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Period

Summary: Perl module to deal with time periods.
Name: perl-Time-Period
Version: 1.20
Release: 2%{?dist}
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Period/

Source: http://www.cpan.org/modules/by-module/Time/Period-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.00503

Obsoletes: perl-Period <= %{version}-%{release}
Provides: perl-Period

%description
Perl module to deal with time periods.

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
%doc README
%doc %{_mandir}/man3/Time::Period.3pm*
%dir %{perl_vendorlib}/Time/
%{perl_vendorlib}/Time/Period.pm

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.20-2
- Initial package. (using DAR)
