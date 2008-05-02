# $Id$
# Authority: dag
# Upstream: Ulric Eriksson <ulric$siag,nu>

Summary: Load balancer for "simple" tcp based protocols
Name: pen
Version: 0.17.3
Release: 1
License: GPL
Group: Applications/Internet
URL: http://siag.nu/pen/

Source: ftp://siag.nu/pub/pen/pen-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Pen is a load balancer for "simple" tcp based protocols such as http or smtp.
It allows several servers to appear as one to the outside and automatically
detects servers that are down and distributes clients among the available
servers. This gives high availability and scalable performance.

%prep
%setup

### FIXME: Added a default pen.httpd for Apache. (Please fix upstream)
%{__cat} <<EOF >pen.httpd
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

%{__install} -Dp -m0755 penctl.cgi %{buildroot}%{_localstatedir}/www/pen/penctl.cgi
%{__install} -Dp -m0644 pen.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/pen.conf

%post
if [ -f %{_sysconfdir}/httpd/conf/httpd.conf ]; then
    if ! grep -q "Include .*/pen.conf" %{_sysconfdir}/httpd/conf/httpd.conf; then
        echo -e "\n# Include %{_sysconfdir}/httpd/conf.d/pen.conf" >> %{_sysconfdir}/httpd/conf/httpd.conf
#       /sbin/service httpd restart
    fi
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING HOWTO NEWS README
%doc %{_mandir}/man1/mergelogs.1*
%doc %{_mandir}/man1/pen.1*
%doc %{_mandir}/man1/penctl.1*
%doc %{_mandir}/man1/penlog.1*
%doc %{_mandir}/man1/penlogd.1*
%dir %{_sysconfdir}/httpd/
%dir %{_sysconfdir}/httpd/conf.d/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/pen.conf
%{_bindir}/mergelogs
%{_bindir}/pen
%{_bindir}/penctl
%{_bindir}/penlog
%{_bindir}/penlogd
%{_localstatedir}/www/pen/
%exclude %{_prefix}/doc/

%changelog
* Fri May 02 2008 Dag Wieers <dag@wieers.com> - 0.17.3-1
- Updated to release 0.17.3.

* Sat Sep 22 2007 Dag Wieers <dag@wieers.com> - 0.17.2-1
- Updated to release 0.17.2.

* Tue Jun 27 2006 Dag Wieers <dag@wieers.com> - 0.17.1-1
- Updated to release 0.17.1.

* Tue Jan 10 2006 Dag Wieers <dag@wieers.com> - 0.17.0-1
- Updated to release 0.17.0.

* Wed Jul 07 2004 Dag Wieers <dag@wieers.com> - 0.15.0-1
- Updated to release 0.15.0.

* Fri Jun 25 2004 Dag Wieers <dag@wieers.com> - 0.14.0-1
- Updated to release 0.14.0.

* Wed Apr 28 2004 Dag Wieers <dag@wieers.com> - 0.13.0-1
- Updated to release 0.13.0.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.12.3-1
- Updated to release 0.12.3.

* Tue Feb 17 2004 Dag Wieers <dag@wieers.com> - 0.12.1-0
- Updated to release 0.12.1.

* Thu Oct 23 2003 Dag Wieers <dag@wieers.com> - 0.12.0-0
- Updated to release 0.12.0.

* Tue Oct 14 2003 Dag Wieers <dag@wieers.com> - 0.11.1-0
- Updated to release 0.11.1.

* Tue Sep 23 2003 Dag Wieers <dag@wieers.com> - 0.11.0-0
- Initial package. (using DAR)
