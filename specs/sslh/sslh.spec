# $Id$
# Authority: dag

Summary: ssl/ssh multiplexer
Name: sslh
Version: 1.7a
Release: 1%{?dist}
License: GPL
Group: System Environment/Shells
URL: http://www.rutschle.net/tech/sslh.shtml

Source: http://www.rutschle.net/tech/sslh-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
sslh lets one accept both HTTPS and SSH connections on the same port.
sslh makes it possible to connect to an SSH server on port 443 (e.g. from
inside a corporate firewall) while still serving HTTPS on that port.

%prep
%setup

%build
%{__cc} %{optflags} -DLIBWRAP -lwrap -o sslh sslh.c

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 sslh %{buildroot}%{_sbindir}/sslh

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
%config %{_initrddir}/sslh
%config(noreplace) %{_sysconfdir}/sysconfig/sslh
%{_sbindir}/sslh

%changelog
* Sun Jul 04 2010 Dag Wieers <dag@wieers.com> - 1.7a-1
- Initial package. (using DAR)
