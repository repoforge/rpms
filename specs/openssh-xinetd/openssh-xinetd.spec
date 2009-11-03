# $Id$
# Authority: dag
# Upstream: Dag Wieers <dag$wieers,com>

Summary: OpenSSH backup xinetd entry
Name: openssh-xinetd
Version: 0.2
Release: 2.2%{?dist}
License: GPL
Group: Applications/Internet
URL: http://dag.wieers.com/packages/openssh-xinetd/

#Source:
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: xinetd
Requires: xinetd, openssh-server

%description
This package contains an OpenSSH xinetd entry that makes OpenSSH
available on port 2022 through xinetd.

This is very useful for remote servers in case your OpenSSH
stand-alone daemon for some reason isn't running. Port 2022 is
used because some ISPs block incoming connections from ports lower
than 1024.

%prep
echo "Dag Wieers <dag@wieers.com>" >AUTHORS

%{__cat} <<EOF >README
The ssh-backup service allows you to connect to your system
using ssh on port 2022 even when the ssh daemon isn't running.

If you have improvements to this package, please send them to:
Dag Wieers <dag@wieers.com>
EOF

%{__cat} <<EOF >ssh-backup.xinetd
# default: on
# description: The ssh-backup service allows you to connect to your system
#	using ssh on port 2022 even when the ssh daemon isn't running.
service ssh-backup
{
	disable = no
	socket_type     = stream
	protocol        = tcp
	port            = 2022
	type            = UNLISTED
	wait            = no
	user            = root
	server          = %{_sbindir}/sshd
	server_args     = -i -b 1024
	log_on_failure  += USERID
#	only_from       = 127.0.0.1 10.15.0.0/24
}
EOF

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0644 ssh-backup.xinetd %{buildroot}%{_sysconfdir}/xinetd.d/ssh-backup

%post
if [ $1 -ne 0 ]; then
    /sbin/service xinetd reload &>/dev/null || :
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS README
%config(noreplace) %{_sysconfdir}/xinetd.d/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 0.2-2.2
- Rebuild for Fedora Core 5.

* Tue Dec 28 2004 Dag Wieers <dag@wieers.com> - 0.2-2
- Change to noarch (Doncho Gunchev)

* Thu Apr 22 2004 Dag Wieers <dag@wieers.com> - 0.2-1
- Restart xinetd when installed.
- Added only_from example with multiple arguments.

* Wed Oct 08 2003 Dag Wieers <dag@wieers.com> - 0.1-0
- Initial package. (using DAR)
