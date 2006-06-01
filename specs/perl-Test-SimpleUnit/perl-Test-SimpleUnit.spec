# $Id$
# Authority: dries
# Upstream: Michael Granger <ged-cpan$faeriemud,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-SimpleUnit

Summary: Simplified unit testing framework
Name: perl-Test-SimpleUnit
Version: 1.21
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-SimpleUnit/

Source: http://www.cpan.org/modules/by-module/Test/Test-SimpleUnit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(Data::Compare)

%description
This is a simplified Perl unit-testing framework for creating unit tests to be
run either standalone or under Test::Harness.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*.3*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/SimpleUnit.pm

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.21-1
- Initial package.
