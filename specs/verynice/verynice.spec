# $Id$
# Authority: dag
# Upstream: Steve Holland <sdh4$cornell,edu>

Summary: Dynamic process renicer and killer
Name: verynice
Version: 1.1
Release: 1.2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://www.tam.cornell.edu/~sdh4/verynice/

Source: http://www.tam.cornell.edu/~sdh4/verynice/down/verynice-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


%description
VeryNice is a tool for dynamically adjusting the nice-level of processes
under UNIX-like operating systems. It can also be used to kill off
runaway processes and increase the priority of multimedia applications,
while properly handling both batch computation jobs and interactive
applications with long periods of high CPU usage.

%prep
%setup -n %{name}
%{__perl} -pi.orig -e 's|^export PREFIX=/usr/local$|export PREFIX=%{_prefix}|' verynice.init

%{__cat} <<EOF >verynice.sysv
#!/bin/bash
#
# Init file for Verynice process renicer
#
# chkconfig: 345 90 10
# description: Verynice process renicer
#
# processname: verynice
# config: %{_sysconfdir}/verynice.conf
# pidfile: %{_localstatedir}/run/verynice.pid

# source function library
. %{_initrddir}/functions

[ -x %{_sbindir}/verynice ] || exit 1
[ -r %{_sysconfdir}/verynice.conf ] || exit 1

RETVAL=0
prog="verynice"
desc="Verynice process renicer daemon"

start() {
	echo -n \$"Starting \$desc: "
	daemon \$prog -d %{_localstatedir}/run/\$prog.pid
	RETVAL=\$?
	echo
	[ \$RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/\$prog
	return \$RETVAL
}

stop() {
	echo -n \$"Shutting down \$desc: "
	killproc \$prog
	RETVAL=\$?
	echo
	[ \$RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/\$prog
	return \$RETVAL
}

restart(){
	stop
	start
}

case "\$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart)
	restart
	;;
  condrestart)
	[ -e %{_localstatedir}/lock/subsys/\$prog ] && restart
	RETVAL=\$?
	;;
  status)
	status \$prog
	RETVAL=\$?
	;;
  reload)     ### reread configuration file and clear bad karma/nice levels
	echo -n \$"Reloading \$prog: "
	killproc \$prog -HUP
	RETVAL=\$?
	echo
	;;
  reconfig) ### reread configuration file
	echo -n \$"Rereading \$prog configuration: "
	killproc \$prog -USR2
	RETVAL=\$?
	echo
	;;
  dump)     ### dump process database to stderr+syslog
	echo -n \$"Dumping \$prog database to syslog: "
	killproc \$prog -USR1
	RETVAL=\$?
	echo
	;;
  *)
	echo \$"Usage: \$0 {start|stop|restart|status|reload|reconfig|dump}"
	RETVAL=1
esac

exit \$RETVAL
EOF

%{__cat} <<EOF >verynice.conf
### verynice.conf -- sample configuration file
###
### Declare root immune (root owned processes will never be adjusted)
immuneuser adm
immuneuser bin
immuneuser bind
immuneuser daemon
immuneuser ldap
immuneuser root
immuneuser xfs

### Declare immune program, matlab in this case. If the line is uncommented,
### any program with "matlab" in it's path will be immune to renicing.
### The quoted quantity must match a substring of the symbolic link in
### /proc/{pid}/exe
### if there is a leading slash, the match must be precise
#immuneexe "matlab"

### Declare "bad" program -- automatically niced to batch job level
#badexe "mathematica"

### Declare "hungry" program -- always assumed to have 100% cpu usage,
###                             regardless of actual usage. For programs
###                             which tend to have lots of little subprocesses
###                             with short lifetimes to do their dirty work
###                             (such as "make")
### (we use leading slashes and various possible paths so that we will never
###  accidentally give this flag to another program)
### Note that it IS possible to set both the "hungry" and "runaway" flags
### simultaneously (process will always be killed after a certain amount of time)
hungryexe "/usr/bin/make"
hungryexe "/usr/bin/gmake"

### Declare "good" program -- automatically negatively reniced to
### multimedia job level. goodexe "xmms" reduces the chances of skipping when
### playing mp3's
goodexe "cdrecord"
goodexe "gcombust"
goodexe "gmplayer"
goodexe "mplayer"
goodexe "ogle"
goodexe "realplay"
goodexe "rvplayer"
goodexe "vlc"
goodexe "xanim"
goodexe "xcdroast"
goodexe "xine"
goodexe "xmms"

### Making the X server a "good" program is usually a good idea too
###   -- X is essentially a multimedia app. These next few lines will
###   work even if root is declared an "immune" user and X is run as root,
###   because "goodexe"'s specified in verynice.conf are exceptions to
###   the "immuneuser" rule
goodexe "/etc/X11/X"
goodexe "/usr/X11R6/bin/XF86_"
goodexe "/usr/X11R6/bin/XFree86"
goodexe "/usr/X11R6/bin/X"

### Declare "potential runaway" program. They can go to a lower priority
### (reniced all the way to +20), and if they exceed that they will be
### killed. Other processes are never killed. This is good for netscape and
### any other programs with a tendency to start eating the CPU for no reason.
runawayexe "Fvwm"
runawayexe "galeon"
runawayexe "gimp"
runawayexe "mozilla"
runawayexe "netscape"
runawayexe "phoenix"
runawayexe "opera-motif-wrapper"
runawayexe "xfig"

### Sample additional parameters, specifying the built in defaults
#notnice    -4
#batchjob   18
#runaway    20
#kill       22
#badkarmarate .0167
#badkarmarestorationrate .0167
#periodicity 60
#rereadcfgperiodicity 60
EOF

%build
%{__make} %{?_smp_mflags} RPM_OPT_FLAGS="%{optflags}" PREFIX="%{_prefix}"

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_initrddir}
%{__make} install PREFIX="%{_prefix}" RPM_BUILD_ROOT="%{buildroot}"
%{__install} -Dp -m0755 verynice.sysv %{buildroot}%{_initrddir}/verynice

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_docdir}

%post
/sbin/chkconfig --add verynice

%preun
if [ $1 -eq 0 ] ; then
	/sbin/service verynice stop &>/dev/null || :
	/sbin/chkconfig --del verynice
fi

%postun
/sbin/service verynice condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG COPYING README* verynice.html
%config(noreplace) %{_sysconfdir}/verynice.conf
%config %{_initrddir}/verynice
%{_sbindir}/verynice

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.1-1.2
- Rebuild for Fedora Core 5.

* Sat Jan 21 2006 Dag Wieers <dag@wieers.com> - 1.1-1
- Fixed a prefix-bug in the binary. (Fred Tam)

* Tue Apr 29 2003 Dag Wieers <dag@wieers.com> - 1.1-0
- Initial package. (using dar)
