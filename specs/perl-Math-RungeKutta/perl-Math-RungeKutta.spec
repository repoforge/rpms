# $Id$
# Authority: dries
# Upstream: Peter Billam <contact,html$pjb,com,au>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-RungeKutta

Summary: Algorithms for numerical integration
Name: perl-Math-RungeKutta
Version: 1.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-RungeKutta/

Source: http://www.cpan.org/modules/by-module/Math/Math-RungeKutta-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module offers algorithms for the numerical integration of
simultaneous differential equations of the form  dY/dt = F(t,Y)
where Y is an array of variables whose initial values Y(0) are
known, and F is a function known from the dynamics of the problem.

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
%doc Changes Install MANIFEST README
%doc %{_mandir}/man3/Math::RungeKutta.3pm*
%dir %{perl_vendorlib}/Math/
#%{perl_vendorlib}/Math/RungeKutta/
%{perl_vendorlib}/Math/RungeKutta.pm

%changelog
* Mon Oct 13 2008 Dag Wieers <dag@wieers.com> - 1.05-1
- Updated to release 1.05.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.02-1
- Initial package.
