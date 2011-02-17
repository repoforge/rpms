# $Id$
# Authority: yury
# Upstream: Thomas Ries <tries$users,sourceforge,net>

Name: siproxd
Summary: A SIP masquerading proxy with RTP support
Version: 0.8.0
Release: 4%{?dist}
License: GPL
Group: Applications/Communications
URL: http://siproxd.sourceforge.net/

Source0: http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: /sbin/chkconfig
Requires: /sbin/service

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libosip2-devel >= 3.0.0

%description
Siproxd is a proxy/masquerading daemon for SIP (Session Initiation
Protocol), which is used in IP telephony.
It handles registrations of SIP clients on a private IP network
and performs rewriting of the SIP message bodies to make SIP
connections work via a masquerading firewall (NAT).
It allows SIP software clients (like kphone, linphone) or SIP
hardware clients (Voice over IP phones which are SIP-compatible,
such as those from Cisco, Grandstream or Snom) to work behind
an IP masquerading firewall or NAT router.

%prep
%setup

%build
export CFLAGS="%{optflags}"

%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR="%{buildroot}"

%{__mv} %{buildroot}%{_sysconfdir}/siproxd.conf.example \
   %{buildroot}%{_sysconfdir}/siproxd.conf

# will be added separately below
%{__rm} -rf %{buildroot}%{_defaultdocdir}/%{name}

%{__install} -Dp contrib/siproxd.init %{buildroot}%{_initrddir}/siproxd

# install pid and registration dirs
%{__install} -d %{buildroot}/var/run/siproxd
%{__install} -d %{buildroot}/var/lib/siproxd

%clean
%{__rm} -rf %{buildroot}

%post
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add siproxd
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/service siproxd stop &>/dev/null || :
    /sbin/chkconfig --del siproxd
fi

%postun
if [ $1 -ge 1 ]; then
    /sbin/service siproxd condrestart &>/dev/null || :
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING INSTALL NEWS README RELNOTES TODO ChangeLog
%doc doc/FAQ
%doc doc/FLI4L_HOWTO.txt
%doc doc/RFC3261_compliance.txt
%doc doc/sample_asterisk.txt
%doc doc/sample_cfg_budgetone.txt
%doc doc/sample_cfg_x-lite.txt
%doc doc/siproxd.conf.example
%doc doc/siproxd_guide.sgml
%doc doc/siproxd_passwd.cfg

%config(noreplace) %{_sysconfdir}/siproxd.conf
%config(noreplace) %{_sysconfdir}/siproxd_passwd.cfg
%{_sbindir}/siproxd
%{_initrddir}/siproxd
%{_libdir}/%{name}/

%attr(0700,nobody,root) /var/run/siproxd
%attr(0700,nobody,root) /var/lib/siproxd

%changelog
* Thu Feb 17 2011 Yury V. Zaytsev <yury@shurup.com> - 0.8.0-4
- Cleanup to meet RPMForge standards

* Tue Jan 25 2011 Denis Fateyev <denis@fateyev.com> - 0.8.0-3
- rebuild for rpmforge

* Fri May 21 2010 Denis Fateyev <denis@fateyev.com> - 0.8.0-2
- bump to version 0.8.0

* Thu Nov 05 2009 Denis Fateyev <denis@fateyev.com> - 0.7.2-2
- some spec cleanup for rhel5 support

* Fri Oct 09 2004 Thomas Ries <tries@gmx.net>
- startup script in /etc/rc.d/init.d/siproxd
- create directories for PID and registration files

* Fri Oct 31 2003 Thomas Ries <tries@gmx.net>
- siproxd is now installed to sbin directory

* Fri Oct 24 2003 Thomas Ries <tries@gmx.net>
- added config files and some more doc files
- rename sample config file and remind user to edit it.
- minor cleanup

* Sat Aug 30 2003 Thomas Ries <tries@gmx.net>
- always use /etc as sysconfdir

* Sat Sep 21 2002 Thomas Ries <tries@gmx.net>
- first RPM support
