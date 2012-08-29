# $Id$
# Authority: dag

%{?el5:%define _without_libwrap 1}

Summary: ssl/ssh multiplexer
Name: sslh
Version: 1.12
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://www.rutschle.net/tech/sslh.shtml

Source: http://www.rutschle.net/tech/sslh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#%{!?_without_libwrap:BuildRequires: tcpwrapper-devel}
#BuildRequires: tcp_wrappers
#BuildRequires: tcp_wrappers-devel

%description
sslh lets one accept both HTTPS and SSH connections on the same port.
sslh makes it possible to connect to an SSH server on port 443 (e.g. from
inside a corporate firewall) while still serving HTTPS on that port.

%prep
%setup

%build
#%{__cc} %{optflags} -DLIBWRAP -lwrap -o sslh sslh.c
%{__make} %{?_smp_mflags} USELIBWRAP=%{!?_without_libwrap:y} USELIBCONFIG=

%install
%{__rm} -rf %{buildroot}
#%{__make} install DESTDIR="%{buildroot}"
#%{__install} -Dp -m0755 sslh %{buildroot}%{_sbindir}/sslh
%{__install} -Dp -m0755 sslh-fork %{buildroot}%{_sbindir}/sslh
%{__install} -Dp -m0644 sslh.8.gz %{buildroot}%{_mandir}/man8/sslh.8.gz

### FIXME: Fix initscript to use success / fail
%{__install} -Dp -m0644 scripts/etc.default.sslh %{buildroot}%{_sysconfdir}/sysconfig/sslh
%{__install} -Dp -m0755 scripts/etc.rc.d.init.d.sslh.centos %{buildroot}%{_initrddir}/sslh

%post
/sbin/chkconfig --add sslh

%preun
if [ $1 -eq 0 ]; then
    /sbin/service sslh stop &>/dev/null || :
    /sbin/chkconfig --del sslh
fi

%postun
/sbin/service sslh condrestart &>/dev/null || :

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog README
%doc %{_mandir}/man8/sslh.8*
%config %{_initrddir}/sslh
%config(noreplace) %{_sysconfdir}/sysconfig/sslh
%{_sbindir}/sslh

%changelog
* Fri May 11 2012 Dag Wieers <dag@wieers.com> - 1.12-1
- Updated to release 1.12.

* Sun Jul 04 2010 Dag Wieers <dag@wieers.com> - 1.7a-1
- Initial package. (using DAR)
