# Authority: dag

Summary: A web-based administration interface for Unix systems.
Name: webmin
Version: 1.060
Release: 0
License: BSD
Group: Applications/System
URL: http://www.webmin.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.webmin.com/download/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503, perl(SSLeay)
AutoReq: no

%description
A web-based administration interface for Unix systems. Using Webmin you can
configure DNS, Samba, NFS, local/remote filesystems and more using your
web browser.

After installation, enter the URL http://localhost:10000/ into your
browser and login as root with your root password.

%prep
%setup

%build
(find . -name '*.cgi' ; find . -name '*.pl') | perl perlpath.pl %{__perl} -
%{__rm} -f mount/freebsd-mounts* mount/openbsd-mounts* mount/macos-mounts* webmin-gentoo-init
%{__chmod} -R og-w .

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libexecdir}/webmin \
		%{buildroot}%{_sysconfdir}/webmin \
		%{buildroot}%{_sysconfdir}/sysconfig/daemons \
		%{buildroot}%{_sysconfdir}/pam.d \
		%{buildroot}%{_localstatedir}/webmin \
		%{buildroot}%{_initrddir}
export config_dir="%{buildroot}%{_sysconfdir}/webmin"
export var_dir="%{buildroot}%{_localstatedir}/webmin"
export perl="%{__perl}"
export port=10000
export login=admin
export crypt=12345
export ssl=1
export atboot=1
./setup.sh

%{__cp} -rp * %{buildroot}%{_libexecdir}/webmin/
%{__install} webmin-daemon %{buildroot}%{_sysconfdir}/sysconfig/daemons/webmin
%{__install} webmin-init %{buildroot}%{_initrddir}/webmin
%{__install} webmin-pam %{buildroot}%{_sysconfdir}/pam.d/webmin
echo "rpm" >%{buildroot}%{_libexecdir}/webmin/install-type

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%config %{_sysconfdir}/webmin/
%config %{_sysconfdir}/pam.d/*
%config %{_sysconfdir}/sysconfig/daemons/*
%config %{_initrddir}/webmin
%{_libexecdir}/webmin/

%preun
if [ "$1" = 0 ]; then
        /sbin/service webmin stop > /dev/null 2>&1 || :
        /sbin/chkconfig --del webmin
fi

%post
/sbin/chkconfig --add webmin

%postun
/sbin/service webmin condrestart > /dev/null 2>&1 || :

%changelog
* Sun Feb 09 2003 Dag Wieers <dag@wieers.com> - 1.060
- Initial package.
