# $Id$
# Authority: dag
# Upstream: <amavis-user@lists.sourceforge.net>

%define milter 1
%{?rhel3:%undefine milter}

%define rrelease p8

%define logmsg logger -t amavisd-new/rpm

Summary: Mail virus-scanner.
Name: amavisd-new
Version: 20030616
Release: 4.%{rrelease}
License: GPL
Group: System Environment/Daemons
URL: http://www.ijs.si/software/amavisd/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.ijs.si/software/amavisd/amavisd-new-%{version}-%{rrelease}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: sendmail
#BuildRequires: postfix
%{?milter:BuildRequires: sendmail-devel >= 8.12}
Requires: arc >= 5.21e, nomarch >= 1.2, unrar >= 2.71, zoo >= 2.10
Requires: bzip2, cpio, file, freeze, lha, lzop, ncompress, unarj
Requires: perl(Archive::Tar), perl(Archive::Zip), perl(Compress::Zlib)
Requires: perl(Convert::TNEF), perl(Convert::UUlib), perl(IO::Stringy)
Requires: perl(MIME::Base64), perl(MIME::Tools), perl(Unix::Syslog)
Requires: perl(Time::HiRes), perl(Digest::MD5), perl(Digest::SHA1)
Requires: perl(Digest::HMAC), perl(Net::DNS), perl(Mail::SpamAssassin)
Requires: perl-MailTools, perl(Net::Server) >= 0.86
Obsoletes: amavisd

%description
AMaViS is a script that interfaces a mail transport agent (MTA) with
one or more virus scanners.
  
Amavisd-new is a development branch created by Mark Martinec that 
adds serveral performance and robustness features. It's partly based on 
work being done on the official amavisd branch. Please see the
README.amavisd-new-RELNOTES file for a detailed description.

%prep
%setup -n amavisd-new-%{version}

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
# config: %{_sysconfdir}/amavis.conf
# pidfile: %{_localstatedir}/run/amavisd.pid

source %{_initrddir}/functions

[ -x %{_sbindir}/amavisd ] || exit 1
[ -r %{_sysconfdir}/amavisd.conf ] || exit 1

RETVAL=0
prog="amavisd"
desc="Mail Virus Scanner"

start() {
	echo -n $"Starting $desc ($prog): "
	daemon $prog
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && touch %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

stop() {
	echo -n $"Shutting down $desc ($prog): "
	killproc $prog
	RETVAL=$?
	echo
	[ $RETVAL -eq 0 ] && rm -f %{_localstatedir}/lock/subsys/$prog
	return $RETVAL
}

reload() {
	echo -n $"Reloading $desc ($prog): "
	killproc $prog -HUP
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
	RETVAL=$?
	;;
  *)
	echo $"Usage: $0 {start|stop|restart|reload|condrestart|status}"
	RETVAL=1
esac

exit $RETVAL
EOF

%build
%if %{?milter:1}%{!?milter:0}
cd helper-progs
%configure \
	--with-user="amavis" \
	--with-sockname="%{_localstatedir}/spool/amavis/amavisd.sock" \
	--with-runtime-dir="%{_localstatedir}/spool/amavis" \
	--enable-postfix \
	--enable-all
%{__make} %{?_smp_mflags}
%endif

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_sbindir}
%{?milter:%makeinstall -C helper-progs}

%{__perl} -pi.orig -e '
		s|= '\''vscan'\''|= "amavis"|;
		s|= '\''sweep'\''|= "amavis"|; 
		s|^#*(\$MYHOME =).*$|\1 "%{_localstatedir}/spool/amavis";|;
		s|^#*(\$QUARANTINEDIR =).*$|\1 "%{_localstatedir}/spool/amavis/virusmails";|;
	' amavisd.conf

%{__install} -d -m0755 %{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/openldap/schema/
%{__install} -d -m0700 %{buildroot}%{_localstatedir}/spool/amavis/virusmails/

#%{__install} -m0755 amavisd amavisdconf %{buildroot}%{_sbindir}
%{__install} -m0755 amavisd %{buildroot}%{_sbindir}
%{__install} -m0755 amavisd.sysv %{buildroot}%{_initrddir}/amavisd
%{__install} -m0700 amavisd.conf %{buildroot}%{_sysconfdir}
%{__install} -m0644 LDAP.schema %{buildroot}%{_sysconfdir}/openldap/schema/amavisd-new.schema

%clean
%{__rm} -rf %{buildroot}

%pre
/usr/sbin/useradd -c "AMaViS email scanner user" -M -s /bin/sh -r amavis \
		-d "/var/spool/amavis" &>/dev/null || :

%post
/sbin/chkconfig --add amavisd

if [ -r /etc/postfixes/aliases ]; then
	if ! grep -q "^virusalert:" /etc/postfix/aliases; then
		echo -e "virusalert:\troot" >> /etc/postfix/aliases
		if [ -x /usr/bin/newaliases ]; then
			/usr/bin/newaliases &>/dev/null
		else
			%logmsg "Cannot exec newaliases. Please run it manually."
		fi
	fi
fi

if [ -r /etc/mail/aliases ]; then
	if ! grep -q "^virusalert:" /etc/mail/aliases; then
		echo -e "virusalert:\troot" >> /etc/mail/aliases
		if [ -x /usr/bin/newaliases ]; then
			/usr/bin/newaliases &>/dev/null
		else
			%logmsg "Cannot exec newaliases. Please run it manually."
		fi
	fi
fi

%if %{?milter:1}%{!?milter:0}
if [ -f /etc/mail/sendmail.mc ]; then
	if ! grep -q "milter-amavis" /etc/mail/sendmail.mc; then
		echo -e "\ndnl define(\`MILTER', 1)\ndnl INPUT_MAIL_FILTER(\`milter-amavis', \`S=local:/var/spool/amavis/amavisd.sock, F=T, T=S:10m;R:10m;E:10m')" >>/etc/mail/sendmail.mc
	fi
fi
%endif

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service amavisd stop &>/dev/null || :
    /sbin/chkconfig --del amavisd
fi

%postun
if [ $1 -ne 0 ]; then
    /sbin/service amavisd condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AAAREADME.first LDAP.schema LICENSE MANIFEST RELEASE_NOTES README_FILES/* test-messages/
%config %{_initrddir}/amavisd
%config %{_sysconfdir}/openldap/schema/*.schema
%{_sbindir}/*
%defattr(0640, amavis, amavis, 0755)
%config(noreplace) %{_sysconfdir}/amavisd.conf
%defattr(0700, amavis, amavis, 0700)
%dir %{_localstatedir}/spool/amavis/
%dir %{_localstatedir}/spool/amavis/virusmails/

%changelog
* Tue Mar 09 2004 Dag Wieers <dag@wieers.com> - 20030616-1.p8
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
