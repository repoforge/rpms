# $Id$
# Authority: dag
# Upstream: <webadmin-devel$lists,sf,net>

# BuildAsRoot: 1

%{?dist: %{expand: %%define %dist 1}}

%define logmsg logger -t %{name}/rpm
#define __spec_install_post %{nil}

Summary: Web-based administration interface
Name: webmin
Version: 1.150
Release: 1
License: BSD
Group: System Environment/Base
URL: http://www.webmin.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://dl.sf.net/webadmin/webmin-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
AutoReq: 0
BuildRequires: perl, perl-Net-SSLeay, perl(CGI), perl(Mon::Client)
Requires: perl, perl(Net::SSLeay), perl(CGI), perl(Mon::Client)

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
%{__cp} -a * %{buildroot}%{_libexecdir}/webmin/

%{__install} -D -m0644 webmin-daemon %{buildroot}%{_sysconfdir}/sysconfig/daemons/webmin
%{__install} -D -m0755 webmin-init %{buildroot}%{_initrddir}/webmin
%{__install} -D -m0644 webmin-pam %{buildroot}%{_sysconfdir}/pam.d/webmin

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/webmin/

echo "rpm" >%{buildroot}%{_libexecdir}/webmin/install-type

### Prepare configuration
export os_type="redhat-linux"
export real_os_type="Redhat Linux"
%{?fc2:export oscheck="Redhat Linux Fedora 2";	export os_version="11.0";	export real_os_version="11.0"}
%{?fc1:export oscheck="Redhat Linux Fedora 1";	export os_version="10.0";	export real_os_version="10.0"}
%{?el3:export oscheck="Redhat Linux 3.0AS";	export os_version="9.0";	export real_os_version="3.0AS"}
%{?rh9:export oscheck="Redhat Linux 9";		export os_version="9.0";	export real_os_version="9.0"}
%{?rh8:export oscheck="Redhat Linux 8.0";	export os_version="8.0";	export real_os_version="8.0"}
%{?rh7:export oscheck="Redhat Linux 7.3";	export os_version="7.3";	export real_os_version="7.3"}
%{?el2:export oscheck="Redhat Linux 2.1AS";	export os_version="7.2";	export real_os_version="2.1AS"}
%{?rh6:export oscheck="Redhat Linux 6.2";	export os_version="6.2";	export real_os_version="6.2"}

export config_dir="%{buildroot}%{_sysconfdir}/webmin"
export var_dir="%{_localstatedir}/webmin"
export perl="%{__perl}"
export autoos=3
export port="10000"
export login="root"
export crypt="x"
export host="localhost"
export ssl=1
export atboot=1
export nochown=1
export autothird=1
export noperlpath=1
export nouninstall=1
export nostart=1
#export password="webmin-admin"
export makeboot=0
%{buildroot}%{_libexecdir}/webmin/setup.sh

### Clean up buildroot
%{__perl} -pi -e 's|%{buildroot}||g' %{buildroot}/etc/webmin/{miniserv.conf,start,stop}
%{__rm} -f %{buildroot}%{_libexecdir}/webmin/{LICENCE*,README*}
%{__rm} -f %{buildroot}%{_libexecdir}/setup.sh

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc LICENCE* README*
%config %{_initrddir}/webmin
%config %{_sysconfdir}/pam.d/webmin
%config %{_sysconfdir}/webmin/
%config(noreplace) %{_sysconfdir}/sysconfig/daemons/webmin
%config(noreplace) %{_sysconfdir}/webmin/config/
%config(noreplace) %{_sysconfdir}/webmin/miniserv.*
%dir %{_localstatedir}/webmin/
%{_libexecdir}/webmin

%post
/sbin/chkconfig --add webmin
/sbin/service webmin start &>/dev/null || :

%preun
if [ $1 -eq 0 ]; then
        /sbin/service webmin stop &>/dev/null || :
        /sbin/chkconfig --del webmin
fi

%postun
/sbin/service webmin condrestart &>/dev/null || :

%changelog
* Sun Jun 06 2004 Dag Wieers <dag@wieers.com> - 1.150-1
- Updated to release 1.150.

* Mon Apr 26 2004 Dag Wieers <dag@wieers.com> - 1.140-1
- Updated to release 1.140.

* Tue Feb 03 2004 Dag Wieers <dag@wieers.com> - 1.060-1
- Initial package. (using DAR)
