# $Id$
# Authority: dries
# Upstream: Kees Cook <cook-cpan$outflux,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Device-SerialPort

Summary: Linux/POSIX emulation of Win32::SerialPort functions
Name: perl-Device-SerialPort
Version: 1.04
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Device-SerialPort/

Source: http://www.cpan.org/modules/by-module/Device/Device-SerialPort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

Obsoletes: perl-Device-SerialPorts <= %{version}-%{release}
Provides: perl-Device-SerialPorts = %{release}-%{version}

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
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" /dev/ttyS1
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find eg/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README TODO eg/
%doc %{_mandir}/man1/modemtest.1*
%doc %{_mandir}/man3/Device::SerialPort.3pm*
%{_bindir}/modemtest
%dir %{perl_vendorarch}/Device/
%{perl_vendorarch}/Device/SerialPort.pm
%dir %{perl_vendorarch}/auto/Device/
%{perl_vendorarch}/auto/Device/SerialPort/

%changelog
* Mon Jul  6 2009 Christoph Maser <cmr@financial.com> - 1.04-1
- Updated to version 1.04.

* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.003001-1
- Updated to release 1.003001.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 1.002-1
- Initial package.

* Mon Jul 21 2003 Dag Wieers <dag@wieers.com> - 0.22-1
- Disabled examples.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.22-0
- Initial package. (using DAR)
