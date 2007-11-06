# $Id$
# Authority: dries
# Upstream: Michael G Schwern <mschwern$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Class-Virtual

Summary: Base class for virtual base classes
Name: perl-Class-Virtual
Version: 0.06
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Class-Virtual/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSCHWERN/Class-Virtual-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
This module contains a base class for virtual base classes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Class/Virtual.pm
%{perl_vendorlib}/Class/Virtually

%changelog
* Mon Sep 18 2006 Dries Verachtert <dries@ulyssis.org> - 0.06-1
- Updated to release 0.06.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.05-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.05-1
- Initial package.
