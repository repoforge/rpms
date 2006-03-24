# $Id$
# Authority: dries
# Upstream: Matt Sergeant <matt$sergeant,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Time-Piece

Summary: Object Oriented time objects
Name: perl-Time-Piece
Version: 2.00_01
Release: 1.2
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Time-Piece/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSERGEANT/Time-Piece-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module contains Object Oriented time objects.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} \
		%{buildroot}%{perl_vendorarch}/auto/*{,/*{,/*}}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%dir %{perl_vendorarch}/Time/
%{perl_vendorarch}/Time/Piece.pm
%{perl_vendorarch}/Time/Seconds.pm
%dir %{perl_vendorarch}/auto/Time/
%{perl_vendorarch}/auto/Time/Piece/

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.00_01-1.2
- Rebuild for Fedora Core 5.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 2.00_01-1
- Updated to release 2.00_01.

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.08-1
- Initial package.
