# $Id$
# Authority: dag
# Upstream: spoon <spoon$ix,netcom,com>

Summary: Linux Capability Remover
Name: lcap
Version: 0.0.6
Release: 6.2%{?dist}
License: GPL
Group: System Environment/Base
URL: http://pweb.netcom.com/~spoon/lcap/

Source: http://svn.rpmforge.net/svn/trunk/rpms/lcap/lcap-%{version}.tar.bz2
Patch1: lcap-0.0.6-morecaps.patch
Patch2: lcap-0.0.6-manpage.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Linux kernel versions 2.2.11 and greater include the idea of a "capability
bounding set," a list of capabilities that can be held by any process on
the system. "Capabilities" are a form of kernel-based access control.

lcap allows a system administrator to remove specific capabilities from
the kernel in order to make the system more secure. lcap modifies the
sysctl file /proc/sys/kernel/cap-bound.

%prep
%setup
%patch1 -p1 -b .morecaps
%patch2 -p1 -b .manpage

%{__perl} -pi.orig -e '
		s|\$\(prefix\)/sbin|\$(DESTDIR)\$(sbindir)|;
		s|\$\(prefix\)/usr/man|\$(DESTDIR)\$(mandir)|;
	' Makefile

%build
%{__make} %{?_smp_mflags} \
	CFLAGS="%{optflags} -Wall -DVERSION=%{version}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -Dp -m0644 lcap.8 %{buildroot}%{_mandir}/man8/lcap.8

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_mandir}/man8/lcap.8*
%{_sbindir}/lcap

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.0.6-6.2
- Rebuild for Fedora Core 5.

* Fri Aug 20 2004 Dag Wieers <dag@wieers.com> - 0.0.6-6
- Package contributed by Troels Arvin.

* Thu Aug 19 2004 Troels Arvin <troels@arvin.dk>
- Additions to manpage.
- Better package description.
- Removed URLs to project home and source, as those seem to be gone.

* Tue Dec 02 2003 Troels Arvin <troels@arvin.dk>
- Redhatized version, based on PLD's package.
