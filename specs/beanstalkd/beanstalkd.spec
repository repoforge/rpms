# $Id$
# Authority: shuff
# Upstream: Keith Rarick <kr$xph,us>

Summary: Simple, fast workqueue service
Name: beanstalkd
Version: 1.4.4
Release: 1%{?dist}
License: GPL
Group: System Environment/Daemons
URL: http://kr.github.com/beanstalkd/

Source: http://xph.us/dist/beanstalkd/beanstalkd-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: binutils, gcc, make
BuildRequires: glibc-devel
BuildRequires: libevent-devel >= 1.4.1
Requires: chkconfig, initscripts

%description
Beanstalk is a simple, fast workqueue service. Its interface is generic, but
was originally designed for reducing the latency of page views in high-volume
web applications by running time-consuming tasks asynchronously.


%prep
%setup

%build
%configure --disable-dependency-tracking
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%{__rm} -rf %{buildroot}
# install the binary
%{__install} -m0755 -d %{buildroot}%{_bindir}
%{__install} -m0755 beanstalkd %{buildroot}%{_bindir}
# install the man pages
%{__install} -m0755 -d %{buildroot}%{_mandir}/man1
%{__gzip} doc/beanstalkd.1
%{__install} -m0644 doc/beanstalkd.1.gz %{buildroot}%{_mandir}/man1
# install the sysconfig
%{__install} -m0755 -d %{buildroot}%{_sysconfdir}/sysconfig
%{__install} -m0644 scripts/beanstalkd.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/beanstalkd
# install the init script
%{__install} -m0755 -d %{buildroot}%{_initrddir}
%{__install} -m0755 scripts/beanstalkd.init %{buildroot}%{_initrddir}/beanstalkd

%clean
%{__rm} -rf %{buildroot}

%post
if [ "$1" -eq 1 ]; then
    /usr/sbin/useradd -r beanstalkd 2>&1 >/dev/null
    /sbin/chkconfig --add beanstalkd 2>&1 >/dev/null
    exit 0
fi

%preun
if [ "$1" -eq 0 ]; then
    /sbin/service beanstalkd stop 2>&1 >/dev/null
    /sbin/chkconfig --del beanstalkd 2>&1 >/dev/null
    /usr/sbin/userdel -rf beanstalkd 2>&1 >/dev/null
    exit 0
fi

%files
%defattr(-, root, root, 0755)
%doc COPYING README README-DEVELOPERS README-TESTS TODO
%doc doc/protocol.txt
%doc %{_mandir}/man?/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/*
%{_initrddir}/*

%changelog
* Wed Apr 07 2010 Steve Huff <shuff@vecna.org> - 1.4.4-1
- Initial package.
