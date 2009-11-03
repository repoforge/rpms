# $Id$
# Authority: dries
# Upstream: Jonathan Leto <jonathan$leto,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Math-MatrixReal

Summary: Manipulate NxN matrices of real numbers
Name: perl-Math-MatrixReal
Version: 2.05
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-MatrixReal/

Source: http://www.cpan.org/modules/by-module/Math/Math-MatrixReal-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)

%description
Implements the data type "matrix of reals" (and consequently also
"vector of reals") which can be used almost like any other basic
Perl type thanks to OPERATOR OVERLOADING.

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
find example/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES CREDITS MANIFEST META.yml README TODO example/
%doc %{_mandir}/man3/Math::Kleene.3pm*
%doc %{_mandir}/man3/Math::MatrixReal.3pm*
%dir %{perl_vendorlib}/Math/
%{perl_vendorlib}/Math/Kleene.pod
%{perl_vendorlib}/Math/MatrixReal.pm
%{perl_vendorlib}/Math/funcs.pl

%changelog
* Mon Mar 03 2008 Dag Wieers <dag@wieers.com> - 2.05-1
- Updated to release 2.05.

* Mon Feb 25 2008 Dag Wieers <dag@wieers.com> - 2.04-1
- Updated to release 2.04.

* Wed Feb 20 2008 Dag Wieers <dag@wieers.com> - 2.03-1
- Updated to release 2.03.

* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 2.02-1
- Updated to release 2.02.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.01-1
- Updated to release 2.01.

* Tue Apr 05 2005 Dries Verachtert <dries@ulyssis.org> - 1.9-1
- Initial package.
