# $Id$
# Authority: dries
# Upstream: Steffen Schwigon <schwigon$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name PDF-FDF-Simple

Summary: Read and write (Acrobat) FDF files
Name: perl-PDF-FDF-Simple
Version: 0.10
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PDF-FDF-Simple/

Source: http://search.cpan.org/CPAN/authors/id/S/SC/SCHWIGON/pdf-fdf-simple/PDF-FDF-Simple-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl, perl-Module-Build

%description
PDF::FDF::Simple helps creating and extracting FDF files. It is
meant to be a simple replacement for the Adobe FdfToolkit when you
just want to read or create fdf files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir="%{buildroot}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/PDF/FDF/Simple.p*

%changelog
* Sat Jan  7 2006 Dries Verachtert <dries@ulyssis.org> - 0.10-1
- Updated to release 0.10.

* Fri Dec  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.09-1
- Initial package.
