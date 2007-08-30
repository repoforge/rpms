# $id$


# Tag: test


%define with_db 1
%define	sbindir	/sbin
%define libdir /lib

Summary: Enhanced system logging and kernel message trapping daemons
Name: rsyslog
Version: 1.19.2
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://www.rsyslog.com/
Source0: http://download.adiscon.com/rsyslog/%{name}-%{version}.tar.gz
Source1: rsyslog.init
Source2: rsyslog.sysconfig
Conflicts: logrotate < 3.5.2
%if %{with_db}
BuildRequires: mysql-devel >= 4.0
%endif
BuildRequires: zlib-devel
Requires: logrotate
Requires: bash >= 2.0
Requires(post): /sbin/chkconfig coreutils
Requires(preun): /sbin/chkconfig /sbin/chkconfig
Requires(postun): /sbin/service
Provides: syslog
Provides: sysklogd = 1.4.3-1
Obsoletes: sysklogd < 1.4.3-1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Rsyslog is an enhanced multi-threaded syslogd supporting, among others, MySQL,
syslog/tcp, RFC 3195, permitted sender lists, filtering on any message part,
and fine grain output format control. It is quite compatible to stock sysklogd
and can be used as a drop-in replacement. Its advanced features make it 
suitable for enterprise-class, encryption protected syslog relay chains while 
at the same time being very easy to setup for the novice user.


%prep
%setup -q

%build
%configure --sbindir=%{sbindir} --enable-mysql --libdir=%{libdir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install -d -m 755 $RPM_BUILD_ROOT%{_initrddir}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/rsyslog
install -p -m 644 redhat/rsyslog.conf $RPM_BUILD_ROOT%{_sysconfdir}/rsyslog.conf
install -p -m 644 redhat/rsyslog.log $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/rsyslog
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/rsyslog

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ $1 = 1 ]; then
	/sbin/chkconfig --add rsyslog
fi
for n in /var/log/{messages,secure,maillog,spooler}
do
	[ -f $n ] && continue
	umask 066 && touch $n
done
#use sysklogd configuration files
if [ -f /etc/syslog.conf ]; then
	mv -f /etc/rsyslog.conf /etc/rsyslog.conf.rpmnew
	mv -f /etc/syslog.conf  /etc/rsyslog.conf
fi
if [ -f /etc/sysconfig/syslog ]; then
	mv -f /etc/sysconfig/rsyslog /etc/sysconfig/rsyslog.rpmnew
	mv -f /etc/sysconfig/syslog  /etc/sysconfig/rsyslog
fi

%preun
if [ $1 = 0 ]; then
	service rsyslog stop >/dev/null 2>&1 ||:
	/sbin/chkconfig --del rsyslog
fi

%postun
if [ "$1" -ge "1" ]; then
	service rsyslog condrestart > /dev/null 2>&1 ||:
fi	

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING INSTALL NEWS README doc
%config(noreplace) %{_sysconfdir}/rsyslog.conf
%config(noreplace) %{_sysconfdir}/sysconfig/rsyslog
%config(noreplace) %{_sysconfdir}/logrotate.d/rsyslog
%{_initrddir}/rsyslog
%{sbindir}/rsyslogd
%{sbindir}/rklogd
%{sbindir}/rfc3195d
%{_mandir}/*/*

%package mysql
Group: System Environment/Daemons
Summary: MySQL plugin for rsyslog
Requires: %{name} = %{version}

%description mysql
MySQL output module for rsyslog

%files mysql
%defattr(-,root,root,-)
%{libdir}/%{name}/ommysql.so*
%exclude %{libdir}/%{name}/*.a
%exclude %{libdir}/%{name}/*.la

%changelog
* Mon Aug 28 2007 Michael Mansour <mic@npgx.com.au> 1.19.2-1
- upstream bugfix release

* Mon Aug 23 2007 Michael Mansour <mic@npgx.com.au> 1.19.1-1
- upstream bugfix and enhancement release

* Mon Aug 16 2007 Michael Mansour <mic@npgx.com.au> 1.19.0-1
- supports dynamically loading of output plug-ins
- the MySQL output module has been converted into a loadable plug-in
- two RPM packages are now created, rsyslog and rsyslog-mysql

* Mon Aug 13 2007 Michael Mansour <mic@npgx.com.au> 1.18.2-1
- upstream bugfix release

* Mon Aug 9 2007 Michael Mansour <mic@npgx.com.au> 1.18.1-1
- upstream bugfix release

* Mon Aug 4 2007 Michael Mansour <mic@npgx.com.au> 1.18.0-1
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
