# $Id$
# Authority: dries
# Upstream: Michael Granger <ged-cpan$faeriemud,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-SimpleUnit

Summary: Simplified unit testing framework
Name: perl-Test-SimpleUnit
Version: 1.21
Release: 2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-SimpleUnit/

Source: http://www.cpan.org/modules/by-module/Test/Test-SimpleUnit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::Compare) >= 0.02
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Carp)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IO::File)
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This is a simplified Perl unit-testing framework for creating unit tests to be
run either standalone or under Test::Harness.

%prep
%setup -n %{real_name}-%{version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc ChangeLog README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/SimpleUnit.pm

%changelog
* Fri Jun 02 2006 Dag Wieers <dag@wieers.com> - 1.21-2
- Got rid of perl-ExtUtils-AutoInstall

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
