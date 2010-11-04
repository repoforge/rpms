# $Id$
# Authority: shuff
# Upstream: Matthias Andree <m-a$users,sourceforge,net>

Summary: NNTP server for small sites
Name: leafnode
Version: 1.11.8
Release: 2%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://leafnode.sourceforge.net/

Source: http://www.dt.e-technik.uni-dortmund.de/~ma/leafnode/leafnode-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils
BuildRequires: gawk
BuildRequires: gcc
BuildRequires: make
BuildRequires: pcre-devel
BuildRequires: rpm-macros-rpmforge
BuildRequires: setup
Requires: setup
Requires: vixie-cron
Requires: xinetd

%description
Leafnode is a software package that implements a store & forward NNTP proxy
(client and server) that supports TCP connections across IPv4 and IPv6. It can
be used to give a regular newsreader off-line functionality, merge news
articles from several upstream newsservers for newsreaders that only support
one server well and avoid duplicate news download for a small LAN with multiple
users reading news.

%prep
%setup

%build
%configure \
    --disable-dependency-tracking \
    --with-ipv6 \
    --with-user=daemon \
    --with-group=daemon \
    --with-lockfile='%{_localstatedir}/lock/leafnode/lock' \
    --sysconfdir=%{_sysconfdir}/leafnode
%{__make} %{?_smp_mflags}

# create xinetd config
%{__cat} <<XINETD >nntp.xinetd
service nntp
{
    disable         = yes

    flags           = NAMEINARGS NOLIBWRAP
    socket_type     = stream
    protocol        = tcp
    wait            = no
    user            = daemon
    server          = /usr/sbin/tcpd
    server_args     = %{_sbindir}/leafnode
    instances       = 10
    per_source      = 2
}
XINETD

# create cron job
%{__cat} <<CRON >nntp.cron
# run texpire to purge old articles
0 4 * * * daemon %{_sbindir}/texpire
# run fetchnews to get new articles
0,30 * * * * daemon %{_sbindir}/fetchnews
CRON

%{__cat} <<SH >leafnode.sh
# if you're using leafnode, you probably want this
export NNTPSERVER=localhost
SH

%{__cat} <<CSH >leafnode.csh
# if you're using leafnode, you probably want this
setenv NNTPSERVER localhost
CSH

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/cron.d/
%{__install} -m0644 nntp.cron %{buildroot}%{_sysconfdir}/cron.d/nntp

%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/profile.d/
%{__install} -m0644 leafnode.csh %{buildroot}%{_sysconfdir}/profile.d/
%{__install} -m0644 leafnode.sh %{buildroot}%{_sysconfdir}/profile.d/

%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/xinetd.d/
%{__install} -m0644 nntp.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/nntp

%{__install} -m0755 -d %{buildroot}%{_localstatedir}/lock/leafnode/
%{__install} -m0755 -d %{buildroot}%{_localstatedir}/spool/news/

# clean up some mess
%{__rm} %{buildroot}%{_sysconfdir}/leafnode/Makefile.dist
%{__rm} %{buildroot}%{_sysconfdir}/leafnode/UNINSTALL-daemontools

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ADD-ONS ChangeLog* COPYING* CREDITS FAQ* INSTALL KNOWNBUGS NEWS OLDNEWS
%doc README* TODO UNINSTALL-daemontools
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_sbindir}/*
%{_sysconfdir}/leafnode/
%config(noreplace) %{_sysconfdir}/profile.d/*
%{_sysconfdir}/cron.d/nntp
%{_sysconfdir}/xinetd.d/nntp
%attr(0755, daemon, daemon) %dir %{_localstatedir}/lock/leafnode/
%attr(0755, daemon, daemon) %dir %{_localstatedir}/spool/news/

%changelog
* Thu Nov 04 2010 Steve Huff <shuff@vecna.org> - 1.11.8-2
- Profile scripts to set NNTPSERVER.

* Tue Oct 26 2010 Steve Huff <shuff@vecna.org> - 1.11.8-1
- Initial package.
