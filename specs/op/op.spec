# $Id: _template.spec 219 2004-04-09 06:21:45Z dag $
# Authority: dag
# Upstream: Alec Thomas <alec$swapoff,org>

Summary: Allows restricted root access for specified users
Name: op
Version: 1.23
Release: 1
License: BSD
Group: Applications/System
URL: http://swapoff.org/op

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://swapoff.org/files/op/op-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex

%description
op provides a flexible means for system administrators to grant access
to certain root operations without having to give them full superuser
privileges. Different sets of users may access different operations,
and the security-related aspects of each operation can be carefully
controlled.

%prep
%setup

### FIXME: Make buildsystem use standard autotools directories (Fix upstream please)
%{__perl} -pi.orig -e '
		s|\$\(BINDIR\)|\$(bindir)|;
		s|\$\(MANDIR\)|\$(mandir)/man1|;
		s|-o \$\(\w+\) -g \$\(\w+\)||;
	' Makefile

%{__cat} <<'EOF' >op.conf
### This is the config file for the op tool.
### For more information about the syntax see manual page op(1)

### Define some users
#OPERATORS=(dag|ramses)

### Define hosts that Fred is restricted to
#DAG_HOSTS=(horsea|jynx)

### Define hosts that Barry is restricted to
#RAMSES_HOSTS=(pikachu|jynx)

### Define user/host access list
#ACCESS_LIST=dag@DAG_HOSTS|ramses@RAMSES_HOSTS

### 'op su' - gives user a root shell.
### Restrict a list of local users.
#su
#	/bin/su -;
#	users=dag,ramses,wim
#	environment
#	password

### 'op reboot' - reboot system
### Shows how to use a simple access list
#reboot
#	/sbin/reboot;
#	users=ACCESS_LIST
#	password

### 'op shutdown <time>' - shutdown at a certain time.
### Restricts argument to valid values only.
#shutdown
#	/sbin/shutdown -h $1;
#	users=ACCESS_LIST
#	$1=(now|[0-1]?[0-9]:[0-9][0-9]|2[0-3]:[0-5][0-9]|+[0-9]+)

### 'op service <service> start|stop|restart|status' - Manipulate services.
#service
#	/sbin/service $1 $2;
#	users=ACCESS_LIST
#	environment
#	$2=start|stop|restart|status

### 'op inetd on|off' - switch inetd on and off.
### Shows complex shell example and 'string' arguments.
#inetd
#	/bin/sh -c '
#		case $1 in
#			on) /usr/sbin/inetd -s ;;
#			off) /usr/bin/pkill inetd ;;
#		esac
#	';
#	users=ACCESS_LIST
#	$1=on|off
EOF

%{__cat} <<EOF >op.pam
#%PAM-1.0
auth       required	pam_stack.so service=system-auth
account    required	pam_stack.so service=system-auth
password   required	pam_stack.so service=system-auth
session    required	pam_stack.so service=system-auth
EOF

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -D -m0600 op.conf %{buildroot}%{_sysconfdir}/op.conf
%{__install} -D -m0644 op.pam %{buildroot}%{_sysconfdir}/pam.d/op

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README op.paper op.conf
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/op.conf
%config %{_sysconfdir}/pam.d/op
%{_bindir}/op

%changelog
* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 1.21-2
- Added default pam configuration.
- Improved the examples in the default config file.

* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 1.21-1
- Initial package. (using DAR)
