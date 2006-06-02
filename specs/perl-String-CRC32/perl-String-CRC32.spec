# $Id$
# Authority: dries
# Upstream: Soenke J. Peters <peters+perl$opcenter,de>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-CRC32

Summary: Cyclic redundency check generation
Name: perl-String-CRC32
Version: 1.4
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-CRC32/

Source: http://search.cpan.org/CPAN/authors/id/S/SO/SOENKE/String-CRC32-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This packages provides a perl module to generate checksums from strings
and from files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" "PREFIX=%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/String/CRC32.p*
%{perl_vendorarch}/auto/String/CRC32

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.3-1.2
- Rebuild for Fedora Core 5.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
