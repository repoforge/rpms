# $Id$
# Authority: dag
# Upstream: <users@conserver.com>
# Upstream: Bryan Stansell <bryan@conserver.com>

### FIXME: Add sysv script using sysconfig file.

Summary: Serial console server daemon/client
Name: conserver
Version: 8.1.7
Release: 1
License: BSD style
Group: System Environment/Daemons
URL: http://www.conserver.com/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.conserver.com/conserver-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Conserver is an application that allows multiple users to watch a
serial console at the same time.  It can log the data, allows users to
take write-access of a console (one at a time), and has a variety of
bells and whistles to accentuate that basic functionality.

%prep
%setup

### FIXME: We don't want to install the solaris conserver.rc file.
%{__perl} -pi.orig -e 's|^.*conserver\.rc.*$||' conserver/Makefile.in

%build
%configure \
	--with-master="console"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__install} -D -m0644 conserver.cf/conserver.cf %{buildroot}%{_sysconfdir}/conserver.cf
%{__install} -D -m0600 conserver.cf/conserver.passwd %{buildroot}%{_sysconfdir}/conserver.passwd
%{__install} -D -m0755 contrib/redhat-rpm/conserver.init %{buildroot}%{_initrddir}/conserver

%post
/sbin/chkconfig --add conserver
if ! egrep -q '\<conserver\>' /etc/services; then
	echo "console		782/tcp		conserver" >> /etc/services
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/service conserver stop &>/dev/null || :
	/sbin/chkconfig --del conserver
fi

#%postun
#/sbin/service conserver condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES FAQ INSTALL README conserver.cf/
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/conserver.*
%config %{_initrddir}/*
%{_bindir}/*
%{_sbindir}/*
%exclude %{_datadir}/examples/

%changelog
* Sat May 29 2004 Dag Wieers <dag@wieers.com> - 8.1.7-1
- Updated to release 8.1.7.

* Thu May 27 2004 Dag Wieers <dag@wieers.com> - 8.1.6-1
- Updated to release 8.1.6.

* Tue May 11 2004 Dag Wieers <dag@wieers.com> - 8.1.5-1
- Updated to release 8.1.5.

* Thu Apr 15 2004 Dag Wieers <dag@wieers.com> - 8.1.4-1
- Updated to release 8.1.4.

* Fri Mar 26 2004 Dag Wieers <dag@wieers.com> - 8.1.3-1
- Updated to release 8.1.3.

* Sat Mar 13 2004 Dag Wieers <dag@wieers.com> - 8.1.2-0
- Updated to release 8.1.2.

* Fri Dec 12 2003 Dag Wieers <dag@wieers.com> - 8.0.9-0
- Updated to release 8.0.9.

* Sun Nov 23 2003 Dag Wieers <dag@wieers.com> - 8.0.7-0
- Updated to release 8.0.7.

* Mon Oct 13 2003 Dag Wieers <dag@wieers.com> - 8.0.1-1
- Fixed a %%post problem.

* Wed Oct 01 2003 Dag Wieers <dag@wieers.com> - 8.0.1-0
- Updated to release 8.0.1.

* Mon Sep 15 2003 Dag Wieers <dag@wieers.com> - 7.2.7-0
- Initial package. (using DAR)
