# $Id$
# Authority: dag

Summary: Heartbeat subsystem for High-Availability Linux
Name: heartbeat
Version: 1.0.2
Release: 0.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://linux-ha.org/

Source: http://linux-ha.org/download/%{name}-%{version}.tar.gz
Patch0: ldirectord.passwd.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: glib-devel, lynx, perl, iputils, /usr/bin/ssh, openssl-devel, libnet
Requires: sysklogd

%package ldirectord
Summary: Monitor daemon for maintaining high availability resources
Group: Applications/Internet
Requires: perl, perl-libwww-perl perl-Net-SSLeay, ipvsadm, perl-HTML-Parser, perl-LDAP, perl-Mail-IMAPClient

%package stonith
Summary: Provides an interface to Shoot The Other Node In The Head
Group: Applications/Internet
Requires: telnet

%package pils
Summary: Provides a general plugin and interface loading library
Group: Applications/Internet

%description
heartbeat is a basic high-availability subsystem for Linux-HA.
It will run scripts at initialization, and when machines go up or down.
This version will also perform IP address takeover using gratuitous ARPs.
It works correctly for a 2-node configuration, and is extensible to larger
configurations.

It implements the following kinds of heartbeats:
	- Bidirectional Serial Rings ("raw" serial ports)
	- UDP/IP broadcast (ethernet, etc)
	- Unicast heartbeats
	- "ping" heartbeats (for routers, switches, etc.)
	   (to be used for breaking ties in 2-node systems)

%description ldirectord
ldirectord is a stand-alone daemon to monitor services of real
for virtual services provided by The Linux Virtual Server
(http://www.linuxvirtualserver.org/). It is simple to install
and works with the heartbeat code (http://www.linux-ha.org/).

%description stonith
The STONITH module (a.k.a. STOMITH) provides an extensible interface
for remotely powering down a node in the cluster.  The idea is quite simple:
When the software running on one machine wants to make sure another
machine in the cluster is not using a resource, pull the plug on the other
machine. It's simple and reliable, albeit admittedly brutal.

%description pils
PILS is an generalized and portable open source
Plugin and Interface Loading System.
PILS was developed as part of the Open Cluster Framework
reference implementation, and is designed
to be directly usable by a wide variety of other applications.
PILS manages both plugins (loadable objects),
and the interfaces these plugins implement.
PILS is designed to support any number of plugins
implementing any number of interfaces.

%prep
%setup
%patch0 -p0

%build
%configure \
	--enable-ltdl-convenience
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -Dp -m0644 rc.config.heartbeat %{buildroot}%{_localstatedir}/adm/fillup-templates/rc.config.heartbeat

%{__ln_s} -f %{_sbindir}/ldirectord %{buildroot}%{_sysconfdir}/ha.d/resource.d/ldirectord

### Clean up docdir
%{__rm} -f doc/Makefile*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc doc/*
%doc %{_mandir}/man8/heartbeat.*
%doc %{_mandir}/man8/apphbd.*
%doc %{_mandir}/man8/stonith.*
%dir /etc/ha.d
/etc/ha.d/harc
/etc/ha.d/shellfuncs
/etc/ha.d/rc.d
/etc/ha.d/README.config
/etc/ha.d/cts/CM_fs.py
/etc/ha.d/cts/CM_hb.py
/etc/ha.d/cts/CTS.py
/etc/ha.d/cts/CTSaudits.py
/etc/ha.d/cts/CTSlab.py
/etc/ha.d/cts/CTStests.py
/etc/ha.d/resource.d/
/etc/init.d/heartbeat
/etc/logrotate.d/heartbeat
/usr/lib/heartbeat
/usr/lib/libhbclient.*
/usr/lib/libccmclient.*
/usr/lib/libplumb.*
/usr/lib/libapphb.*
/usr/include/heartbeat
/usr/include/clplumbing
/usr/include/ocf
/usr/include/ccm.h
/usr/include/ccmlib.h
/var/adm/fillup-templates/rc.config.heartbeat
%dir /var/lib/heartbeat
%attr (600, root, root)       /var/lib/heartbeat/fifo
%dir %attr (750, root, haclient) /var/lib/heartbeat/api
%attr (620, root, haclient) /var/lib/heartbeat/register
%attr (755, hacluster, haclient) /var/lib/heartbeat/ccm
%attr (1770, root, haclient) /var/lib/heartbeat/casual
%attr (200, hacluster, haclient) /var/lib/heartbeat/api/ccm.req
%attr (600, hacluster, haclient) /var/lib/heartbeat/api/ccm.rsp
%attr (200, hacluster, haclient) /var/lib/heartbeat/api/ipfail.req
%attr (600, hacluster, haclient) /var/lib/heartbeat/api/ipfail.rsp
#
# if ENABLE_SNMP_SUBAGENT=1; then
#	install mib files and other subagent related stuff;
# fi
#
%define ENABLE_SNMP_SUBAGENT 0
%if %{ENABLE_SNMP_SUBAGENT}
	/LINUX-HA-MIB.mib
%endif

%files ldirectord
%defattr(-, root, root, 0755)
/etc/ha.d/conf
/usr/sbin/ldirectord
/usr/sbin/supervise-ldirectord-config
/etc/logrotate.d/ldirectord
/etc/init.d/ldirectord
/etc/ha.d/resource.d/ldirectord
/usr/man/man8/ldirectord.8*
%doc ldirectord/ldirectord.cf

%files stonith
%defattr(-, root, root, 0755)
/usr/include/stonith
/usr/lib/libstonith.*
/usr/lib/stonith
/usr/sbin/stonith
/usr/sbin/meatclient

%files pils
%defattr(-, root, root, 0755)
/usr/include/pils
/usr/lib/libpils.*
/usr/lib/pils/plugins

%pre
###########################################################
#
#	This isn't perfect.  But getting every distribution
#	to agree on group id's seems hard to me :-(
#
if
  getent group haclient >/dev/null
then
  : OK group haclient already present
else
  GROUPOPT="-g 65"
  if
    usr/sbin/groupadd $GROUPOPT haclient 2>/dev/null
  then
    : OK we were able to add group haclient
  else
    usr/sbin/groupadd haclient
  fi
fi

if
  getent passwd hacluster >/dev/null
then
  : OK user hacluster already present
else
  USEROPT="-g haclient"
  if
    usr/sbin/useradd $USEROPT hacluster 2>/dev/null
  then
    : OK we were able to add user hacluster
  else
    usr/sbin/useradd hacluster
  fi
fi

%post
if
  [ -f etc/SuSE-release ]
then
  start=75
  stop=05
  for d in etc/init.d/rc[235].d
  do
    rm -f $d/[SK]*[0-9]heartbeat
    ln -s ../heartbeat $d/S${start}heartbeat
    ln -s ../heartbeat $d/K${stop}heartbeat
  done
  FILLUP=/bin/fillup
  if
    $FILLUP -q -d = etc/rc.config var/adm/fillup-templates/rc.config.heartbeat
  then
    : $FILLUP returned OK
  else
    echo "ERROR: $FILLUP failed. This should not happen. Please compare"
    echo "/etc/rc.config and /var/adm/fillup-templates/rc.config.heartbeat"
    echo "and update by hand."
  fi
elif
  [ -x sbin/chkconfig ]
then
  sbin/chkconfig --add heartbeat
fi
true

%preun
Uninstall_PPP_hack() {
  file2hack=etc/ppp/ip-up.local
  echo "NOTE: Restoring /$file2hack"
  MARKER="Heartbeat"
  ed -s $file2hack <<-!EOF  2>/dev/null
H
g/ $MARKER\$/d
w
!EOF
}

if
  [ $1 = 0 ]
then
  [ -x sbin/chkconfig ] && sbin/chkconfig --del heartbeat
  if
    [ ! -x etc/ppp/ip-up.heart ]
  then
    Uninstall_PPP_hack
  fi
fi
if
   [ -r etc/SuSE-release ]
then
  rm -f etc/init.d/rc[235].d/[SK]*[0-9]heartbeat
fi
true

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.2-0.2
- Rebuild for Fedora Core 5.

* Sun Jan 19 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)

