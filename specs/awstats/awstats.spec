# $Id$
# Authority: dag

Summary: Powerful and fullfeatured server logfile analyzer
Name: awstats
Version: 6.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://awstats.sourceforge.net/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/awstats/awstats-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch

%description
Advanced Web Statistics is a powerful and featureful tool that generates
advanced web server graphic statistics. This server log analyzer works
from command line or as a CGI and shows you all information your log contains,
in graphical web pages. It can analyze a lot of web/wap/proxy servers like
Apache, IIS, Weblogic, Webstar, Squid, ... but also mail or ftp servers.

This program can measure visits, unique vistors, authenticated users, pages,
domains/countries, OS busiest times, robot visits, type of files, search
engines/keywords used, visits duration, HTTP errors and more...
Statistics can be updated from a browser or your scheduler.
The program also supports virtual servers, plugins and a lot of features.

%prep
%setup

### Commit permanent changes to default configuration
%{__perl} -pi.orig -e '
		s|^LogFile=.*$|LogFile="%{_localstatedir}/log/httpd/access_log"|;
		s|^DirData=.*$|DirData="%{_localstatedir}/www/awstats"|;
		s|^DirCgi=.*$|DirCgi="/awstats"|;
		s|^DirIcons=.*$|DirIcons="/awstats/icon"|;
		s|^SiteDomain=.*$|SiteDomain="localhost.localdomain"|;
		s|^HostAliases=.*$|HostAliases="localhost 127.0.0.1"|;
		s|^EnableLockForUpdate=.*$|EnableLockForUpdate=1|;
		s|^SaveDatabaseFilesWithPermissionsForEveryone=.*$|SaveDatabaseFilesWithPermissionsForEveryone=0|;
		s|^KeepBackupOfHistoricFiles=.*$|KeepBackupOfHistoricFiles=1|;
		s|^SkipHosts=.*$|SkipHosts="127.0.0.1$"|;
		s|^Expires=.*$|Expires=3600|;
		s|^FirstDayOfWeek=.*$|FirstDayOfWeek=0|;
		s|ShowLinksToWhoIs=.*$|ShowLinksToWhoIs=1|;
	' wwwroot/cgi-bin/awstats.model.conf

%{__cat} <<EOF >awstats.cron
#!/bin/bash

if [ -f %{_localstatedir}/log/httpd/access_log ] ; then
	exec %{_bindir}/awstats_updateall.pl now \
		-confdir="%{_sysconfdir}" \
		-awstatsprog="%{_localstatedir}/www/awstats/awstats.pl" >/dev/null
fi
exit 0
EOF

%{__cat} <<EOF >awstats.httpd
Alias /awstats/icon/ %{_localstatedir}/www/awstats/icon/

ScriptAlias /awstats/ %{_localstatedir}/www/awstats/
<Directory %{_localstatedir}/www/awstats/>
	DirectoryIndex awstats.pl
	Options ExecCGI
	order deny,allow
	deny from all
	allow from 127.0.0.1
</Directory>

#Alias /css/ %{_localstatedir}/www/awstats/css/
#Alias /js/ %{_localstatedir}/www/awstats/js/
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -D -m0644 wwwroot/cgi-bin/awstats.model.conf %{buildroot}%{_sysconfdir}/awstats/awstats.model.conf
%{__install} -D -m0644 wwwroot/cgi-bin/awstats.model.conf %{buildroot}%{_sysconfdir}/awstats/awstats.localhost.localdomain.conf
%{__install} -D -m0755 awstats.cron %{buildroot}%{_sysconfdir}/cron.hourly/00awstats
%{__install} -D -m0644 awstats.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/awstats.conf
%{__install} -D -m0755 tools/logresolvemerge.pl %{buildroot}%{_bindir}/logresolvemerge.pl
%{__install} -D -m0755 tools/awstats_buildstaticpages.pl %{buildroot}%{_bindir}/awstats_buildstaticpages.pl
%{__install} -D -m0755 tools/awstats_exportlib.pl %{buildroot}%{_bindir}/awstats_exportlib.pl
%{__install} -D -m0755 tools/awstats_updateall.pl %{buildroot}%{_bindir}/awstats_updateall.pl
%{__install} -D -m0755 tools/maillogconvert.pl %{buildroot}%{_bindir}/maillogconvert.pl
%{__install} -D -m0755 tools/urlaliasbuilder.pl %{buildroot}%{_bindir}/urlaliasbuilder.pl

%{__install} -D -m0755 wwwroot/cgi-bin/awstats.pl %{buildroot}%{_localstatedir}/www/awstats/awstats.pl
%{__install} -D -m0755 wwwroot/cgi-bin/awredir.pl %{buildroot}%{_localstatedir}/www/awstats/awredir.pl
%{__install} -D -m0644 wwwroot/classes/awgraphapplet.jar %{buildroot}%{_localstatedir}/www/awstats/classes/awgraphapplet.jar
%{__install} -D -m0644 wwwroot/js/awstats_misc_tracker.js %{buildroot}%{_localstatedir}/www/awstats/js/awstats_misc_tracker.js

%{__cp} -av wwwroot/{css,icon}/ %{buildroot}%{_localstatedir}/www/awstats/
%{__cp} -av wwwroot/cgi-bin/{lang,lib,plugins} %{buildroot}%{_localstatedir}/www/awstats/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README.TXT docs/*
%config(noreplace) %{_sysconfdir}/awstats/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*
%config %{_sysconfdir}/cron.hourly/*
%{_bindir}/*
%{_localstatedir}/www/awstats/

%changelog
* Sat Jun 19 2004 Dag Wieers <dag@wieers.com> - 6.1-1
- Updated to release 6.1.
- Added tooltips. (Eric Hopper)

* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 6.0-1
- Updated to release 6.0.

* Fri Sep 26 2003 Dag Wieers <dag@wieers.com> - 5.9-1
- Fixed missing icon/mime set. (Gerke Kok)

* Fri Sep 26 2003 Dag Wieers <dag@wieers.com> - 5.9-0
- Updated to release 5.9.

* Sun Aug 17 2003 Dag Wieers <dag@wieers.com> - 5.7-0
- Initial package. (using DAR)
