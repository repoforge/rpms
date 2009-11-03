# $Id$
# Authority: dag
# Upstream: Robert Redelmeier <redelm$ev1,net>

# Archs: i586 i686 athlon

%define real_version 1_4

Summary: CPU maximum load (heat) stability test
Name: cpuburn
Version: 1.4
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://users.ev1.net/~redelm/

Source: http://pages.sbcglobal.net/redelm/cpuburn_%{real_version}_tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

ExclusiveArch: i586 i686 athlon

%description
cpuburn is a suite of assembly-coded routines designed to put maximum
heat stress on the CPU and motherboard components by a
P6/P5/K6/K7-optimized mix of FPU and ALU instructions. There are also
routines to test RAM controllers (burnMMX/BX). Please note that this
program is designed to heavily load chips. Undercooled, overclocked,
or otherwise weak systems may fail, causing data loss (filesystem
corruption) and possibly permanent damage to electronic components.
Use it at your own risk!!

%prep
%setup
%{__perl} -pi.orig -e 's|gcc|\$(CC) \$(CFLAGS)|' Makefile

%build
%{__make} %{?_smp_mflags} \
	CC="%{__cc}" \
	CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -p -m0755 burn{BX,K6,K7,MMX,P5,P6} %{buildroot}%{_sbindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Design README
%{_sbindir}/burn*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.4-1.2
- Rebuild for Fedora Core 5.

* Fri Sep 24 2004 Dag Wieers <dag@wieers.com> - 1.4-1
- Initial package. (using DAR)
