# $Id$
# Authority: dag
# Upstream: Alec Thomas <alec$swapoff,org>

Summary: Allows restricted root access for specified users
Name: op
Version: 1.32
Release: 3
License: BSD
Group: Applications/System
URL: http://swapoff.org/op/

Source: http://swapoff.org/files/op/op-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: flex, pam-devel

%description
op provides a flexible means for system administrators to grant access
to certain root operations without having to give them full superuser
privileges. Different sets of users may access different operations,
and the security-related aspects of each operation can be carefully
controlled.

%prep
%setup

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
#    /bin/su -;
#    users=dag,ramses,wim
#    environment
#    password

### 'op reboot' - reboot system
### Shows how to use a simple access list
#reboot
#    /sbin/reboot;
#    users=ACCESS_LIST
#    password

### 'op shutdown <time>' - shutdown at a certain time.
### Restricts argument to valid values only.
#shutdown
#    /sbin/shutdown -h $1;
#    users=ACCESS_LIST
#    $1=(now|[0-1]?[0-9]:[0-9][0-9]|2[0-3]:[0-5][0-9]|+[0-9]+)

### 'op service <service> start|stop|restart|status' - Manipulate services.
#service
#    /sbin/service $1 $2;
#    users=ACCESS_LIST
#    environment
#    $2=start|stop|restart|status

### 'op inetd on|off' - switch inetd on and off.
### Shows complex shell example and 'string' arguments.
#inetd
#    /bin/sh -c '
#    case $1 in
#            (on) /usr/sbin/inetd -s ;;
#            (off) /usr/bin/pkill inetd ;;
#    esac
#    ';
#    users=ACCESS_LIST
#    $1=on|off
EOF

%{__cat} <<EOF >su.conf
### 'op su' - gives user a root shell.
### Restrict a list of local users.
#su
#    /bin/su -;
#    users=dag,ramses,wim
#    environment
#    password
EOF

%{__cat} <<EOF >op.pam
#%PAM-1.0
auth       required	pam_stack.so service=system-auth
account    required	pam_stack.so service=system-auth
password   required	pam_stack.so service=system-auth
session    required	pam_stack.so service=system-auth
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0600 op.conf %{buildroot}%{_sysconfdir}/op.conf
%{__install} -Dp -m0644 op.pam %{buildroot}%{_sysconfdir}/pam.d/op
%{__install} -d -m0700 %{buildroot}%{_sysconfdir}/op.d/
%{__install} -Dp -m0600 su.conf %{buildroot}%{_sysconfdir}/op.d/su.conf

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING op.conf* op.paper README
%doc %{_mandir}/man1/op.1*
%config(noreplace) %{_sysconfdir}/op.conf
%config(noreplace) %{_sysconfdir}/op.d/
%config(noreplace) %{_sysconfdir}/pam.d/op
%{_bindir}/op

%changelog
* Mon Nov 10 2008 Dag Wieers <dag@wieers.com> - 1.32-3
- Fix some configuration files.

* Thu Aug 16 2007 Dag Wieers <dag@wieers.com> - 1.32-2
- Change permissions of /etc/op.d/ to 0700.
- Added su.conf example to show how it works.

* Thu Dec 08 2005 Dries Verachtert <dries@ulyssis.org> - 1.32-1
- Updated to release 1.32.

* Sat Sep 03 2005 Dag Wieers <dag@wieers.com> - 1.31-1
- Updated to release 1.31.

* Sat May 28 2005 Dag Wieers <dag@wieers.com> - 1.30-1
- Updated to release 1.30.

* Fri Apr 29 2005 Dag Wieers <dag@wieers.com> - 1.29-1
- Updated to release 1.29.

* Fri Apr 08 2005 Dag Wieers <dag@wieers.com> - 1.28-1
- Updated to release 1.28.

* Thu Jul 22 2004 Dag Wieers <dag@wieers.com> - 1.25-1
- Updated to release 1.25.

* Wed May 05 2004 Dag Wieers <dag@wieers.com> - 1.23-1
- Updated to release 1.23.

* Mon May 03 2004 Dag Wieers <dag@wieers.com> - 1.22-1
- Updated to release 1.22.

* Fri Apr 30 2004 Dag Wieers <dag@wieers.com> - 1.21-2
- Added default pam configuration.
- Improved the examples in the default config file.

* Fri Apr 23 2004 Dag Wieers <dag@wieers.com> - 1.21-1
- Initial package. (using DAR)
