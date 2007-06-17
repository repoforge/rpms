# $Id$
# Authority: dries
# Upstream: Kees Cook <cook-cpan$outflux,net>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Device-SerialPort

Summary: Linux/POSIX emulation of Win32::SerialPort functions
Name: perl-Device-SerialPort
Version: 1.002
Release: 1.2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Device-SerialPort/

Source: http://search.cpan.org/CPAN/authors/id/C/CO/COOK/Device-SerialPort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, perl(ExtUtils::MakeMaker)

%description
This is a POSIX-based version of the Win32::Serialport module ported by
Joe Doss for the MisterHouse Home Automation Package from Version 0.08
of the Win32 module. He replaced calls to the Win32 API with similar
functions implemented using POSIX calls. While most of the testing has
occurred on linux, the package should work on other POSIX-compliant
Operating Systems.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} -pi -e 's/^if \(\!defined\(\$file\)\)/if (1 == 0)/g;' Makefile.PL
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" TESTPORT=/dev/ttyS1
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
%doc %{_mandir}/man?/*
%{_bindir}/modemtest
%{perl_vendorarch}/Device/SerialPort.pm
%{perl_vendorarch}/auto/Device/SerialPort

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 1.002-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.002-1
- Initial package.
