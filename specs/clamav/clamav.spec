# $Id$

%{!?_without_milter: %{expand: %%define milter 1}}
%{?_without_milter:  %{expand: %%define milter 0}}

Name:			clamav
Summary:		An anti-virus utility for Unix.
Version:		0.60
Release:		4
Source0:		%{name}-%{version}.tar.gz
Source1:		%{name}-%{version}.tar.gz.sig
Source2:		%{name}.init.bz2
Source3:		%{name}-milter.init.bz2
Source4:		%{name}-milter.sysconfig.bz2
Source5:		freshclam.cron.bz2
Source6:		freshclam.logrotate.bz2
Source7:		%{name}.logrotate.bz2
Patch0:			%{name}-%{version}-config.patch.bz2
URL:			http://clamav.elektrapro.com/
License:		GPL
Group:			Applications/System
Requires:		%{name}-db = %{version}-%{release}
BuildRequires:		bzip2-devel zlib-devel
%if %{milter}
BuildRequires:		sendmail-devel
%endif
Obsoletes:		lib%{name} = 0.54	
Provides:		lib%{name}
BuildRoot:		%{_tmppath}/%{name}-%{version}-root

%description 
Clam Antivirus is a powerful anti-virus scanner for Unix. It
supports AMaViS, compressed files, uses the virus database from
OpenAntivirus.org, and includes a program for auto-updating.

The scanner is multithreaded, written in C, and POSIX compliant. 

Available rpmbuild rebuild options :
--without : milter

%package -n		clamd
Summary:		The Clam AntiVirus Daemon
Group:			System Environment/Daemons
License: 		GPL
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-db = %{version}-%{release}

%description -n		clamd
The Clam AntiVirus Daemon

%package -n		%{name}-milter
Summary:		The Clam AntiVirus sendmail-milter Daemon
Group:			Applications/System
License: 		GPL
Requires:		%{name} = %{version}-%{release}
Requires:		%{name}-db = %{version}-%{release}
Requires:		clamd = %{version}-%{release}
Requires:		sendmail

%description -n		%{name}-milter
The Clam AntiVirus sendmail-milter Daemon

%package		db
Summary:		Virus database for %{name}
Group:			Applications/Databases
License: 		GPL

%description		db
The actual virus database for %{name}

%package devel
Summary:		Headers and static libarys for Development
Group:			Development/Libraries
License:		GPL
Requires:		%{name} = %{version}-%{release}
Obsoletes:		lib%{name}-static-devel = 0.54 
Obsoletes:		lib%{name}-devel = 0.54
Provides:		lib%{name}-static-devel lib%{name}-devel

%description devel
Headers and static libarys for Development


%prep
%setup -q
%patch0 -p0

bzcat %{SOURCE2} > clamd.init
bzcat %{SOURCE3} > %{name}-milter.init
bzcat %{SOURCE4} > %{name}-milter.sysconfig
bzcat %{SOURCE5} > freshclam.cron
bzcat %{SOURCE6} > freshclam.logrotate
bzcat %{SOURCE7} > %{name}.logrotate

%build
%configure  \
	--program-prefix=%{?_program_prefix} \
	%if %{milter}
	--enable-milter \
	%endif
	--disable-%{name} \
	--with-user=%{name} \
	--with-group=%{name} \
	--with-dbdir=%{_localstatedir}/%{name}
%{__make}

%install
rm -rf %{buildroot}
make DESTDIR="%{buildroot}" install

# install the init scripts
install -d %{buildroot}%{_initrddir}
install -m755 clamd.init %{buildroot}%{_initrddir}/clamd
%if %{milter}
install -m755 %{name}-milter.init %{buildroot}%{_initrddir}/%{name}-milter
%endif

# install the milter config
%if %{milter}
install -d %{buildroot}%{_sysconfdir}/sysconfig
install -m644 %{name}-milter.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/%{name}-milter
%endif

# install the cron script to auto update the virus database 
install -d %{buildroot}%{_sysconfdir}/cron.daily
install -m755 freshclam.cron %{buildroot}%{_sysconfdir}/cron.daily/freshclam

# install the logrotate stuff
install -d %{buildroot}%{_sysconfdir}/logrotate.d
install -m644 freshclam.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/freshclam
install -m644 %{name}.logrotate %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

install -d %{buildroot}/var/log/%{name}
touch %{buildroot}/var/log/%{name}/freshclam.log
touch %{buildroot}/var/log/%{name}/%{name}.log

# huh? a bug?
install -m644 etc/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}.conf

# pid file dir
install -d %{buildroot}/var/run/%{name}

%pre -n clamd
/usr/sbin/groupadd -r clamav 2>/dev/null || :
/usr/sbin/useradd -r -d /var/clamav  -s /sbin/nologin -c "Clam Anti Virus Checker" -g clamav clamav 2>/dev/null || :

%post -n clamd
if [ $1 = 1 ]; then /sbin/chkconfig --add clamd; else if [ -f /var/lock/subsys/clamd ]; then service clamd restart > /dev/null 2>/dev/null || : ; fi; fi;

%preun -n clamd
if [ $1 = 0 ]; then service clamd stop > /dev/null 2>/dev/null || :; /sbin/chkconfig --del clamd; fi;

%post -n %{name}-milter
if [ $1 = 1 ]; then /sbin/chkconfig --add clamav-milter; else if [ -f /var/lock/subsys/clamav-milter ]; then service clamav-milter restart > /dev/null 2>/dev/null || : ; fi; fi;
                                                                               
%preun -n %{name}-milter
if [ $1 = 0 ]; then service clamav-milter stop > /dev/null 2>/dev/null || :; /sbin/chkconfig --del clamav-milter; fi;

%pre -n %{name}-db
/usr/sbin/groupadd -r clamav 2>/dev/null || :
/usr/sbin/useradd -r -d /var/clamav  -s /sbin/nologin -c "Clam Anti Virus Checker" -g clamav clamav 2>/dev/null || : 

%post -n %{name} -p /sbin/ldconfig
%postun -n %{name} -p /sbin/ldconfig

%post -n %{name}-db -p /sbin/ldconfig
%postun -n %{name}-db -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog FAQ NEWS README TODO test
%doc docs/DMS/Debian_Mail_server.html 
%doc docs/clamdoc.*
%doc docs/html
%doc docs/Japanese
%doc docs/Spanish
%{_bindir}/clamscan
%{_bindir}/freshclam
%{_bindir}/sigtool
%{_mandir}/man1/sigtool.1*
%{_mandir}/man1/clamscan.1*
%{_mandir}/man1/freshclam.1*
%{_libdir}/*.so.*

%files -n clamd
%defattr(-,root,root)
%attr(0644,root,root) %config %{_sysconfdir}/%{name}.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%attr(0755,root,root) %config(noreplace) %{_initrddir}/clamd
%{_sbindir}/clamd
%{_bindir}/clamdscan
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/clamd.8*
%{_mandir}/man1/clamdscan.1*
%dir %attr(0755,%{name},%{name}) /var/run/%{name}
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/%{name}
%attr(0644,%{name},%{name}) /var/log/%{name}/%{name}.log

%if %{milter}
%files -n %{name}-milter
%defattr(-,root,root)
%doc %{name}-milter/INSTALL
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/%{name}-milter
%attr(0755,root,root) %config(noreplace) %{_initrddir}/%{name}-milter
%{_sbindir}/%{name}-milter
%{_mandir}/man1/%{name}-milter.1*
%endif

%files -n %{name}-db
%defattr(-,root,root)
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/cron.daily/freshclam
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/logrotate.d/freshclam
%dir %attr(0755,%{name},%{name}) %{_localstatedir}/%{name}
%attr(0644,%{name},%{name}) %config(noreplace) %{_localstatedir}/%{name}/viruses.db*
%attr(0644,%{name},%{name}) %config(noreplace) %{_localstatedir}/%{name}/mirrors.txt
%attr(0644,%{name},%{name}) /var/log/%{name}/freshclam.log

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/*.a

%changelog
* Mon Aug 22 2003 Matthias Saou/Che
- Added "--without milter" build option. (Matthias Saou)
- Fixed freshclam cron (Matthias Saou)
- Built the new package. (Che)

* Tue Jun 24 2003 Che
- clamav-milter introduced.
- a few more smaller fixes.

* Sun Jun 22 2003 Che
- version upgrade

* Mon Jun 16 2003 Che
- rh9 build
- various fixes
- got rid of rpm-helper prereq

* Fri Mar 24 2003 Che
- some cleanups and fixes
- new patch added

* Fri Nov 22 2002 Che
- fixed a config patch issue

* Fri Nov 22 2002 Che
- version upgrade and some fixes

* Sat Nov 02 2002 Che
- version upgrade

* Wed Oct 24 2002 Che
- some important changes for lsb compliance

* Wed Oct 23 2002 Che
- initial rpm release
