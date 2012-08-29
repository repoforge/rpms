# $Id$
# Authority: dag

### EL6 ships with tftp-0.49-5.1.el6
### EL5 ships with tftp-0.49-2
### EL4 ships with tftp-0.39-3.el4
### EL3 ships with tftp-0.39-0.EL3.4
### EL2 ships with tftp-0.17-14
# Tag: rfx

%define _default_patch_fuzz 2

%{?el5:%define _without_tcpwrappersdevel 1}
%{?el4:%define _without_tcpwrappersdevel 1}
%{?el3:%define _without_tcpwrappersdevel 1}

Summary: The client for the Trivial File Transfer Protocol (TFTP)
Name: tftp
Version: 5.2
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: http://www.kernel.org/pub/software/network/tftp/

Source0: http://www.kernel.org/pub/software/network/tftp/tftp-hpa-%{version}.tar.bz2
Patch0: tftp-0.40-remap.patch
Patch2: tftp-hpa-0.39-tzfix.patch
Patch3: tftp-0.42-tftpboot.patch
Patch4: tftp-0.49-chk_retcodes.patch
Patch5: tftp-hpa-0.49-fortify-strcpy-crash.patch
Patch6: tftp-0.49-stats.patch
Patch7: tftp-0.49-ebuf.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: readline-devel
%{!?_without_tcpwrappersdevel:BuildRequires: tcp_wrappers-devel}
%{!?_without_tcpwrappers:BuildRequires: tcp_wrappers}

%description
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations.  The tftp package provides the user
interface for TFTP, which allows users to transfer files to and from a
remote machine.  This program and TFTP provide very little security,
and should not be enabled unless it is expressly needed.

%package server
Group: System Environment/Daemons
Summary: The server for the Trivial File Transfer Protocol (TFTP)
Requires: xinetd
Requires(post): /sbin/service
Requires(postun): /sbin/service

%description server
The Trivial File Transfer Protocol (TFTP) is normally used only for
booting diskless workstations.  The tftp-server package provides the
server for TFTP, which allows users to transfer files to and from a
remote machine. TFTP provides very little security, and should not be
enabled unless it is expressly needed.  The TFTP server is run from
%{_sysconfdir}/xinetd.d/tftp, and is disabled by default.

%prep
%setup -n tftp-hpa-%{version}
%patch0 -p1 -b .zero
%patch2 -p1 -b .tzfix
%patch3 -p1 -b .tftpboot
%patch4 -p1 -b .chk_retcodes
%patch5 -p1 -b .fortify-strcpy-crash
%patch6 -p1 -b .stats
#patch7 -p1 -b .ebuf

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__install} -d -m0755 %{buildroot}%{_mandir}/man1/
%{__install} -d -m0755 %{buildroot}%{_mandir}/man8/
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/tftpboot/
%{__make} install \
    INSTALLROOT="%{buildroot}" \
    MANDIR="%{_mandir}" \
    SBINDIR="%{_sbindir}" \
    INSTALL="install -p"

%{__sed} -i.orig \
    -e 's:/var:%{_localstatedir}:' \
    -e 's:/usr/sbin:%{_sbindir}:' \
    tftp-xinetd
touch -r tftp-xinetd.orig tftp-xinetd
%{__install} -Dp -m0755 tftp-xinetd %{buildroot}%{_sysconfdir}/xinetd.d/tftp

%post server
/sbin/service xinetd reload &>/dev/null || :

%postun server
if (( $1 == 0 )); then
    /sbin/service xinetd reload &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL README*
%doc %{_mandir}/man1/tftp.1*
%{_bindir}/tftp

%files server
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL README*
%doc %{_mandir}/man8/in.tftpd.8*
%doc %{_mandir}/man8/tftpd.8*
%config(noreplace) %{_sysconfdir}/xinetd.d/tftp
%dir %{_localstatedir}/lib/tftpboot/
%{_sbindir}/in.tftpd

%changelog
* Wed Jul 04 2012 Dag Wieers <dag@wieers.com> - 5.2-1
- Updated to release 5.2.

* Mon Jul 18 2011 Jiri Skala <jskala@redhat.com> - 0.49-7
- Resolves: #714240 - rebuild for fastrack

* Thu Jul 14 2011 Jiri Skala <jskala@redhat.com> - 0.49-6
- Resolves: #655830 - transferring small files using -v returns strange values
- Resolves: #714240 - utimeout option parsing buffer overflow

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.49-5.1
- Rebuilt for RHEL 6

* Wed Aug 05 2009 Warren Togami <wtogami@redhat.com> - 0.49-5
- Bug #515361 tftp FORTIFY_SOURCE strcpy crash 

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Jiri Skala <jskala@redhat.com> - 0.49-2
- #473487 - unchecked return values

* Tue Nov 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.49-1
- update to 0.49

* Wed May 21 2008 Warren Togami <wtogami@redhat.com. - 0.48-6
- undo symlink stuff completely because they are problematic
  See Bug #447135 for details.

* Wed May 21 2008 Martin Nagy <mnagy@redhat.com> - 0.48-5
- fix troubles caused by added symlink

* Tue May 20 2008 Martin Nagy <mnagy@redhat.com> - 0.48-4
- add symlink to /var/lib/tftpboot

* Mon Mar 03 2008 Martin Nagy <mnagy@redhat.com> - 0.48-3
- changed description (#234099)

* Mon Feb 11 2008 Martin Nagy <mnagy@redhat.com> - 0.48-2
- rebuild for gcc-4.3

* Tue Jan 22 2008 Martin Nagy <mnagy@redhat.com> - 0.48-1
- upgrade to 0.48
- remove the old sigjmp patch (fixed in upstream)
- make some changes in spec file (#226489)

* Tue Jan 22 2008 Martin Nagy <mnagy@redhat.com> - 0.42-6
- changed the location of tftpboot directory to /var/lib/

* Fri Aug 31 2007 Maros Barabas <mbarabas@redhat.com> - 0.42-5
- rebuild

* Mon Feb 19 2007 Maros Barabas <mbarabas@redhat.com> - 0.42-4
- make some changes in spec file (review)
- Resolves #226489

* Mon Dec 04 2006 Maros Barabas <mbarabas@redhat.com> - 0.42-3.2
- change BuildRequires from tcp_wrappers to tcp_wrappers-devel

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.42-3.1
- rebuild

* Mon Apr 10 2006 Radek Vokál <rvokal@redhat.com> 0.42-3
- show localtime instead of GMT (#172274)

* Wed Mar 22 2006 Radek Vokál <rvokal@redhat.com> 0.42-2
- fix double free error when hitting ^C (#186201)

* Wed Feb 22 2006 Radek Vokál <rvokal@redhat.com> 0.42-1
- upgrade to 0.42

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 0.41-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 0.41-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Nov 03 2005 Radek Vokal <rvokal@redhat.com> 0.41-1
- upstream update (patterns fixes)

* Tue Apr 19 2005 Radek Vokal <rvokal@redhat.com> 0.40-6
- fix remap rules convert error <pjones@redhat.com>

* Wed Mar 23 2005 Radek Vokal <rvokal@redhat.com> 0.40-5
- use tftp-xinetd from tarball (#143589)

* Fri Mar 04 2005 Radek Vokal <rvokal@redhat.com> 0.40-4
- gcc4 rebuilt

* Sun Feb 27 2005 Florian La Roche <laroche@redhat.com>
- Copyright: -> License

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 0.40-2
- Rebuilt for new readline.

* Mon Nov 15 2004 Radek Vokal <rvokal@redhat.com> 0.40-1
- Update to new upstream version, fixes #139328

* Mon Sep 13 2004 Elliot Lee <sopwith@redhat.com> 0.39-1
- Update to new version makes tftp work, says upstream.
- Remove malta patch

* Mon Sep 13 2004 Elliot Lee <sopwith@redhat.com> 0.38-1
- Update to new version fixes #131736

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Jun 03 2004 Elliot Lee <sopwith@redhat.com> 0.36-1
- Update version

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 11 2003 Elliot Lee <sopwith@redhat.com>
- 0.33
- Add /tftpboot directory (#88204)

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun Feb 23 2003 Tim Powers <timp@redhat.com>
- add BuildPreReq on tcp_wrappers

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 11 2002 Elliot Lee <sopwith@redhat.com> 0.32-1
- Update to 0.32

* Wed Oct 23 2002 Elliot Lee <sopwith@redhat.com> 0.30-1
- Fix #55789
- Update to 0.30

* Thu Jun 27 2002 Elliot Lee <sopwith@redhat.com>
- Try applying HJ's patch from #65476

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon Jun 17 2002 Elliot Lee <sopwith@redhat.com>
- Update to 0.29

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Dec 18 2001 Elliot Lee <sopwith@redhat.com> 0.17-15
- Add patch4: netkit-tftp-0.17-defaultport.patch for bug #57562
- Update to tftp-hpa-0.28 (bug #56131)
- Remove include/arpa/tftp.h to fix #57259
- Add resource limits in tftp-xinetd (#56722)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Tue Jun 12 2001 Helge Deller <hdeller@redhat.de> (0.17-13)
- updated tftp-hpa source to tftp-hpa-0.17
- tweaked specfile with different defines for tftp-netkit and tftp-hpa version
- use hpa's tftpd.8 man page instead of the netkits one

* Mon May 07 2001 Helge Deller <hdeller@redhat.de>
- rebuilt in 7.1.x

* Wed Apr 18 2001 Helge Deller <hdeller@redhat.de>
- fix tftp client's put problems (#29529)
- update to tftp-hpa-0.16

* Wed Apr  4 2001 Jakub Jelinek <jakub@redhat.com>
- don't let configure to guess compiler, it can pick up egcs

* Thu Feb 08 2001 Helge Deller <hdeller@redhat.de>
- changed "wait" in xinetd file to "yes" (hpa-tftpd forks and exits) (#26467)
- fixed hpa-tftpd to handle files greater than 32MB (#23725)
- added "-l" flag to hpa-tftpd for file-logging (#26467)
- added description for "-l" to the man-page 

* Thu Feb 08 2001 Helge Deller <hdeller@redhat.de>
- updated tftp client to 0.17 stable (#19640),
- drop dependency on xinetd for tftp client (#25051),

* Wed Jan 17 2001 Jeff Johnson <jbj@redhat.com>
- xinetd shouldn't wait on tftp (which forks) (#23923).

* Sat Jan  6 2001 Jeff Johnson <jbj@redhat.com>
- fix to permit tftp put's (#18128).
- startup as root with chroot to /tftpboot with early reversion to nobody
  is preferable to starting as nobody w/o ability to chroot.
- %%post is needed by server, not client. Add %%postun for erasure as well.

* Wed Aug 23 2000 Nalin Dahyabhai <nalin@redhat.com>
- default to being disabled

* Thu Aug 17 2000 Jeff Johnson <jbj@redhat.com>
- correct group.

* Tue Jul 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- change user from root to nobody

* Sat Jul 22 2000 Jeff Johnson <jbj@redhat.com>
- update to tftp-hpa-0.14 (#14003).
- add server_args (#14003).
- remove -D_BSD_SOURCE (#14003).

* Fri Jul 21 2000 Nalin Dahyabhai <nalin@redhat.com>
- cook up an xinetd config file for tftpd

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to 0.17.

* Fri May  5 2000 Matt Wilson <msw@redhat.com>
- use _BSD_SOURCE for hpa's tftpd so we get BSD signal semantics.

* Fri Feb 11 2000 Bill Nottingham <notting@redhat.com>
- fix description

* Wed Feb  9 2000 Jeff Johnson <jbj@redhat.com>
- compress man pages (again).

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- man pages are compressed
- fix description and summary

* Tue Jan  4 2000 Bill Nottingham <notting@redhat.com>
- split client and server

* Tue Dec 21 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.16.

* Sat Aug 28 1999 Jeff Johnson <jbj@redhat.com>
- update to 0.15.

* Wed Apr  7 1999 Jeff Johnson <jbj@redhat.com>
- tftpd should truncate file when overwriting (#412)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 22)

* Mon Mar 15 1999 Jeff Johnson <jbj@redhat.com>
- compile for 6.0.

* Fri Aug  7 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Sep 22 1997 Erik Troan <ewt@redhat.com>
- added check for getpwnam() failure

* Tue Jul 15 1997 Erik Troan <ewt@redhat.com>
- initial build
