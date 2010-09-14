# $Id$
# Authority: shuff
# Upstream: https://issues.apache.org/jira/browse/COUCHDB

%define real_name apache-couchdb
%define curl_version 7.21.1

Summary: A document database server, accessible via a RESTful JSON API
Name: couchdb
Version: 1.0.1
Release: 2%{?dist}
License: Apache
Group: Applications/Databases
URL: http://couchdb.apache.org/

Source0: http://mirror.cloudera.com/apache/couchdb/%{version}/apache-couchdb-%{version}.tar.gz
Source1: http://curl.haxx.se/download/curl-%{curl_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# Buildarch: noarch
#BuildRequires: autoconf >= 2.69
BuildRequires: autoconf
BuildRequires: automake >= 1.6.3
BuildRequires: erlang
BuildRequires: gcc
BuildRequires: js-devel >= 1.7
BuildRequires: libicu-devel >= 3.0
BuildRequires: libtool
BuildRequires: make
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: which
BuildRequires: rpm-macros-rpmforge
Requires: erlang
Requires: initscripts
Requires: logrotate

# for curl
BuildRequires: gnutls-devel
BuildRequires: krb5-devel
BuildRequires: libidn-devel
BuildRequires: libssh2-devel
BuildRequires: nss-devel
BuildRequires: openldap-devel
BuildRequires: zlib-devel

%description
Apache CouchDB is a document-oriented database that can be queried and indexed
in a MapReduce fashion using JavaScript. CouchDB also offers incremental
replication with bi-directional conflict detection and resolution.

CouchDB provides a RESTful JSON API than can be accessed from any environment
that allows HTTP requests. There are myriad third-party client libraries that
make this even easier from your programming language of choice. CouchDB’s built
in Web administration console speaks directly to the database using HTTP
requests issued from your browser.

%prep
%setup -n %{real_name}-%{version}
%setup -n %{real_name}-%{version} -T -D -a 1

%build
#### First, make a local curl
pushd curl-%{curl_version}
RESULT_DIR=`pwd`/result

./configure \
    --disable-dependency-tracking \
    --disable-shared \
    --enable-static \
    --prefix="$RESULT_DIR" \
    --libdir="$RESULT_DIR/usr/%{_lib}"

%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" install
popd



### Now, make couchdb
export PKG_CONFIG_PATH="$RESULT_DIR/usr/%{_lib}/pkgconfig:$PKG_CONFIG_PATH"
export PATH="$RESULT_DIR/bin:$PATH"
%configure \
    --disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

# put the init script in the right place
%{__install} -m755 -d %{buildroot}%{_initrddir}
%{__mv} %{buildroot}%{_sysconfdir}/rc.d/couchdb %{buildroot}%{_initrddir}

# make a homedir for the admin user
%{__install} -m2750 -d %{buildroot}%{_var}/lib/couchdb

# make a log directory
%{__install} -m2750 -d %{buildroot}%{_var}/log/couchdb

%pre
if [ $1 == 1 ]; then
    /usr/sbin/useradd -r --home %{_var}/lib/couchdb -M --shell /bin/bash --comment "CouchDB Administrator" couchdb >/dev/null 2>&1
fi

%post
if [ $1 == 1 ]; then
    /sbin/chkconfig --add couchdb >/dev/null 2>&1
fi

%preun
if [ $1 == 0 ]; then
    /sbin/chkconfig --del couchdb >/dev/null 2>&1
fi

%postun
if [ $1 == 0 ]; then
    /usr/sbin/userdel couchdb >/dev/null 2>&1
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS CHANGES DEVELOPERS INSTALL INSTALL.Unix LICENSE
%doc NEWS NOTICE README THANKS
%exclude %{_docdir}/couchdb/
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/couchdb/
%{_initrddir}/couchdb/
%{_libdir}/couchdb/
%attr(-, couchdb, couchdb) %dir %{_sysconfdir}/couchdb/
%attr(-, couchdb, couchdb) %{_sysconfdir}/couchdb/default.ini
%attr(-, couchdb, couchdb) %config(noreplace) %{_sysconfdir}/couchdb/local.ini
%{_sysconfdir}/default/couchdb
%{_sysconfdir}/logrotate.d/couchdb
%attr(-, couchdb, couchdb) %dir %{_var}/lib/couchdb
%attr(-, couchdb, couchdb) %dir %{_var}/log/couchdb

%changelog
* Tue Sep 14 2010 Steve Huff <shuff@vecna.org> - 1.0.1-2
- Oops, forgot the dependency on Erlang :(

* Mon Aug 30 2010 Steve Huff <shuff@vecna.org> - 1.0.1-1
- Initial package.
- Static libcurl dependency satisfied by means of Zaytsev's Technique.
