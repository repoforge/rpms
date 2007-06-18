# $Id$

# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define real_name Business-ISBN
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Work with International Standard Book Numbers
Name: perl-Business-ISBN
Version: 1.84
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Business-ISBN/

Source: http://www.cpan.org/modules/by-module/Business/Business-ISBN-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker), perl

%description
With this module you can work with ISBN numbers.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Business/ISBN.pm

%changelog
* Mon Jun 18 2007 Dries Verachtert <dries@ulyssis.org> - 1.84-1
- Updated to release 1.84.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.82-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.82-1
- Updated to release 1.82.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.80-1
- Updated to release 1.80.

* Sun Mar  6 2005 Dries Verachtert <dries@ulyssis.org> - 1.79-1
- Initial package.
