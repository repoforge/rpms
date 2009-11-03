# $Id$

# Authority: dries
# Upstream: Jan Gyselinck <jan at b0rken dot net>

Summary: Generates an iptables-restoreable config
Name: fw-rulegen
Version: 1.0
Release: 1.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://www.b0rken.net/fw-rulegen/

Source0: http://www.b0rken.net/fw-rulegen/data/fw/example/rules.conf
Source1: http://www.b0rken.net/fw-rulegen/data/fw/example/global.conf
Source2: http://www.b0rken.net/fw-rulegen/data/fw/example/interfaces.conf
Source3: http://www.b0rken.net/fw-rulegen/data/sbin/fw-rulegen.pl
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: iptables

%description
 It's a GPL'd perlscript that generates an iptables-restoreable iptables
config. The config is located in /etc/fw/, using three files: rules.conf,
global.conf and interfaces.conf. This config is read by fw-rulegen.pl. It
then outputs the result on STDOUT, it just suffices to pipe it through
iptables-restore and presto.

I have an init.d alike script for it to start/stop the firewall. You can
find it here. Beware though, I use a homedeveloped init.d-alike system, so
you will need to modify the script to make it work.

%prep
%setup

%build
cat > fw-rulegen <<EOF
#!/bin/sh
#
# fw-rulegen	Start the fw-rulegen firewall
#
# chkconfig: 2345 08 92
# description:  Starts and stops the fw-rulegen firewall
#
# config: /etc/fw/rules.conf
# config: /etc/fw/global.conf
# config: /etc/fw/interfaces.conf

# Source function library.
. /etc/init.d/functions

case "$1" in
	start)
		/usr/bin/fw-rulegen.pl|iptables-restore
		echo 1 > /proc/sys/net/ipv4/ip_forward
		exit 0
		;;
	stop)
		echo 0 > /proc/sys/net/ipv4/ip_forward
		iptables -F INPUT
		iptables -F FORWARD
		iptables -F OUTPUT
		iptables -P INPUT ACCEPT
		iptables -P OUTPUT ACCEPT
		exit 0
		;;
	*)
		echo $"Usage: $0 {start|stop}"
		exit 1
esac
EOF

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 %{SOURCE3} %{buildroot}%{_bindir}/fw-rulegen.pl
%{__install} -Dp -m0755 fw-rulegen %{buildroot}%{_initrddir}/fw-rulegen

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/fw/
%{__install} -p -m0644 %{SOURCE0} %{SOURCE1} %{SOURCE2} %{buildroot}%{_sysconfdir}/fw/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/fw/
%config %{_initrddir}/fw-rulegen
%{_bindir}/fw-rulegen.pl

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0-1.2
- Rebuild for Fedora Core 5.

* Fri May 7 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
