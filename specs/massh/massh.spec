# $Id$
# Authority: dag
# Upstream: 

Summary: Parallel shell and copy
Name: massh
%define real_version 1.0-4
Version: 1.0.4
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://m.a.tt/er/massh.html

Source: http://m.a.tt/er/massh-%{real_version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Buildarch: noarch

%description
Massh is a full featured mass ssh'er that can also push files and push/run
scripts on remote hosts.  Ambit is a string set expander or ranged interpolator
used to define sets of hosts that Massh and Pingz can use. Pingz is a mass
pinger/resolver that can use Ambit ranges or files for host sets.

%prep
%setup -n %{name}-1.0

### Put documentation in place
%{__mv} -v usr/local/share/doc/massh/* .

%{__perl} -pi -e '
        s|/usr/local/bin|%{_bindir}|g;
        s|/usr/local/var|%{_localstatedir}|g;
        s|/usr/local/etc|%{_sysconfdir}|g;
' usr/local/bin/* usr/local/etc/* usr/local/share/doc/massh/*

%build

%install
%{__rm} -rf %{buildroot}

%{__install} -Dp -m0755 usr/local/bin/ambit %{buildroot}%{_bindir}/ambit
%{__install} -Dp -m0755 usr/local/bin/massh %{buildroot}%{_bindir}/massh
%{__install} -Dp -m0755 usr/local/bin/pingz %{buildroot}%{_bindir}/pingz

%{__install} -Dp -m0644 usr/local/etc/ambit %{buildroot}%{_sysconfdir}/ambit
%{__install} -Dp -m0644 usr/local/etc/massh %{buildroot}%{_sysconfdir}/massh

%{__install} -d -m0755 %{buildroot}%{_localstatedir}/massh/

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc massh.html massh.txt
%config(noreplace) %{_sysconfdir}/ambit
%config(noreplace) %{_sysconfdir}/massh
%{_bindir}/ambit
%{_bindir}/massh
%{_bindir}/pingz
%dir %{_localstatedir}/massh/

%changelog
* Wed Aug 25 2010 Dag Wieers <dag@wieers.com> - 1.0.4-1
- Updated to release 1.0.4.

* Fri Aug 13 2010 Dag Wieers <dag@wieers.com> - 1.0.3-1
- Initial package. (using DAR)
