# $Id$
# Authority: shuff
# Upstream: Yaron Minsky <yminsky$gmail.com>

Summary: SKS distributed OpenPGP keyserver
Name: sks-keyserver
Version: 1.1.3
Release: 1%{?dist}
License: GPL
Group: Applications/
URL: http://minsky-primus.homeip.net/sks/

Source: http://sks-keyserver.googlecode.com/files/sks-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: db4-devel
BuildRequires: make
BuildRequires: ocaml >= 3.10.2
BuildRequires: ocaml-camlp4 >= 3.10.2
BuildRequires: zlib-devel
BuildRequires: rpm-macros-rpmforge
Requires: db4

Provides: sks = %{version}

%description
SKS is an OpenPGP keyserver whose goal is to provide easy to deploy,
decentralized, and highly reliable synchronization. That means that a key
submitted to one SKS server will quickly be distributed to all key servers, and
even wildly out-of-date servers, or servers that experience spotty
connectivity, can fully synchronize with rest of the system.

%prep
%setup -n sks-%{version}

%{__cat} <<'MAKEFILE' >Makefile.local
BDBLIB=-L%{_libdir}
BDBINCLUDE=-I%{_includedir}
PREFIX=%{_usr}
LIBDB=-ldb
MANDIR=%{_mandir}
export BDBLIB
export BDBINCLUDE
export PREFIX
export LIBDB
export MANDIR
MAKEFILE

%{__cat} <<'CONF' >sksconf
# sks-keyserver config file

# base directory
basedir: %{_localstatedir}/sks

# write logs to local files
logfile: log

# set a reasonable debug level (max is 10)
debuglevel: 4

# set the hostname
#hostname: localhost.localdomain

# ports for hkp and recon services (default)
#hkp_port: 11371
#recon_port:11370

# set the email address we user for PKS sync
#from_addr: keysync@localhost.localdomain

# check the membership file every 6 hours (default)
#membership_reload_interval: 6
CONF

%{__cat} <<'MEMBERSHIP' >membership
# membership
#
# With SKS, two hosts can efficiently compare their databases then
# repair whatever differences are found.  In order to set up
# reconciliation, you first need to find other SKS servers that will
# agree to gossip with you. The hostname and port of the server that
# has agreed to do so should be added to this file.
#
# Empty lines and whitespace-only lines are ignored, as are lines
# whose first non-whitespace character is a `#'. Comments preceded by '#'
# are allowed at the ends of lines
#
# Example:
# keyserver.linux.it 11370
#
# The following operators have agreed to have their peering info included in this sample file.
# NOTE: This does NOT mean you may uncomment the lines and have peers. First you must contact the
# server owner and ask permission. You should include a line styled like these for your own server.
# Until two SKS membership files contain eact others peering info, they will not gossip.
#
#yourserver.example.net     11370   # Your full name <emailaddress>             0xPreferredPGPkey
#keyserver.gingerbear.net   11370   # John P. Clizbe <John@Gingerbear.net>      0xD6569825
#sks.keyservers.net         11370   # John P. Clizbe <John@Gingerbear.net>      0xD6569825
#keyserver.rainydayz.org    11370   # Andy Ruddock <andy.ruddock@rainydayz.org> 0xEEC3AFB3
#keyserver.computer42.org   11370   # H.-Dirk Schmitt <dirk@computer42.org>     0x6A017B17
MEMBERSHIP

%{__cat} <<'INIT' >rc.sks
#! /bin/sh
#
# chkconfig: - 95 30
# description: SKS keyserver db and recon daemons
# config: /etc/sks/sksconf

CLIENT=%{_bindir}/sks
DIR=%{_localstatedir}/sks
STARTOPTS=""

test -e $CLIENT || exit 0

test -d $DIR || exit 0

case "$1" in
        start)
        cd $DIR
                echo -n "Starting SKS:"
                echo -n \ sks_db
                $CLIENT db &
                echo -n \ sks_recon
                $CLIENT recon &
                echo "."
        ;;
        stop)
                echo -n "Stopping SKS:"
        killall sks
        while [ "`pidof sks`" ]; do sleep 1; done # wait until SKS processes have exited
                echo "."
        ;;
        restart|force-reload)
        $0 stop
        sleep 1
        $0 start
    ;;
        *)
        echo "Usage: $0 {start|stop|reload|restart|force-reload}"
        exit 1
    ;;
esac

exit 0
INIT

%build
%{__make} dep
%{__make} all
%{__make} all.bc

%install
%{__rm} -rf %{buildroot}
%{__make} install PREFIX="%{buildroot}%{_usr}" MANDIR="%{buildroot}%{_mandir}"

# install the config files
%{__install} -m755 -d %{buildroot}%{_sysconfdir}/sks
%{__install} -m644 sksconf %{buildroot}%{_sysconfdir}/sks
%{__install} -m644 membership %{buildroot}%{_sysconfdir}/sks

# install the init script
%{__install} -m755 -d %{buildroot}%{_initrddir}
%{__install} -m755 rc.sks %{buildroot}%{_initrddir}/sks

# make a data directory
%{__install} -m755 -d %{buildroot}%{_localstatedir}/sks
pushd %{buildroot}%{_localstatedir}/sks && %{__ln_s} ../..%{_sysconfdir}/sks/sksconf && popd
pushd %{buildroot}%{_localstatedir}/sks && %{__ln_s} ../..%{_sysconfdir}/sks/membership && popd

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ANNOUNCEMENT BUGS CHANGELOG COPYING FILES README TODO VERSION
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_initrddir}/sks
%{_localstatedir}/sks/
%config(noreplace) %{_sysconfdir}/sks/

%changelog
* Mon Apr 16 2012 Steve Huff <shuff@vecna.org> - 1.1.3-1
- Initial package.
