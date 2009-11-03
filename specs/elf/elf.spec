# $Id$
# Authority: dag

%define real_version 0.5.4p1

Summary: Simple ELF header analyzer
Name: elf
Version: 0.5.4
Release: 0.p1.2%{?dist}
License: GPL
Group: Applications/System
URL: http://www.kerneled.com/projects/elf/

#Source: http://www.kerneled.com/projects/elf/elf-%{real_version}.tar.bz2
Source: http://distro.ibiblio.org/pub/linux/distributions/sorcerer/sources/elf/%{real_version}/elf-%{real_version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: readline-devel

%description
elf is an ELF header (e_header) analysis tool. It allows you to gather
various information from a binary's ELF header. An intuitive interactive
and command-line mode is available.

%prep
%setup -n %{name}-%{real_version}

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|\$\(BINDIR\)|\$(bindir)|;
		s|\$\(INSDIR\)|\$(mandir)/man1|;
	' src/Makefile.in doc/Makefile.in

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
### FIXME: Makefile doesn't create target directories (Please fix upstream)
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING CREDITS README
%doc %{_mandir}/man?/*
%{_bindir}/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.5.4-0.p1.2
- Rebuild for Fedora Core 5.

* Sun Oct 19 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0.p1
- Updated to release 0.5.4p1.

* Fri Sep 19 2003 Dag Wieers <dag@wieers.com> - 0.5.4-0
- Initial package. (using DAR)
