# $Id: $
# Authority: ae
# vim: set expandtab tabstop=3:
# kate: tab-width 3; indent-width 3;
# TODO: make this relocatable
Summary: A set of PHP-scripts to manage MySQL over the web
Name: phpMyAdmin
Version: 2.10.2
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.phpmyadmin.net
Source0: http://dl.sf.net/phpmyadmin/%{name}-%{version}-all-languages.tar.bz2
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
%setup -q -n %{name}-%{version}-all-languages

%build


%install
%{__rm} -rf %{buildroot}

install -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

install -d -m755 $RPM_BUILD_ROOT%{_datadir}/%{name}/config

cp $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/config.default.php \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/config.inc.php

cat <<EOF >%{name}.conf
#
#  %{summary}
#

<Directory "%{_datadir}/%{name}">
  Order Deny,Allow
  Deny from all
  Allow from 127.0.0.1
</Directory>

Alias /%{name} %{_datadir}/%{name}
Alias /mysqladmin %{_datadir}/%{name}

EOF

install -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m644 %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
	chmod g+w $RPM_BUILD_ROOT%{_datadir}/%{name}/config
	chmod g+w $RPM_BUILD_ROOT%{_datadir}/%{name}/config.inc.php
fi


%files
%defattr(-,root,root)
%doc ChangeLog CREDITS Documentation.* INSTALL LICENSE README RELEASE-DATE*
%attr(755,root,apache) %{_datadir}/%{name}
%attr(640,root,apache) %config(noreplace) %{_datadir}/%{name}/config.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf


%changelog
* Sun Jun 17 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.10.2
- Updated to latest upstream version

* Tue Mar 6 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.10.0.2-1
- Updated to latest upstream version

* Tue Jan 16 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.2-1
- Updated to latest upstream version

* Tue Jan 16 2007 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.2-1
- Updated to latest upstream version

* Mon Nov 20 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.1.1-1
- Updated to latest upstream version

* Fri Nov 10 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.1-1
- Updated to latest upstream version

* Sun Nov 5 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.0.3-1
- Updated to latest upstream version

* Wed Oct 4 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.0.2-1
- Updated to latest upstream version

* Mon Oct 2 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.0.1-1
- Updated to latest upstream version

* Wed Sep 20 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.9.0-1
- Updated to latest upstream version

* Tue Aug 22 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.8.2.4-1
- Updated to latest upstream version

* Wed Aug 2 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.8.2.1-1
- Updated to latest upstream version

* Sun May 21 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.8.1-2
- Fixed an issue with the apache conf file

* Sat May 20 2006 Quien Sabe (aka Jim) <quien-sabe@metaorg.com> - 2.8.1-1
- Updated to lastest upstream version

* Fri Apr 7 2006 Jim Richardson <devlop@aidant.net> - 2.8.0.3-1
- Initial package.
