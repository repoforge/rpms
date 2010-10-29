# $Id$
# Upstream: Daniel Muey <dmuey@cpan.org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)
%define real_name Math-Fibonacci-Phi

Summary: Perl extension for calculating Phi and phi for Fibonacci numbers.
Name: perl-Math-Fibonacci-Phi
Version: 0.02
Release: 1%{?dist}
License: unknown
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Math-Fibonacci-Phi/

Source: http://search.cpan.org/CPAN/authors/id/D/DM/DMUEY/Math-Fibonacci-Phi-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl(Math::Fibonacci)
Requires: perl(Math::Fibonacci)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup


%description
Perl extension for calculating Phi and phi for Fibonacci numbers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Math::Fibonacci::Phi.3pm*
%dir %{perl_vendorlib}/
%{perl_vendorlib}/Math/Fibonacci/Phi.pm
%exclude %{perl_vendorarch}/auto/Math/Fibonacci/Phi/.packlist

%changelog
* Fri Oct 29 2010 Christoph Maser <cmaser.gmx.de> - 0.02-1
- initial package
