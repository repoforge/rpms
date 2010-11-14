# $Id$
# Authority: dag
# Upstream: Pedro L. Orso <orso$onda,com,br>
# Upstream: <orso$yahoogroups,com>
# Tag: rft

Summary: Squid usage report generator per user/ip/name
Name: sarg
Version: 2.3
Release: 2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://sarg.sourceforge.net/sarg.php

Source: http://downloads.sourceforge.net/project/sarg/sarg/sarg-%{version}/sarg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: gd-devel >= 1.8
BuildRequires: openldap-devel
Requires: bash
Requires: gd >= 1.8
Requires: squid
Obsoletes: sqmgrlog

%description
Squid Analysis Report Generator is a tool that allows you to view "where"
your users are going to on the Internet. Sarg generate reports in html
showing users, IP addresses, bytes, sites and times.

%prep
%setup

%{__chmod} u+wx sarg-php/locale/

%{__perl} -pi.orig -e '
        s|^#(access_log) (.+)$|#$1 $2\n$1 %{_localstatedir}/log/squid/access.log|;
        s|^#(output_dir) (.+)$|#$1 $2\n$1 %{_localstatedir}/www/sarg/ONE-SHOT|;
        s|^#(resolve_ip) (.+)$|#$1 $2\n$1 yes|;
        s|^#(show_successful_message) (.+)$|#$1 $2\n$1 no|;
        s|^#(mail_utility) (.+)$|#$1 $2\n$1 mail|;
        s|^#(external_css_file) (.+)$|#$1 $2\n$1 %{_localstatedir}/www/sarg/sarg.css|;
    ' sarg.conf

%{__cat} <<'EOF' >sarg.daily
#!/bin/bash

# Get yesterday's date
YESTERDAY=$(date --date "1 day ago" +%d/%m/%Y)

exec %{_bindir}/sarg \
    -o %{_localstatedir}/www/sarg/daily \
    -d $YESTERDAY &>/dev/null
exit 0
EOF

%{__cat} <<'EOF' >sarg.weekly
#!/bin/bash
LOG_FILES=
if [ -s %{_localstatedir}/log/squid/access.log.1.gz ]; then
    LOG_FILES="$LOG_FILES -l %{_localstatedir}/log/squid/access.log.1.gz"
fi
if [ -s %{_localstatedir}/log/squid/access.log ]; then
    LOG_FILES="$LOG_FILES -l %{_localstatedir}/log/squid/access.log"
fi

# Get yesterday's date
YESTERDAY=$(date --date "1 day ago" +%d/%m/%Y)

# Get one week ago date
WEEKAGO=$(date --date "7 days ago" +%d/%m/%Y)

exec %{_bindir}/sarg \
    $LOG_FILES \
    -o %{_localstatedir}/www/sarg/weekly \
    -d $WEEKAGO-$YESTERDAY &>/dev/null
exit 0
EOF

%{__cat} <<'EOF' >sarg.monthly
#!/bin/bash
LOG_FILES=
if [ -s %{_localstatedir}/log/squid/access.log.4.gz ]; then
    LOG_FILES="$LOG_FILES -l %{_localstatedir}/log/squid/access.log.4.gz"
fi
if [ -s %{_localstatedir}/log/squid/access.log.3.gz ]; then
    LOG_FILES="$LOG_FILES -l %{_localstatedir}/log/squid/access.log.3.gz"
fi
if [ -s %{_localstatedir}/log/squid/access.log.2.gz ]; then
    LOG_FILES="$LOG_FILES -l %{_localstatedir}/log/squid/access.log.2.gz"
fi
if [ -s %{_localstatedir}/log/squid/access.log.1.gz ]; then
    LOG_FILES="$LOG_FILES -l %{_localstatedir}/log/squid/access.log.1.gz"
fi
if [ -s %{_localstatedir}/log/squid/access.log ]; then
    LOG_FILES="$LOG_FILES -l %{_localstatedir}/log/squid/access.log"
fi

# Get yesterday's date
YESTERDAY=$(date --date "1 day ago" +%d/%m/%Y)

# Get 1 month ago date
MONTHAGO=$(date --date "1 month ago" +%d/%m/%Y)

exec %{_bindir}/sarg \
    $LOG_FILES \
    -o %{_localstatedir}/www/sarg/monthly \
    -d $MONTHAGO-$YESTERDAY &>/dev/null
exit 0
EOF

%{__cat} <<EOF >sarg-index.html
<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <title>Squid User's Access Report</title>
    <style type="text/css">
        #content         { width:20em; margin-left:auto; margin-right:auto; }
        h1               { color:green; font-size:1.2em; text-align:center; }
        table#reports    { border-collapse:collapse; width:20em; margin-left:auto; margin-right:auto; font-size:0.8em; }
        table#reports td { padding:2px; background-color:#f5f5dc; border:solid white 1px; }
        table#reports th { background-color:#feebcd; border:solid white 1px; color:#00008b; }
    </style>
</head>
<body>

<div id="content">
    <h1>Squid User's Access Report</h1>

    <table summary="" id="reports">
    <tbody>
    <tr>
        <th>DIRECTORY</th>
        <th>DESCRIPTION</th>
    </tr>
    <tr>
        <td><a href="ONE-SHOT/index.html">ONE-SHOT</a></td>
        <td>One shot reports</td>
    </tr>
    <tr>
        <td><a href="daily/index.html">daily</a></td>
        <td>Daily reports</td>
    </tr>
    <tr>
        <td><a href="weekly/index.html">weekly</a></td>
        <td>Weekly reports</td>
    </tr>
    <tr>
        <td><a href="monthly/index.html">monthly</a></td>
        <td>Monthly reports</td>
    </tr>
    </tbody>
    </table>
</div>
</body>
</html>
EOF

%{__cat} <<EOF >sarg-http.conf
Alias /sarg %{_localstatedir}/www/sarg

<Directory %{_localstatedir}/www/sarg>
    DirectoryIndex index.html
    Order deny,allow
    Deny from all
    Allow from 127.0.0.1
    Allow from ::1
    # Allow from your-workstation.com
</Directory>
EOF

%build
%configure \
    --enable-bindir=%{_bindir} \
    --enable-sysconfdir=%{_sysconfdir}/sarg \
    --enable-mandir=%{_mandir}/man1 \
    --enable-htmldir=%{_localstatedir}/www/sarg \
    --disable-rpath

%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 sarg %{buildroot}%{_bindir}/sarg
%{__install} -Dp -m0644 sarg.conf %{buildroot}%{_sysconfdir}/sarg/sarg.conf
%{__install} -Dp -m0644 exclude_codes %{buildroot}%{_sysconfdir}/sarg/exclude_codes
%{__install} -Dp -m0644 sarg.1 %{buildroot}%{_mandir}/man1/sarg.1

%{__install} -Dp -m0644 sarg-http.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/sarg.conf
%{__install} -Dp -m0755 sarg.daily %{buildroot}%{_sysconfdir}/cron.daily/sarg
%{__install} -Dp -m0755 sarg.weekly %{buildroot}%{_sysconfdir}/cron.weekly/sarg
%{__install} -Dp -m0755 sarg.monthly %{buildroot}%{_sysconfdir}/cron.monthly/sarg
%{__install} -Dp -m0644 sarg-index.html %{buildroot}%{_localstatedir}/www/sarg/index.html
%{__install} -Dp -m0644 css.tpl %{buildroot}%{_localstatedir}/www/sarg/sarg.css

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/sarg/{ONE-SHOT,daily,weekly,monthly}/
%{__cp} -av fonts/ images/ languages/ %{buildroot}%{_sysconfdir}/sarg/

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_sysconfdir}/sarg/languages/.new

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog CONTRIBUTORS COPYING DONATIONS README
%doc %{_mandir}/man1/sarg.1*
%dir %{_sysconfdir}/sarg/
%config %{_sysconfdir}/sarg/exclude_codes
%config(noreplace) %{_sysconfdir}/sarg/sarg.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/sarg.conf
%config %{_sysconfdir}/cron.daily/sarg
%config %{_sysconfdir}/cron.weekly/sarg
%config %{_sysconfdir}/cron.monthly/sarg
%{_bindir}/sarg
%{_localstatedir}/www/sarg/
%{_sysconfdir}/sarg/fonts/
%{_sysconfdir}/sarg/images/
%{_sysconfdir}/sarg/languages/

%changelog
* Tue Jun 22 2010 Christoph Maser <cmaser@gmx.de> - 2.3-2
- Build with ldap support.

* Tue Jun 22 2010 Christoph Maser <cmaser@gmx.de> - 2.3-1
- Updated to version 2.3.

* Thu Jun 19 2008 Dries Verachtert <dries@ulyssis.org> - 2.2.5-1
- Updated to release 2.2.5.

* Sat Aug 25 2007 Dag Wieers <dag@wieers.com> - 2.2.3.1-1
- Updated to release 2.2.3.1.

* Sat Aug 25 2007 Dag Wieers <dag@wieers.com> - 2.2.3-1
- Updated to release 2.2.3.
- Fixed typo in monthly script. (Rabie Van der Merwe)

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 2.2.1-1
- Updated to release 2.2.1.
- Many changes to reflect release 2.2. (Bernard Lheureux)

* Wed Aug 04 2004 Dag Wieers <dag@wieers.com> - 1.4.1-5
- Fixed ugly bug in weekly and monthly cron entries. (Viktor Zoubkov)

* Wed Jun 30 2004 Dag Wieers <dag@wieers.com> - 1.4.1-4
- Fixed default mail_utility. (John Florian)

* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 1.4.1-3
- Fixed problem with inline cron-scripts. (Luigi Iotti)

* Tue Apr 06 2004 Dag Wieers <dag@wieers.com> - 1.4.1-2
- Fixed missing directories in sarg. (William Hooper)

* Wed Mar 17 2004 Dag Wieers <dag@wieers.com> - 1.4.1-1
- Initial package. (using DAR)
