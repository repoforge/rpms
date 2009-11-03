# $Id$
# Authority: dag

Summary: Database logging module for Apache
Name: mod_log_sql
Version: 1.100
Release: 1.2%{?dist}
License: Other
Group: System Environment/Daemons
URL: http://www.outoforder.cc/projects/apache/mod_log_sql/

Source: http://www.outoforder.cc/downloads/mod_log_sql/mod_log_sql-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: mysql-devel, httpd-devel
#BuildRequires: mod_ssl
Requires: httpd, mod_ssl

%description
mod_log_sql is a logging module for Apache that logs all requests
to a database.

%prep
%setup

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g;' configure Makefile.in

%{__cat} <<EOF >mod_log_sql.conf
### This is a very basic logging setup. I would HIGHLY recommend reading
### the documentation either at:
###
###	http://www.outoforder.cc/projects/apache/mod_log_sql/docs-2.0/

### You will need to create a database for your logs. It doesn't need
### to be on the local machine. You can log remotely. There is a
### create_tables.sql script in /usr/share/mod_log_sql-%{version}/contrib/ to
### generate this table for you if you like. You should also consider
### creating a user just for apache logs. This can be done using the
### commands below.

### mysql -u root -h <hostname> -p < create_tables.sql
### mysql> grant insert,create on apachelogs.* to
### loguser@my.apachemachine.com identified by 'l0gger';


### Uncomment the lines below to load mod_log_sql

#LoadModule log_sql_module modules/mod_log_sql.so
#LoadModule log_sql_mysql_module modules/mod_log_sql_mysql.so
#<IfModule mod_ssl.c>
#LoadModule log_sql_ssl_module modules/mod_log_sql_ssl.so
#</IfModule>


### Now we need to tell apache where to send the logs.

### For remote logging, use this line.
#LogSQLLoginInfo mysql://loguser:l0gg3r@dbmachine.foo.com/apachelogs
#LogSQLDBParam port 3306

### For logging to a database on localhost, use something like this.
#LogSQLDBParam socketfile /your/path/to/mysql.sock
#LogSQLCreateTables on


### From this point on, these settings belong in the appropriate
### virtual host config section.
#<VirtualHost 1.2.3.4>
# [snip]
# LogSQLTransferLogTable access_log
# LogSQLTransferLogFormat AbHhmRSsTUuv
# [snip]
#</VirtualHost>

### Additionally mod_log_sql can be directed to ignore certain requests
### For example:
### To ignore requests from a specific domain
#LogSQLRemhostIgnore example.com

### To ignore requests for specific files (good for ignoring viruses)
# LogSQLRequestIgnore root.exe cmd.exe default.ida

### To ignore specific types of files, match the extension.
# LogSQLRequestIgnore .gif .jpg
EOF

%build
%configure \
	--with-apxs="%{_sbindir}/apxs" \
	--with-ssl-inc="%{_includedir}/httpd"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 .libs/mod_log_sql.so %{buildroot}%{_libdir}/httpd/modules/mod_log_sql.so
%{__install} -Dp -m0755 .libs/mod_log_sql_mysql.so %{buildroot}%{_libdir}/httpd/modules/mod_log_sql_mysql.so
%{__install} -Dp -m0755 .libs/mod_log_sql_ssl.so %{buildroot}%{_libdir}/httpd/modules/mod_log_sql_ssl.so
%{__install} -Dp -m0644  mod_log_sql.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/mod_log_sql.conf


%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS CHANGELOG contrib/ docs/* INSTALL LICENSE TODO
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mod_log_sql.conf
%{_libdir}/httpd/modules/mod_log_sql.so
%{_libdir}/httpd/modules/mod_log_sql_mysql.so
%{_libdir}/httpd/modules/mod_log_sql_ssl.so

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.100-1.2
- Rebuild for Fedora Core 5.

* Thu Mar 03 2005 Jim Perrin <jperrin@gmail.com> - 1.100-1
- Initial Package.
