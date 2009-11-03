# $Id$
# Authority: dag

# ExclusiveDist: rh7 rh6
# SourceDists: rh7

%{?dtag: %{expand: %%define %dtag 1}}

%define optflags -O2 -fno-strict-aliasing

%define initdir /etc/rc.d/init.d
# If you want to build this on older Red Hat Linux releases, this defines
# the version number to build on. Supported should be 62 70 71 72 for
# Red Hat Linux 6.2 up to 7.2 and "100" for the current rawhide version.
%{?rh6:%define errata 62}
%{?el2:%define errata 72}
%{?rh7:%define errata 73}

%if %{errata} <= 70
%define sendmailcf usr/lib/sendmail-cf
%else
%define sendmailcf usr/share/sendmail-cf
%endif

%if %{errata} >= 72
%define smshell /sbin/nologin
%else
%define smshell /dev/null
%endif

Summary: widely used Mail Transport Agent (MTA)
Name: sendmail
Version: 8.12.8
Release: 0%{?dist}
License: BSD
Group: System Environment/Daemons
Provides: smtpdaemon
Source0: ftp://ftp.cs.berkeley.edu/ucb/sendmail/sendmail.%{version}.tar.gz
Source1: sendmail.init
Source3: aliases
Source4: sendmail.sysconfig
Source5: sendmail.etc-mail-Makefile
Source6: sendmail-redhat.mc
Source7: Sendmail.conf
Source8: sendmail.pam
Source9: sendmail-8.12.5-newconfig.readme
Patch0: sendmail-8.12.2-redhat.patch
Patch1: sendmail-8.11.0-redhat.patch
Patch2: sendmail-8.11.0-redhat.patch2
Patch3: sendmail-8.12.2-makemapman.patch
Patch4: sendmail-8.12.2-smrsh-paths.patch
Patch5: sendmail-8.12.2-movefiles.patch
#Patch6: sendmail-8.12.2-unix.patch
Patch7: sendmail-8.12.5-pid.patch
Patch9: sendmail-8.12.7-hesiod.patch
Patch10: sendmail-8.12.7-manpage.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gdbm-devel

%if %{errata} > 62
%if %{errata} <= 70
BuildRequires: cyrus-sasl
%else
BuildRequires: cyrus-sasl-devel
%endif
%if %{errata} >= 73
BuildRequires: hesiod-devel
%else
BuildRequires: db3-devel
%endif
BuildRequires: openldap-devel, tcp_wrappers
%endif
%if %{errata} >= 73
Prereq: /usr/sbin/alternatives
Provides: %{_sbindir}/sendmail %{_bindir}/mailq %{_bindir}/newaliases
Provides: %{_bindir}/rmail %{_mandir}/man1/mailq.1.gz
Provides: %{_mandir}/man1/newaliases.1.gz %{_mandir}/man5/aliases.5.gz
Prereq: chkconfig >= 1.3
%else
Prereq: /sbin/chkconfig
%endif
Prereq: /usr/sbin/useradd /bin/mktemp fileutils gawk sed sh-utils
%if %{errata} < 73
Conflicts: postfix exim
%endif
Requires: procmail
%if %{errata} > 62
Requires: bash >= 2.0
%endif
%description
The Sendmail program is a very widely used Mail Transport Agent (MTA).
MTAs send mail from one machine to another. Sendmail is not a client
program, which you use to read your email. Sendmail is a
behind-the-scenes program which actually moves your email over
networks or the Internet to where you want it to go.

If you ever need to reconfigure Sendmail, you will also need to have
the sendmail.cf package installed. If you need documentation on
Sendmail, you can install the sendmail-doc package.

%package doc
Summary: Documentation about the Sendmail Mail Transport Agent program
Group: Documentation

%description doc
The sendmail-doc package contains documentation about the Sendmail
Mail Transport Agent (MTA) program, including release notes, the
Sendmail FAQ, and a few papers written about Sendmail. The papers are
provided in PostScript(TM) and troff formats.

%package devel
Summary: Extra development include files and development files
Group: System Environment/Daemons

%description devel
Include files and devel libraries for e.g. the milter addons as part
of sendmail.

%package cf
Summary: The files needed to reconfigure Sendmail
Group: System Environment/Daemons

%description cf
This package includes the configuration files you need to generate the
sendmail.cf file distributed with the sendmail package. You will need
the sendmail-cf package if you ever need to reconfigure and rebuild
your sendmail.cf file.

%prep
%setup -q
if test %{errata} -gt 72 ; then
%patch0 -p1
elif test %{errata} -gt 62 ; then
%patch1 -p1
else
%patch2 -p1
fi
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1
%patch7 -p1
%patch9 -p1
%patch10 -p1

%build
sed     -e 's,%%{_libdir},%{_libdir},g' \
        -e 's,%%{_lib},%{_lib},g' redhat.config.m4.in > redhat.config.m4

for i in libmilter libsmutil sendmail mailstats rmail praliases \
	smrsh makemap ; do
	pushd $i
	sh Build -f ../redhat.config.m4
	popd
done

%install
%{__rm} -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT
mkdir -p etc/sysconfig .%{initdir} etc/pam.d
mkdir -p usr/bin usr/include/libmilter usr/lib .%{_mandir}/man{1,5,8}
mkdir -p usr/sbin var/log var/spool %{sendmailcf}
cd -

OBJDIR=obj.$(uname -s).$(uname -r).$(arch)
nameuser=`id -nu`
namegroup=`id -ng`

Make() {
	make $@ \
		DESTDIR=$RPM_BUILD_ROOT \
		MANROOT=%{_mandir}/man \
		SBINOWN=${nameuser} SBINGRP=${namegroup} \
		UBINOWN=${nameuser} UBINGRP=${namegroup} \
		MANOWN=${nameuser}  MANGRP=${namegroup} \
		INCOWN=${nameuser}  INCGRP=${namegroup} \
		LIBOWN=${nameuser}  LIBGRP=${namegroup} \
		GBINOWN=${nameuser} GBINGRP=${namegroup} \
		CFOWN=${nameuser}   CFGRP=${namegroup} \
		MSPQOWN=${nameuser}
}

Make install -C $OBJDIR/libmilter
Make install -C $OBJDIR/libsmutil
Make install -C $OBJDIR/sendmail
Make install -C $OBJDIR/mailstats
Make force-install -C $OBJDIR/rmail
Make install -C $OBJDIR/praliases
Make install -C $OBJDIR/smrsh
Make install -C $OBJDIR/makemap

touch $RPM_BUILD_ROOT/rootfile
root=..
while [ ! -r $RPM_BUILD_ROOT/%{_bindir}/${root}/rootfile ] ; do
	root=${root}/..
done
ln -sf ${root}%{_sbindir}/makemap $RPM_BUILD_ROOT/%{_bindir}/makemap

# Install docs by hand for the sendmail-doc package.
DOC=$RPM_BUILD_ROOT%{_docdir}/sendmail
mkdir -p $DOC
cp -ar FAQ LICENSE KNOWNBUGS README RELEASE_NOTES doc $DOC
cp sendmail/README   $DOC/README.sendmail
cp sendmail/SECURITY $DOC/SECURITY
cp smrsh/README      $DOC/README.smrsh
cp libmilter/README  $DOC/README.libmilter
cp cf/README         $DOC/README.cf
cp %{SOURCE9}        $DOC/README.redhat

# Install the cf files for the sendmail-cf package.
cp -ar cf/* $RPM_BUILD_ROOT/%{sendmailcf}

install -d -m755 $RPM_BUILD_ROOT/etc/mail

sed -e 's|@@PATH@@|/%{sendmailcf}|' < %{SOURCE6} > $RPM_BUILD_ROOT/etc/mail/sendmail.mc
%if %{errata} <= 62
perl -pi -e 's/.*confAUTH_OPTIONS.*//' $RPM_BUILD_ROOT/etc/mail/sendmail.mc
%endif
%if %{errata} <= 70
perl -pi -e 's/^DAEMON_OPTIONS/dnl DAEMON_OPTIONS/' $RPM_BUILD_ROOT/etc/mail/sendmail.mc
%endif

sed -e 's|/%{sendmailcf}|\.\.|' < $RPM_BUILD_ROOT/etc/mail/sendmail.mc > cf/cf/redhat.mc
(cd cf/cf && m4 redhat.mc > redhat.cf)
install -m 644 cf/cf/redhat.cf $RPM_BUILD_ROOT/etc/mail/sendmail.cf
install -m 644 cf/cf/submit.mc $RPM_BUILD_ROOT/etc/mail/submit.mc

echo "# local-host-names - include all aliases for your machine here." \
	> $RPM_BUILD_ROOT/etc/mail/local-host-names
( echo "# trusted-users - users that can send mail as others without a warning"
echo "# apache, mailman, majordomo, uucp, are good candidates" ) \
	> $RPM_BUILD_ROOT/etc/mail/trusted-users


touch $RPM_BUILD_ROOT/rootfile
root=..
while [ ! -r $RPM_BUILD_ROOT/%{_libdir}/${root}/rootfile ] ; do
	root=${root}/..
done
#ln -sf ${root}%{_sbindir}/sendmail $RPM_BUILD_ROOT/%{_libdir}/sendmail
ln -sf ../sbin/sendmail $RPM_BUILD_ROOT/%{_libdir}/sendmail
install -d -m775 $RPM_BUILD_ROOT/var/spool/mqueue
install -d -m755 $RPM_BUILD_ROOT/var/spool/clientmqueue

# dangling symlinks
touch $RPM_BUILD_ROOT/rootfile
root=..
while [ ! -r $RPM_BUILD_ROOT/%{_bindir}/${root}/rootfile ] ; do
	root=${root}/..
done
for f in hoststat mailq newaliases purgestat ; do
    ln -sf ${root}%{_sbindir}/sendmail $RPM_BUILD_ROOT%{_bindir}/${f}
done
install -d -m755 $RPM_BUILD_ROOT/etc/smrsh

cat <<EOF > $RPM_BUILD_ROOT/etc/mail/access
# Check the /usr/share/doc/sendmail/README.cf file for a description
# of the format of this file. (search for access_db in that file)
# The /usr/share/doc/sendmail/README.cf is part of the sendmail-doc
# package.
#
# by default we allow relaying from localhost...
localhost.localdomain		RELAY
localhost			RELAY
127.0.0.1			RELAY

EOF
for map in virtusertable access domaintable mailertable ; do
    touch $RPM_BUILD_ROOT/etc/mail/${map}
    chmod 0644 $RPM_BUILD_ROOT/etc/mail/${map}
    $RPM_BUILD_ROOT%{_bindir}/makemap -C $RPM_BUILD_ROOT/etc/mail/sendmail.cf hash $RPM_BUILD_ROOT/etc/mail/${map}.db < $RPM_BUILD_ROOT/etc/mail/${map}
    chmod 0644 $RPM_BUILD_ROOT/etc/mail/${map}.db
done
install -m644 %{SOURCE3} $RPM_BUILD_ROOT/etc/aliases
$RPM_BUILD_ROOT/usr/bin/makemap -C $RPM_BUILD_ROOT/etc/mail/sendmail.cf hash $RPM_BUILD_ROOT/etc/aliases.db < %{SOURCE3}

install -m644 %SOURCE4 $RPM_BUILD_ROOT/etc/sysconfig/sendmail
install -m755 %SOURCE1 $RPM_BUILD_ROOT%{initdir}/sendmail

install -m 644 %{SOURCE5} $RPM_BUILD_ROOT/etc/mail/Makefile

chmod u+w $RPM_BUILD_ROOT/usr/sbin/{mailstats,praliases}
chmod u+w $RPM_BUILD_ROOT/usr/bin/rmail

%if %{errata} > 62
install -m755 -d $RPM_BUILD_ROOT%{_libdir}/sasl
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{_libdir}/sasl/Sendmail.conf
install -m 644 %{SOURCE8} $RPM_BUILD_ROOT/etc/pam.d/smtp
%endif

install -m 755 -d $RPM_BUILD_ROOT%{_libdir}
install -m 644  $OBJDIR/libmilter/libmilter.a $RPM_BUILD_ROOT%{_libdir}
install -m 644  $OBJDIR/libsmutil/libsmutil.a $RPM_BUILD_ROOT%{_libdir}
install -m 644  $OBJDIR/libsm/libsm.a         $RPM_BUILD_ROOT%{_libdir}

%if %{errata} > 72
mv $RPM_BUILD_ROOT%{_sbindir}/sendmail $RPM_BUILD_ROOT%{_sbindir}/sendmail.sendmail
for i in mailq newaliases rmail; do
	mv $RPM_BUILD_ROOT%{_bindir}/$i $RPM_BUILD_ROOT%{_bindir}/$i.sendmail
done
mv $RPM_BUILD_ROOT%{_mandir}/man1/mailq.1 $RPM_BUILD_ROOT%{_mandir}/man1/mailq.sendmail.1
mv $RPM_BUILD_ROOT%{_mandir}/man1/newaliases.1 $RPM_BUILD_ROOT%{_mandir}/man1/newaliases.sendmail.1
mv $RPM_BUILD_ROOT%{_mandir}/man5/aliases.5 $RPM_BUILD_ROOT%{_mandir}/man5/aliases.sendmail.5
%endif

%clean
%{__rm} -rf %{buildroot}

%pre
/usr/sbin/useradd -u 47 -d /var/spool/mqueue -r -s %{smshell} mailnull >/dev/null 2>&1
/usr/sbin/useradd -u 51 -d /var/spool/mqueue -r -s %{smshell} smmsp >/dev/null 2>&1
exit 0

%postun
if [ "$1" -ge "1" ]; then
	%{initdir}/sendmail condrestart >/dev/null 2>&1
fi
exit 0

%post
#
# Convert old format to new
#
if [ -f /etc/mail/deny ] ; then
    cat /etc/mail/deny | \
	awk 'BEGIN{ print "# Entries from obsoleted /etc/mail/deny"} \
		  {print $1" REJECT"}' >> /etc/mail/access
    cp /etc/mail/deny /etc/mail/deny.rpmorig
fi
for oldfile in relay_allow ip_allow name_allow ; do
    if [ -f /etc/mail/$oldfile ] ; then
	cat /etc/mail/$oldfile | \
		awk "BEGIN { print \"# Entries from obsoleted /etc/mail/$oldfile\" ;} \
	     { print \$1\" RELAY\" }" >> /etc/mail/access
	cp /etc/mail/$oldfile /etc/mail/$oldfile.rpmorig
     fi
done

#
# Remove deprecated config flags which are probably harmless to remove
#
cf=`/bin/mktemp /etc/mail/sendmail.cf.XXXXXX`
if [ "$cf" != "" ] ; then
	sed 's/^O AutoRebuildAliases$/#&/g' /etc/mail/sendmail.cf > ${cf} && \
	cat ${cf} > /etc/mail/sendmail.cf
	rm ${cf}
fi

/sbin/chkconfig --add sendmail
%if %{errata} > 72
#
# Set up the alternatives files for MTAs.
#
/usr/sbin/alternatives --install %{_sbindir}/sendmail mta %{_sbindir}/sendmail.sendmail 90 \
	--slave %{_bindir}/mailq mta-mailq %{_bindir}/mailq.sendmail \
	--slave %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.sendmail \
	--slave %{_bindir}/rmail mta-rmail %{_bindir}/rmail.sendmail \
	--slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/mailq.sendmail.1.gz \
	--slave %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man1/newaliases.sendmail.1.gz \
	--slave %{_mandir}/man5/aliases.5.gz mta-aliasesman %{_mandir}/man5/aliases.sendmail.5.gz \
	--initscript sendmail
%endif


#
# Oops, these files moved
#
if [ -f /etc/sendmail.cw ] ; then
    cat /etc/sendmail.cw  | \
      awk 'BEGIN { print "# Entries from obsoleted /etc/sendmail.cw" ;} \
           { print $1 }' >> /etc/mail/local-host-names
    cp /etc/sendmail.cw /etc/sendmail.cw.rpmorig
fi
#
# Rebuild maps (next reboot will rebuild also)
#
{ /usr/bin/newaliases
  for map in virtusertable access domaintable mailertable
  do
    if [ -f /etc/mail/${map} ] ; then
      /usr/bin/makemap hash /etc/mail/${map} < /etc/mail/${map}
      sleep 1
    fi
  done
} > /dev/null 2>&1


%preun
if [ $1 = 0 ]; then
	%{initdir}/sendmail stop >/dev/null 2>&1
	/sbin/chkconfig --del sendmail
%if %{errata} >= 73
	/usr/sbin/alternatives --remove mta %{_sbindir}/sendmail.sendmail
%endif
fi
exit 0

%triggerpostun -- sendmail < 8.10.0
/sbin/chkconfig --add sendmail

%if %{errata} >= 73
%triggerpostun -- sendmail < 8.11.6-11
/usr/sbin/alternatives --auto mta
%endif

%files
%defattr(-, root, root, 0755)
/usr/bin/hoststat
/usr/bin/makemap
/usr/bin/purgestat
/usr/sbin/mailstats
/usr/sbin/makemap
/usr/sbin/praliases
%if %{errata} > 72
%attr(2755,root,smmsp)/usr/sbin/sendmail.sendmail
/usr/bin/rmail.sendmail
/usr/bin/newaliases.sendmail
/usr/bin/mailq.sendmail
%else
%attr(2755,root,smmsp)/usr/sbin/sendmail
/usr/bin/rmail
/usr/bin/newaliases
/usr/bin/mailq
%endif
/usr/sbin/smrsh
/usr/lib/sendmail

%{_mandir}/man8/rmail.8*
%{_mandir}/man8/praliases.8*
%{_mandir}/man8/mailstats.8*
%{_mandir}/man8/makemap.8*
%{_mandir}/man8/sendmail.8*
%{_mandir}/man8/smrsh.8*
%if %{errata} > 72
%{_mandir}/man5/aliases.sendmail.5*
%{_mandir}/man1/newaliases.sendmail.1*
%{_mandir}/man1/mailq.sendmail.1*
%else
%{_mandir}/man5/aliases.5*
%{_mandir}/man1/newaliases.1*
%{_mandir}/man1/mailq.1*
%endif

%config(noreplace)		/etc/mail/statistics
%config(noreplace)		/etc/mail/sendmail.cf
%config(noreplace)		/etc/mail/submit.cf
%attr(0644,root,root) %config(noreplace)	/etc/mail/sendmail.mc
%attr(0644,root,root) %config(noreplace)	/etc/mail/submit.mc
%config(noreplace)		/etc/mail/local-host-names
%config(noreplace)		/etc/aliases
%attr(0644,root,root) %ghost	/etc/aliases.db
%attr(0770,smmsp,smmsp) %dir	/var/spool/clientmqueue
%attr(0700,root,mail) %dir	/var/spool/mqueue
%dir /etc/smrsh
%dir /etc/mail

%config /etc/mail/Makefile
%attr(0644,root,root) %ghost			/etc/mail/virtusertable.db
%attr(0644,root,root) %config(noreplace)	/etc/mail/virtusertable

%attr(0644,root,root) %ghost			/etc/mail/access.db
%attr(0644,root,root) %config(noreplace)	/etc/mail/access

%attr(0644,root,root) %ghost			/etc/mail/domaintable.db
%attr(0644,root,root) %config(noreplace)	/etc/mail/domaintable

%attr(0644,root,root) %ghost			/etc/mail/mailertable.db
%attr(0644,root,root) %config(noreplace)	/etc/mail/mailertable

%attr(0644,root,root) %config(noreplace)	/etc/mail/helpfile
%attr(0644,root,root) %config(noreplace)	/etc/mail/trusted-users

%config(noreplace) /etc/sysconfig/sendmail

%config %{initdir}/sendmail

%if %{errata} > 62
%config %{_libdir}/sasl/Sendmail.conf
/etc/pam.d/smtp
%endif

%files cf
%defattr(-, root, root, 0755)
/%{sendmailcf}

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libmilter/*.h
%{_libdir}/libmilter.a
%{_libdir}/libsmutil.a
%{_libdir}/libsm.a

%files doc
%defattr(-, root, root, 0755)
%{_docdir}/sendmail

%changelog
* Mon Mar 10 2003 Bert de Bruijn <bert@debruijn.be> - 8.12.8-0
- Updated to 8.12.8.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 8.12.5-0
- Updated to 8.12.5.

* Thu Aug 29 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- clean up some specfile cruft
- add more pseudo accounts to /etc/aliases

* Thu Aug 29 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- clean up some specfile cruft
- add more pseudo accounts to /etc/aliases

* Thu Jul 25 2002 Phil Knirsch <pknirsch@redhat.com>
- Only generate new cf files if the /usr/share/sendmail-cf/m4/cf.m4 exists.

* Wed Jul 24 2002 Phil Knirsch <pknirsch@redhat.com>
- Changed the behaviour in /etc/mail/Makefile to generate the sendmail.cf and
  submit.cf from the mc files if they changed.
- Added a small README.redhat that descibed the new mc file behaviour and the
  split into sendmail.cf and submit.cf.

* Wed Jul 24 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- suggestions form Stephane Lentz:
	- add correct include statement into submit.mc (like sendmail.mc)
	- add commented out further suggestions into submit.mc
	- disable ident lookups

* Thu Jul 11 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix initscript for the second daemon and pidfile location #67910

* Mon Jul 01 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 8.12.5

* Thu Jun 27 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add further queue runs, slight spec-file cleanups

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 11 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 8.12.4, adjust smrsh patch

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sat Apr 13 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 8.12.3

* Tue Mar 26 2002 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Mar 25 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix alternatives --remove  #61737
- add sendmail/SECURITY as docu #61870, #61545

* Wed Mar 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add libsm.a    #61270
- change from /etc/sendmail.cf to /etc/mail/sendmail.cf
- add milter patch

* Wed Mar 13 2002 Bill Nottingham <notting@redhat.com>
- ignore DAEMON=no; that configuration no longer functions

* Wed Mar 13 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- make sure more version information is in the cf file #54418
- do not use "-b" flag when patching in spec file
- require newer chkconfig version #61035
- fix preun script #60880
- add TMPF to access file creation #60956

* Sat Mar 09 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- mv include files to /usr/include/libmilter/ #60795
- do not use "-f" option to virtusertable #60196
- ad an example smarthost entry to config file #58298

* Fri Mar  8 2002 Bill Nottingham <notting@redhat.com> 8.12.2-5
- use alternatives --initscript support
- run chkconfig --add before alternatives

* Thu Feb 28 2002 Bill Nottingham <notting@redhat.com> 8.12.2-3
- run alternatives --remove in %preun
- add some prereqs

* Mon Feb 25 2002 Nalin Dahyabhai <nalin@redhat.com> 8.12.2-2
- fix smmsp useradd invocation in %%pre
- switch back to db3 for storing db files

* Wed Feb 20 2002 Nalin Dahyabhai <nalin@redhat.com> 8.12.2-1
- update to 8.12.2 (adds STARTTLS support without need for sfio)
- don't forcibly strip binaries; let the build root handle it
- add creation of the smmsp account (51/51) in %%pre
- enable hesiod map support
- modify default config to use an MSP
- comment out 'O AutoRebuildAliases' in %%post, otherwise sendmail will
  fail to restart on upgrades

* Wed Feb 20 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- add proper ifdefs around new alternative stuff to also be able
  to build this for older releases

* Fri Feb  1 2002 Bill Nottingham <notting@redhat.com> 8.11.6-12
- %triggerpostun on older versions to make sure alternatives work on
  upgrades

* Thu Jan 31 2002 Bill Nottingham <notting@redhat.com> 8.11.6-11
- clean up alternatives somewhat, provide /usr/sbin/sendmail & friends

* Thu Jan 31 2002 Bernhard Rosenkraenzer <bero@redhat.com> 8.11.6-10
- Use alternatives

* Tue Jan 22 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix quotation in spec-file

* Thu Jan 10 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- integrate ugly logic to compile this src.rpm also on older Red Hat
  Linux releases
- clean up spec file and patches a bit
- add db4 support

* Wed Jan 09 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix another path to correct docu
- include sendmail/README in the docu
- compile with -D_FFR_WORKAROUND_BROKEN_NAMESERVERS, but do not
  enable this at runtime
- devel subpackage files owned by root now

* Fri Dec 07 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- change "-q" to "-s" as option to make #57216
- move milter lib into separate "devel" sub-package
- add include files to devel sub-package #56064
- fix pointer in access file to docu #54351

* Mon Sep 10 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add libmilter docu
- add support for userdb to /etc/mail/Makefile
- use "btree" database files if a userdb is used
- buildrequires tcp_wrappers

* Fri Aug 31 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix libmilter support
- fix init script to use /etc/mail/Makefile #52932

* Sat Aug 25 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add libmilter library

* Thu Aug 23 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 8.11.6
- correctly use /etc/mail/statistics

* Thu Aug 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- change init script back to older conventions #51297
- remove DoS patch, not needed anymore #51247

* Mon Aug 06 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add option '-t' to procmail for local mail delivery

* Tue Jul 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- point to the map files in sendmail.cf as pointed out by
  David Beveridge <David@beveridge.com>

* Mon Jul 23 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add build requires #49695
- do not call "userdel"

* Tue Jul 10 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- change sendmail.cf to "noreplace"

* Thu Jun 07 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 8.11.4

* Wed May 09 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 8.11.3
- add "localhost.localdomain" to the list of hostnames accepted
  for local delivery "Cw" in /etc/mail/sendmail.mc
- add patches from Pekka Savola <pekkas@netcore.fi>
	- Enable IPv6 at compile time, patch for glibc 2.2 from PLD
	- Add a commented-out IPv6 daemon .mc line to sendmail.mc
	- buildrequire: openldap-devel, cyrus-sasl-devel

* Fri Mar  2 2001 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Feb 27 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add noreplace for /etc/sysconfig/sendmail and /etc/mail/sendmail.mc

* Wed Feb 21 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- add changes from Christopher McCrory <chrismcc@pricegrabber.com>:
	- prepare /etc/mail/Makefile for more maps not shipped with this rpm
	- changed sendmail.mc to include some more commented out options,
	  so that people are directly pointed at important options
	- add /etc/pam.d/smtp for AUTH
	- add FEATURE(use_ct_file) and /etc/mail/trusted-users

* Fri Feb 16 2001 Tim Powers <timp@redhat.com>
- don't obsolete postfix and exim, only conflict (for RHN purposes)

* Thu Feb 15 2001 Trond Eivind Glomsrød <teg@redhat.com>
- obsolete and conflict with exim and postfix

* Wed Feb 14 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix devision by zero bug in #20395
- mv /usr/lib/sendmail-cf /usr/share/sendmail-cf

* Wed Feb  7 2001 Trond Eivind Glomsrød <teg@redhat.com>
- i18n tweaks to initscript

* Wed Feb 07 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- aliases.db should be owned by group root

* Wed Jan 24 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- prepare for startup-script translation

* Tue Jan 23 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- enable daemon mode again, but only listen to the loopback device
  instead of all devices.
- do not include check.tar with old anti-spam rules

* Fri Jan 12 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix configuration of /etc/aliases

* Mon Jan 08 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- fix interoperation problems with communigate pro
- disable msa

* Thu Jan 04 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- update to (security release) 8.11.2
- build also on RHL 6.x #16061
- include smrsh man-page #17901
- use the "-f" flag for makemap to preserve case for virtusertable
  and userdb in /etc/mail/Makefile - suggested by Harald Hoyer
- fix /usr/doc -> usr/share/doc in docu #20611
- wrong path in sendmail.mc #20691
- tcp-wrapper support wasn't enabled correctly #21642
- do not expose user "root" when masquerading like in older releases #21643
- disable the VRFY and EXPN smtp commands #21801
- disable queue-runs for normal users (restrictqrun privacy flag)
- fix typo in sendmail.mc #21880, #22682
- disable daemon mode to see what needs fixing

* Mon Oct 02 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 8.11.1

* Fri Sep 08 2000 Nalin Dahyabhai <nalin@redhat.com>
- rebuild in new environment

* Tue Aug 22 2000 Nalin Dahyabhai <nalin@redhat.com>
- apply fixes for LDAP maps being closed too soon

* Mon Aug 14 2000 Nalin Dahyabhai <nalin@redhat.com>
- provide /usr/lib/sasl/Sendmail.conf so that people know we can use it (#16064)

* Mon Aug  7 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- enable listening on the smtp port again

* Fri Aug  4 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix "missing find_m4.sh" problem by defining M4=/usr/bin/m4 (#14767)

* Mon Jul 31 2000 Nalin Dahyabhai <nalin@redhat.com>
- okay, enable LDAP support again
- enable SMTP auth support via Cyrus SASL

* Tue Jul 25 2000 Nalin Dahyabhai <nalin@redhat.com>
- disable the LDAP support until we can remove the sendmail->OpenLDAP->perl dep
- fix prereq

* Tue Jul 25 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- update to sendmail 8.11.0
- add LDAP support

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jul  9 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- require procmail
- add further aliases

* Sat Jul  8 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- prereq init.d
- fix typo

* Tue Jul  4 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- ignore error from useradd

* Fri Jun 30 2000 Than Ngo <than@redhat.de>
- FHS fixes
- /etc/rc.d/init.d -> /etc/init.d
- fix initscript

* Fri Jun 23 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- change to /usr/share/man

* Wed Jun 21 2000 Preston Brown <pbrown@redhat.com>
- turn off daemon behaviour by default

* Mon Jun 18 2000 Bill Nottingham <notting@redhat.com>
- rebuild, fix dependencies

* Sat Jun 10 2000 Bill Nottingham <notting@redhat.com>
- prereq /usr/sbin/useradd

* Fri May 19 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- enable MAP_REGEX
- enable tcp_wrapper support

* Thu May 18 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- fix etc/mail/aliases -> /etc/aliases in sendmail-redhat.mc

* Wed May  3 2000 Bill Nottingham <notting@redhat.com>
- update to 8.10.1
- fix build without sendmail installed
- add 'mailnull' user

* Wed Mar 15 2000 Bill Nottingham <notting@redhat.com>
- update to 8.10.0
- remove compatiblity chkconfig links
- add a mailnull user for sendmail to use

* Thu Feb 17 2000 Cristian Gafton <gafton@redhat.com>
- break the hard link for makemap and create it as a symlnk (#8223)

* Thu Feb 17 2000 Bernhard Rosenkränzer <bero@redhat.com>
- Fix location of mailertable (Bug #6035)

* Sat Feb  5 2000 Bill Nottingham <notting@redhat.com>
- fixes for non-root builds (#8178)

* Wed Feb  2 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- change perms on /etc/sysconfig/sendmail from 0755 to 0644
- allow compressed man-pages

* Thu Dec 02 1999 Cristian Gafton <gafton@redhat.com>
- add patch to prevent the DoS when rebuilding aliases

* Wed Sep  1 1999 Jeff Johnson <jbj@redhat.com>
- install man pages, not groff output (#3746).
- use dnl not '#' in m4 comment (#3749).
- add FEATURE(mailtertable) to the config -- example file needs this (#4649).
- use db2 not db1.

* Tue Aug 31 1999 Jeff Johnson <jbj@redhat.com>
- add 127.0.0.1 to /etc/mail/access to avoid IDENT: relay problem (#3178).

* Tue Aug 31 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in preun, not postun (#3982)

* Mon Aug 16 1999 Bill Nottingham <notting@redhat.com>
- initscript munging

* Fri Jul 02 1999 Cristian Gafton <gafton@redhat.com>
- fixed typo bug in comment in the default .mc file (#2812)

* Mon Apr 19 1999 Cristian Gafton <gafton@redhat.com>
- fox the awk scripts in the postinstall
- enable FEATURE(accept_unresolvable_domains) by default to make laptop
  users happy.

* Sun Apr 18 1999 Cristian Gafton <gafton@redhat.com>
- make the redhat.mc be a separate source files. Sanitize patches that used
  to touch it.
- install redhat.mc as /etc/sendmail.mc so that people can easily modify
  their sendmail.cf configurations.

* Mon Apr 05 1999 Cristian Gafton <gafton@redhat.com>
- fixed virtusertable patch
- make smrsh look into /etc/smrsh

* Mon Mar 29 1999 Jeff Johnson <jbj@redhat.com>
- remove noreplace attr from sednmail.cf.

* Thu Mar 25 1999 Cristian Gafton <gafton@redhat.com>
- provide a more sane /etc/mail/access default config file
- use makemap to initializa the empty databases, not touch
- added a small, but helpful /etc/mail/Makefile

* Mon Mar 22 1999 Jeff Johnson <jbj@redhat.com>
- correxct dangling symlinks.
- check for map file existence in %post.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 3)

* Fri Mar 19 1999 Jeff Johnson <jbj@redhat.com>
- improved 8.9.3 config from Mike McHenry <mmchen@minn.net>

* Tue Mar 16 1999 Cristian Gafton <gafton@redhat.com>
- version 8.9.3

* Tue Dec 29 1998 Cristian Gafton <gafton@redhat.com>
- build for 6.0
- use the libdb1 stuff correctly

* Mon Sep 21 1998 Michael K. Johnson <johnsonm@redhat.com>
- Allow empty QUEUE in /etc/sysconfig/sendmail for those who
  want to run sendmail in daemon mode without processing the
  queue regularly.

* Thu Sep 17 1998 Michael K. Johnson <johnsonm@redhat.com>
- /etc/sysconfig/sendmail

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sat May 02 1998 Cristian Gafton <gafton@redhat.com>
- enhanced initscripts

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- added a rmail patch

* Wed Oct 29 1997 Donnie Barnes <djb@redhat.com>
- argh!  Fixed some of the db1 handling that had to be added for glibc 2.1

* Fri Oct 24 1997 Donnie Barnes <djb@redhat.com>
- added support for db1 on SPARC

* Thu Oct 16 1997 Donnie Barnes <djb@redhat.com>
- added chkconfig support
- various spec file cleanups
- changed group to Networking/Daemons (from Daemons).  Sure, it runs on
  non networked systems, but who really *needs* it then?

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- made /etc/mail/deny.db a ghost
- removed preun that used to remove deny.db (ghost handles that now)
- NOTE: upgrading from the sendmail packages in 4.8, 4.8.1, and possibly
  4.9 (all Red Hat betas between 4.2 and 5.0) could cause problems.  You
  may need to do a makemap in /etc/mail and a newaliases after upgrading
  from those packages.  Upgrading from 4.2 or prior should be fine.

* Mon Oct 06 1997 Erik Troan <ewt@redhat.com>
- made aliases.db a ghost

* Tue Sep 23 1997 Donnie Barnes <djb@redhat.com>
- fixed preuninstall script to handle aliases.db on upgrades properly

* Mon Sep 15 1997 Donnie Barnes <djb@redhat.com>
- fixed post-install output and changed /var/spool/mqueue to 755

* Thu Sep 11 1997 Donnie Barnes <djb@redhat.com>
- fixed /usr/lib/sendmail-cf paths

* Tue Sep 09 1997 Donnie Barnes <djb@redhat.com>
- updated to 8.8.7
- added some spam filtration
- combined some makefile patches
- added BuildRoot support

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- marked initscript symlinks as missingok
- run newalises after creating /var/spool/mqueue

* Thu Jun 12 1997 Erik Troan <ewt@redhat.com>
- built against glibc, udated release to -6 (skipped -5!)

* Tue Apr 01 1997 Erik Troan <ewt@redhat.com>
- Added -nsl on the Alpha (for glibc to provide NIS functions).

* Mon Mar 03 1997 Erik Troan <ewt@redhat.com>
- Added nis support.
