# $Id$
# Authority: dries
# Upstream: Richard Soderberg <perl$crystalflame,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Reporter

Summary: Report test results of a package retrieved from CPAN
Name: perl-Test-Reporter
Version: 1.27
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Reporter/

Source: http://www.cpan.org/modules/by-module/Test/Test-Reporter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Test::Reporter reports the test results of any given distribution to the
CPAN testing service. See http://testers.cpan.org/ for details.
Test::Reporter has wide support for various perl5's and platforms.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man1/*
%doc %{_mandir}/man3/*
%{_bindir}/cpantest
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Reporter.pm
%{perl_vendorlib}/Test/Reporter/*

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.27-1.2
- Rebuild for Fedora Core 5.

* Fri Mar  4 2005 Dries Verachtert <dries@ulyssis.org> - 1.27-1
- Updated to release 1.27.

* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Updated to release 1.25.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.

