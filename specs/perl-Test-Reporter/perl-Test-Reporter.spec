# $Id$

# Authority: dries
# Upstream: Richard Soderberg <perl$crystalflame,net>

%define real_name Test-Reporter
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Report test results of a package retrieved from CPAN
Name: perl-Test-Reporter
Version: 1.25
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Reporter/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/R/RS/RSOD/Test-Reporter-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Test::Reporter reports the test results of any given distribution to the
CPAN testing service. See http://testers.cpan.org/ for details.
Test::Reporter has wide support for various perl5's and platforms.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/cpantest
%{perl_vendorlib}/Test/Reporter.pm
%{perl_vendorlib}/Test/Reporter/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.25-1
- Updated to release 1.25.

* Mon Dec 27 2004 Dries Verachtert <dries@ulyssis.org> - 1.24-1
- Initial package.

