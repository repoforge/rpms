# $Id$
# Authority: dries
# Upstream: Soenke J. Peters <peters+perl$opcenter,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name String-CRC32

Summary: Cyclic redundency check generation
Name: perl-String-CRC32
Version: 1.4
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/String-CRC32/

Source: http://www.cpan.org/modules/by-module/String/String-CRC32-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This packages provides a perl module to generate checksums from strings
and from files.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/String/
%{perl_vendorarch}/String/CRC32.pm
%{perl_vendorarch}/String/CRC32.pod
%dir %{perl_vendorarch}/auto/String/
%{perl_vendorarch}/auto/String/CRC32

%changelog
* Fri Jun  2 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1
- Updated to release 1.4.

* Wed Jun  8 2005 Dries Verachtert <dries@ulyssis.org> - 1.3-1
- Updated to release 1.3.

* Sat Apr  2 2005 Dries Verachtert <dries@ulyssis.org> - 1.2-1
- Initial package.
