# $Id$
# Authority: cheusov
# Upstream:  Aleksey Cheusov <vle$gmx,net>

Summary: DICT protocol (RFC 2229) server and command-line client
Name: dict
Version: 1.12.0
Release: 1%{?dist}
License: GPL+ and zlib and MIT
Group: Applications/Internet
URL: http://www.dict.org/

Source0: http://dl.sf.net/dict/dictd-%{version}.tar.gz
Source1: dictd.init
Source2: dictd.sysconfig
Source3: dictd.conf
Source4: dict.conf
BuildRoot: %{_tmppath}/dictd-%{version}-%{release}-root

BuildRequires: byacc
BuildRequires: flex
BuildRequires: gawk
BuildRequires: libmaa-devel
BuildRequires: libtool
BuildRequires: shadow-utils
BuildRequires: zlib-devel

%description
Command-line client for the DICT protocol.  The Dictionary Server
Protocol (DICT) is a TCP transaction based query/response protocol that
allows a client to access dictionary definitions from a set of natural
language dictionary databases.

%package server
Summary: Server for the Dictionary Server Protocol (DICT)
Group: System Environment/Daemons
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(postun): initscripts
Requires: m4

%description server
A server for the DICT protocol. You need to install dictd-usable databases
befor you can use this server. Those can be found p.e. at 
ftp://ftp.dict.org/pub/dict/pre/
More information can be found in the INSTALL file in this package.

%prep
%setup -n dictd-%{version}

%build
%configure --disable-plugin
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%{__install} -Dp -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/rc.d/init.d/dictd
%{__install} -Dp -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/dictd
%{__install} -Dp -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/dictd.conf
%{__install} -Dp -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/dict.conf

%clean
%{__rm} -rf %{buildroot}

%post server
if [ $1 -eq 1 ]; then
    /usr/sbin/groupadd -f -r dictd
    /usr/sbin/useradd -d %{_datadir}/dictd -g dictd -r -s /bin/false dictd
    /sbin/chkconfig --add dictd
fi

%preun server
if [ $1 -eq 0 ]; then
    /etc/rc.d/init.d/dictd stop &>/dev/null || :
    /sbin/chkconfig --del dictd
    /usr/sbin/userdel dictd
    /usr/sbin/groupdel dictd
fi

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README TODO doc/rfc2229.txt
%doc examples/dict1.conf
%doc %{_mandir}/man1/colorit.1*
%doc %{_mandir}/man1/dict.1*
%doc %{_mandir}/man1/dict_lookup.1*
%doc %{_mandir}/man1/dictl.1*
%config(noreplace) %{_sysconfdir}/dict.conf
%{_bindir}/colorit
%{_bindir}/dict
%{_bindir}/dict_lookup
%{_bindir}/dictl

%files server
%doc ChangeLog COPYING NEWS README TODO doc/rfc2229.txt
%doc examples/dictd*
%doc %{_mandir}/man1/dictfmt*
%doc %{_mandir}/man1/dictun*
%doc %{_mandir}/man1/dictzip*
%doc %{_mandir}/man8/dictd*
%config %{_initrddir}/*
%config(noreplace) %{_sysconfdir}/sysconfig/dictd
%config(noreplace) %{_sysconfdir}/dictd.conf
%{_bindir}/dictfmt*
%{_bindir}/dictun*
%{_bindir}/dictzip*
%{_sbindir}/dictd

%changelog
* Sun Jan 29 2012 Aleksey Cheusov <vle@gmx.net> - 1.12.0-1
- Reworked for repoforge
- New dict.conf, dictd.conf and /etc/sysconfig/dictd

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 04 2011 Karsten Hopp <karsten@redhat.com> 1.12.0-1
- update to version 1.12.0
- split into server and client packages
- add most of Oron Peled's <oron@actcom.co.il> changes from
  https://bugzilla.redhat.com/attachment.cgi?id=381332
  - The daemon now runs as 'dictd' user. This user is added/remove
    during install/uninstall.
  - Create and own a default configuration file
  - By default listen only on 127.0.0.1 (secure by default)
  - Default directory for dictionaries (datadir) is
    now /usr/share/dict/dictd and not /usr/share
  - Add the examples directory to the documentation

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 28 2009 Karsten Hopp <karsten@redhat.com> 1.11.0-3
- add disttag

* Thu Jan 22 2009 Karsten Hopp <karsten@redhat.com> 1.11.0-2
- add postun script (#225694)
- fix file permissions (defattr)

* Wed Jan 14 2009 Karsten Hopp <karsten@redhat.com> 1.11.0-1
- update

* Wed Jul 16 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.10.11-3
- fix license tag

* Wed May 07 2008 Karsten Hopp <karsten@redhat.com> 1.10.11-2
- update to 1.10.11

* Tue Apr 01 2008 Karsten Hopp <karsten@redhat.com> 1.10.10-1
- fix typo (#281981)
- update

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.10.9-2
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Karsten Hopp <karsten@redhat.com> 1.10.9-1
- new upstream version

* Wed Aug 22 2007 Karsten Hopp <karsten@redhat.com> 1.9.15-11
- update license tag and rebuild

* Mon Aug 13 2007 Karsten Hopp <karsten@redhat.com> 1.9.15-10
- add LSB stuff (#246910)

* Wed Feb 21 2007 Karsten Hopp <karsten@redhat.com> 1.9.15-9
- misc. merge review fixes

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.9.15-8.1
- rebuild

* Mon May 22 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-8
- buildrequires zlib-devel

* Thu May 18 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-7
- Buildrequires: libdbi-devel

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-6
- BuildRequires: byacc

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.9.15-5.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.9.15-5.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan 02 2006 Karsten Hopp <karsten@redhat.de> 1.9.15-5
- add BuildRequires libtool-ltdl-devel (#176505)

* Tue Dec 20 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-4
- consult dict.org if no server is specified on the commandline
  (#176038)

* Mon Dec 12 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-3
- rebuild with gcc-4.1

* Tue Jul 12 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-2
- Buildrequires libtool (ltdl.h)

* Wed Jul 06 2005 Karsten Hopp <karsten@redhat.de> 1.9.15-1
- update to dictd-1.9.15
- drop gcc34 patch

* Mon May 02 2005 Karsten Hopp <karsten@redhat.de> 1.9.7-9
- use _bindir / _sysconfdir macros

* Sat Apr 02 2005 Florian La Roche <laroche@redhat.com>
- /etc/init.d -> /etc/rc.d/init.d


* Thu Mar 10 2005 Bill Nottingham <notting@redhat.com> 1.9.7-7
- prereq chkconfig

* Wed Mar 02 2005 Karsten Hopp <karsten@redhat.de> 1.9.7-6
- build with gcc-4

* Tue Jan 25 2005 Karsten Hopp <karsten@redhat.de> 1.9.7-5
- don't install config file, leave it to the dictionary packages to
  populate it. (#135920)

* Mon Oct 04 2004 Karsten Hopp <karsten@redhat.de> 1.9.7-4
- add initscript

* Sat Jun 19 2004 Karsten Hopp <karsten@redhat.de> 1.9.7-3
- fix build with gcc34

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 02 2004 Karsten Hopp <karsten@redhat.de> 1.9.7-1
- update

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- build on all arches

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Mar 26 2000 Philip Copeland <bryce@redhat.com> 1.5.5-1
- initial rpm version
