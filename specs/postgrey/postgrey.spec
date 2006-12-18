# $Id$
# Authority: matthias

%define confdir %{_sysconfdir}/postfix

Summary: Postfix Greylisting Policy Server
Name: postgrey
Version: 1.27
Release: 3
License: GPL
Group: System Environment/Daemons
Source0: http://isg.ee.ethz.ch/tools/postgrey/pub/postgrey-%{version}.tar.gz
Source1: postgrey.init
Source2: README-rpm
Patch0: postgrey-1.27-group.patch
URL: http://isg.ee.ethz.ch/tools/postgrey/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# We require postfix for its directories and gid
Requires: postfix
# This module seems to be a weak dependency from Net::Server, so we need to
# explicitly require it or it won't get installed.
Requires: perl(IO::Multiplex)
Requires(pre): /usr/sbin/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service, /sbin/chkconfig
Requires(postun): /sbin/service
BuildArch: noarch

%description
Postgrey is a Postfix policy server implementing greylisting.  When a request
for delivery of a mail is received by Postfix via SMTP, the triplet CLIENT_IP /
SENDER / RECIPIENT is built.  If it is the first time that this triplet is
seen, or if the triplet was first seen less than 5 minutes, then the mail gets
rejected with a temporary error. Hopefully spammers or viruses will not try
again later, as it is however required per RFC.


%prep
%setup
%patch0 -p1 -b .group
%{__install} -p -m 0644 %{SOURCE2} README-rpm


%build
# We only have perl scripts, so just "build" the man page
pod2man \
    --center="Postgrey Policy Server for Postfix" \
    --section="8" \
    postgrey > postgrey.8


%install
%{__rm} -rf %{buildroot}

# Configuration files
%{__mkdir_p} %{buildroot}%{confdir}
%{__install} -p -m 0644 postgrey_whitelist_{clients,recipients} \
    %{buildroot}%{confdir}/
touch %{buildroot}%{confdir}/postgrey_whitelist_clients.local

# Main script
%{__install} -D -p -m 0755 postgrey %{buildroot}%{_sbindir}/postgrey

# Spool directory
%{__mkdir_p} %{buildroot}%{_var}/spool/postfix/postgrey

# Init script
%{__install} -D -p -m 0755 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/rc.d/init.d/postgrey

# Man page
%{__install} -D -p -m 0644 postgrey.8 \
    %{buildroot}%{_mandir}/man8/postgrey.8

# Optional report script
%{__install} -D -p -m 0755 contrib/postgreyreport \
    %{buildroot}%{_sbindir}/postgreyreport


%clean
%{__rm} -rf %{buildroot}


%pre
/usr/sbin/useradd -d %{_var}/spool/postfix/postgrey -s /sbin/nologin \
    -M -r postgrey &>/dev/null || :

%post
/sbin/chkconfig --add postgrey

%preun
if [ $1 -eq 0 ]; then
    /sbin/service postgrey stop &>/dev/null || :
    /sbin/chkconfig --del postgrey
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service postgrey condrestart &>/dev/null || :
fi


%files
%defattr(-, root, root)
%doc Changes COPYING README README-rpm
%{_sysconfdir}/rc.d/init.d/postgrey
%config(noreplace) %{confdir}/postgrey_whitelist_clients
%config(noreplace) %{confdir}/postgrey_whitelist_recipients
%config(noreplace) %{confdir}/postgrey_whitelist_clients.local
%{_sbindir}/postgrey
%{_sbindir}/postgreyreport
%{_mandir}/man8/postgrey.8*
%dir %attr(0751, postgrey, postfix) %{_var}/spool/postfix/postgrey/


%changelog
* Mon Dec  4 2006 Matthias Saou <http://freshrpms.net/> 1.27-3
- Add man page generation (Mike Wohlgemuth).

* Fri Dec  1 2006 Matthias Saou <http://freshrpms.net/> 1.27-2
- Include postgreyreport script.

* Mon Nov  6 2006 Matthias Saou <http://freshrpms.net/> 1.27-1
- Spec file cleanup.

* Wed Jan 18 2006 Levente Farkas <lfarkas@lfarkas.org> 1.24
- some minor changes thanks to Peter Bieringer <pb@bieringer.de>

* Mon Jan 16 2006 Levente Farkas <lfarkas@lfarkas.org> 1.24
- upgrade to 1.24

* Sun Nov 13 2005 Levente Farkas <lfarkas@lfarkas.org> 1.22
- upgrade to 1.22

* Mon Aug 22 2005 Levente Farkas <lfarkas@lfarkas.org> 1.21
- spec file update from Luigi Iotti <luigi@iotti.biz>

* Thu Apr 28 2005 Levente Farkas <lfarkas@lfarkas.org> 1.21
- update to 1.21

* Tue Mar  8 2005 Levente Farkas <lfarkas@lfarkas.org> 1.18
- update to 1.18

* Tue Dec 14 2004 Levente Farkas <lfarkas@lfarkas.org> 1.17
- update to 1.17

* Wed Jul 14 2004 Levente Farkas <lfarkas@lfarkas.org> 1.14
- guard the pre and post scripts

* Wed Jul  7 2004 Levente Farkas <lfarkas@lfarkas.org> 1.13
- initial release 1.13
