# $Id$
# Authority: dries
# Upstream: Steffen Beyer <sb$engelschall,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bit-ShiftReg

Summary: Bit Shift Registers with Rotate / Shift Operations
Name: perl-Bit-ShiftReg
Version: 2.0
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bit-ShiftReg/

Source: http://www.cpan.org/modules/by-module/Bit/Bit-ShiftReg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
This module implements rotate left, rotate right, arithmetic shift left
and logical shift right operations with carry flag for all C integer types.

The results depend on the number of bits that the integer types unsigned
char, unsigned short, unsigned int and unsigned long have on your machine.

The module automatically determines the number of bits of each integer type
and adjusts its internal constants accordingly.

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
%dir %{perl_vendorarch}/Bit/
%{perl_vendorarch}/Bit/ShiftReg.pm
%dir %{perl_vendorarch}/auto/Bit/
%{perl_vendorarch}/auto/Bit/ShiftReg/

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
