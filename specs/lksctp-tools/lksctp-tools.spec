# $Id$
# Authority: shuff
# Upstream: Sridhar Samudrala <sri$us,ibm,com>

# ExclusiveDist: el4 el5

### EL6 ships with lksctp-tools-1.0.10-5.el6
### EL5 ships with lksctp-tools-1.0.6-3.el5
%{?el5:# Tag: rfx}
### EL4 ships with lksctp-tools-1.0.2-6.4E.1
%{?el4:# Tag: rfx}

Summary: User-space access to Linux Kernel SCTP
Name: lksctp-tools
Version: 1.0.10
Release: 3%{?dist}
License: LGPL
Group: System Environment/Libraries
URL: http://lksctp.sourceforge.net/

Source: http://dl.sf.net/project/lksctp/lksctp/lksctp-tools-%{version}/lksctp-tools-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: kernel-devel >= 2.5.36
BuildRequires: libtool
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
%setup

%build
%configure --enable-shared --enable-static
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING COPYING.lib
%doc %{_mandir}/man7/sctp.7*
%{_bindir}/checksctp
%{_bindir}/sctp_darn
%{_bindir}/sctp_status
%{_bindir}/sctp_test
%{_bindir}/withsctp
%{_libdir}/libsctp.so.*
%dir %{_libdir}/lksctp-tools/
%{_libdir}/lksctp-tools/*.so.*
%exclude %{_libdir}/lksctp-tools/*.a
%exclude %{_libdir}/lksctp-tools/*.la

%files devel
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/sctp_*.3*
%{_datadir}/lksctp-tools/
%dir %{_includedir}/netinet/
%{_includedir}/netinet/sctp.h
%{_libdir}/libsctp.so
%dir %{_libdir}/lksctp-tools/
%{_libdir}/lksctp-tools/*.so*
%exclude %{_libdir}/libsctp.a
%exclude %{_libdir}/libsctp.la

%files doc
%defattr(-, root, root, 0755)
%doc doc/*.txt

%changelog
* Wed Feb 16 2011 Dag Wieers <dag@wieers.com> - 1.0.10-3
- Remove .a and .la files.
- Include directories.
- Add man(7) to main package.

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
