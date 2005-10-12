# $Id$
# Authority: dries
# Upstream: Geoffrey Rommel <grommel$sears,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Convert-IBM390

Summary: Functions for manipulating mainframe data
Name: perl-Convert-IBM390
Version: 0.20
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-IBM390/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-IBM390-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
onvert::IBM390 is a Perl module.  It supplies various functions that
you may find useful when messing with IBM System/3[679]0 data.  See the
POD documentation in the module, or "man Convert::IBM390" after you have
installed it.

asc2eb, eb2asc, eb2ascp:  ASCII/EBCDIC conversion
packeb, unpackeb:  pack/unpack and convert an EBCDIC record
hexdump:  dump memory in an MVS-like format

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Convert/IBM390.pm
%{perl_vendorarch}/auto/Convert/IBM390/*

%changelog
* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 0.20-1
- Updated to release 0.20.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.19-1
- Initial package.
