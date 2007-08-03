# $Id$
# Authority: dag

%define real_name Device-SerialPort

Summary: Device-SerialPort - Linux/POSIX emulation of Win32::SerialPort functions
Name: perl-Device-SerialPorts
Version: 0.22
Release: 1.2
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Device-SerialPorts/

Source: http://www.cpan.org/modules/by-module/Device/Device-SerialPort-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0, perl(ExtUtils::MakeMaker)
Requires: perl >= 0:5.8.0

%description
This module provides an object-based user interface essentially
identical to the one provided by the Win32::SerialPort module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO
### FIXME: Disabled examples
#%doc eg/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.22-1.2
- Rebuild for Fedora Core 5.

* Mon Jul 21 2003 Dag Wieers <dag@wieers.com> - 0.22-1
- Disabled examples.

* Sun Jul 20 2003 Dag Wieers <dag@wieers.com> - 0.22-0
- Initial package. (using DAR)
