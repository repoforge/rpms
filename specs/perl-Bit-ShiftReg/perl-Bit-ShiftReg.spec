# $Id$
# Authority: dries
# Upstream: Steffen Beyer <sb$engelschall,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Bit-ShiftReg

Summary: Bit Shift Registers with Rotate / Shift Operations
Name: perl-Bit-ShiftReg
Version: 2.0
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Bit-ShiftReg/

Source: http://search.cpan.org/CPAN/authors/id/S/ST/STBEY/Bit-ShiftReg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(ExtUtils::MakeMaker), perl

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
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install
%{__rm} -rf %{buildroot}%{perl_archlib}/perllocal.pod %{buildroot}%{perl_vendorarch}/auto/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Bit/ShiftReg.pm
%{perl_vendorarch}/auto/Bit/ShiftReg

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 2.0-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
