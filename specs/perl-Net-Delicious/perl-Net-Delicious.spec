# $Id$
# Authority: dries
# Upstream: Aaron Straup Cope <ascope$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Delicious

Summary: OOP for the del.icio.us API
Name: perl-Net-Delicious
Version: 1.01
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Delicious/

Source: http://search.cpan.org/CPAN/authors/id/A/AS/ASCOPE/Net-Delicious-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
OOP for the del.icio.us API.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Net/Delicious.pm
%{perl_vendorlib}/Net/Delicious/

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 1.01-1
- Updated to release 1.01.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.96-1
- Updated to release 0.96.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1.2
- Rebuild for Fedora Core 5.

* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.95-1
- Updated to release 0.95.

* Thu Dec 22 2005 Dries Verachtert <dries@ulyssis.org> - 0.94-1
- Initial package.
