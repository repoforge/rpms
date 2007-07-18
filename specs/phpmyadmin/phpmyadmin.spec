# $Id: $
# Authority: jim

%define real_name phpMyAdmin

Summary: Web application to manage MySQL
Name: phpmyadmin
Version: 2.10.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.phpmyadmin.net/
Source: http://dl.sf.net/phpmyadmin/phpMyAdmin-%{version}-all-languages.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: php-mysql >= 4.1.0
Requires: webserver

%description
phpMyAdmin can manage a whole MySQL server (needs a super-user) as well as a
single database. To accomplish the latter you'll need a properly set up MySQL
user who can read/write only the desired database. It's up to you to look up
the appropriate part in the MySQL manual.

%prep
%setup -n %{real_name}-%{version}-all-languages

%{__cat} <<EOF >%{real_name}.conf
#
#  %{summary}
#

<Directory "%{_datadir}/%{real_name}">
  Order Deny,Allow
  Deny from all
  Allow from 127.0.0.1
</Directory>

Alias /%{real_name} %{_datadir}/%{real_name}
Alias /mysqladmin %{_datadir}/%{real_name}

EOF

ls *.{php,html,css,ico} | sed 's/^/\/usr\/share\/phpMyAdmin\//' > level1files.list

%build


%install
%{__rm} -rf %{buildroot}

%{__install} -d -m755 %{buildroot}%{_datadir}/%{real_name}
%{__cp} *.{php,html,css,ico} %{buildroot}%{_datadir}/%{real_name}
%{__cp} -a contrib css js lang libraries pmd scripts test themes %{buildroot}%{_datadir}/%{real_name}

%{__install} -d -m755 %{buildroot}%{_datadir}/%{real_name}/config

%{__cp} %{buildroot}%{_datadir}/%{real_name}/libraries/config.default.php \
	%{buildroot}%{_datadir}/%{real_name}/config.inc.php


%{__install} -d %{buildroot}%{_sysconfdir}/httpd/conf.d
%{__install} -m644 %{real_name}.conf %{buildroot}%{_sysconfdir}/httpd/conf.d

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
	chmod g+w %{_datadir}/%{real_name}/config
	chmod g+w %{_datadir}/%{real_name}/config.inc.php
fi


%files -f level1files.list
%defattr(-,root,root)
%doc ChangeLog CREDITS Documentation.* INSTALL LICENSE README RELEASE-DATE*
%{_datadir}/%{real_name}/contrib
%{_datadir}/%{real_name}/css
%{_datadir}/%{real_name}/js
%{_datadir}/%{real_name}/lang
%{_datadir}/%{real_name}/libraries
%{_datadir}/%{real_name}/pmd
%{_datadir}/%{real_name}/scripts
%{_datadir}/%{real_name}/test
%{_datadir}/%{real_name}/themes
%attr(640,root,apache) %config(noreplace) %{_datadir}/%{real_name}/config.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf


%changelog
* Sun Jun 17 2007 Jim <quien-sabe@metaorg.com> - 2.10.2
- Updated to latest upstream version

* Tue Mar 6 2007 Jim <quien-sabe@metaorg.com> - 2.10.0.2-1
- Updated to latest upstream version

* Tue Jan 16 2007 Jim <quien-sabe@metaorg.com> - 2.9.2-1
- Updated to latest upstream version

* Tue Jan 16 2007 Jim <quien-sabe@metaorg.com> - 2.9.2-1
- Updated to latest upstream version

* Mon Nov 20 2006 Jim <quien-sabe@metaorg.com> - 2.9.1.1-1
- Updated to latest upstream version

* Fri Nov 10 2006 Jim <quien-sabe@metaorg.com> - 2.9.1-1
- Updated to latest upstream version

* Sun Nov 5 2006 Jim <quien-sabe@metaorg.com> - 2.9.0.3-1
- Updated to latest upstream version

* Wed Oct 4 2006 Jim <quien-sabe@metaorg.com> - 2.9.0.2-1
- Updated to latest upstream version

* Mon Oct 2 2006 Jim <quien-sabe@metaorg.com> - 2.9.0.1-1
- Updated to latest upstream version

* Wed Sep 20 2006 Jim <quien-sabe@metaorg.com> - 2.9.0-1
- Updated to latest upstream version

* Tue Aug 22 2006 Jim <quien-sabe@metaorg.com> - 2.8.2.4-1
- Updated to latest upstream version

* Wed Aug 2 2006 Jim <quien-sabe@metaorg.com> - 2.8.2.1-1
- Updated to latest upstream version

* Sun May 21 2006 Jim <quien-sabe@metaorg.com> - 2.8.1-2
- Fixed an issue with the apache conf file

* Sat May 20 2006 Jim <quien-sabe@metaorg.com> - 2.8.1-1
- Updated to lastest upstream version

* Fri Apr 7 2006 Jim Richardson <devlop@aidant.net> - 2.8.0.3-1
- Initial package.
