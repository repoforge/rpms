# $Id$
# Authority: dries
# Upstream: Andrea Spinelli <aspinelli$imteam,it>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-VecStat

Summary: Some basic numeric stats on vectors
Name: perl-Math-VecStat
Version: 0.08
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-VecStat/

Source: http://www.cpan.org/modules/by-module/Math/Math-VecStat-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This package provides some basic statistics on numerical vectors. All the
subroutines can take a reference to the vector to be operated on. In some
cases a copy of the vector is acceptable, but is not recommended for
efficiency.

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
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Math/VecStat.pm

%changelog
* Sun Apr  3 2005 Dries Verachtert <dries@ulyssis.org> - 0.08-1
- Initial package.
