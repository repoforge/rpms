# $Id$
# Authority: shuff
# Upstream: Jonathan Rockway <jrockway$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-TableDriven

Summary: write tests, not scripts that run them
Name: perl-Test-TableDriven
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-TableDriven/

Source: http://search.cpan.org/CPAN/authors/id/J/JR/JROCKWAY/Test-TableDriven-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Writing table-driven tests is usually a good idea. Adding a test case doesn't
require adding code, so it's easy to avoid fucking up the other tests. However,
actually going from a table of tests to a test that runs is non-trivial.

Test::TableDriven makes writing the test drivers trivial. You simply define
your test cases and write a function that turns the input data into output data
to compare against. Test::TableDriven will compute how many tests need to be
run, and then run the tests.

Concentrate on your data and what you're testing, not plan tests = scalar keys
%test_cases> and a big foreach loop.


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
%doc MANIFEST
%doc %{_mandir}/man3/Test::TableDriven*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/TableDriven.pm

%changelog
* Mon Sep 28 2009 Steve Huff <shuff@vecna.org> - 0.02-1
- Initial package
