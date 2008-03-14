# $Id$
# Authority: dag
# Upstream: <amavis-user$lists,sourceforge,net>

### FIXME: If clamd is installed, add user clamav to group amavis
### FIXME: Look into amavis own stop/reload functionality

##ExclusiveDist: fc1 fc2 fc3 el4

%define logmsg logger -t %{name}/rpm

Summary: Mail virus-scanner
Name: amavisd-new
Version: 2.5.4
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://www.ijs.si/software/amavisd/

Source: http://www.ijs.si/software/amavisd/amavisd-new-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 5.8.1, sendmail-devel >= 8.12, sendmail
Requires: arc >= 5.21e, nomarch >= 1.2, unrar >= 2.71, zoo >= 2.10
Requires: bzip2, cpio, file, freeze, lha, lzop, ncompress, unarj
Requires: cabextract, ripole, perl(BerkeleyDB)
Requires: perl(Archive::Tar), perl(Archive::Zip) >= 1.14, perl(Compress::Zlib) >= 1.35
Requires: perl(Convert::TNEF), perl(Convert::UUlib), perl(IO::Stringy)
Requires: perl(MIME::Base64), perl(MIME::Tools) >= 5.420, perl(Unix::Syslog)
Requires: perl(Time::HiRes) >= 1.49, perl(Digest::MD5), perl(Digest::SHA1)
Requires: perl(Digest::HMAC), perl(Net::DNS), perl(Mail::SpamAssassin)
Requires: perl-MailTools, perl(Net::Server) >= 0.93, perl-HTML-Parser >= 3.24
Requires: perl(DB_File), perl(Digest::MD5) >= 2.22, perl(DBI) >= 1.43
Requires: perl(Net::Cmd) >= 2.24

Obsoletes: amavisd
Obsoletes: amavisd-new-utils <= %{version}-%{release}
Provides: amavisd-new-utils = %{version}-%{release}

%description
AMaViS is a program that interfaces a mail transfer agent (MTA) with
one or more virus scanners.

Amavisd-new is a branch created by Mark Martinec that adds serveral
performance and robustness features. It's partly based on
work being done on the official amavisd branch. Please see the
README.amavisd-new-RELNOTES file for a detailed description.

%package milter
Summary: The Amavisd-new sendmail-milter Daemon
Group: Applications/System
Requires: amavisd-new = %{version}-%{release}
Requires: sendmail

%description milter
The Amavisd-new sendmail-milter Daemon

%prep
%setup -n amavisd-new-%{version}

### FIXME: Some versions of install fail to change permissions when failing to change ownership. (Please fix upstream)
%{__perl} -pi.orig -e 's| -o root | |g' helper-progs/Makefile.in

%{__cat} <<EOF >amavisd.logrotate
%{_localstatedir}/log/amavis.log {
    create 600 amavis amavis
    missingok
    copytruncate
    notifempty
}
EOF

%{__cat} <<EOF >amavisd.cron
/usr/sbin/tmpwatch 720 %{_localstatedir}/virusmails/
EOF

%{__perl} -pi.orig -e '
        s|^(my\(\$db_home\))\s*=.*$|$1 = "%{_localstatedir}/amavis/db";|;
    ' amavisd-nanny

%{__perl} -pi.orig -e '
        s|/var/amavis/db|%{_localstatedir}/amavis/db|;
    ' amavisd-agent

%{__perl} -pi.orig -e '
        s|^(\s\$socketname)\s*=.*$|$1 = "%{_localstatedir}/amavis/amavisd.sock";|;
    ' amavisd-release

%{__cat} <<'EOF' >amavisd.sysconfig
### Uncomment this if you want to use amavis with sendmail milter interface.
### See README.milter for details.
#
#MILTER_SOCKET="local:/var/amavis/amavis-milter.sock"
#MILTER_SOCKET="10024@127.0.0.1"

### These are other defaults.
#AMAVIS_ACCOUNT="amavis"
#CONFIG_FILE="%{_sysconfdir}/amavisd.conf"
#MILTER_FLAGS=""
EOF

%{__cat} <<'EOF' >amavisd.sysv
#!/bin/bash
#
# Init script for AMaViS email virus scanner.
#
# Written by Dag Wieers <dag@wieers.com>.
#
# chkconfig: 2345 79 31
# description: AMaViS virus scanner.
#
# processname: amavisd
# config: %{_sysconfdir}/amavisd.conf
# pidfile: %{_localstatedir}/run/amavisd.pid

source %{_initrddir}/functions

[ -x %{_sbindir}/amavisd ] || exit 1
[ -r %{_sysconfdir}/amavisd.conf ] || exit 1

### Default variables
AMAVIS_USER="amavis"
CONFIG_FILE="%{_sysconfdir}/amavisd.conf"
MILTER_SOCKET=""
MILTER_FLAGS=""
SYSCONFIG="%{_sysconfdir}/sysconfig/amavisd"

### Read configuration
[ -r "$SYSCONFIG" ] && source "$SYSCONFIG"

### Backward compatibility
[ "$AMAVIS_ACCOUNT" ] && AMAVIS_USER="$AMAVIS_ACCOUNT"

RETVAL=0
prog="amavisd"
prog2="amavis-milter"
desc="Mail Virus Scanner"

start() {
    if [ "$MILTER_SOCKET" -a -x "%{_sbindir}/$prog2" ]; then
        echo -n $"Starting $desc ($prog2): "
        daemon --user "$AMAVIS_USER" %{_sbindir}/$prog2 -p "$MILTER_SOCKET" $MILTER_FLAGS
        RETVAL=$?
        echo
        [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog2
    fi
    echo -n $"Starting $desc ($prog): "
    daemon --user "$AMAVIS_USER" %{_sbindir}/$prog -c "$CONFIG_FILE"
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
    return $RETVAL
}

stop() {
    echo -n $"Shutting down $desc ($prog): "
    killproc $prog
#   su - $AMAVIS_USER -c "%{_sbindir}/$prog -c $CONFIG_FILE stop"
    RETVAL=$?
    echo
    [ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
    if [ "$MILTER_SOCKET" -o -f %{_localstatedir}/lock/subsys/$prog2 ]; then
        echo -n $"Shutting down $desc ($prog2): "
        killproc $prog2
        RETVAL=$?
        echo
        [ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog2
    fi
    return $RETVAL
}

reload() {
    echo -n $"Reloading $desc ($prog): "
    killproc $prog -HUP
#   su - $AMAVIS_USER -c "%{_sbindir}/$prog -c $CONFIG_FILE reload"
    RETVAL=$?
    echo
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
  restart)
    restart
    ;;
  reload)
    reload
    ;;
  condrestart)
    [ -e %{_localstatedir}/lock/subsys/$prog ] && restart
    RETVAL=$?
    ;;
  status)
    status $prog
    status $prog2
    RETVAL=$?
    ;;
  *)
    echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
    RETVAL=1
esac

exit $RETVAL
EOF

%build
cd helper-progs
%configure \
    --enable-postfix \
    --enable-all \
    --with-milterlib="%{_libdir}" \
    --with-runtime-dir="%{_localstatedir}/amavis" \
    --with-sockname="%{_localstatedir}/amavis/amavisd.sock" \
    --with-user="amavis"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%makeinstall -C helper-progs

%{__perl} -pi.orig -e '
        s|=\s*'\''vscan'\''|= "amavis"|;
        s|^#*(\$MYHOME)\s*=.*$|$1 = "%{_localstatedir}/amavis";|;
        s|^(#*\$SYSLOG.+)$|$1\n\$LOGFILE = "%{_localstatedir}/log/amavis.log";|;
        s|^#*(\$QUARANTINEDIR)\s*=.*$|$1 = "%{_localstatedir}/virusmails";|;
        s|^#* *(\$db_home\s+=.*)$|$1|;
    ' amavisd.conf

%{__install} -d -m0700 %{buildroot}%{_localstatedir}/virusmails/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/amavis/{db,tmp,var}/

%{__install} -Dp -m0755 amavisd %{buildroot}%{_sbindir}/amavisd
%{__install} -Dp -m0755 amavisd-agent %{buildroot}%{_sbindir}/amavisd-agent
%{__install} -Dp -m0755 amavisd-nanny %{buildroot}%{_sbindir}/amavisd-nanny
%{__install} -Dp -m0755 amavisd-release %{buildroot}%{_sbindir}/amavisd-release
%{__install} -Dp -m0755 p0f-analyzer.pl %{buildroot}%{_sbindir}/p0f-analyzer
%{__install} -Dp -m0755 amavisd.sysv %{buildroot}%{_initrddir}/amavisd
%{__install} -Dp -m0700 amavisd.conf %{buildroot}%{_sysconfdir}/amavisd.conf
%{__install} -Dp -m0644 LDAP.schema %{buildroot}%{_sysconfdir}/openldap/schema/amavisd-new.schema
%{__install} -Dp -m0644 amavisd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/amavisd
%{__install} -Dp -m0644 amavisd.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/amavisd
%{__install} -Dp -m0755 amavisd.cron %{buildroot}%{_sysconfdir}/cron.daily/amavisd

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/log/
touch %{buildroot}%{_localstatedir}/log/amavis.log

%clean
%{__rm} -rf %{buildroot}

%pre
if ! /usr/bin/id amavis &>/dev/null; then
    /usr/sbin/useradd -r -d "/var/amavis" -s /bin/sh -c "Amavis email scan user" -M amavis || \
        %logmsg "Unexpected error adding user \"amavis\"."
fi

if ! /usr/bin/id -n -G amavis | grep -q "\<clamav\>"; then
    /usr/sbin/usermod -G $(id -Gn clamav | tr ' ' ','),amavis clamav || \
        %logmsg "Failed to add user \"amavis\" to group \"clamav\"."
fi

%post
/sbin/chkconfig --add amavisd

for file in /etc/postfix/aliases /etc/mail/aliases /etc/aliases; do
    if [ -r "$file" ]; then
        if ! grep -q "^virusalert:" "$file"; then
            echo -e "virusalert:\troot" >> "$file"
            /usr/bin/newaliases &>/dev/null || \
                %logmsg "Cannot exec newaliases. Please run it manually."
        fi
    fi
done

%post milter
if [ -f /etc/mail/sendmail.mc ]; then
    if ! grep -q "milter-amavis" /etc/mail/sendmail.mc; then
        echo -e "\ndnl define(\`MILTER', 1)\ndnl INPUT_MAIL_FILTER(\`milter-amavis', \`S=local:/var/amavis/amavis-milter.sock, F=T, T=S:10m;R:10m;E:10m')" >>/etc/mail/sendmail.mc
    fi
fi

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service amavisd stop &>/dev/null || :
    /sbin/chkconfig --del amavisd
fi

%postun
if [ $1 -eq 0 ]; then
    /usr/sbin/userdel amavis || %logmsg "User \"amavis\" could not be deleted."
    /usr/sbin/groupdel amavis || %logmsg "Group \"amavis\" could not be deleted."
else
    /sbin/service amavisd condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AAAREADME.first LDAP.schema LICENSE MANIFEST README_FILES/* RELEASE_NOTES
%doc amavisd.conf* test-messages/
%config %{_initrddir}/amavisd
%config %{_sysconfdir}/openldap/schema/*.schema
%config(noreplace) %{_sysconfdir}/logrotate.d/amavisd
%config(noreplace) %{_sysconfdir}/cron.daily/amavisd
%{_sbindir}/amavisd
%{_sbindir}/amavisd-agent
%{_sbindir}/amavisd-nanny
%{_sbindir}/amavisd-release
%{_sbindir}/p0f-analyzer

%defattr(0640, root, amavis, 0755)
%config(noreplace) %{_sysconfdir}/amavisd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/amavisd

%defattr(0600, amavis, amavis, 0750)
%dir %{_localstatedir}/amavis/
%dir %{_localstatedir}/amavis/db/
%dir %{_localstatedir}/amavis/tmp/
%dir %{_localstatedir}/amavis/var/
%dir %{_localstatedir}/virusmails/
%ghost %{_localstatedir}/log/amavis.log

%files milter
%defattr(-, root, root, 0755)
%{_sbindir}/amavis
%{_sbindir}/amavis-milter

%changelog
* Thu Mar 13 2008 Dag Wieers <dag@wieers.com> - 2.5.4-1
- Updated to release 2.5.4.

* Mon Jan 28 2008 Dag Wieers <dag@wieers.com> - 2.5.3-2
- Added missing amavisd helper-utils. (Ralph Angenendt)

* Mon Dec 31 2007 Dag Wieers <dag@wieers.com> - 2.5.3-1
- Updated to release 2.5.3.

* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 2.5.2-1
- Updated to release 2.5.2.

* Fri Jun 01 2007 Dag Wieers <dag@wieers.com> - 2.5.1-1
- Updated to release 2.5.1.

* Wed Jan 31 2007 Dag Wieers <dag@wieers.com> - 2.4.5-1
- Updated to release 2.4.5.

* Sun Dec 24 2006 Dries Verachtert <dries@ulyssis.org> - 2.4.4-1
- Updated to release 2.4.4.

* Tue Oct 03 2006 Dag Wieers <dag@wieers.com> - 2.4.3-1
- Updated to release 2.4.3.

* Thu Jun 29 2006 Dag Wieers <dag@wieers.com> - 2.4.2-1
- Updated to release 2.4.2.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 2.4.1-2
- Added perl-Net-Cmd >= 2.24 as a new dependency. (Peter Bieringer)

* Tue Apr 18 2006 Dag Wieers <dag@wieers.com> - 2.4.0-3
- Added perl-DBI >= 1.43 as a new dependency. (Jim)

* Mon Apr 17 2006 Dag Wieers <dag@wieers.com> - 2.4.0-2
- perl-MIME-tools dependency raised to >= 5.420. (Michael Kratz)

* Sat Apr 15 2006 Dag Wieers <dag@wieers.com> - 2.4.0-1
- Updated to release 2.4.0.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 2.3.2-3
- Added perl(Time::HiRes) >= 1.49 requirement.

* Tue Jan 10 2006 Dag Wieers <dag@wieers.com> - 2.3.2-2
- Added perl(Compress::Zlib) >= 1.35 requirement. (Luigi Iotti)

* Thu Jan 05 2006 Dries Verachtert <dries@ulyssis.org> - 2.3.2-1
- Updated to release 2.3.3.

* Mon Jul 11 2005 Dag Wieers <dag@wieers.com> - 2.3.2-1
- Updated to release 2.3.2.

* Tue May 10 2005 Dag Wieers <dag@wieers.com> - 2.3.1-1
- Updated to release 2.3.1.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 2.3.0-1
- Updated to release 2.3.0.

* Tue Mar 29 2005 Dag Wieers <dag@wieers.com> - 2.2.1-2
- Change order of shutting down milter/amavisd.
- Added ripole as a dependency.

* Mon Feb 07 2005 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.

* Mon Nov 29 2004 Dag Wieers <dag@wieers.com> - 2.2.0-3
- Fixes to handling of aliases. (Ed Solis)
- Now add user amavis to group clamav (if not already). (Luigi Iotti)

* Fri Nov 05 2004 Dag Wieers <dag@wieers.com> - 2.2.0-2
- Added upstream improvements. (Marius Andreiana)
- Added cabextract as a requirement. (Luigi Iotti)
- Reverted some of my user changes. (Luigi Iotti)
- Fixed permissions and added configfiles to docs. (Luigi Iotti)

* Thu Nov 04 2004 Dag Wieers <dag@wieers.com> - 2.2.0-1
- Change of version format, requires manual intervention.
- Directory changes to conform to amavisd standard.
- Now using user vscan instead of amavis.
- Added logrotate config for amavisd. (Anders Nielsen)
- Added a clean-up cron script for /var/virusmails. (Anders Nielsen)
- Updated to release 2.2.0.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 20030616-9.p10
- Updated to release 20030616-p10.

* Wed Apr 21 2004 Dag Wieers <dag@wieers.com> - 20030616-8.p9
- Moved milter to subpackage. Please add it if you need it !

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 20030616-7.p9
- Added perl(DB_File) dependency. (Edward Rudd)

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 20030616-6.p9
- Updated to release 20030616-p9.

* Mon Mar 29 2004 Dag Wieers <dag@wieers.com> - 20030616-6.p8
- Fixed problem with certain versions of 'install'. (Peter Soos)
- Added contributed amavis-milter support in sysv-script. (Peter Soos)

* Mon Mar 15 2004 Dag Wieers <dag@wieers.com> - 20030616-5.p8
- Fixed amavis-milter.sock example in sendmail.mc (Ivo Clarysse)

* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 20030616-4.p8
- Updated to release 20030616-p8.
- Make milter-support optional (for RHEL3).
- Added lzop requirement.
- Added perl-Net-Server >= 0.86 as a static requirement. (Alfredo Milani-Comparetti)

* Mon Jan 05 2004 Dag Wieers <dag@wieers.com> - 20030616-3.p7
- Updated to release 20030616-p7

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 20030616-3.p6
- Updated to release 20030616-p6.

* Tue Nov 04 2003 Dag Wieers <dag@wieers.com> - 20030616-3.p5
- Fixed the %%post section. (Alfredo Milani-Comparetti)

* Mon Sep 08 2003 Dag Wieers <dag@wieers.com> - 20030616-2.p5
- Added %%logmsg for output.
- Added LDAP schema. (Stephane Lentz)
- Updated to release 20030616-p5.

* Tue Jul 15 2003 Dag Wieers <dag@wieers.com> - 20030616-2
- Fixed user/group in amavisd.conf typo. (Alexander Hoogerhuis)
- Fixed user-creation.

* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 20030616-1
- Fixed typo in requirements. (Alexander Hoogerhuis)
- Simplified the %%pre/%%post scriptlets. (Matthias Saou)
- Fixed files being listed twice in %%{_localstatedir}. (Matthias Saou)
- Improved sysv script to mimic template.
- Updated to release 20030616-p2.

* Tue Jan 14 2003 Dag Wieers <dag@wieers.com> - 20021227-0
- Initial package. (using DAR)
