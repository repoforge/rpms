# $Id$
# Authority: dag

# Tag: test

### This defines the library version that this package builds.
%define LIBVER 1.19.0

Summary: Mouse server for the Linux console
Name: gpm
Version: 1.20.1
Release: 35.1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://linux.schottelius.org/gpm/

Source: http://ftp.linux.it/pub/People/rubini/gpm/%{name}-%{version}.tar.bz2
Source1: gpm.init
Patch5: gpm-1.20.1-secenhance.patch
Patch6: gpm-1.20.1-limits.patch
Patch7: gpm-1.20.1-serialconsole.patch
Patch10: gpm-1.20.1-norepeater.patch
Patch11: gpm-1.20.1-weak-wgetch.patch
Patch12: gpm-1.20.1-math.patch
Patch13: gpm-1.20.1-nodebug.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildPrereq: sed gawk texinfo
Prereq: /sbin/chkconfig /sbin/ldconfig /sbin/install-info
Requires: bash >= 2.0

%description
Gpm provides mouse support to text-based Linux applications like the
Emacs editor and the Midnight Commander file management system.  Gpm
also provides console cut-and-paste operations using the mouse and
includes a program to allow pop-up menus to appear at the click of a
mouse button.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup
%patch5 -p1 -b .secenhance
%patch6 -p1 -b .limits
#%patch7 -p1 -b .serialconsole
%patch10 -p1 -b .repeater
%patch11 -p1 -b .weak-wgetch
%patch12 -p1 -b .math
%patch13 -p1 -b .nodebug

%{__cat} <<EOF >gpm.sysconfig
# Additional options for gpm (e.g. acceleration), device
OPTIONS=""
MOUSETYPE=""
DEVICE="/dev/mouse"
EOF

%{__cat} <<'EOF' >gpm.sysv
#!/bin/bash
#
# Init file for gpm.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 85 15
# description: GPM adds mouse support to text-based Linux applications such \
#              the Midnight Commander. Is also allows mouse-based console \
#              cut-and-paste operations, and includes support for pop-up \
#              menus on the console.
#
# processname: gpm
# config: /etc/sysconfig/mouse
# pidfile: /var/run/gpm.pid

source %{_initrddir}/functions
if [ -e /etc/sysconfig/gpm ]; then
	 source /etc/sysconfig/gpm
fi

MOUSECFG="/etc/sysconfig/mouse"

RETVAL=0
prog="gpm"
desc="console mouse services"

start() {
	echo -n $"Starting $desc ($prog): "
	if [ -f "$MOUSECFG" ]; then
		source "$MOUSECFG"
	else
		echo $"(no mouse is configured)"
		exit 0
	fi

	if [ "$MOUSETYPE" = "none" ]; then
		echo $"(no mouse is configured)"
		exit 0
	fi


	if [ "$MOUSETYPE" = "Microsoft" ]; then
		MOUSETYPE="ms"
	fi

	if [ -z "$DEVICE" ]; then
	    DEVICE="/dev/mouse"
	fi

	if [ -n "$MOUSETYPE" ]; then
		daemon $prog -m $DEVICE -t $MOUSETYPE $OPTIONS
	else
		daemon $prog -m $DEVICE $OPTIONS
	fi
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down console mouse services: "
	killproc $prog
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

restart() {
	stop
	start
}

case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart|reload)
	restart
	;;
  condrestart)
	[ -e %{_localstatedir}/lock/subsys/$prog ] && restart
	RETVAL=$?
	;;
  status)
	status $prog
	RETVAL=$?
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
%{__autoconf}
CFLAGS="-D_GNU_SOURCE %{optflags}" \
lispdir="%{buildroot}%{_datadir}/emacs/site-lisp" \
	%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/sysconfig/ \
			%{buildroot}%{_datadir}/emacs/site-lisp/
%makeinstall lispdir="%{buildroot}%{_datadir}/emacs/site-lisp"

%{__install} -p -m0644 contrib/emacs/t-mouse.el* %{buildroot}%{_datadir}/emacs/site-lisp/

%ifnarch s390 s390x
	%{__install} -Dp -m0755 gpm.sysv %{buildroot}%{_initrddir}/gpm
	%{__install} -Dp -m0644 gpm.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/gpm
	%{__install} -Dp -m0644 doc/gpm-root.1 %{buildroot}%{_mandir}/man1/gpm-root.1
	%{__install} -Dp -m0644 conf/gpm-root.conf %{buildroot}%{_sysconfdir}/gpm-root.conf
	%{__install} -Dp -m0755 src/prog/hltest %{buildroot}%{_bindir}/hltest
%else
	%{__rm} -f %{buildroot}%{_bindir}/mev \
			%{buildroot}%{_bindir}gpm-root
%endif

%{__chmod} +x %{buildroot}%{_libdir}/libgpm.so*
%{__ln_s} -f libgpm.so.%{LIBVER} %{buildroot}%{_libdir}/libgpm.so

### Clean up buildroot
%{__rm} -f %{buildroot}%{_bindir}/disable-paste \
		%{buildroot}%{_mandir}/man1/mouse-test.1*

%ifarch s390 s390x
%{__rm} -rf %{buildroot}%{_mandir}
%{__rm} -f %{buildroot}%{_sbindir}/gpm \
		%{buildroot}%{_bindir}/hltest \
		%{buildroot}%{_bindir}/mouse-test
%endif

%post
%ifnarch s390 s390x
/sbin/chkconfig --add gpm
%endif
/sbin/ldconfig 2>/dev/null
/sbin/install-info %{_infodir}/gpm.info.gz %{_infodir}/dir

%preun
if [ $1 -eq 0 ]; then
    /sbin/install-info %{_infodir}/gpm.info.gz --delete %{_infodir}/dir
%ifnarch s390 s390x
    service gpm stop &>/dev/null
    /sbin/chkconfig --del gpm
%endif
fi

%postun
%ifnarch s390 s390x
if [ "$1" -ge "1" ]; then
  service gpm condrestart >/dev/null 2>&1
fi
%endif
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%ifnarch s390 s390x
%config(noreplace) %{_sysconfdir}/gpm-root.conf
%config(noreplace) %{_sysconfdir}/sysconfig/*
%config %{_initrddir}/*
%{_bindir}/*
%{_sbindir}/*
%endif
%{_datadir}/emacs/site-lisp/*
%{_infodir}/gpm.info*
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.20.1-35.1.2
- Rebuild for Fedora Core 5.

* Mon Oct 20 2003 Dag Wieers <dag@wieers.com> - 1.20.1-35.1
- Fixed sysconfig and %%config.

* Sat Jul 19 2003 Dag Wieers <dag@wieers.com> - 1.20.1-35.0
- Cleaned up SPEC file.
- Added $OPTIONS to gpm.sysv and standardized gpm.sysv.

* Wed Jul 02 2003 Adrian Havill <havill@redhat.com> 1.20.1-35
- remove debug output from gpm_report() to prevent spurious
  debugging msgs even when not in debug mode (#98210)

* Thu Jun 26 2003 Adrian Havill <havill@redhat.com> 1.20.1-33
- reversed -t and -m params in init script, removed $OPTION
- add doc blurb regarding no auto-repeat with multiple mice

* Tue Jun 24 2003 Adrian Havill <havill@redhat.com> 1.20.1-32
- update version
- add -lm for ceil()
- add hltest, mouse-test for all but zSeries

* Mon Jun 16 2003 Jakub Jelinek <jakub@redhat.com>
- don't link against -lncurses, instead make wgetch and stdscr weak
  undefined symbols to break library dependency cycle

* Thu Jun 12 2003 Elliot Lee <sopwith@redhat.com>
- Remove pam requirement

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 29 2003 Bill Nottingham <notting@redhat.com> 1.19.13-27
- ship libraries on s390/s390x

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Bill Nottingham <notting@redhat.com> 1.19.13-25
- don't automatically enable the repeater when '-M' is in use

* Fri Nov 22 2002 Tim Powers <timp@redhat.com>
- remove unpackaged files from the buildroot

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Apr  9 2002 Bernhard Rosenkraenzer <bero@redhat.com>
- Revert to the version from 7.2 because later versions have some grave
  issues I can't {reproduce,debug} with my hardware, such as
  #62540 and #61691

* Thu Jul 19 2001 Preston Brown <pbrown@redhat.com>
- more documentation fixes for Netmouse type devices (#48885)

* Tue Jun 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add link from library major version number

* Mon Jun 25 2001 Preston Brown <pbrown@redhat.com>
- small fixlet in init script (#36995)

* Tue Jun 19 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add ExcludeArch: s390 s390x

* Fri Apr  6 2001 Preston Brown <pbrown@redhat.com>
- work better with unsupported devfs (#23500, #34883)

* Mon Feb 05 2001 Karsten Hopp <karsten@redhat.de>
- found another bug: tmpfile was never removed if
  gpm was already running

* Mon Feb 05 2001 Karsten Hopp <karsten@redhat.de>
- really fix tmpfile path

* Mon Feb 05 2001 Karsten Hopp <karsten@redhat.de>
- fix tmpfile path (bugzilla  #25967)

* Tue Jan 30 2001 Preston Brown <pbrown@redhat.com>
- don't make PID file world-writable.

* Mon Jan 29 2001 Preston Brown <pbrown@redhat.com>
- fix up devel dependency on main package

* Sun Jan 28 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Don't crash if we can't open /dev/console
  (Happens with some devfs enabled kernels)

* Tue Jan 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- fix bug in i18n of initscript

* Tue Jan 23 2001 Preston Brown <pbrown@redhat.com>
- bash2 style of i18n for initscript

* Wed Jan 17 2001 Preston Brown <pbrown@redhat.com>
- i18n the initscript.

* Thu Jan 11 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Add hooks for extra options in /etc/sysconfig/gpm (#23547)

* Fri Jan 05 2001 Preston Brown <pbrown@redhat.com>
- patch added to abort if running on a serial console (#15784)

* Fri Jul 28 2000 Preston Brown <pbrown@redhat.com>
- cleaned up post section

* Wed Jul 26 2000 Preston Brown <pbrown@redhat.com>
- clarification: pam requirement added to fix permissions on /dev/gpmctl (#12849)

* Sat Jul 22 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 1.19.3

* Sat Jul 15 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Fri Jun 30 2000 Matt Wilson <msw@redhat.com>
- use sysconf(_SC_OPEN_MAX)

* Tue Jun 27 2000 Preston Brown <pbrown@redhat.com>
- don't prereq, only require initscripts

* Mon Jun 26 2000 Preston Brown <pbrown@redhat.com>
- fix up and move initscript
- prereq initscripts >= 5.20

* Sat Jun 17 2000 Bill Nottingham <notting@redhat.com>
- fix %config tag for initscript

* Thu Jun 15 2000 Bill Nottingham <notting@redhat.com>
- move it back

* Thu Jun 15 2000 Preston Brown <pbrown@redhat.com>
- move init script

* Wed Jun 14 2000 Preston Brown <pbrown@redhat.com>
- security patch on socket descriptor from Chris Evans.  Thanks Chris.
- include limits.h for OPEN_MAX

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- 1.19.2, fix up root (setuid) patch
- FHS paths

* Thu Apr  6 2000 Jakub Jelinek <jakub@redhat.com>
- 1.19.1
- call initgroups in gpm-root before spawning command as user
- make gpm-root work on big endian

* Sun Mar 26 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- call ldconfig directly in postun

* Wed Mar 22 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- rebuild with new libncurses

* Sat Mar 18 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.19.0
- fix build on systems that don't have emacs
  (configure built t-mouse* only if emacs was installed)

* Tue Feb 29 2000 Preston Brown <pbrown@redhat.com>
- important fix: improperly buildrooted for /usr/share/emacs/site-lisp, fixed.

* Tue Feb 15 2000 Jakub Jelinek <jakub@redhat.com>
- avoid cluttering of syslog with gpm No data messages

* Mon Feb 14 2000 Preston Brown <pbrown@redhat.com>
- disable-paste and mouse-test removed, they seem broken.

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- updated gpm.init to have better shutdown and descriptive messages
- strip lib

* Wed Feb 02 2000 Cristian Gafton <gafton@redhat.com>
- fix description
- man pages are compressed

* Wed Jan 12 2000 Preston Brown <pbrown@redhat.com>
- 1.18.1.

* Tue Sep 28 1999 Preston Brown <pbrown@redhat.com>
- upgraded to 1.18, hopefully fixes sparc protocol issues

* Fri Sep 24 1999 Bill Nottingham <notting@redhat.com>
- install-info sucks, and then you die.

* Fri Sep 10 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %preun, not %postun

* Fri Aug 27 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 1.17.9
- the maintainers are taking care of .so version now, removed patch

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Wed Jun  2 1999 Jeff Johnson <jbj@redhat.com>
- disable-paste need not be setuid root in Red Hat 6.0 (#2654)

* Tue May 18 1999 Michael K. Johnson <johnsonm@redhat.com>
- gpm.init had wrong pidfile name in comments; confused linuxconf

* Mon Mar 22 1999 Preston Brown <pbrown@redhat.com>
- make sure all binaries are stripped, make init stuff more chkconfig style
- removed sparc-specific mouse stuff
- bumped libver to 1.17.5
- fixed texinfo source

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Thu Mar  4 1999 Matt Wilson <msw@redhat.com>
- updated to 1.75.5

* Tue Feb 16 1999 Cristian Gafton <gafton@redhat.com>
- avoid using makedev for internal functions (it is a #define in the system
  headers)

* Wed Jan 13 1999 Preston Brown <pbrown@redhat.com>
- upgrade to 1.17.2.

* Wed Jan 06 1999 Cristian Gafton <gafton@redhat.com>
- enforce the use of -D_GNU_SOURCE so that it will compile on the ARM
- build against glibc 2.1

* Tue Aug 11 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 22 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhanced initscript

* Fri Apr 10 1998 Cristian Gafton <gafton@redhat.com>
- recompiled for manhattan

* Wed Apr 08 1998 Erik Troan <ewt@redhat.com>
- updated to 1.13

* Mon Nov 03 1997 Donnie Barnes <djb@redhat.com>
- added patch from Richard to get things to build on the SPARC

* Tue Oct 28 1997 Donnie Barnes <djb@redhat.com>
- fixed the emacs patch to install the emacs files in the right
  place (hopefully).

* Mon Oct 13 1997 Erik Troan <ewt@redhat.com>
- added chkconfig support
- added install-info

* Thu Sep 11 1997 Donald Barnes <djb@redhat.com>
- upgraded from 1.10 to 1.12
- added status/restart functionality to init script
- added define LIBVER 1.11

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
