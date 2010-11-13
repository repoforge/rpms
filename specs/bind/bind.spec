# $Id$
# Authority: dag

# ExclusiveDist: rh6
BuildRequires: bind < 9.1.3

Summary: DNS (Domain Name System) server
Name: bind
Version: 9.1.3
Release: 2.2%{?dist}
License: BSD-like
Group: System Environment/Daemons
URL: http://www.isc.org/products/BIND/

Source: ftp://ftp.isc.org/isc/bind9/%{version}/bind-%{version}.tar.bz2
Source1: bind-manpages.tar.bz2
Source2: named.sysconfig
Source3: named.init
Source4: named.logrotate
Source5: keygen.c
Patch0: bind-9.1.0b1-reverse.patch
Patch1: bind-9.1.0b1-varrun.patch
Patch3: bind-9.1.3rc2-key.patch
Patch4: bind-9.1.3-ttl.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildPrereq: tar >= 1.13.18
Requires(pre,preun): shadow-utils
Requires(post,preun): chkconfig
Requires(post): textutils, fileutils, sed
Requires: bind-utils

%description
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.


%package utils
Summary: DNS (Domain Name System) server
Group: System Environment/Daemons

%description utils
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.


%package devel
Summary: DNS (Domain Name System) server
Group: System Environment/Daemons
Requires: bind = %{version}

%description devel
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named),
which resolves host names to IP addresses; a resolver library
(routines for applications to use when interfacing with DNS); and
tools for verifying that the DNS server is operating properly.


%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .rev
%patch1 -p1 -b .varrun
%patch3 -p1 -b .key
%patch4 -p1 -b .ttl
# We don't want backups in the doc files
find doc -name "*.fixes" |xargs rm -f

%build
%configure --with-libtool --with-openssl=/usr
make %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}/etc/{rc.d/init.d,logrotate.d}
mkdir -p %{buildroot}/usr/{bin,lib,sbin,include}
mkdir -p %{buildroot}/var/named
mkdir -p %{buildroot}%{_mandir}/{man1,man5,man8}
mkdir -p %{buildroot}/var/run/named

make DESTDIR=%{buildroot} install
install -c -m 640 bin/rndc/rndc.conf %{buildroot}/etc
install -c -m 755 contrib/named-bootconf/named-bootconf.sh %{buildroot}/usr/sbin/named-bootconf
install -c -m 755 %SOURCE3 %{buildroot}/etc/rc.d/init.d/named
install -c -m 644 %SOURCE4 %{buildroot}/etc/logrotate.d/named
install -c -m 644 doc/man/bin/named.8 %{buildroot}%{_mandir}/man8
install -c -m 644 doc/man/bin/rndc.8 %{buildroot}%{_mandir}/man8
install -c -m 644 doc/man/bin/rndc.conf.5 %{buildroot}%{_mandir}/man5
install -c -m 644 doc/man/bin/host.1 %{buildroot}%{_mandir}/man1
install -c -m 644 doc/man/bin/lwresd.8 %{buildroot}%{_mandir}/man8
install -c -m 644 doc/man/bin/nsupdate.8 %{buildroot}%{_mandir}/man8
install -c -m 644 doc/man/dnssec/*.8 %{buildroot}/%{_mandir}/man8
install -c -m 755 bin/dig/.libs/nslookup %{buildroot}/usr/bin
touch %{buildroot}/etc/rndc.key
gcc $RPM_OPT_FLAGS -o %{buildroot}/usr/sbin/dns-keygen %{SOURCE5}
cd %{buildroot}%{_mandir}
tar xjf %{SOURCE1}
mkdir -p %{buildroot}/etc/sysconfig
cp %{SOURCE2} %{buildroot}/etc/sysconfig/named

%pre
/usr/sbin/useradd -c "Named" -u 25 \
	-s /bin/false -r -d /var/named named 2>/dev/null || :

%post
/sbin/chkconfig --add named
if [ -f /etc/named.boot -a ! -f /etc/named.conf ]; then
  if [ -x /usr/sbin/named-bootconf ]; then
    cat /etc/named.boot | /usr/sbin/named-bootconf > /etc/named.conf
    chmod 644 /etc/named.conf
  fi
fi
if [ ! -e /etc/rndc.conf.rpmnew ]; then
  sed -e "s/@KEY@/`/usr/sbin/dns-keygen`/" /etc/rndc.conf >/etc/rndc.conf.tmp
  mv -f /etc/rndc.conf.tmp /etc/rndc.conf
fi
if [ ! -e /etc/rndc.key.rpmnew ]; then
  tail -n 4 /etc/rndc.conf >/etc/rndc.key
fi

%preun
if [ $1 = 0 ]; then
   /usr/sbin/userdel named 2>/dev/null || :
   /usr/sbin/groupdel named 2>/dev/null || :
   /sbin/chkconfig --del named
   [ -f /var/lock/subsys/named ] && /etc/rc.d/init.d/named stop >/dev/null 2>&1
fi
exit 0

%postun
if [ "$1" -ge 1 ]; then
	/etc/rc.d/init.d/named condrestart >/dev/null 2>&1 || :
fi

%triggerpostun -- bind < 8.2.2_P5-15
/sbin/chkconfig --add named

%clean
%{__rm} -rf %{buildroot} ${RPM_BUILD_DIR}/%{name}-%{version}

%post utils
/sbin/ldconfig 2>/dev/null

%postun utils
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGES README
%doc doc/arm doc/draft doc/misc doc/rfc
%config(noreplace) /etc/logrotate.d/named
%config /etc/rc.d/init.d/named
%config(noreplace) /etc/sysconfig/named
%config(noreplace) %attr(0640,root,named) /etc/rndc.conf
%verify(not size,not md5) %config(noreplace) %attr(0640,root,named) /etc/rndc.key

/usr/sbin/dnssec*
/usr/sbin/lwresd
/usr/sbin/named
/usr/sbin/named-bootconf
/usr/sbin/named-check*
/usr/sbin/rndc
/usr/sbin/dns-keygen

%{_mandir}/man5/named.conf.5*
%{_mandir}/man5/rndc.conf.5*
%{_mandir}/man8/rndc.8*
%{_mandir}/man8/named.8*
%{_mandir}/man8/lwresd.8*
%{_mandir}/man8/dnssec*.8*

%attr(-,named,named) %dir /var/named
%attr(-,named,named) %dir /var/run/named

%files utils
%defattr(-, root, root, 0755)
/usr/bin/dig
/usr/bin/host
/usr/bin/nslookup
/usr/bin/nsupdate
/usr/lib/*.so.*
%{_mandir}/man1/host.1*
%{_mandir}/man8/nsupdate.8*
%{_mandir}/man1/dig.1*
%{_mandir}/man5/resolver.5*
%{_mandir}/man8/nslookup.8*

%files devel
%defattr(-, root, root, 0755)
/usr/lib/*.so
/usr/lib/*.la
/usr/lib/*.a
/usr/include/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 9.1.3-2.2
- Rebuild for Fedora Core 5.

* Mon Jul 16 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-2
- Don't use rndc status, it's not yet implemented (#48839)

* Sun Jul 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 9.1.3 release

* Tue Jul  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc3.1
- Fix up rndc configuration and improve security (#46586)

* Tue Jun 26 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc2.2
- Sync with caching-nameserver-7.1-6

* Mon Jun 25 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc2.1
- Update to rc2

* Fri Jun  1 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc1.3
- Remove resolv.conf(5) man page, it's now in man-pages

* Thu May 31 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc1.2
- Add named.conf man page from bind 8.x (outdated, but better than nothing,
  #42732)
- Rename the rndc key (#42895)
- Add dnssec* man pages

* Mon May 28 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.3-0.rc1.1
- 9.1.3rc1
- s/Copyright/License/

* Mon May  7 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.2-1
- 9.1.2 final. No changes between 9.1.2-0.rc1.1 and this one, except for
  the version number, though.

* Thu May  3 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.2-0.rc1.1
- 9.1.2rc1

* Thu Mar 29 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.1-1
- 9.1.1

* Thu Mar 15 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.0-10
- Merge fixes from 9.1.1rc5

* Sun Mar 11 2001 Bernhard Rosenkraenzer <bero@redhat.com> 9.1.0-9
- Work around bind 8 -> bind 9 migration problem when using buggy zone files:
  accept zones without a TTL, but spew out a big fat warning. (#31393)

* Thu Mar  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add fixes from rc4

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Thu Mar  1 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- killall -HUP named if rndc reload fails (#30113)

* Tue Feb 27 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Merge some fixes from 9.1.1rc3

* Tue Feb 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Don't use the standard rndc key from the documentation, instead, create a random one
  at installation time (#26358)
- Make /etc/rndc.conf readable by user named only, it contains secret keys

* Tue Feb 20 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.1 probably won't be out in time, revert to 9.1.0 and apply fixes
  from 9.1.1rc2
- bind requires bind-utils (#28317)

* Tue Feb 13 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to rc2, fixes 2 more bugs
- Fix build with glibc >= 2.2.1-7

* Thu Feb  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update to 9.1.1rc1; fixes 17 bugs (14 of them affecting us;
  1 was fixed in a Red Hat patch already, 2 others are portability
  improvements)

* Wed Feb  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Remove initscripts 5.54 requirement (#26489)

* Mon Jan 29 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add named-checkconf, named-checkzone (#25170)

* Mon Jan 29 2001 Trond Eivind Glomsrød <teg@redhat.com>
- use echo, not gprintf

* Wed Jan 24 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix problems with $GENERATE
  Patch from Daniel Roesen <droesen@entire-systems.com>
  Bug #24890

* Thu Jan 18 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0 final

* Sat Jan 13 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0rc1
- i18nify init script
- bzip2 source to save space

* Thu Jan 11 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix %%postun script

* Tue Jan  9 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0b3

* Mon Jan  8 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add named.conf man page from bind8 (#23503)

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Make /etc/rndc.conf and /etc/sysconfig/named noreplace
- Make devel require bind = %%{version} rather than just bind

* Sun Jan  7 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix init script for real

* Sat Jan  6 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix init script when ROOTDIR is not set

* Thu Jan  4 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add hooks for setting up named to run chroot (RFE #23246)
- Fix up requirements

* Fri Dec 29 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0b2

* Wed Dec 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Move run files to /var/run/named/ - /var/run isn't writable
  by the user we're running as. (Bug #20665)

* Tue Dec 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix reverse lookups (#22272)
- Run ldconfig in %post utils

* Tue Dec 12 2000 Karsten Hopp <karsten@redhat.de>
- fixed logrotate script (wrong path to kill)
- include header files in -devel package
- bugzilla #22049, #19147, 21606

* Fri Dec  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.1.0b1 (9.1.0 is in our timeframe and less buggy)

* Mon Nov 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.0.1

* Mon Oct 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix initscript (Bug #19956)
- Add sample rndc.conf (Bug #19956)
- Fix build with tar 1.13.18

* Tue Oct 10 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Add some missing man pages (taken from bind8) (Bug #18794)

* Sun Sep 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.0.0 final

* Wed Aug 30 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rc5
- fix up nslookup

* Thu Aug 24 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rc4

* Thu Jul 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 9.0.0rc1

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul  9 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add "exit 0" for uninstall case

* Fri Jul  7 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- add prereq init.d and cleanup install section

* Fri Jun 30 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fix the init script

* Wed Jun 28 2000 Nalin Dahyabhai <nalin@redhat.com>
- make libbind.a and nslookup.help readable again by setting INSTALL_LIB to ""

* Mon Jun 26 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Fix up the initscript (Bug #13033)
- Fix build with current glibc (Bug #12755)
- /etc/rc.d/init.d -> /etc/init.d
- use %%{_mandir} rather than /usr/share/man

* Mon Jun 19 2000 Bill Nottingham <notting@redhat.com>
- fix conflict with man-pages
- remove compatibilty chkconfig links
- initscript munging

* Wed Jun 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify logrotate setup to use PID file
- temporarily disable optimization by unsetting $RPM_OPT_FLAGS at build-time
- actually bump the release this time

* Sun Jun  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- FHS compliance

* Mon Apr 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- clean up restart patch

* Mon Apr 10 2000 Nalin Dahyabhai <nalin@redhat.com>
- provide /var/named (fix for bugs #9847, #10205)
- preserve args when restarted via ndc(8) (bug #10227)
- make resolv.conf(5) a link to resolver(5) (bug #10245)
- fix SYSTYPE bug in all makefiles
- move creation of named user from %%post into %%pre

* Mon Feb 28 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Fix TTL (patch from ISC, Bug #9820)

* Wed Feb 16 2000 Bernhard Rosenkränzer <bero@redhat.com>
- fix typo in spec (it's %post, without a leading blank) introduced in -6
- change SYSTYPE to linux

* Sat Feb 11 2000 Bill Nottingham <notting@redhat.com>
- pick a standard < 100 uid/gid for named

* Thu Feb 04 2000 Elliot Lee <sopwith@redhat.com>
- Pass named a '-u named' parameter by default, and add/remove user.

* Thu Feb  3 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- fix host mx bug (Bug #9021)

* Mon Jan 31 2000 Cristian Gafton <gafton@redhat.com>
- rebuild to fix dependencies
- man pages are compressed

* Wed Jan 19 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- It's /usr/bin/killall, not /usr/sbin/killall (Bug #8063)

* Mon Jan 17 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- Fix up location of named-bootconf.pl and make it executable
  (Bug #8028)
- bind-devel requires bind

* Mon Nov 15 1999 Bernhard Rosenkraenzer <bero@redhat.com>
- update to 8.2.2-P5

* Wed Nov 10 1999 Bill Nottingham <notting@redhat.com>
- update to 8.2.2-P3

* Tue Oct 12 1999 Cristian Gafton <gafton@redhat.com>
- add patch to stop a cache only server from complaining about lame servers
  on every request.

* Fri Sep 24 1999 Preston Brown <pbrown@redhat.com>
- use real stop and start in named.init for restart, not ndc restart, it has
  problems when named has changed during a package update... (# 4890)

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %preun, not %postun

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Mon Jul 26 1999 Bill Nottingham <notting@redhat.com>
- fix installed chkconfig links to match init file

* Sat Jul  3 1999 Jeff Johnson <jbj@redhat.com>
- conflict with new (in man-1.24) man pages (#3876,#3877).

* Tue Jun 29 1999 Bill Nottingham <notting@redhat.com>
- fix named.logrotate (wrong %SOURCE)

* Fri Jun 25 1999 Jeff Johnson <jbj@redhat.com>
- update to 8.2.1.
- add named.logrotate (#3571).
- hack around egcs-1.1.2 -m486 bug (#3413, #3485).
- vet file list.

* Fri Jun 18 1999 Bill Nottingham <notting@redhat.com>
- don't run by default

* Sun May 30 1999 Jeff Johnson <jbj@redhat.com>
- nslookup fixes (#2463).
- missing files (#3152).

* Sat May  1 1999 Stepan Kasal <kasal@math.cas.cz>
- nslookup patched:
  to count numRecords properly
  to fix subsequent calls to ls -d
  to parse "view" and "finger" commands properly
  the view hack updated for bind-8 (using sed)

* Wed Mar 31 1999 Bill Nottingham <notting@redhat.com>
- add ISC patch
- add quick hack to make host not crash
- add more docs

* Fri Mar 26 1999 Cristian Gafton <gafton@redhat.com>
- add probing information in the init file to keep linuxconf happy
- dont strip libbind

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Wed Mar 17 1999 Preston Brown <pbrown@redhat.com>
- removed 'done' output at named shutdown.

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.2

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- patch to use the __FDS_BITS macro
- build for glibc 2.1

* Wed Sep 23 1998 Jeff Johnson <jbj@redhat.com>
- change named.restart to /usr/sbin/ndc restart

* Sat Sep 19 1998 Jeff Johnson <jbj@redhat.com>
- install man pages correctly.
- change K10named to K45named.

* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- don't start if /etc/named.conf doesn't exist.

* Sat Aug  8 1998 Jeff Johnson <jbj@redhat.com>
- autmagically create /etc/named.conf from /etc/named.boot in %post
- remove echo in %post

* Wed Jun 10 1998 Jeff Johnson <jbj@redhat.com>
- merge in 5.1 mods

* Sun Apr 12 1998 Manuel J. Galan <manolow@step.es>
- Several essential modifications to build and install correctly.
- Modified 'ndc' to avoid deprecated use of '-'

* Mon Dec 22 1997 Scott Lampert <fortunato@heavymetal.org>
- Used buildroot
- patched bin/named/ns_udp.c to use <libelf/nlist.h> for include
  on Redhat 5.0 instead of <nlist.h>

