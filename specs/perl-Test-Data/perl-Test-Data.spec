# $Id$
# Authority: dries
# Upstream: brian d foy <bdfoy$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Data

Summary: Test functions for particular variable types
Name: perl-Test-Data
Version: 1.20
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Data/

Source: http://search.cpan.org/CPAN/authors/id/B/BD/BDFOY/Test-Data-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
Test functions for particular variable types.

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
%{perl_vendorlib}/Test/Data.pm
%{perl_vendorlib}/Test/Data

%changelog
* Sun Apr 29 2007 Dries Verachtert <dries@ulyssis.org> - 1.20-1
- Updated to release 1.20.

* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.19-1
- Updated to release 1.19.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.18-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 1.18-1
- Updated to release 1.18.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.17-1
- Initial package.
