# $Id$
# Authority: yury
# Upstream: Wietse Venema <wietse$wzv,win,tue,nl>

### EL6 ships with tcp_wrappers-7.6-56.3.el6
### EL5 ships with tcp_wrappers-7.6-40.7.el5
### EL4 ships with tcp_wrappers-7.6-37.9.el4
### EL3 ships with tcp_wrappers-7.6-34.1
### EL2 ships with tcp_wrappers-7.6-19
# Tag: rfx

Summary: A security tool which acts as a wrapper for TCP daemons
Name: tcp_wrappers
Version: 7.6
Release: 57%{?dist}

%define LIB_MAJOR 0
%define LIB_MINOR 7
%define LIB_REL 6

License: BSD
Group: System Environment/Daemons
Source: ftp://ftp.porcupine.org/pub/security/%{name}_%{version}.tar.gz
URL: ftp://ftp.porcupine.org/pub/security/index.html
Patch0: tcpw7.2-config.patch
Patch1: tcpw7.2-setenv.patch
Patch2: tcpw7.6-netgroup.patch
Patch3: tcp_wrappers-7.6-bug11881.patch
Patch4: tcp_wrappers-7.6-bug17795.patch
Patch5: tcp_wrappers-7.6-bug17847.patch
Patch6: tcp_wrappers-7.6-fixgethostbyname.patch
Patch7: tcp_wrappers-7.6-docu.patch
Patch9: tcp_wrappers.usagi-ipv6.patch
Patch10: tcp_wrappers.ume-ipv6.patch
Patch11: tcp_wrappers-7.6-shared.patch
Patch12: tcp_wrappers-7.6-sig.patch
Patch13: tcp_wrappers-7.6-strerror.patch
Patch14: tcp_wrappers-7.6-ldflags.patch
Patch15: tcp_wrappers-7.6-fix_sig-bug141110.patch
Patch16: tcp_wrappers-7.6-162412.patch
Patch17: tcp_wrappers-7.6-220015.patch
Patch18: tcp_wrappers-7.6-restore_sigalarm.patch
Patch19: tcp_wrappers-7.6-siglongjmp.patch
Patch20: tcp_wrappers-7.6-sigchld.patch
Patch21: tcp_wrappers-7.6-196326.patch
Patch22: tcp_wrappers_7.6-249430.patch
# required by sin_scope_id in ipv6 patch
BuildRequires: glibc-devel >= 2.2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: tcp_wrappers-libs = %{version}-%{release}
Obsoletes: tcp_wrappers < 7.6-41

%description
The tcp_wrappers package provides small daemon programs which can
monitor and filter incoming requests for systat, finger, FTP, telnet,
rlogin, rsh, exec, tftp, talk and other network services.

Install the tcp_wrappers program if you need a security tool for
filtering incoming network services requests.

This version also supports IPv6.

%package libs
Summary: tcp_wrappers libraries
Group: System Environment/Libraries
Obsoletes: tcp_wrappers < 7.6-41

%description libs
tcp_wrappers-libs contains the libraries of the tcp_wrappers package.

%package devel
Summary: tcp_wrappers development libraries and headers
Group: Development/Libraries
Obsoletes: tcp_wrappers < 7.6-41
Requires: tcp_wrappers-libs = %{version}-%{release}

%description devel
tcp_wrappers-devel contains the libraries and header files needed to
develop applications with tcp_wrappers support.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1 -b .config
%patch1 -p1 -b .setenv
%patch2 -p1 -b .netgroup
%patch3 -p1 -b .bug11881
%patch4 -p1 -b .bug17795
%patch5 -p1 -b .bug17847
%patch6 -p1 -b .fixgethostbyname
%patch7 -p1 -b .docu
%patch9 -p1 -b .usagi-ipv6
%patch10 -p1 -b .ume-ipv6
%patch11 -p1 -b .shared
%patch12 -p1 -b .sig
%patch13 -p1 -b .strerror
%patch14 -p1 -b .cflags
%patch15 -p1 -b .fix_sig
%patch16 -p1 -b .162412
%patch17 -p1 -b .220015
%patch18 -p1 -b .restore_sigalarm
%patch19 -p1 -b .siglongjmp
%patch20 -p1 -b .sigchld
%patch21 -p1 -b .196326
%patch22 -p1 -b .249430

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR" LDFLAGS="-pie" MAJOR=%{LIB_MAJOR} MINOR=%{LIB_MINOR} REL=%{LIB_REL} linux


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
mkdir -p ${RPM_BUILD_ROOT}/%{_lib}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man{3,5,8}
mkdir -p ${RPM_BUILD_ROOT}%{_sbindir}

install -p -m644 hosts_access.3 ${RPM_BUILD_ROOT}%{_mandir}/man3
install -p -m644 hosts_access.5 hosts_options.5 ${RPM_BUILD_ROOT}%{_mandir}/man5
install -p -m644 tcpd.8 tcpdchk.8 tcpdmatch.8 ${RPM_BUILD_ROOT}%{_mandir}/man8
ln -sf hosts_access.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/hosts.allow.5
ln -sf hosts_access.5 ${RPM_BUILD_ROOT}%{_mandir}/man5/hosts.deny.5
#cp -a libwrap.a ${RPM_BUILD_ROOT}%{_libdir}
cp -a libwrap.so* ${RPM_BUILD_ROOT}/%{_lib}
install -p -m644 tcpd.h ${RPM_BUILD_ROOT}%{_includedir}
install -m755 safe_finger ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 tcpd ${RPM_BUILD_ROOT}%{_sbindir}
install -m755 try-from ${RPM_BUILD_ROOT}%{_sbindir}

# XXX remove utilities that expect /etc/inetd.conf (#16059).
#install -m755 tcpdchk ${RPM_BUILD_ROOT}%{_sbindir}
#install -m755 tcpdmatch ${RPM_BUILD_ROOT}%{_sbindir}
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man8/tcpdmatch.*
rm -f ${RPM_BUILD_ROOT}%{_mandir}/man8/tcpdchk.*

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
%{_sbindir}/*
%{_mandir}/man8/*

%files libs
%defattr(-,root,root,-)
%doc BLURB CHANGES README* DISCLAIMER Banners.Makefile
/%{_lib}/*.so.*
%{_mandir}/man5/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
#%{_libdir}/*.a
/%{_lib}/*.so
%{_mandir}/man3/*

%changelog
* Fri Dec 25 2009 Yury V. Zaytsev <yury@shurup.com> - 7.6-57
- Ported over RPMForge with minor changes.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-56
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Jan F. Chadima <jchadima@redhat.com> - 7.6-55
- resolving addr when name == "" (repair of patch #220015)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Jan Safranek <jsafranek@redhat.com> - 7.6-53
- rediff all patches to get rid of patch fuzz

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 7.6-52
- Autorebuild for GCC 4.3

* Tue Oct 16 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-51
- review changes

* Fri Aug 24 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-50
- license tag update (and rebuild for BuildID, etc.)
- include docs in the -libs subpackage, as it is the only one installed on most
  systems (and to comply with the license text)

* Wed Jul 25 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-49
- fix for a.b.c.d/255.255.255.255 - fixes #249430

* Thu Jun 28 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-48
- dropped the hostname resolving patch
- resolve the address given to hosts_ctl to hostname, if hostname not given
- compare localhost and localhost.localdomain as the same
- fixed a few compile warnings

* Wed Jun 06 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-47
- fix the hostname resolving patch for x86_64

* Mon May 28 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-46
- modified the fix for #112975 to fix #156373 as well

* Fri May 25 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-45
- unblock and catch SIGCHLD from spawned shell commands, fixes #112975

* Mon Apr 16 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-44
- added restore_sigalarm and siglongjmp patches from Debian, fixes #205129

* Fri Mar 09 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-43
- resolve hostnames in hosts.{allow,deny}, should fix a bunch of issues with
  IPv4/6

* Thu Mar 08 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-42.1
- moved libwrap.so* to /lib
- removed the static library libwrap.a

* Mon Mar 05 2007 Tomas Janousek <tjanouse@redhat.com> - 7.6-42
- added Obsoletes field so that the upgrade goes cleanly
- added dist tag

* Mon Dec  4 2006 Thomas Woerner <twoerner@redhat.com> 7.6-41
- moved devel libraries, headers and man pages into devel sub package (#193188)
- new libs sub package for libraries
- using BuildRequires instead of BuildPreReq

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 7.6-40.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 7.6-40.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 7.6-40.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 24 2006 Thomas Woerner <twoerner@redhat.com> 7.6-40
- fixed uninitialized fp in function inet_cfg (#162412)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri May  6 2005 Thomas Woerner <twoerner@redhat.com> 7.6-39
- fixed sig patch (#141110). Thanks to Nikita Shulga for the patch

* Wed Feb  9 2005 Thomas Woerner <twoerner@redhat.com> 7.6-38
- rebuild

* Thu Oct  7 2004 Thomas Woerner <twoerner@redhat.com> 7.6-37.2
- new URL and spec file cleanup, patch from Robert Scheck

* Mon Oct  4 2004 Thomas Woerner <twoerner@redhat.com> 7.6-37.1
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Mar  5 2004 Thomas Woerner <twoerner@redhat.com> 7.6-36
- pied tcpd

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Feb 16 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- use strerror  #84312

* Tue Feb 11 2003 Harald Hoyer <harald@redhat.de> 7.6-33
- revert Nalins weak version
- link libwrap.so against libnsl, on which it depends

* Mon Feb 10 2003 Nalin Dahyabhai <nalin@redhat.com> 7.6-32
- link libwrap.so against libnsl, on which it depends
- add default (weak) versions of allow_severity and deny_severity to the shared
  library so that configure tests can find it correctly

* Mon Feb 10 2003 Harald Hoyer <harald@redhat.de> 7.6-29
- shared library generated and added #75494
- added security patch tcp_wrappers-7.6-sig.patch
- compile and link with -fPIC -DPIC

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan  7 2003 Jeff Johnson <jbj@redhat.com> 7.6-25
- don't include -debuginfo files in package.

* Tue Nov 19 2002 Tim Powers <timp@redhat.com>
- rebuild on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix #61192
- added Patch8 to fix #17847
- update IPv6 patch

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Mar 11 2001 Pekka Savola <pekkas@netcore.fi>
- Add IPv6 patch from USAGI, enable it.

* Mon Feb  5 2001 Preston Brown <pbrown@redhat.com>
- fix gethostbyname to work better with dot "." notation (#16949)

* Sat Dec 30 2000 Jeff Johnson <jbj@redhat.com>
- permit hosts.{allow,deny} to be assembled from included components (#17795).
- permit '*' and '?' wildcard matches on hostnames (#17847).

* Sun Nov 19 2000 Bill Nottingham <notting@redhat.com>
- ia64 needs -fPIC too

* Mon Aug 14 2000 Jeff Johnson <jbj@redhat.com>
- remove utilities that expect /etc/inetd.conf (#16059).

* Thu Jul 27 2000 Jeff Johnson <jbj@redhat.com>
- security hardening (#11881).

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun  6 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.

* Tue May 16 2000 Chris Evans <chris@ferret.lmh.ox.ac.uk>
- Make tcpd mode -rwx--x--x as a security hardening measure

* Mon Feb  7 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages.

* Mon Aug 23 1999 Jeff Johnson <jbj@redhat.com>
- add netgroup support (#3940).

* Wed May 26 1999 Jeff Johnson <jbj@redhat.com>
- compile on sparc with -fPIC.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 7)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- build for glibc 2.1

* Sat Aug 22 1998 Jeff Johnson <jbj@redhat.com>
- close setenv bug (problem #690)
- spec file cleanup

* Thu Jun 25 1998 Alan Cox <alan@redhat.com>
- Erp where did the Dec 05 patch escape to

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Dec 05 1997 Erik Troan <ewt@redhat.com>
- don't build setenv.o module -- it just breaks things

* Wed Oct 29 1997 Marc Ewing <marc@redhat.com>
- upgrade to 7.6

* Thu Jul 17 1997 Erik Troan <ewt@redhat.com>
- built against glibc

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Upgraded to version 7.5
- Uses a build root
