# Authority: dag
# Dists: rh62 rhel21 rh73
# SourceDists: rh73
BuildRequires: dhcp < 3.0pl1

Summary: A DHCP (Dynamic Host Configuration Protocol) server and relay agent.
Name: dhcp
Epoch: 1
Version: 3.0pl1
Release: 23.0
License: distributable
Group: System Environment/Daemons
URL: http://isc.org/products/DHCP/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: ftp://ftp.isc.org/isc/dhcp/dhcp-%{version}.tar.gz
Source1: dhcpd.conf.sample
Source2: dhcpd.init
Source3: dhcrelay.init
Patch: dhcp-3.0-alignment.patch
Patch10: dhcp-3.0pl1-RHscript.patch
Patch100: dhcp-3.0-jbuild.patch
Patch101: dhcp-3.0pl1-dhhostname-68650.patch
Patch102: dhcp-3.0pl1-dhcpctlman-69731.patch
Patch103: dhcp-3.0pl1-miscfixes.patch
Patch104: dhcp-3.0pl1-fixoptparse.patch
Patch105: dhcp-3.0pl1-ntp.patch
Patch106: dhcp-3.0pl1-minires.patch
Patch107: dhcp-3.0pl1-hops.patch
Patch108: dhcp-3.0pl1-ntpscript.patch
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

Prereq: /sbin/chkconfig
Requires: kernel >= 2.2.18

%description
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.  The dhcp package includes the
ISC DHCP service and relay agent.

To use DHCP on your network, install a DHCP service (or relay agent),
and on clients run a DHCP client daemon.  The dhcp package provides
the ISC DHCP service and relay agent.

%package -n dhclient
Summary: Development headers and libraries for interfacing to the DHCP server
Requires: initscripts >= 6.75
Group: System Environment/Base

%package devel
Summary: Development headers and libraries for interfacing to the DHCP server
Requires: dhcp = %{version}
Group: Development/Libraries

%description -n dhclient
DHCP (Dynamic Host Configuration Protocol) is a protocol which allows
individual devices on an IP network to get their own network
configuration information (IP address, subnetmask, broadcast address,
etc.) from a DHCP server. The overall purpose of DHCP is to make it
easier to administer a large network.

To use DHCP on your network, install a DHCP service (or relay agent),
and on clients run a DHCP client daemon.  The dhclient package 
provides the ISC DHCP client daemon.

%description devel
Libraries for interfacing with the ISC DHCP server.

%prep
%setup

%patch -p1 -b .alignment
%patch10 -p1 -b .RHscript
%patch100 -p1 -b .jbuild
%patch101 -p1
%patch102 -p1
%patch103 -p1 -b .miscfixes
%patch104 -p1 -b .fixoptparse
%patch105 -p1 -b .ntp
%patch106 -p1 -b .minires
%patch107 -p1 -b .hops
%patch108 -p1 -b .ntpscript

cp %SOURCE1 .
cat <<EOF >site.conf
VARDB=%{_localstatedir}/lib/dhcp
ADMMANDIR=%{_mandir}/man8
FFMANDIR=%{_mandir}/man5
LIBMANDIR=%{_mandir}/man3
USRMANDIR=%{_mandir}/man1
LIBDIR=%{_libdir}
INCDIR=%{_includedir}
EOF
cat <<EOF >>includes/site.h
#define _PATH_DHCPD_DB          "%{_localstatedir}/lib/dhcp/dhcpd.leases"
#define _PATH_DHCLIENT_DB       "%{_localstatedir}/lib/dhcp/dhclient.leases"
EOF

%build
cat <<EOF >findptrsize.c
#include <stdio.h>
int main(void) { printf("%%d\n", sizeof(void *)); return 0; }
EOF
cc -o findptrsize findptrsize.c
[ "`./findptrsize`" -ge 8 ] && RPM_OPT_FLAGS="$RPM_OPT_FLAGS -DPTRSIZE_64BIT"
./configure --copts "$RPM_OPT_FLAGS"

make %{?_smp_mflags} CC="cc"

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/sysconfig

make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/etc/rc.d/init.d
install -m 0755 %SOURCE2 %{buildroot}/etc/rc.d/init.d/dhcpd

touch %{buildroot}%{_localstatedir}/lib/dhcp/dhcpd.leases

cat <<EOF > %{buildroot}/etc/sysconfig/dhcpd
# Command line options here
DHCPDARGS=
EOF

install -m0755 %SOURCE3 %{buildroot}/etc/rc.d/init.d/dhcrelay

cat <<EOF > %{buildroot}/etc/sysconfig/dhcrelay
# Command line options here
INTERFACES=""
DHCPSERVERS=""
EOF

# Copy sample dhclient.conf file into position
cp client/dhclient.conf dhclient.conf.sample
chmod 755 %{buildroot}/sbin/dhclient-script

%clean
rm -rf %{buildroot}

%post
/sbin/chkconfig --add dhcpd
/sbin/chkconfig --add dhcrelay

%preun
if [ $1 = 0 ]; then	# execute this only if we are NOT doing an upgrade
    service dhcpd stop >/dev/null 2>&1
    service dhcrelay stop >/dev/null 2>&1
    /sbin/chkconfig --del dhcpd 
    /sbin/chkconfig --del dhcrelay
fi

%postun
if [ "$1" -ge "1" ]; then
    service dhcpd condrestart >/dev/null 2>&1
    service dhcrelay condrestart >/dev/null 2>&1
fi

%files
%defattr(-,root,root)
%doc CHANGES README RELNOTES dhcpd.conf.sample
%dir %{_localstatedir}/lib/dhcp
%verify(not size md5 mtime) %config(noreplace) %{_localstatedir}/lib/dhcp/dhcpd.leases
%config(noreplace) /etc/sysconfig/dhcpd
%config(noreplace) /etc/sysconfig/dhcrelay
%config /etc/rc.d/init.d/dhcpd
%config /etc/rc.d/init.d/dhcrelay
%{_bindir}/omshell
%{_sbindir}/dhcpd
%{_sbindir}/dhcrelay
%{_mandir}/man1/omshell.1*
%{_mandir}/man5/dhcp-eval.5*
%{_mandir}/man5/dhcpd.conf.5*
%{_mandir}/man5/dhcpd.leases.5*
%{_mandir}/man8/dhcpd.8*
%{_mandir}/man8/dhcrelay.8*

%files -n dhclient
%defattr(-,root,root)
%doc dhclient.conf.sample
%dir %{_localstatedir}/lib/dhcp
/sbin/dhclient
/sbin/dhclient-script
%{_mandir}/man5/dhclient.conf.5*
%{_mandir}/man5/dhclient.leases.5*
%{_mandir}/man8/dhclient.8*
%{_mandir}/man8/dhclient-script.8*
%{_mandir}/man5/dhcp-options.5*

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.a
%{_mandir}/man3/*

%changelog
* Fri May 09 2003 Dag Wieers <dag@wieers.com> - 3.0pl1-23.0
- Adapted for Red Hat 7.3

* Mon Feb 3 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-23
- fix script to handle ntp.conf correctly

* Thu Jan 29 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-22
- Increment release to add to 8.1

* Wed Jan 29 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-21
- Implement max hops patch

* Wed Jan 29 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-20
- It has now been decided to just have options within dhclient kit

* Sun Jan 26 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add defattr() to have files not owned by root

* Fri Jan 24 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-17
- require kernel version

* Fri Jan 24 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-16
- move dhcp-options to separate package 

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Thu Jan 9 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-15
- eliminate dhcp-options from dhclient in order to get errata out

* Wed Jan 8 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-14
- VU#284857 - ISC DHCPD minires library contains multiple buffer overflows

* Mon Jan 6 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-13
- Fix when ntp is not installed.

* Mon Jan 6 2003 Dan Walsh <dwalsh@redhat.com> 3.0pl1-12
- Fix #73079 (dhcpctl man page) 

* Thu Nov 14 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-11
- Use generic PTRSIZE_64BIT detection instead of ifarch.

* Thu Nov 14 2002 Preston Brown <pbrown@redhat.com> 3.0pl1-10
- fix parsing of command line args in dhclient.  It was missing a few.

* Mon Oct 07 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- work on 64bit archs

* Wed Aug 28 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-9
- Fix #72795

* Mon Aug 26 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-8
- More #68650 (modify requested options)
- Fix #71453 (dhcpctl man page) and #71474 (include libdst.a) and
  #72622 (hostname setting)

* Thu Aug 15 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-7
- More #68650 (modify existing patch to also set NIS domain)

* Tue Aug 13 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-6
- Patch102 (dhcp-3.0pl1-dhcpctlman-69731.patch) to fix #69731

* Tue Aug 13 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-5
- Patch101 (dhcp-3.0pl1-dhhostname-68650.patch) to fix #68650

* Fri Jul 12 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-4
- Fix unaligned accesses when decoding a UDP packet

* Thu Jul 11 2002 Elliot Lee <sopwith@redhat.com> 3.0pl1-3
- No apparent reason for the dhclient -> dhcp dep mentioned in #68001,
  so removed it

* Wed Jun 27 2002 David Sainty <saint@redhat.com> 3.0pl1-2
- Move dhclient.conf.sample from dhcp to dhclient

* Mon Jun 25 2002 David Sainty <saint@redhat.com> 3.0pl1-1
- Change to dhclient, dhcp, dhcp-devel packaging
- Move to 3.0pl1, do not strip binaries
- Drop in sysconfig-enabled dhclient-script

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Jan 26 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- prereq chkconfig

* Tue Jan 22 2002 Elliot Lee <sopwith@redhat.com> 3.0-5
- Split headers/libs into a devel subpackage (#58656)

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 28 2001 Elliot Lee <sopwith@redhat.com> 3.0-3
- Fix the #52856 nit.
- Include dhcrelay scripts from #49186

* Thu Dec 20 2001 Elliot Lee <sopwith@redhat.com> 3.0-2
- Update to 3.0, include devel files installed by it (as part of the main package).

* Sun Aug 26 2001 Elliot Lee <sopwith@redhat.com> 2.0pl5-8
- Fix #26446

* Mon Aug 20 2001 Elliot Lee <sopwith@redhat.com>
- Fix #5405 for real - it is dhcpd.leases not dhcp.leases.

* Mon Jul 16 2001 Elliot Lee <sopwith@redhat.com>
- /etc/sysconfig/dhcpd
- Include dhcp.leases file (#5405)

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Feb 14 2001 Tim Waugh <twaugh@redhat.com>
- Fix initscript typo (bug #27624).

* Wed Feb  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Improve spec file i18n

* Mon Feb  5 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- i18nize init script (#26084)

* Sun Sep 10 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 2.0pl5
- redo buildroot patch

* Wed Aug 30 2000 Matt Wilson <msw@redhat.com>
- rebuild to cope with glibc locale binary incompatibility, again

* Mon Aug 14 2000 Preston Brown <pbrown@redhat.com>
- check for existence of /var/lib/dhcpd.leases in initscript before starting

* Wed Jul 19 2000 Jakub Jelinek <jakub@redhat.com>
- rebuild to cope with glibc locale binary incompatibility

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jul  7 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- /etc/rc.d/init.d -> /etc/init.d
- fix /var/state/dhcp -> /var/lib/dhcp

* Fri Jun 16 2000 Preston Brown <pbrown@redhat.com>
- condrestart for initscript, graceful upgrades.

* Thu Feb 03 2000 Erik Troan <ewt@redhat.com>
- gzipped man pages
- marked /etc/rc.d/init.d/dhcp as a config file

* Mon Jan 24 2000 Jakub Jelinek <jakub@redhat.com>
- fix booting of JavaStations
  (reported by Pete Zaitcev <zaitcev@metabyte.com>).
- fix SIGBUS crashes on SPARC (apparently gcc is too clever).

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %preun, not %postun

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0.

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Wed Jun  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 2.0b1pl28.

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- copy the source file in prep, not move

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 4)

* Mon Jan 11 1999 Erik Troan <ewt@redhat.com>
- added a sample dhcpd.conf file
- we don't need to dump rfc's in /usr/doc

* Sun Sep 13 1998 Cristian Gafton <gafton@redhat.com>
- modify dhcpd.init to exit if /etc/dhcpd.conf is not present

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- Upgraded to 2.0b1pl6 (patch1 no longer needed).

* Thu Jun 11 1998 Erik Troan <ewt@redhat.com>
- applied patch from Chris Evans which makes the server a bit more paranoid
  about dhcp requests coming in from the wire

* Mon Jun 01 1998 Erik Troan <ewt@redhat.com>
- updated to dhcp 2.0b1pl1
- got proper man pages in the package

* Tue Mar 31 1998 Erik Troan <ewt@redhat.com>
- updated to build in a buildroot properly
- don't package up the client, as it doens't work very well <sigh>

* Tue Mar 17 1998 Bryan C. Andregg <bandregg@redhat.com>
- Build rooted and corrected file listing.

* Mon Mar 16 1998 Mike Wangsmo <wanger@redhat.com>
- removed the actual inet.d links (chkconfig takes care of this for us)
  and made the %postun section handle upgrades.

* Mon Mar 16 1998 Bryan C. Andregg <bandregg@redhat.com>
- First package.
