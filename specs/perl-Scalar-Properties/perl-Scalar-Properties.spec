# $Id$
# Authority: dries
# Upstream: David Cantrell <pause$barnyard,co,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Scalar-Properties

Summary: Run-time properties on scalar variables
Name: perl-Scalar-Properties
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Scalar-Properties/

Source: http://www.cpan.org/modules/by-module/Scalar/Scalar-Properties-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.6.0 
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
Requires: perl >= 0:5.6.0 

%description
Scalar::Properties attempts to make Perl more object-oriented by taking
an idea from Ruby: Everything you manipulate is an object, and the
results of those manipulations are objects themselves.

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
%doc Changes MANIFEST META.yml README TODO
%doc %{_mandir}/man3/Scalar::Properties.3pm*
%dir %{perl_vendorlib}/Scalar/
#%{perl_vendorlib}/Scalar/Properties/
%{perl_vendorlib}/Scalar/Properties.pm

%changelog
* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.13-1
- Updated to release 0.13.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.12-1
- Initial package.
