# $Id$

# Authority: dag
# Upstream: Ulric Eriksson <ulric@siag.nu>

Summary: Load balancer for "simple" tcp based protocols
Name: pen
Version: 0.12.1
Release: 0
License: GPL
Group: Applications/Internet
URL: http://siag.nu/pen/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: ftp://siag.nu/pub/pen/pen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Pen is a load balancer for "simple" tcp based protocols such as http or smtp.
It allows several servers to appear as one to the outside and automatically
detects servers that are down and distributes clients among the available
servers. This gives high availability and scalable performance.

%prep
%setup

### FIXME: Add a default pen.conf for Apache. (Please fix upstream)
%{__cat} <<EOF >%{name}.conf
ScriptAlias /pen/ %{_localstatedir}/www/pen/
<Directory %{_localstatedir}/www/pen/>
	DirectoryIndex penctl.cgi
	Options ExecCGI
	order deny,allow
	deny from all
	allow from 127.0.0.1
</Directory>
EOF

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/www/pen/ \
			%{buildroot}%{_sysconfdir}/httpd/conf.d/
%{__install} -m0755 penctl.cgi %{buildroot}%{_localstatedir}/www/pen/
%{__install} -m0644 pen.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_prefix}/doc/

%post
if [ -f %{_sysconfdir}/httpd/conf/httpd.conf ]; then
        if ! grep -q "Include .*/pen.conf" %{_sysconfdir}/httpd/conf/httpd.conf; then
                echo -e "\n# Include %{_sysconfdir}/httpd/conf.d/pen.conf" >> %{_sysconfdir}/httpd/conf/httpd.conf
#               /sbin/service httpd restart
        fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING HOWTO NEWS README
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/httpd/conf.d/*.conf
%{_bindir}/*
%{_localstatedir}/www/pen/

%changelog
* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.12.1-0
- Updated to release 0.12.1.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.12.0-0
- Updated to release 0.12.0.

* Tue Oct 14 2003 Dag Wieers <dag@wieers.com> - 0.11.1-0
- Updated to release 0.11.1.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.11.0-0
- Initial package. (using DAR)
