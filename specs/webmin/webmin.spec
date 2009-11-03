# $Id$
# Authority: dag
# Upstream: <webadmin-devel$lists,sf,net>

# BuildAsRoot: 1

### FIXME: The official webmin RPM package is broken. Please back up all configuration files before upgrading.

%{?dtag: %{expand: %%define %dtag 1}}

%define logmsg logger -t %{name}/rpm
#define __spec_install_post #{nil}

Summary: Web-based administration interface
Name: webmin
Version: 1.310
Release: 1%{?dist}
License: BSD
Group: System Environment/Base
URL: http://www.webmin.com/

Source: http://dl.sf.net/webadmin/webmin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
AutoReq: 0
BuildRequires: perl, perl-Net-SSLeay, perl(CGI), perl(Mon::Client)
BuildRequires: perl-Mon
Requires: perl, perl(Net::SSLeay), perl(CGI), perl(Mon::Client)
Requires: perl(Authen::PAM)
Requires(post): openssl

%description
A web-based administration interface for Unix systems. Using Webmin you can
configure DNS, Samba, NFS, local/remote filesystems and more using your
web browser.

%prep
%setup

%{__perl} -pi -e 's|^\S*#!/\S*bin/perl|#!%{__perl}|i;' *.{cgi,pl} */*.{cgi,pl}
#find . -type f -name "*.cgi" -exec %{__perl} -pi -e 's|^\S*#!/\S*bin/perl|#!%{__perl}|i;' {} \;
#find . -type f -name "*.pl" -exec %{__perl} -pi -e 's|^\S*#!/\S*bin/perl|#!%{__perl}|i;' {} \;

### Disable port check
%{__perl} -pi -e 's|(\$perl -e .use Socket; socket)|#$1|' setup.sh

%{__rm} -f mount/freebsd-mounts* mount/openbsd-mounts* mount/macos-mounts* webmin-gentoo-init
#%{__rm} -f {,config-}{aix,cobalt,corel,cygwin,debian,freebsd,gentoo,hpux,irix,lfs,macos,mandrake,msc,netbsd,open,openbsd,openserver,osf1,slackware,suse,trustix,turbo,united,unixware,solaris}{,-*}

%{__chmod} -R og-w .

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libexecdir}/webmin/
%{__cp} -ap * %{buildroot}%{_libexecdir}/webmin/

%{__install} -Dp -m0644 webmin-daemon %{buildroot}%{_sysconfdir}/sysconfig/daemons/webmin
%{__install} -Dp -m0755 webmin-init %{buildroot}%{_initrddir}/webmin
%{__install} -Dp -m0644 webmin-pam %{buildroot}%{_sysconfdir}/pam.d/webmin

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/webmin/

echo 'rpm' >%{buildroot}%{_libexecdir}/webmin/install-type

### Prepare configuration (see os_list.txt)
os_type="redhat-linux"
%{?el4:os_version="12.0"; real_os_type="Red Hat Enterprise Linux"; real_os_version="4"}
%{?el3:os_version="9.0";  real_os_type="Red Hat Enterprise Linux"; real_os_version="3"}
%{?el2:os_version="7.2";  real_os_type="Red Hat Enterprise Linux"; real_os_version="2.1"}
%{?fc5:os_version="14.0"; real_os_type="Fedora Core";      real_os_version="5"}
%{?fc4:os_version="13.0"; real_os_type="Fedora Core";      real_os_version="4"}
%{?fc3:os_version="12.0"; real_os_type="Fedora Core";      real_os_version="3"}
%{?fc2:os_version="11.0"; real_os_type="Fedora Core";      real_os_version="2"}
%{?fc1:os_version="10.0"; real_os_type="Fedora Core";      real_os_version="1"}
%{?rh9:os_version="9.0";  real_os_type="Red Hat Linux";    real_os_version="9"}
%{?rh8:os_version="8.0";  real_os_type="Red Hat Linux";    real_os_version="8.0"}
%{?rh7:os_version="7.3";  real_os_type="Red Hat Linux";    real_os_version="7.3"}
%{?rh6:os_version="6.2";  real_os_type="Red Hat Linux";    real_os_version="6.2"}
%{?yd4:os_version="11.0"; real_os_type="Yellow Dog Linux"; real_os_version="4.0"}
%{?yd3:os_version="9.0";  real_os_type="Yellow Dog Linux"; real_os_version="3.0"}
%{?yd2:os_version="8.0";  real_os_type="Yellow Dog Linux"; real_os_version="2.3"}
export os_type os_version real_os_type real_os_version

export config_dir="%{buildroot}%{_sysconfdir}/webmin"
export var_dir="%{_localstatedir}/webmin"
export perl="%{__perl}"
export autoos="3"
export port="10000"
export login="root"
export crypt="x"
export host="localhost"
export ssl="1"
export atboot="1"
export nochown="1"
export autothird="1"
export noperlpath="1"
export nouninstall="1"
export nostart="1"
#export password="webmin-admin"
export makeboot="0"
%{buildroot}%{_libexecdir}/webmin/setup.sh

### Clean up buildroot
%{__perl} -pi -e 's|%{buildroot}||g' %{buildroot}/etc/webmin/{miniserv.conf,restart,start,stop}
%{__rm} -f %{buildroot}%{_libexecdir}/webmin/{LICENCE*,README*}
%{__rm} -f %{buildroot}%{_libexecdir}/setup.sh
#%{__rm} -f %{buildroot}%{_sysconfdir}/webmin/miniserv.pem

%clean
%{__rm} -rf %{buildroot}

%post
echo -e ".\n.\n.\nWebmin Webserver on $(hostname)\n.\n*\nroot@$(hostname)" | \
openssl req -newkey rsa:512 -x509 -nodes -days 1825 -set_serial $(date +%s) -out %{_tmppath}/cert -keyout %{_tmppath}/key &>/dev/null
if [ $? -eq 0 ]; then
	PEMFILE="%{_sysconfdir}/webmin/miniserv.pem"
	if [ -f "$PEMFILE" ]; then PEMFILE="$PEMFILE.rpmnew"; fi
	%{__cat} %{_tmppath}/{cert,key} >"$PEMFILE"
	%{__rm} -f %{_tmppath}/{cert,key}
	%{__chmod} 0600 "$PEMFILE"
fi
/sbin/chkconfig --add webmin
/sbin/service webmin start &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
        /sbin/service webmin stop &>/dev/null || :
        /sbin/chkconfig --del webmin
fi

%postun
/sbin/service webmin condrestart &>/dev/null || :

%files
%defattr(-, root, root, 0755)
%doc LICENCE* README*
%config %{_initrddir}/webmin
%config %{_sysconfdir}/pam.d/webmin
%config %{_sysconfdir}/webmin/
%config(noreplace) %{_sysconfdir}/sysconfig/daemons/webmin
%config(noreplace) %{_sysconfdir}/webmin/config/
%config(noreplace) %{_sysconfdir}/webmin/miniserv.*
%config(noreplace) %{_sysconfdir}/webmin/webmin.acl
%ghost %{_sysconfdir}/webmin/miniserv.pem
%ghost %{_sysconfdir}/webmin/module.infos.cache
%dir %{_localstatedir}/webmin/
%{_libexecdir}/webmin

%changelog
* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> - 1.310-1
- Updated to release 1.310.

* Tue Apr 11 2006 Dag Wieers <dag@wieers.com> - 1.270-1
- Updated to release 1.270.

* Thu Feb 02 2006 Dag Wieers <dag@wieers.com> - 1.260-1
- Updated to release 1.260.

* Fri Dec 02 2005 Dag Wieers <dag@wieers.com> - 1.250-1
- Updated to release 1.250.

* Wed Nov 30 2005 Dag Wieers <dag@wieers.com> - 1.240-1
- Updated to release 1.240.

* Fri Jul 22 2005 Dag Wieers <dag@wieers.com> - 1.220-1
- Updated to release 1.220.
- Added /etc/webmin/webmin.acl to noreplace config files. (Ralph Angenendt)

* Mon Jun 06 2005 Dag Wieers <dag@wieers.com> - 1.210-1
- Updated to release 1.210.

* Sat Apr 30 2005 Dag Wieers <dag@wieers.com> - 1.200-1
- Updated to release 1.200.
- Added perl(Authen::PAM) dependency. (Treyavn)

* Mon Mar 28 2005 Dag Wieers <dag@wieers.com> - 1.190-1
- Updated to release 1.190.

* Fri Jan 28 2005 Dag Wieers <dag@wieers.com> - 1.180-1
- Updated to release 1.180.

* Sun Nov 21 2004 Dag Wieers <dag@wieers.com> - 1.170-1
- Updated to release 1.170.
- Added -set_serial to openssl. (Donavan Nelson)

* Sat Oct 09 2004 Dag Wieers <dag@wieers.com> - 1.160-1
- Updated to release 1.160.
- Cleaned up buildroot artifacts in restart script. (Bill Thompson)
- Removed locally build certificate. (Christopher V. Browne)

* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 1.150-1
- Updated to release 1.150.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 1.140-1
- Updated to release 1.140.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 1.060-1
- Initial package. (using DAR)
