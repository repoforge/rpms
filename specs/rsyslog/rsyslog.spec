# $Id$
# Authority: dag

# Rationale: This package is part of RHEL5

# ExclusiveDist: el2 rh7 rh9 el3 el4

%{?el3:%define _without_mysql4 1}
%{?rh9:%define _without_mysql4 1}
%{?rh7:%define _without_mysql4 1}
%{?el2:%define _without_mysql4 1}

%define _sbindir /sbin

Summary: Enhanced system logging and kernel message trapping daemons
Name: rsyslog
Version: 2.0.0
Release: 0.11
License: GPLv2+
Group: System Environment/Daemons
URL: http://www.rsyslog.com/

Source0: http://download.rsyslog.com/rsyslog/rsyslog-%{version}.tar.gz
Source1: rsyslog.init
Source2: rsyslog.sysconfig
Source3: syslog.log
Patch1: rsyslog-2.0.0-sockhang.patch
Patch2: rsyslog-2.0.0-forwardMsg.patch
Patch3: rsyslog-2.0.0-manPage.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf >= 1.10
BuildRequires: automake
BuildRequires: libtool
BuildRequires: zlib-devel
%{!?_without_mysql4:BuildRequires: mysql-devel >= 4.0}
Requires: logrotate >= 3.5.2
Requires: bash >= 2.0
Requires(post): /sbin/chkconfig coreutils
Requires(preun): /sbin/chkconfig /sbin/service
Requires(postun): /sbin/service
Provides: syslog
#Conflicts: sysklogd < 1.4.1-43
### A lot of packages depend on sysklogd, we provide this for RHEL4 and older
Provides: sysklogd

%package mysql
Summary: MySQL support for rsyslog
Group: System Environment/Daemons
Requires: %{name} = %{version}-%{release}

%description
Rsyslog is an enhanced multi-threaded syslogd supporting, among others, MySQL,
syslog/tcp, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is quite compatible to stock sysklogd
and can be used as a drop-in replacement. Its advanced features make it 
suitable for enterprise-class, encryption protected syslog relay chains while 
at the same time being very easy to setup for the novice user.


%description mysql
The rsyslog-mysql package contains a dynamic shared object that will add
MySQL database support to rsyslog.

%prep
%setup
%patch1 -p1 -b .sockHang
%patch2 -p1 -b .forwardMsg
%patch3 -p1 -b .manPage

%build
export CFLAGS="%{optflags} -DHAVE_DECL_STRERROR_R -DSTRERROR_R_CHAR_P"
%configure --disable-static --enable-mysql
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m0644 redhat/rsyslog.conf %{buildroot}%{_sysconfdir}/rsyslog.conf
%{__install} -Dp -m0755 %{SOURCE1} %{buildroot}%{_initrddir}/rsyslog
%{__install} -Dp -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/rsyslog
%{__install} -Dp -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/syslog

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/chkconfig --add rsyslog
for log in /var/log/{messages,secure,maillog,spooler}; do
    [ -f $log ] && continue
    umask 066 && touch $log
done

%preun
if [ $1 -eq 0 ]; then
    service rsyslog stop &>/dev/null ||:
    /sbin/chkconfig --del rsyslog
fi

%postun
if [ $1 -ge 1 ]; then
    service rsyslog condrestart &>/dev/null ||:
fi

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README doc/*html
%doc %{_mandir}/man5/rsyslog.conf.5*
%doc %{_mandir}/man8/rfc3195d.8*
%doc %{_mandir}/man8/rklogd.8*
%doc %{_mandir}/man8/rsyslogd.8*
%config(noreplace) %{_sysconfdir}/logrotate.d/syslog
%config(noreplace) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/rsyslog
%config %{_initrddir}/rsyslog
%dir %{_libdir}/rsyslog/
%{_sbindir}/rfc3195d
%{_sbindir}/rklogd
%{_sbindir}/rsyslogd

%if %{!?_without_mysql4:1}0
%files mysql
%defattr(-, root, root, 0755)
%doc plugins/ommysql/createDB.sql
%dir %{_libdir}/rsyslog/
%{_libdir}/rsyslog/ommysql.so
%exclude %{_libdir}/rsyslog/*.la
%endif

%changelog
* Thu Oct 02 2008 Dag Wieers <dag@wieers.com> - 2.0.0-0.11
- Initial package. (based on RHEL5)

* Thu Feb 07 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-11
- spec file adjustment
  Resolves: #431070

* Thu Feb 07 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-10
- fix documentation problems
- init sript fixes
  Resolves: #431070, #431583

* Wed Jan 23 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-9
- do not use autoconf in order to build it on RHEL5,
  Resolves: #178855

* Tue Jan 22 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-8
- strerror fix,
  Resolves: #178855
 
* Mon Jan 21 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-7
- change from requires sysklogd to conflicts sysklogd

* Fri Jan 18 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-6
- change logrotate file
- use rsyslog own pid file

* Thu Jan 17 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-5
- fixing bad descriptor (#428775)

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-4
- rename logrotate file

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-3
- fix post script and init file

* Wed Jan 16 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-2
- change pid filename and use logrotata script from sysklogd

* Tue Jan 15 2008 Peter Vrabec <pvrabec@redhat.com> 2.0.0-1
- upgrade to stable release
- spec file clean up

* Wed Jan 02 2008 Peter Vrabec <pvrabec@redhat.com> 1.21.2-1
- new upstream release

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.19.11-2
- Rebuild for deps

* Thu Nov 29 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.11-1
- new upstream release
- add conflicts (#400671)

* Mon Nov 19 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.10-1
- new upstream release

* Wed Oct 03 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.6-3
- remove NUL character from recieved messages

* Tue Sep 25 2007 Tomas Heinrich <theinric@redhat.com> 1.19.6-2
- fix message suppression (303341)

* Tue Sep 25 2007 Tomas Heinrich <theinric@redhat.com> 1.19.6-1
- upstream bugfix release

* Tue Aug 28 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.2-1
- upstream bugfix release
- support for negative app selector, patch from 
  theinric@redhat.com

* Fri Aug 17 2007 Peter Vrabec <pvrabec@redhat.com> 1.19.0-1
- new upstream release with MySQL support(as plugin)

* Wed Aug 08 2007 Peter Vrabec <pvrabec@redhat.com> 1.18.1-1
- upstream bugfix release

* Mon Aug 06 2007 Peter Vrabec <pvrabec@redhat.com> 1.18.0-1
- new upstream release

* Thu Aug 02 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.6-1
- upstream bugfix release

* Mon Jul 30 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.5-1
- upstream bugfix release
- fix typo in provides 

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 1.17.2-4
- rebuild for toolchain bug

* Tue Jul 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-3
- take care of sysklogd configuration files in %%post

* Tue Jul 24 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-2
- use EVR in provides/obsoletes sysklogd

* Mon Jul 23 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.2-1
- upstream bug fix release

* Fri Jul 20 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.1-1
- upstream bug fix release
- include html docs (#248712)
- make "-r" option compatible with sysklogd config (248982)

* Tue Jul 17 2007 Peter Vrabec <pvrabec@redhat.com> 1.17.0-1
- feature rich upstream release

* Thu Jul 12 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.1-2
- use obsoletes and hadle old config files

* Wed Jul 11 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.1-1
- new upstream bugfix release

* Tue Jul 10 2007 Peter Vrabec <pvrabec@redhat.com> 1.15.0-1
- new upstream release introduce capability to generate output 
  file names based on templates

* Tue Jul 03 2007 Peter Vrabec <pvrabec@redhat.com> 1.14.2-1
- new upstream bugfix release

* Mon Jul 02 2007 Peter Vrabec <pvrabec@redhat.com> 1.14.1-1
- new upstream release with IPv6 support

* Tue Jun 26 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-3
- add BuildRequires for  zlib compression feature

* Mon Jun 25 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-2
- some spec file adjustments.
- fix syslog init script error codes (#245330)

* Fri Jun 22 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.5-1
- new upstream release

* Fri Jun 22 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.4-2
- some spec file adjustments.

* Mon Jun 18 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.4-1
- upgrade to new upstream release

* Wed Jun 13 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.2-2
- DB support off

* Tue Jun 12 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.2-1
- new upstream release based on redhat patch

* Fri Jun 08 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.1-2
- rsyslog package provides its own kernel log. daemon (rklogd)

* Mon Jun 04 2007 Peter Vrabec <pvrabec@redhat.com> 1.13.1-1
- Initial rpm build
