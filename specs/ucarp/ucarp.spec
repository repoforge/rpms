# $Id$
# Authority: matthias


%{!?dtag:%define _with_libpcapdevel 1}
%{?el5:%define _with_libpcapdevel 1}
%{?fc6:%define _with_libpcapdevel 1}

Summary: Common Address Redundancy Protocol (CARP) for Unix
Name: ucarp
Version: 1.1
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
URL: http://www.ucarp.org/
Source: http://www.pureftpd.org/ucarp/ucarp-%{version}.tar.bz2
Source1: carp.init
Source2: vip-001.conf.example
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig, /sbin/service
Requires(postun): /sbin/service
BuildRequires: libpcap, gettext
%{?_with_libpcapdevel:BuildRequires:libpcap-devel}


%description
UCARP allows a couple of hosts to share common virtual IP addresses in order
to provide automatic failover. It is a portable userland implementation of the
secure and patent-free Common Address Redundancy Protocol (CARP, OpenBSD's
alternative to the patents-bloated VRRP).
Strong points of the CARP protocol are: very low overhead, cryptographically
signed messages, interoperability between different operating systems and no
need for any dedicated extra network link between redundant hosts.


%prep
%setup


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

# Install the init script
%{__install} -Dp -m 0755 %{SOURCE1} \
    %{buildroot}/etc/rc.d/init.d/carp

# Install the example config file
%{__install} -Dp -m 0600 %{SOURCE2} \
    %{buildroot}/etc/sysconfig/carp/vip-001.conf.example

# Install trivial interface up/down scripts
%{__cat} << 'EOF' > %{buildroot}/etc/sysconfig/carp/vip-up
#!/bin/sh
# We could use ifup directly, but it complains if the address is already used
#/sbin/ifup $1
. /etc/sysconfig/network-scripts/ifcfg-$1
#exec /sbin/ip addr add ${IPADDR}/${NETMASK} dev "$1"
exec /sbin/ifconfig $1 ${IPADDR} netmask ${NETMASK} up
EOF
%{__cat} << 'EOF' > %{buildroot}/etc/sysconfig/carp/vip-down
#!/bin/sh
#. /etc/sysconfig/network-scripts/ifcfg-$1
#exec /sbin/ip addr del ${IPADDR}/${NETMASK} dev "$1"
exec /sbin/ifconfig $1 down
EOF


%clean
%{__rm} -rf %{buildroot}


%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add carp
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service carp stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del carp
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service carp condrestart >/dev/null 2>&1 || :
fi


%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING ChangeLog NEWS README examples/linux/*.sh
%config %{_initrddir}/carp
%dir /etc/sysconfig/carp/
%{_sysconfdir}/sysconfig/carp/vip-001.conf.example
%attr(0700, root, root) %config(noreplace) %{_sysconfdir}/sysconfig/carp/vip-up
%attr(0700, root, root) %config(noreplace) %{_sysconfdir}/sysconfig/carp/vip-down
%{_sbindir}/ucarp


%changelog
* Sun Oct 17 2004 Dag Wieers <dag@wieers.com> - 1.1-1
- Updated to release 1.1.

* Fri Jul  9 2004 Matthias Saou <http://freshrpms.net/> 1.0-1
- Initial RPM release.

