# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Prereq

Summary: Check if Makefile.PL has the right pre-requisites
Name: perl-Test-Prereq
Version: 1.029
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Prereq/

Source: http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/Test-Prereq-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Check if Makefile.PL has the right pre-requisites.

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
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Test/Prereq.pm
%{perl_vendorlib}/Test/Prereq

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.029-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 1.029-1
- Updated to release 1.029.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.028-1
- Updated to release 1.028.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.027-1
- Initial package.
