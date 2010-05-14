# $Id$
# Authority: matthias

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

Summary: PECL package to save sessions to a MySQL database
Name: php-pecl-session_mysql
Version: 1.9
Release: 2%{?dist}
License: MIT/Beerware
Group: Development/Languages
URL: http://websupport.sk/~stanojr/projects/session_mysql/
Source: http://websupport.sk/~stanojr/projects/session_mysql/session_mysql-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: php, php-mysql
BuildRequires: php, php-devel, mysql-devel
# Required by phpize
BuildRequires: autoconf, automake, libtool, gcc-c++

Provides: php-pecl(session_mysql) = %{version}-%{release}

%description
MySQL session save handler for php.


%prep
%setup -n session_mysql-%{version}


%build
# Workaround for broken old phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
# Workaround... strange issue seen on RHEL4 i386 at least
%{__perl} -pi -e 's|PHP_SESSIONMYSQL|PHP_SESSION_MYSQL|g' configure
%configure --with-mysql=%{_prefix}
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/session_mysql.ini << 'EOF'
; Enable MySQL session extension module
; To actually make use of it, you will need to edit the main php.ini :
; session.save_handler = mysql
extension=session_mysql.so

; Database details
; sock=
; host=localhost
; port=
; db=phpsession
; user=phpsession
; pass=phpsession
session_mysql.db = "host=localhost db=phpsession user=phpsession pass=phpsession"

; When inserting, retreiving and deleting session from database, add a check
; for $_SERVER['SERVER_NAME']
; This disables potential security problem (when used in mass virtualhosting),
; because users cannot read and edit session for other domains.
; $_SERVER['SERVER_NAME'] is copied to local variable before script is executed
; so when users change $_SERVER['SERVER_NAME'] variable, it does not hurt.
session_mysql.hostcheck = 1

; Remove "www." if exist from $_SERVER['SERVER_NAME'], so the same session will
; work on www.example.com and example.com.
session_mysql.hostcheck_removewww = 1

; Use persistent connection to MySQL (every httpd process will use one).
session_mysql.persistent = 1

; Remove sessions older than x seconds when GC (garbage collector) is woken up
session_mysql.gc_maxlifetime = 21600

; Locking support via GET_LOCK()/RELEASE_LOCK().
session_mysql.locking = 1

; Lock timeout, defaults to 5 seconds
session_mysql.lock_timeout = 5

; When set to 1, return always SUCCESSFUL
session_mysql.quiet = 0

; OTHER USEFUL OPTIONS (to change in the main php.ini!)
; session.save_handler - must be set to "mysql"
; session.gc_probability = 1
; session.gc_divisor     = 100
;   Define the probability that the 'garbage collection' process is started
;   on every session initialization.
;   The probability is calculated by using gc_probability/gc_divisor,
;   e.g. 1/100 means there is a 1% chance that the GC process starts
;   on each request.
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc LICENCE README
%config(noreplace) %{_sysconfdir}/php.d/session_mysql.ini
%{php_extdir}/session_mysql.so


%changelog
* Fri May 14 2010 Steve Huff <shuff@vecna.org> - 1.9-2
- Added Provides: to conform to upstream standards.

* Fri Jan 12 2007 Matthias Saou <http://freshrpms.net/> 1.9-1
- Update to 1.9.

* Thu May  4 2006 Matthias Saou <http://freshrpms.net/> 1.8-1
- Initial RPM release.

