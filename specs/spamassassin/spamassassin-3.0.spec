# $Id: spamassassin.spec 3306 2005-06-18 14:54:54Z dries $
# Authority: dag

%{?rh8:%define _with_perl_5_6 1}
%{?rh7:%define _with_perl_5_6 1}
%{?el2:%define _with_perl_5_6 1}

%define perl_vendorlib  %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch  %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Mail-SpamAssassin

Summary: Spam filter for email which can be invoked from mail delivery agents
Name: spamassassin
Version: 3.0.6
Release: 1%{?dist}
License: Apache License
Group: Applications/Internet
URL: http://spamassassin.apache.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.apache.org/dist/spamassassin/source/Mail-SpamAssassin-%{version}.tar.bz2
Source99: filter-requires-spamassassin.sh
Patch3: spamassassin-3.0.2-krb5-backcompat.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl(HTML::Parser), perl(Net::DNS), perl(Time::HiRes), openssl-devel
Requires: procmail, perl(Net::DNS), perl(Time::HiRes)
Requires: /sbin/chkconfig, /sbin/service
#Requires: perl(Mail::SpamAssassin) = %{version}-%{release}
Provides: perl(Mail::SpamAssassin) = %{version}-%{release}
Obsoletes: perl-Mail-SpamAssassin

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

%package tools
Summary: Miscellaneous tools and documentation for SpamAssassin
Group: System Environment/Daemons
Requires: perl(Mail::SpamAssassin) = %{version}

%description tools
Miscellaneous tools and documentation from various authors, distributed
with SpamAssassin. See /usr/share/doc/SpamAssassin-tools-*/.

%prep
%setup -n %{real_name}-%{version}
%patch3 -p0

%{__cat} <<EOF >local.cf		### SOURCE2
# These values can be overridden by editing ~/.spamassassin/user_prefs.cf 
# (see spamassassin(1) for details)

# These should be safe assumptions and allow for simple visual sifting
# without risking lost emails.

required_hits 5
report_safe 0
rewrite_header Subject [SPAM]
EOF

%{__cat} <<EOF >spamassassin-default.rc	### SOURCE3
### send mail through spamassassin
:0fw
| /usr/bin/spamassassin
EOF

%{__cat} <<EOF >spamassassin-spamc.rc	### SOURCE4
# send mail through spamassassin
:0fw
| /usr/bin/spamc
EOF

%{__cat} <<EOF >spamassassin.sysconfig		### SOURCE5
# Options to spamd
SPAMDOPTIONS="-d -c -m5 -H"
EOF

%{__cat} <<EOF >spamassassin-helper.sh		### SOURCE10
#!/bin/sh
/usr/bin/spamassassin -e
EOF

%build
export CFLAGS="%{optflags} -fPIC"
%{__perl} Makefile.PL \
%{!?_with_perl_5_6:DESTDIR="%{buildroot}"} \
		SYSCONFDIR="%{_sysconfdir}" \
		INSTALLDIRS="vendor" \
		ENABLE_SSL="yes" </dev/null
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags} -fPIC"
%{__make} %{?_smp_mflags} spamc/libspamc.so \
	LIBS="-ldl %{optflags} -fPIC"

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

### Disable find-requires for documentation
find contrib/ masses/ sql/ tools/ -type f -exec %{__chmod} -x {} \;

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib}
%{__rm} -rf %{buildroot}%{perl_vendorarch}

%post
if [ $1 -eq 1 ]; then
        /sbin/chkconfig --add spamassassin
fi

if [ -f %{_sysconfdir}/spamassassin.cf ]; then
	%{__mv} -f %{_sysconfdir}/spamassassin.cf %{_sysconfdir}/mail/spamassassin/migrated.cf
fi

if [ -f %{_sysconfdir}/mail/spamassassin.cf ]; then
	%{__mv} -f %{_sysconfdir}/mail/spamassassin.cf %{_sysconfdir}/mail/spamassassin/migrated.cf
fi

/sbin/service spamassassin condrestart &>/dev/null || :

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
%doc BUGS Changes CREDITS LICENSE NOTICE PACKAGING README STATUS TRADEMARK
%doc UPGRADE USAGE *.txt spamc/README.qmail
%doc %{_mandir}/man1/*.1*
%doc %{_mandir}/man3/*.3pm*
%config %{_initrddir}/spamassassin
%config(noreplace) %{_sysconfdir}/mail/spamassassin/
%config(noreplace) %{_sysconfdir}/sysconfig/spamassassin
%{_bindir}/*
%{_datadir}/spamassassin/
%{_libdir}/libspamc.so
%{perl_vendorlib}/Mail/
%{_includedir}/libspamc.h

%files tools
%defattr(0644, root, root, 0755)
%doc contrib/ masses/ sql/ tools/

%changelog
* Wed Jun 21 2006 Dag Wieers <dag@wieers.com> - 3.0.6-1
- Updated to release 3.0.6.

* Thu Dec 01 2005 Dag Wieers <dag@wieers.com> - 3.0.5-1
- Updated to release 3.0.5.

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
