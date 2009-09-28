# $Id$
# Authority: shuff
# Upstream: Sridhar Samudrala <sri$us,ibm,com>

Summary: User-space access to Linux Kernel SCTP
Name: lksctp-tools
Version: 1.0.10
Release: 2
License: LGPL
Group: System Environment/Libraries
URL: http://lksctp.sourceforge.net
Source0: http://downloads.sourceforge.net/project/lksctp/lksctp/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gcc
BuildRequires: libtool, automake, autoconf
BuildRequires: kernel-devel >= 2.5.36

Requires: kernel >= 2.5.36

%description
This is the lksctp-tools package for Linux Kernel SCTP Reference
Implementation.

This package is intended to supplement the Linux Kernel SCTP Reference
Implementation now available in the Linux kernel source tree in
versions 2.5.36 and following.  For more information on LKSCTP see the
package documentation README file, section titled "LKSCTP - Linux
Kernel SCTP."

This package contains the base run-time library & command-line tools.

%package devel
Summary: Development kit for lksctp-tools
Group: Development/Libraries
Requires: %{name} = %{version}
Requires: glibc-devel

%description devel
Development kit for lksctp-tools

- Man pages
- Header files
- Static libraries
- Symlinks to dynamic libraries
- Tutorial source code

%package doc
Summary: Documents pertaining to SCTP
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description doc
Documents pertaining to LKSCTP & SCTP in general
- IETF RFC's & Internet Drafts

%prep
%setup -q -n %{name}-%{version}

%build
%configure --enable-shared --enable-static
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog COPYING.lib
%{_bindir}/*
%{_libdir}/libsctp.so.*
%{_libdir}/lksctp-tools/*

%files devel
%defattr(-,root,root,-)
%{_includedir}
%{_libdir}/libsctp.so
%{_libdir}/libsctp.a
%{_libdir}/libsctp.la
%{_datadir}/lksctp-tools/*
%{_mandir}/*

%files doc
%defattr(-,root,root,-)
%doc doc/*.txt

%changelog
* Mon Sep 28 2009 Steve Huff <shuff@vecna.org> - 1.0.10-2
- some fixes for RPMforge standards compliance
- updated to latest version

* Tue Sep 08 2009 Steve Huff <shuff@vecna.org> - 1.0.6-2
- ported specfile from sf.net SRPM

* Fri Feb 3 2006 Sridhar Samudrala <sri@us.ibm.com> 1.0.6-1
- 1.0.6 Release

* Tue Jan 3 2006 Sridhar Samudrala <sri@us.ibm.com> 1.0.5-1
- 1.0.5 Release
 
* Fri Oct 28 2005 Sridhar Samudrala <sri@us.ibm.com> 1.0.4-1
- 1.0.4 Release
 
* Thu Sep 1 2005 Sridhar Samudrala <sri@us.ibm.com> 1.0.3-1
- 1.0.3 Release
 
* Thu Dec 30 2004 Sridhar Samudrala <sri@us.ibm.com> 1.0.2-1
- 1.0.2 Release
 
* Tue May 11 2004 Sridhar Samudrala <sri@us.ibm.com> 1.0.1-1
- 1.0.1 Release
 
* Thu Feb 26 2004 Sridhar Samudrala <sri@us.ibm.com> 1.0.0-1
- 1.0.0 Release
 
* Fri Feb  6 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 0.9.0-1
- package only .txt doc files

* Wed Feb  4 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 0.7.5-1
- badly placed & undelivered files
- simplified delivery list

* Tue Jan 27 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 0.7.5-1
- Integrate comment from project team

* Sat Jan 10 2004 Francois-Xavier Kowalski <francois-xavier.kowalski@hp.com> 2.6.0_test7_0.7.4-1
- Creation
