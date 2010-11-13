# $Id$
# Authority: dag

# Rationale: Some features of the newer sudo are nice to have (eg. -i)
### EL6 ships with sudo-1.7.2p2-9.el6
### EL5 ships with sudo-1.7.2p1-9.el5_5
### EL4 ships with sudo-1.6.7p5-30.1.5
### EL3 ships with sudo-1.6.7p5-1.2
### EL2 ships with sudo-1.6.5p2-1.7x.2
# Tag: rfx
# ExclusiveDist: el2 rh7 rh9 el3 el4

Summary: Allows restricted root access for specified users.
Name: sudo
Version: 1.6.8p12
Release: 0.12%{?dist}
License: BSD
Group: Applications/System
URL: http://www.courtesan.com/sudo/

Source0: http://www.courtesan.com/sudo/dist/sudo-%{version}.tar.gz
Source1: sudo-1.6.8p12-sudoers
# 154511 - sudo does not use limits.conf
Patch2: sudo-1.6.8p8-pam-sess.patch
# don't strip
Patch3: sudo-1.6.7p5-strip.patch
# Default sudoers: reset env.
Patch4: sudo-1.6.8p12-env-reset.patch
# Default sudoers; require tty (#190062)
Patch5: sudo-1.6.8p12-requiretty.patch
# Use specific PAM session for sudo -i (#198755)
Patch6: sudo-1.6.8p12-pam-login.patch
# IPv6 support
Patch7: sudo-1.6.8p12-ipv6.patch
# audit support
Patch8: sudo-1.6.8p12-audit.patch 
# segfaults on s390
Patch9: sudo-1.6.8p12-s390.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: flex
BuildRequires: groff
BuildRequires: libcap-devel
BuildRequires: openldap-devel
BuildRequires: pam-devel
Requires: /etc/pam.d/system-auth
Requires: vim-minimal

%description
Sudo (superuser do) allows a system administrator to give certain
users (or groups of users) the ability to run some (or all) commands
as root while logging all commands and arguments. Sudo operates on a
per-command basis.  It is not a replacement for the shell.  Features
include: the ability to restrict what commands a user may run on a
per-host basis, copious logging of each command (providing a clear
audit trail of who did what), a configurable timeout of the sudo
command, and the ability to use the same configuration file (sudoers)
on many different machines.

%prep
%setup
%patch2 -p1 -b .sess
%patch3 -p1 -b .strip
%patch4 -p1 -b .env_reset
%patch5 -p1 -b .tty
%patch6 -p1 -b .login
%patch7 -p1 -b .ipv6
#patch8 -p1 -b .audit
%patch9 -p1 -b .s390

%{__cat} <<EOF >sudo.pam
#%PAM-1.0
auth       required	pam_stack.so service=system-auth
account    required	pam_stack.so service=system-auth
password   required	pam_stack.so service=system-auth
session    required	pam_limits.so
EOF

%{__cat} <<EOF >sudo-i.pam
#%PAM-1.0
auth       required	pam_stack.so service=system-auth
account    required	pam_stack.so service=system-auth
password   required	pam_stack.so service=system-auth
session    required	pam_limits.so
EOF

%build
# Note: there is a problem rebuild the ./configure script (for pam-login patch), 
#       so we use -DHAVE_PAM_LOGIN rather than --with-pam-login... 
#       (it's workaround that should be fixed)
%ifarch s390 s390x
export CFLAGS="%{optflags} -fPIE -DHAVE_PAM_LOGIN -DWITH_AUDIT" 
%else
export CFLAGS="%{optflags} -fpie -DHAVE_PAM_LOGIN -DWITH_AUDIT" 
%endif
export LDFLAGS="-pie" 
export LIBS="-lcap"

%configure \
    --prefix="%{_prefix}" \
    --sbindir="%{_sbindir}" \
    --with-editor="/bin/vi" \
    --with-env-editor \
    --with-ignore-dot \
    --with-ldap \
    --with-logfac="authpriv" \
    --with-logging="syslog" \
    --with-pam \
    --with-tty-tickets
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -dp -m0755 %{buildroot}
%{__make} install DESTDIR="%{buildroot}" \
    install_uid="$(id -u)" \
    install_gid="$(id -g)" \
    sudoers_uid="$(id -u)" \
    sudoers_gid="$(id -g)"
%{__chmod} 0755 %{buildroot}%{_bindir}/*
%{__chmod} 0755 %{buildroot}%{_sbindir}/*
%{__install} -d -m0700 %{buildroot}%{_localstatedir}/run/sudo
%{__install} -Dp -m0440 %{SOURCE1} %{buildroot}%{_sysconfdir}/sudoers

%{__install} -Dp -m06440 sudo.pam %{buildroot}%{_sysconfdir}/pam.d/sudo
%{__install} -Dp -m06440 sudo-i.pam %{buildroot}%{_sysconfdir}/pam.d/sudo-i

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc BUGS CHANGES HISTORY LICENSE README RUNSON TODO TROUBLESHOOTING UPGRADE *.pod
%doc %{_mandir}/man5/sudoers.5*
%doc %{_mandir}/man8/sudo.8*
%doc %{_mandir}/man8/sudoedit.8*
%doc %{_mandir}/man8/visudo.8*
%config(noreplace) %{_sysconfdir}/pam.d/sudo
%config(noreplace) %{_sysconfdir}/pam.d/sudo-i
%dir %{_localstatedir}/run/sudo
%{_libexecdir}/sudo_noexec.*

%defattr(0440, root, root, 0755)
%config(noreplace) %{_sysconfdir}/sudoers

%defattr(4111, root, root, 0755)
%{_bindir}/sudo
%{_bindir}/sudoedit

%defattr(0755, root, root, 0755)
%{_sbindir}/visudo

# Make sure permissions are ok even if we're updating
%post
%{__chmod} 0440 %{_sysconfdir}/sudoers || :

%changelog
* Thu Mar 06 2008 Peter Vrabec <pvrabec@redhat.com> 1.6.8p12-12
- adjust audit patch,
  Resolves: #320671

* Fri Jan 04 2008 Peter Vrabec <pvrabec@redhat.com> 1.6.8p12-11
- fix segfaults when using ldap on s390,
  Resolves: #305331
- add audit support,
  Resolves: #320671

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> - 1.6.8p12-10
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Thu Sep 21 2006 Peter Vrabec <pvrabec@redhat.com> 1.6.8p12-9
- fix sudoers file, X apps didn't work (#206320)

* Tue Aug 08 2006 Peter Vrabec <pvrabec@redhat.com> 1.6.8p12-8
- use Red Hat specific default sudoers file

* Sun Jul 16 2006 Karel Zak <kzak@redhat.com> 1.6.8p12-7
- fix #198755 - make login processes (sudo -i) initialise session keyring
  (thanks for PAM config files to David Howells)
- add IPv6 support (patch by Milan Zazrivec)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.6.8p12-6.1
- rebuild

* Mon May 29 2006 Karel Zak <kzak@redhat.com> 1.6.8p12-6
- fix #190062 - "ssh localhost sudo su" will show the password in clear

* Tue May 23 2006 Karel Zak <kzak@redhat.com> 1.6.8p12-5
- add LDAP support (#170848)

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.6.8p12-4.1
- bump again for double-long bug on ppc(64)

* Wed Feb  8 2006 Karel Zak <kzak@redhat.com> 1.6.8p12-4
- reset env. by default

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.6.8p12-3.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 23 2006 Dan Walsh <dwalsh@redhat.com> 1.6.8p12-3
- Remove selinux patch.  It has been decided that the SELinux patch for sudo is
- no longer necessary.  In tageted policy it had no effect.  In strict/MLS policy
- We require the person using sudo to execute newrole before using sudo.

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Nov 25 2005 Karel Zak <kzak@redhat.com> 1.6.8p12-1
- new upstream version 1.6.8p12

* Tue Nov  8 2005 Karel Zak <kzak@redhat.com> 1.6.8p11-1
- new upstream version 1.6.8p11

* Thu Oct 13 2005 Tomas Mraz <tmraz@redhat.com> 1.6.8p9-6
- use include instead of pam_stack in pam config

* Tue Oct 11 2005 Karel Zak <kzak@redhat.com> 1.6.8p9-5
- enable interfaces in selinux patch
- merge sudo-1.6.8p8-sesh-stopsig.patch to selinux patch

* Mon Sep 19 2005 Karel Zak <kzak@redhat.com> 1.6.8p9-4
- fix debuginfo

* Mon Sep 19 2005 Karel Zak <kzak@redhat.com> 1.6.8p9-3
- fix #162623 - sesh hangs when child suspends

* Mon Aug 1 2005 Dan Walsh <dwalsh@redhat.com> 1.6.8p9-2
- Add back in interfaces call, SELinux has been fixed to work around

* Tue Jun 21 2005 Karel Zak <kzak@redhat.com> 1.6.8p9-1
- new version 1.6.8p9 (resolve #161116 - CAN-2005-1993 sudo trusted user arbitrary command execution)

* Tue May 24 2005 Karel Zak <kzak@redhat.com> 1.6.8p8-2
- fix #154511 - sudo does not use limits.conf

* Mon Apr  4 2005 Thomas Woerner <twoerner@redhat.com> 1.6.8p8-1
- new version 1.6.8p8: new sudoedit and sudo_noexec

* Wed Feb  9 2005 Thomas Woerner <twoerner@redhat.com> 1.6.7p5-31
- rebuild

* Mon Oct  4 2004 Thomas Woerner <twoerner@redhat.com> 1.6.7p5-30.1
- added missing BuildRequires for libselinux-devel (#132883) 

* Wed Sep 29 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-30
- Fix missing param error in sesh

* Mon Sep 27 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-29
- Remove full patch check from sesh

* Thu Jul 8 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-28
- Fix selinux patch to switch to root user

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 13 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-26
- Eliminate tty handling from selinux

* Thu Apr  1 2004 Thomas Woerner <twoerner@redhat.com> 1.6.7p5-25
- fixed spec file: sesh in file section with selinux flag (#119682)

* Thu Mar 30 2004 Colin Walters <walters@redhat.com> 1.6.7p5-24
- Enhance sesh.c to fork/exec children itself, to avoid
  having sudo reap all domains.
- Only reinstall default signal handlers immediately before
  exec of child with SELinux patch

* Thu Mar 18 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-23
- change to default to sysadm_r 
- Fix tty handling

* Thu Mar 18 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-22
- Add /bin/sesh to run selinux code.
- replace /bin/bash -c with /bin/sesh

* Tue Mar 16 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-21
- Hard code to use "/bin/bash -c" for selinux 

* Tue Mar 16 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-20
- Eliminate closing and reopening of terminals, to match su.

* Mon Mar 15 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-19
- SELinux fixes to make transitions work properly

* Fri Mar  5 2004 Thomas Woerner <twoerner@redhat.com> 1.6.7p5-18
- pied sudo

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jan 27 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-16
- Eliminate interfaces call, since this requires big SELinux privs
- and it seems to be useless.

* Tue Jan 27 2004 Karsten Hopp <karsten@redhat.de> 1.6.7p5-15
- visudo requires vim-minimal or setting EDITOR to something useful (#68605)

* Mon Jan 26 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-14
- Fix is_selinux_enabled call

* Tue Jan 13 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-13
- Clean up patch on failure

* Tue Jan 6 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-12
- Remove sudo.te for now.

* Fri Jan 2 2004 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-11
- Fix usage message

* Mon Dec 22 2003 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-10
- Clean up sudo.te to not blow up if pam.te not present

* Thu Dec 18 2003 Thomas Woerner <twoerner@redhat.com>
- added missing BuildRequires for groff

* Tue Dec 16 2003 Jeremy Katz <katzj@redhat.com> 1.6.7p5-9
- remove left-over debugging code

* Tue Dec 16 2003 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-8
- Fix terminal handling that caused Sudo to exit on non selinux machines.

* Mon Dec 15 2003 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-7
- Remove sudo_var_run_t which is now pam_var_run_t

* Fri Dec 12 2003 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-6
- Fix terminal handling and policy

* Thu Dec 11 2003 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-5
- Fix policy

* Thu Nov 13 2003 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-4.sel
- Turn on SELinux support

* Tue Jul 29 2003 Dan Walsh <dwalsh@redhat.com> 1.6.7p5-3
- Add support for SELinux

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 19 2003 Thomas Woerner <twoerner@redhat.com> 1.6.7p5-1

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Nov 12 2002 Nalin Dahyabhai <nalin@redhat.com> 1.6.6-2
- remove absolute path names from the PAM configuration, ensuring that the
  right modules get used for whichever arch we're built for
- don't try to install the FAQ, which isn't there any more

* Thu Jun 27 2002 Bill Nottingham <notting@redhat.com> 1.6.6-1
- update to 1.6.6

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 18 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.5p2-2
- Fix bug #63768

* Thu Mar 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.5p2-1
- 1.6.5p2

* Fri Jan 18 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.5p1-1
- 1.6.5p1
- Hope this "a new release per day" madness stops ;)

* Thu Jan 17 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.5-1
- 1.6.5

* Tue Jan 15 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.4p1-1
- 1.6.4p1

* Mon Jan 14 2002 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.4-1
- Update to 1.6.4

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 1.6.3p7-2
- Add build requirements (#49706)
- s/Copyright/License/
- bzip2 source

* Sat Jun 16 2001 Than Ngo <than@redhat.com>
- update to 1.6.3p7
- use %%{_tmppath}

* Fri Feb 23 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.6.3p6, fixes buffer overrun

* Tue Oct 10 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.6.3p5

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 06 2000 Karsten Hopp <karsten@redhat.de>
- fixed owner of sudo and visudo

* Thu Jun  1 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth
- clean up buildrooting by using the makeinstall macro

* Tue Apr 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- initial build in main distrib
- update to 1.6.3
- deal with compressed man pages

* Tue Dec 14 1999 Preston Brown <pbrown@redhat.com>
- updated to 1.6.1 for Powertools 6.2
- config files are now noreplace.

* Thu Jul 22 1999 Tim Powers <timp@redhat.com>
- updated to 1.5.9p2 for Powertools 6.1

* Wed May 12 1999 Bill Nottingham <notting@redhat.com>
- sudo is configured with pam. There's no pam.d file. Oops.

* Mon Apr 26 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 1.59p1 for powertools 6.0

* Tue Oct 27 1998 Preston Brown <pbrown@redhat.com>
- fixed so it doesn't find /usr/bin/vi first, but instead /bin/vi (always installed)

* Fri Oct 08 1998 Michael Maher <mike@redhat.com>
- built package for 5.2 

* Mon May 18 1998 Michael Maher <mike@redhat.com>
- updated SPEC file. 

* Thu Jan 29 1998 Otto Hammersmith <otto@redhat.com>
- updated to 1.5.4

* Tue Nov 18 1997 Otto Hammersmith <otto@redhat.com>
- built for glibc, no problems

* Fri Apr 25 1997 Michael Fulbright <msf@redhat.com>
- Fixed for 4.2 PowerTools 
- Still need to be pamified
- Still need to move stmp file to /var/log

* Mon Feb 17 1997 Michael Fulbright <msf@redhat.com>
- First version for PowerCD.
