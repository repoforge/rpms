# $Id$
# Authority: dries
# Upstream: Matt S Trout <perl-stuff$trout,me,uk>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Guile

Summary: Interface to the Guile Scheme interpreter
Name: perl-Guile
Version: 0.002
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Guile/

Source: http://search.cpan.org/CPAN/authors/id/M/MS/MSTROUT/Guile-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, guile-devel

%description
This module provides an interface to the Gnu Guile system.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Guile.pm
%{perl_vendorarch}/Guile
%{perl_vendorarch}/auto/Guile

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.002-1
- Initial package.
