# $Id$
# Authority: shuff
# Upstream: George Schollnagle <george$omniti.com>
# ExcludeDist: el2 el3

%define php_extdir %(php-config --extension-dir 2>/dev/null || echo %{_libdir}/php4)

%define real_name APC

Summary: APC is a PHP opcode cache
Name: php-pecl-apc
Version: 3.1.9
Release: 1%{?dist}
License: PHP
Group: Development/Languages
URL: http://pecl.php.net/package/APC
Source: http://pecl.php.net/get/APC-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: /usr/bin/iconv
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: pcre-devel
BuildRequires: php-devel >= 5.1.0
BuildRequires: php-pear
Requires: php >= 5.1.0

Provides: php-pecl(fileinfo) = %{version}-%{release}

# use only one PHP accelerator at a time
Conflicts: php-eaccelerator
Conflicts: php-xcache

%description
The Alternative PHP Cache (APC) is a free and open opcode cache for PHP. Its
goal is to provide a free, open, and robust framework for caching and
optimizing PHP intermediate code. 

%package devel
Summary: PHP includes for %{name}/
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the PHP header files for %{name}. If you like to develop
programs using %{name}, you will need to install %{name}-devel.

%prep
%setup -n %{real_name}-%{version}

%build
# Workaround for broken old phpize on 64 bits
%{__cat} %{_bindir}/phpize | sed 's|/lib/|/%{_lib}/|g' > phpize && sh phpize
%configure \
    --enable-apc-mmap \
    --with-php-config=%{_bindir}/php-config
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install INSTALL_ROOT=%{buildroot}

%{__install} -m0755 -Dp apc.php %{buildroot}%{_datadir}/%{name}/apc.php

# Fix the charset of NOTICE
iconv -f iso-8859-1 -t utf8 NOTICE >NOTICE.utf8
mv NOTICE.utf8 NOTICE

# Drop in the bit of configuration
%{__mkdir_p} %{buildroot}%{_sysconfdir}/php.d
%{__cat} > %{buildroot}%{_sysconfdir}/php.d/apc.ini << 'EOF'
; Enable apc extension module
extension = apc.so

; Options for the APC module version >= 3.1.3
; See http://www.php.net/manual/en/apc.configuration.php

; This can be set to 0 to disable APC. 
apc.enabled=1
; The number of shared memory segments to allocate for the compiler cache. 
apc.shm_segments=1
; The size of each shared memory segment, with M/G suffixe
apc.shm_size=64M
; A "hint" about the number of distinct source files that will be included or 
; requested on your web server. Set to zero or omit if you are not sure;
apc.num_files_hint=1024
; Just like num_files_hint, a "hint" about the number of distinct user cache
; variables to store.  Set to zero or omit if you are not sure;
apc.user_entries_hint=4096
; The number of seconds a cache entry is allowed to idle in a slot in case this
; cache entry slot is needed by another entry.
apc.ttl=7200
; use the SAPI request start time for TTL
apc.use_request_time=1
; The number of seconds a user cache entry is allowed to idle in a slot in case
; this cache entry slot is needed by another entry.
apc.user_ttl=7200
; The number of seconds that a cache entry may remain on the garbage-collection list. 
apc.gc_ttl=3600
; On by default, but can be set to off and used in conjunction with positive
; apc.filters so that files are only cached if matched by a positive filter.
apc.cache_by_default=1
; A comma-separated list of POSIX extended regular expressions.
apc.filters
; The mktemp-style file_mask to pass to the mmap module 
apc.mmap_file_mask=/tmp/apc.XXXXXX
; This file_update_protection setting puts a delay on caching brand new files.
apc.file_update_protection=2
; Setting this enables APC for the CLI version of PHP (Mostly for testing and debugging).
apc.enable_cli=0
; Prevents large files from being cached
apc.max_file_size=1M
; Whether to stat the main script file and the fullpath includes.
apc.stat=1
; Vertification with ctime will avoid problems caused by programs such as svn or rsync by making 
; sure inodes have not changed since the last stat. APC will normally only check mtime.
apc.stat_ctime=0
; Whether to canonicalize paths in stat=0 mode or fall back to stat behaviour
apc.canonicalize=0
; With write_lock enabled, only one process at a time will try to compile an 
; uncached script while the other processes will run uncached
apc.write_lock=1
; Logs any scripts that were automatically excluded from being cached due to early/late binding issues.
apc.report_autofilter=0
; RFC1867 File Upload Progress hook handler
apc.rfc1867=0
apc.rfc1867_prefix =upload_
apc.rfc1867_name=APC_UPLOAD_PROGRESS
apc.rfc1867_freq=0
apc.rfc1867_ttl=3600
; Optimize include_once and require_once calls and avoid the expensive system calls used.
apc.include_once_override=0
apc.lazy_classes=0
apc.lazy_functions=0
; Enables APC handling of signals, such as SIGSEGV, that write core files when signaled. 
; APC will attempt to unmap the shared memory segment in order to exclude it from the core file
apc.coredump_unmap=0
; Records a md5 hash of files. 
apc.file_md5=0
; not documented
apc.preload_path
EOF


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGELOG INSTALL LICENSE NOTICE TECHNOTES.txt TODO 
%config(noreplace) %{_sysconfdir}/php.d/apc.ini
%{_datadir}/%{name}/
%{php_extdir}/apc.so

%files devel
%{_includedir}/php/ext/apc

%changelog
* Wed Aug 31 2011 Steve Huff <shuff@vecna.org> - 3.1.9-1
- Initial package (ported from EPEL).
