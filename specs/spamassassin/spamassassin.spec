# $Id$
# Authority: dag

### EL6 ships with spamassassin-3.3.1-2.el6
%{?el6:# Tag: rfx}
### EL5 ships with spamassassin-3.2.5-1.el5
%{?el5:# Tag: rfx}
### EL4 ships with spamassassin-3.2.4-1.el4.1
%{?el4:# Tag: rfx}
### EL3 ships with spamassassin-2.55-3.4
%{?el3:# Tag: rfx}
# ExclusiveDist: el2 el3 el4 el5 el6

%{?el2:%define _with_perl_5_6 1}

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SpamAssassin

Summary: Spam filter for email which can be invoked from mail delivery agents
Name: spamassassin
Version: 3.3.2
Release: 4%{?dist}
License: Apache License
Group: Applications/Internet
URL: http://spamassassin.apache.org/

Source: http://www.apache.org/dist/spamassassin/source/Mail-SpamAssassin-%{version}.tar.bz2
Source99: filter-requires-spamassassin.sh
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: openssl-devel
%{?el6:BuildRequires: perl-devel}
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(HTML::Parser) >= 3.24
BuildRequires: perl(Net::DNS)
BuildRequires: perl(NetAddr::IP) >= 4.000
BuildRequires: perl(Time::HiRes)

Requires: gcc
Requires: gnupg
Requires: perl(Archive::Tar) >= 1.23
Requires: perl(DB_File)
Requires: perl(Encode::Detect)
Requires: perl(HTTP::Date)
Requires: perl(IO::Zlib)
Requires: perl(IO::Socket::SSL)
Requires: perl(IP::Country)
Requires: perl(LWP::UserAgent)
Requires: perl(Mail::SPF)
Requires: perl(Mail::DKIM) >= 0.37
Requires: perl(Net::DNS)
Requires: perl(Net::Ident)
Requires: perl(NetAddr::IP) >= 4.000
Requires: perl(Razor2::Client::Agent) >= 2.61
Requires: perl(Time::HiRes)
Requires: perl-libwww-perl
Requires: procmail
Requires: re2c
Requires: /sbin/chkconfig
Requires: /sbin/service

Obsoletes: perl-Mail-SpamAssassin <= %{version}-%{release}
Obsoletes: spamassassin-tools <= %{version}-%{release}

Conflicts: amavisd-new < 2.6.2

%define __find_requires %{SOURCE99}

%description
SpamAssassin provides you with a way to reduce if not completely eliminate
Unsolicited Commercial Email (spam) from your incoming email.  It can
be invoked by a MDA such as sendmail or postfix, or can be called from
a procmail script, .forward file, etc.  It uses a genetic-algorithm
evolved scoring system to identify messages which look spammy, then
adds headers to the message so they can be filtered by the user's mail
reading software.  This distribution includes the spamd/spamc components
which create a server that considerably speeds processing of mail.

To enable spamassassin, if you are receiving mail locally, simply add
this line to your ~/.procmailrc:
INCLUDERC=/etc/mail/spamassassin/spamassassin-default.rc

To filter spam for all users, add that line to /etc/procmailrc
(creating if necessary).

%prep
%setup -n %{real_name}-%{version}

%{__cat} <<EOF >local.cf        ### SOURCE2
# These values can be overridden by editing ~/.spamassassin/user_prefs.cf
# (see spamassassin(1) for details)

# These should be safe assumptions and allow for simple visual sifting
# without risking lost emails.

required_hits 5
report_safe 0
rewrite_header Subject [SPAM]
EOF

%{__cat} <<EOF >spamassassin-default.rc ### SOURCE3
### send mail through spamassassin
:0fw
| /usr/bin/spamassassin
EOF

%{__cat} <<EOF >spamassassin-spamc.rc   ### SOURCE4
# send mail through spamassassin
:0fw
| /usr/bin/spamc
EOF

%{__cat} <<EOF >spamassassin.sysconfig      ### SOURCE5
# Options to spamd
SPAMDOPTIONS="-d -c -m5 -H"
EOF

%{__cat} <<EOF >sa-update.logrotate     ### SOURCE 6
/var/log/sa-update.log {
    monthly
    notifempty
    missingok
}
EOF

%{__cat} <<EOF >sa-update.crontab       ### SOURCE 7
### OPTIONAL: Spamassassin Rules Updates ###
#
# http://wiki.apache.org/spamassassin/RuleUpdates
# Highly recommended that you read the documentation before using this.
# ENABLE UPDATES AT YOUR OWN RISK.
#
# /var/log/sa-update.log contains a history log of sa-update runs

#10 4 * * * root /usr/share/spamassassin/sa-update.cron 2>&1 | tee -a /var/log/sa-update.log
EOF

%{__cat} <<'EOF' >sa-update.cronscript      ### SOURCE 8
#!/bin/bash

sleep $(expr $RANDOM % 7200)
# Only restart spamd if sa-update returns 0, meaning it updated the rules
/usr/bin/sa-update && /etc/init.d/spamassassin condrestart > /dev/null
EOF

%{__cat} <<EOF >spamassassin-helper.sh      ### SOURCE10
#!/bin/sh
/usr/bin/spamassassin -e
EOF

%build
export CFLAGS="%{optflags} -I/usr/kerberos/include"
%{__perl} Makefile.PL \
%{!?_with_perl_5_6:DESTDIR="%{buildroot}"} \
        SYSCONFDIR="%{_sysconfdir}" \
        INSTALLDIRS="vendor" \
        ENABLE_SSL="yes" </dev/null
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags} spamc/libspamc.so LIBS="-ldl %{optflags} -fPIC"

%install
%{__rm} -rf %{buildroot}
%makeinstall \
    PREFIX="%{buildroot}%{_prefix}" \
    INSTALLMAN1DIR="%{buildroot}%{_mandir}/man1" \
    INSTALLMAN3DIR="%{buildroot}%{_mandir}/man3" \
    LOCAL_RULES_DIR="%{buildroot}%{_sysconfdir}/mail/spamassassin"

%{__install} -Dp -m0755 spamd/redhat-rc-script.sh %{buildroot}%{_initrddir}/spamassassin
%{__install} -Dp -m0644 spamc/libspamc.so %{buildroot}%{_libdir}/libspamc.so
%{__install} -Dp -m0644 spamc/libspamc.h %{buildroot}%{_includedir}/libspamc.h

%{__install} -Dp -m0644 local.cf %{buildroot}%{_sysconfdir}/mail/spamassassin/local.cf
%{__install} -Dp -m0644 spamassassin.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/spamassassin
%{__install} -Dp -m0644 spamassassin-default.rc %{buildroot}%{_sysconfdir}/mail/spamassassin/spamassassin-default.rc
%{__install} -Dp -m0644 spamassassin-spamc.rc %{buildroot}%{_sysconfdir}/mail/spamassassin/spamassassin-spamc.rc
%{__install} -Dp -m0644 spamassassin-helper.sh %{buildroot}%{_sysconfdir}/mail/spamassassin/spamassassin-helper.sh
%{__install} -Dp -m0644 sa-update.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/sa-update
%{__install} -Dp -m0600 sa-update.crontab %{buildroot}%{_sysconfdir}/cron.d/sa-update
%{__install} -Dp -m0744 sa-update.cronscript %{buildroot}%{_datadir}/spamassassin/sa-update.cron

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/lib/spamassassin/
%{__install} -d -m0755 %{buildroot}%{_localstatedir}/run/spamassassin/

### Allows stripping of binaries
%{__chmod} 755 %{buildroot}%{_bindir}/*

### Disable find-requires for documentation
find ldap/ sql/ -type f -exec %{__chmod} -x {} \;

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -rf %{buildroot}%{perl_vendorarch}

%post
/sbin/chkconfig --add spamassassin

# -a and --auto-whitelist options were removed from 3.0.0
# prevent service startup failure
TMPFILE=$(/bin/mktemp /etc/sysconfig/spamassassin.XXXXXX) || exit 1
cp /etc/sysconfig/spamassassin $TMPFILE
perl -p -i -e 's/(["\s]-\w+)a/$1/ ; s/(["\s]-)a(\w+)/$1$2/ ; s/(["\s])-a\b/$1/' $TMPFILE
perl -p -i -e 's/ --auto-whitelist//' $TMPFILE
# replace /etc/sysconfig/spamassassin only if it actually changed
cmp /etc/sysconfig/spamassassin $TMPFILE || cp $TMPFILE /etc/sysconfig/spamassassin
rm $TMPFILE

if [ -f %{_sysconfdir}/spamassassin.cf ]; then
    %{__mv} -f %{_sysconfdir}/spamassassin.cf %{_sysconfdir}/mail/spamassassin/migrated.cf
fi

if [ -f %{_sysconfdir}/mail/spamassassin.cf ]; then
    %{__mv} -f %{_sysconfdir}/mail/spamassassin.cf %{_sysconfdir}/mail/spamassassin/migrated.cf
fi

%preun
if [ $1 -eq 0 ]; then
        /sbin/service spamassassin stop &>/dev/null || :
        /sbin/chkconfig --del spamassassin
fi

%postun
if [ $1 -ne 0 ]; then
    /sbin/service spamassassin condrestart &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes CREDITS LICENSE NOTICE PACKAGING README TRADEMARK UPGRADE USAGE
%doc *.txt spamc/README.qmail ldap/ sql/
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3pm*
%config %{_initrddir}/spamassassin
%config(noreplace) %{_sysconfdir}/cron.d/sa-update
%config(noreplace) %{_sysconfdir}/logrotate.d/sa-update
%config(noreplace) %{_sysconfdir}/mail/spamassassin/
%config(noreplace) %{_sysconfdir}/sysconfig/spamassassin
%dir %{_sysconfdir}/mail
%dir %{_datadir}/spamassassin/
%dir %{_localstatedir}/lib/spamassassin/
%dir %{_localstatedir}/run/spamassassin/
%{_bindir}/*
%{_datadir}/spamassassin/
%{_includedir}/libspamc.h
%{_libdir}/libspamc.so
%{perl_vendorlib}/Mail/
%{perl_vendorlib}/spamassassin-run.pod

%changelog
* Sat Jan 21 2012 David Hrbáč <david@hrbac.cz> - FIXME
- another enable for EL6 build

* Tue Jan 17 2012 David Hrbáč <david@hrbac.cz> - 3.3.2-3
- enable EL6 build

* Fri Jul 29 2011 Yury V. Zaytsev <yury@shurup.com> - 3.3.2-2
- Fixed file permissions to allow for stripping debuginfo. (Philip J. Perry)
- Spamassassin now owns the /etc/mail dir. (Philip J. Perry)
- Tagged RFX on RHEL6.

* Wed Jun 22 2011 David Hrbáč <david@hrbac.cz> - 3.3.2-1
- New upstream release.

* Mon Mar 22 2010 Steve Huff <shuff@vecna.org> - 3.3.1-3
- Don't install concurrently with amavisd-new < 2.6.2
  (https://issues.apache.org/SpamAssassin/show_bug.cgi?id=6257)

* Mon Mar 22 2010 Dag Wieers <dag@wieers.com> -  3.3.1-2
- Fixed incorrect dependency for perl-Razor2. (Steve Huff)

* Sun Mar 21 2010 Dag Wieers <dag@wieers.com> - 3.3.1-1
- Updated to release 3.3.1.

* Thu Oct 29 2009 David Hrbáč <david@hrbac.cz> - 3.2.5-2
- Updated requires to satisfy sa-compile and sa-update

* Thu Jun 19 2008 Dries Verachtert <dries@ulyssis.org> - 3.2.5-1
- Updated to release 3.2.5.

* Tue Jan 08 2008 Dag Wieers <dag@wieers.com> - 3.2.4-1
- Updated to release 3.2.4.

* Sat Aug 11 2007 Dag Wieers <dag@wieers.com> - 3.2.3-1
- Updated to release 3.2.3.

* Wed Jul 25 2007 Dag Wieers <dag@wieers.com> - 3.2.2-1
- Updated to release 3.2.2.

* Wed Jun 13 2007 Dag Wieers <dag@wieers.com> - 3.2.1-1
- Updated to release 3.2.1.

* Wed May 02 2007 Dag Wieers <dag@wieers.com> - 3.2.0-1
- Updated to release 3.2.0.

* Fri Feb 16 2007 Dag Wieers <dag@wieers.com> - 3.1.8-1
- Updated to release 3.1.8.

* Mon Dec 18 2006 Dag Wieers <dag@wieers.com> - 3.1.7-2
- Added missing perl dependencies for sa-update. (Pekka Savola)

* Wed Oct 11 2006 Dag Wieers <dag@wieers.com> - 3.1.7-1
- Updated to release 3.1.7.

* Thu Aug 31 2006 Dag Wieers <dag@wieers.com> - 3.1.5-1
- Updated to release 3.1.5.

* Thu Jul 27 2006 Dag Wieers <dag@wieers.com> - 3.1.4-1
- Updated to release 3.1.4.

* Fri Jun 16 2006 Dag Wieers <dag@wieers.com> - 3.1.3-1
- Updated to release 3.1.3.

* Sun May 28 2006 Dag Wieers <dag@wieers.com> - 3.1.2-1
- Updated to release 3.1.2.

* Sun Mar 12 2006 Dag Wieers <dag@wieers.com> - 3.1.1-1
- Added -I/usr/kerberos/include to CFLAGS to build on RH9 and EL3. (Michael Schout)
- Updated to release 3.1.1.

* Wed Jan 11 2006 Dag Wieers <dag@wieers.com> - 3.1.0-1
- Updated to release 3.1.0.

* Sat Aug 20 2005 Dag Wieers <dag@wieers.com> - 3.0.4-1
- Updated to release 3.0.4.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 3.0.3-1
- Updated to release 3.0.3.

* Thu Mar 31 2005 Dag Wieers <dag@wieers.com> - 3.0.2-2
- Removed accidental %%{buildroot} from scripts. (Robert Evans)
- Reinserted perl(Mail::SpamAssassin) provides. (Josh Kelley)

* Fri Mar 25 2005 Dag Wieers <dag@wieers.com> - 3.0.2-1
- Updated to release 3.0.2.

* Sun Aug 08 2004 Dag Wieers <dag@wieers.com> - 2.64-2
- Cosmetic changes.

* Thu Aug 05 2004 Dag Wieers <dag@wieers.com> - 2.64-1
- Updated to release 2.64.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 2.63-1
- Merge spamassassin and perl-Mail-SpamAssassin.

* Sat Jan 31 2004 Dag Wieers <dag@wieers.com> - 2.63-0
- Updated to release 2.63.

* Sun Jan 18 2004 Dag Wieers <dag@wieers.com> - 2.62-0
- Updated to release 2.62.
- Added missing BuildRequires. (Dries Verachtert)

* Sat Dec 13 2003 Dag Wieers <dag@wieers.com> - 2.61-1
- Added specific Red Hat procmail changes. (John Mellor)

* Tue Dec 09 2003 Dag Wieers <dag@wieers.com> - 2.61-0
- Updated to release 2.61.

* Wed Sep 24 2003 Dag Wieers <dag@wieers.com> - 2.60-0
- Updated to release 2.60.

* Sun Jun 15 2003 Dag Wieers <dag@wieers.com> - 2.55-2
- Removed the runaway perllocal.pod. (Koenraad Heijlen)

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.55-1
- Added DarBuildArchs to work-around the noarch-subpackage.

* Tue May 20 2003 Dag Wieers <dag@wieers.com> - 2.55-0
- Updated to release 2.55.

* Tue May 13 2003 Dag Wieers <dag@wieers.com> - 2.54-0
- Updated to release 2.54.

* Fri Apr 04 2003 Dag Wieers <dag@wieers.com> - 2.53-0
- Updated to release 2.53.

* Tue Mar 25 2003 Dag Wieers <dag@wieers.com> - 2.52-0
- Updated to release 2.52.

* Fri Mar 21 2003 Dag Wieers <dag@wieers.com> - 2.51-0
- Updated to release 2.51.

* Thu Feb 20 2003 Dag Wieers <dag@wieers.com> - 2.50-0
- Updated to release 2.50.

* Fri Feb  7 2003 Dag Wieers <dag@wieers.com> - 2.44-0
- Updated to release 2.44.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com> - 2.43-0
- Initial package. (using DAR)
