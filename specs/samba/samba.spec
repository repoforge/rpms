# $Id$
# Authority: dag

# Tag: test

%{?dist: %{expand %%define %dist 1}}

Summary: The Samba SMB server
Name: samba
Version: 3.0.1
Release: 0
License: GPL
Group: System Environment/Daemons
URL: http://www.samba.org/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://download.samba.org/samba/ftp/%{name}-%{version}.tar.bz2

# Red Hat specific replacement-files
Source1: samba.log
Source2: samba.xinetd
Source3: swat.desktop
Source4: samba.sysconfig
Source5: smb.init
Source6: samba.pamd
Source7: smbprint
Source8: winbind.init

# Don't depend on Net::LDAP
Source999: filter-requires-samba.sh

# generic patches
Patch1: samba-2.2.0-smbw.patch
#Patch3: samba-2.0.5a-gawk.patch
#Patch5: samba-2.0.7-krb5-1.2.patch
Patch6: samba-2.0.7-buildroot.patch
#Patch11: samba-2.2.0-logname.patch
# ??? Patch13: samba-2.2.2-winsfixes.patch
#Patch14: samba-2.2.3-smbadduserloc.patch
# Patch15: samba-2.2.7-lfsclient.patch
# Not used, but it have some patches which might be needed later...
Patch16: samba-2.2.2-smbadduser.patch
Patch17: samba-2.2.8-smb.conf.patch
Patch20: samba-3.0.0beta1-pipedir.patch
Patch24: samba-3.0.0-logfiles.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


Requires: pam >= 0.64, samba-common = %{version}-%{release}
Requires: logrotate >= 3.4, initscripts >= 5.54-1 
Prereq: /sbin/chkconfig /bin/mktemp /usr/bin/killall
Prereq: fileutils sed /etc/init.d 
BuildRequires: pam-devel, readline-devel, ncurses-devel
BuildRequires: fileutils
%{?rh8:BuildRequires: libacl-devel}
%{?rh9:BuildRequires: libacl-devel}

# Working around perl dependency problem from docs
%define __perl_requires %{SOURCE999}

%description
Samba provides an SMB/CIFS server which can be used to provide
network file and print services to SMB/CIFS clients, including
various versions of MS Windows, OS/2, and other Linux machines.
Samba also provides some SMB clients, which complement the
built-in SMB filesystem in Linux. Samba uses NetBIOS over TCP/IP
(NetBT) protocols and does NOT need NetBEUI (Microsoft Raw NetBIOS
frame) protocol.

Samba 3.0 also introduces UNICODE support and kerberos/ldap
integration as a member server in a Windows 2000 domain.

%package client
Summary: Samba (SMB) client programs
Group: Applications/System
Requires: samba-common = %{version}-%{release}
Obsoletes: smbfs

%description client
The samba-client package provides some SMB clients to compliment the
built-in SMB filesystem in Linux. These clients allow access of SMB
shares and printing to SMB printers.

%package common
Summary: Files used by both Samba servers and clients
Group: Applications/System

%description common
Samba-common provides files necessary for both the server and client
packages of Samba.

%package swat
Summary: The Samba SMB server configuration program
Group: Applications/System
Requires: samba = %{version}-%{release}, xinetd

%description swat
The samba-swat package includes the new SWAT (Samba Web Administration
Tool), for remotely managing Samba's smb.conf file using your favorite
Web browser.

%prep
%setup

# copy Red Hat specific scripts
%{__cp} %{SOURCE5} packaging/RedHat/
%{__cp} %{SOURCE6} packaging/RedHat/
%{__cp} %{SOURCE7} packaging/RedHat/
%{__cp} %{SOURCE8} packaging/RedHat/winbind.init

%patch1 -p1 -b .smbw
#%patch3 -p1 -b .gawk
#%patch5 -p1 -b .krb5-1.2
#%patch6 -p1 -b .buildroot
%patch20 -p1 -b .pipedir
%patch24 -p1 -b .logfiles

# crap
%{__rm} -f examples/VFS/.cvsignore

%build
cd source
RPM_OPT_FLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE"
%configure \
%{?el3:--with-acl-support} \
%{?fc1:--with-acl-support} \
%{?rh9:--with-acl-support} \
%{?rh8:--with-acl-support} \
	--with-automount \
	--with-codepagedir="%{_datadir}/samba/codepages" \
	--with-configdir="%{_sysconfdir}/samba" \
	--with-dce-dfs \
	--with-fhs \
	--with-ldapsam \
	--with-libsmbclient \
	--with-lockdir="%{_localstatedir}/cache/samba" \
	--with-manpages-langs="en" \
	--with-mmap \
	--with-pam \
	--with-pam_smbpass \
	--with-piddir="%{_localstatedir}/run" \
	--with-privatedir="%{_sysconfdir}/samba" \
	--with-quotas \
	--with-sambabook="%{_datadir}/swat/using_samba" \
	--with-smbmount \
	--with-swatdir="%{_datadir}/swat" \
	--with-syslog \
	--with-tdbsam \
	--with-utmp \
	--with-vfs \
	--without-smbwrapper
#	--with-afs
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" proto
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" all nsswitch/libnss_wins.so modules
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" debug2html
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" smbfilter
%{__make} %{?_smp_mflags} CFLAGS="%{optflags}" bin/smbspool

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}/sbin/ \
			%{buildroot}%{_sbindir} \
			%{buildroot}%{_bindir} \
			%{buildroot}%{_initrddir} \
			%{buildroot}%{_sysconfdir}/{logrotate.d,pam.d,samba}/ \
			%{buildroot}%{_localstatedir}/cache/samba/ \
			%{buildroot}%{_datadir}/samba/codepages/
%{__install} -d -m0700 %{buildroot}%{_localstatedir}/log/samba
%{__install} -d -m1777 %{buildroot}%{_localstatedir}/spool/samba

%makeinstall -C source \
	BINDIR="%{buildroot}%{_bindir}" \
	BASEDIR="%{buildroot}%{_prefix}" \
	SBINDIR="%{buildroot}%{_sbindir}" \
	DATADIR="%{buildroot}%{_datadir}" \
	LOCKDIR="%{buildroot}%{_localstatedir}/cache/samba" \
	PRIVATEDIR="%{buildroot}%{_sysconfdir}/samba" \
	LIBDIR="%{buildroot}%{_libdir}/samba" \
	CONFIGDIR="%{buildroot}%{_sysconfdir}/samba" \
	MANDIR="%{buildroot}%{_mandir}" \
	VARDIR="%{buildroot}%{_localstatedir}/log/samba" \
	CODEPAGEDIR="%{buildroot}%{_datadir}/samba/codepages" \
	SWATDIR="%{buildroot}%{_datadir}/swat" \
	SAMBABOOK="%{buildroot}%{_datadir}/swat/using_samba" \
	PIDDIR="%{buildroot}%{_localstatedir}/run"

%{__install} -d -m0755 %{buildroot}/%{_lib}/security/ \
			%{buildroot}%{_sysconfdir}/{sysconfig,xinetd.d}/ \
			%{buildroot}%{_libdir} \
			%{buildroot}%{_includedir} \

# Install other stuff
%{__install} -m0644 packaging/RedHat/smb.conf %{buildroot}%{_sysconfdir}/samba/smb.conf
%{__install} -m0755 source/script/mksmbpasswd.sh %{buildroot}%{_bindir}
%{__install} -m0644 packaging/RedHat/smbusers %{buildroot}/etc/samba/smbusers
%{__install} -m0755 packaging/RedHat/smbprint %{buildroot}%{_bindir}
# %{__install} -m0755 source/script/smbadduser %{buildroot}%{_bindir}
%{__install} -m0755 packaging/RedHat/smb.init %{buildroot}%{_initrddir}/smb
%{__install} -m0755 packaging/RedHat/winbind.init %{buildroot}%{_initrddir}/winbind
%{__ln_s} -f ../..%{_initrddir}/smb  %{buildroot}%{_sbindir}/samba
%{__install} -m0644 packaging/RedHat/samba.pamd.stack %{buildroot}/etc/pam.d/samba
%{__install} -m0644 $RPM_SOURCE_DIR/samba.log %{buildroot}/etc/logrotate.d/samba
%{__ln_s} -f ../usr/bin/smbmount %{buildroot}/sbin/mount.smb
%{__ln_s} -f ../usr/bin/smbmount %{buildroot}/sbin/mount.smbfs
echo "127.0.0.1 localhost" > %{buildroot}%{_sysconfdir}/samba/lmhosts

%{__install} -m0755 source/bin/pam_smbpass.so %{buildroot}/%{_lib}/security/pam_smbpass.so
#%{__cp} -r source/pam_smbpass/ docs/
#%{__rm} -f docs/pam_smbpass/*.*

# winbind
%{__install} -m0755 source/nsswitch/pam_winbind.so %{buildroot}/%{_lib}/security/pam_winbind.so
%{__install} -m0755 source/nsswitch/libnss_winbind.so %{buildroot}/%{_lib}/libnss_winbind.so.2
%{__ln_s} -f /%{_lib}/libnss_winbind.so.2  %{buildroot}%{_libdir}/libnss_winbind.so
%{__install} -m0755 source/nsswitch/libnss_wins.so %{buildroot}/%{_lib}/libnss_wins.so.2
%{__ln_s} -f /%{_lib}/libnss_wins.so.2  %{buildroot}%{_libdir}/libnss_wins.so

# libsmbclient
%{__install} -m0644 source/bin/libsmbclient.so %{buildroot}%{_libdir}/libsmbclient.so
%{__install} -m0644 source/bin/libsmbclient.a %{buildroot}%{_libdir}/libsmbclient.a
%{__install} -m0644 source/include/libsmbclient.h %{buildroot}%{_includedir}

%{__install} -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xinetd.d/swat
%{__install} -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/samba

# remove this or it ends up in %doc
%{__rm} -rf docs/htmldocs/using_samba
%{__rm} -rf docs/{docbook,manpages,yodldocs}
%{__rm} -f docs/faq/*sgml
# remove html'ized man pages:
%{__rm} -rf docs/htmldocs/*.[0-9].*

### Clean up buildroot
#%{__rm} -rf %{buildroot}/usr/bin/findsmb
%{__rm} -f %{buildroot}%{_mandir}/man1/smbsh.1* \
		%{buildroot}%{_mandir}/man1/editreg.1*
#%{__rm} -f %{buildroot}/%{_datadir}/swat/help/findsmb.1.html

%post
/sbin/chkconfig --add smb

%preun
if [ $1 -eq 0 ]; then
    /sbin/service smb stop &>/dev/null || :
    /sbin/chkconfig --del smb
#    rm -rf /var/log/samba/* /var/cache/samba/*
fi

%postun
if [ $1 -ge 1 ]; then
	/sbin/service smb condrestart &>/dev/null || :
fi	

%post common
/sbin/ldconfig 2>/dev/null
/sbin/chkconfig --add winbind

%preun common
if [ $1 -eq 0 ]; then
    /sbin/service winbind stop &>/dev/null || :
    /sbin/chkconfig --del winbind
fi

%postun common
/sbin/ldconfig 2>/dev/null

%triggerpostun -- samba < 1.9.18p7
if [ $1 -ne 0 ]; then
    /sbin/chkconfig --add smb
fi

%triggerpostun -- samba < 2.0.5a-3
if [ $1 -ne 0 ]; then
    [ ! -d /var/lock/samba ] && mkdir -m 0755 /var/lock/samba
    [ ! -d /var/spool/samba ] && mkdir -m 1777 /var/spool/samba
    chmod 644 /etc/services
    [ -f /etc/inetd.conf ] && chmod 644 /etc/inetd.conf
fi

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README COPYING Manifest Read-Manifest-Now
%doc WHATSNEW.txt Roadmap
%doc docs/
%doc examples/

%dir %{_libdir}/samba/
%dir %{_localstatedir}/cache/samba
%dir %{_localstatedir}/log/samba
%dir %{_localstatedir}/spool/samba

%config(noreplace) %{_sysconfdir}/sysconfig/samba/
%config(noreplace) %{_sysconfdir}/samba/smbusers/
%config(noreplace) %{_sysconfdir}/logrotate.d/samba/
%config(noreplace) %{_sysconfdir}/pam.d/samba/
%config %{_initrddir}/smb

/%{_lib}/security/pam_smbpass.so
%{_sbindir}/smbd
%{_sbindir}/nmbd
# %{_bindir}/make_unicodemap
%{_bindir}/mksmbpasswd.sh
%{_bindir}/smbcontrol
%{_bindir}/smbstatus
# %{_bindir}/smbadduser
%{_bindir}/tdbbackup
# %{_mandir}/man1/make_unicodemap.1*
%{_mandir}/man1/smbcontrol.1*
%{_mandir}/man1/smbstatus.1*
%{_mandir}/man5/smbpasswd.5*
%{_mandir}/man7/samba.7*
%{_mandir}/man7/Samba.7*
%{_mandir}/man8/nmbd.8*
%{_mandir}/man8/pdbedit.8*
%{_mandir}/man8/smbd.8*
%{_mandir}/man8/tdbbackup.8*
#%{_mandir}/ja/man1/smbstatus.1*
#%{_mandir}/ja/man5/smbpasswd.5*
#%{_mandir}/ja/man7/samba.7*
#%{_mandir}/ja/man8/smbd.8*
#%{_mandir}/ja/man8/nmbd.8*
%{_libdir}/samba/vfs/

%files swat
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/xinetd.d/swat
%{_sbindir}/swat
%{_datadir}/swat/
%{_mandir}/man8/swat.8*
#%{_mandir}/ja/man8/swat.8*

%files client
%defattr(-, root, root, 0755)
%dir %{_libdir}/samba/
/sbin/mount.smb
/sbin/mount.smbfs
%{_libdir}/samba/lowcase.dat
%{_libdir}/samba/upcase.dat
%{_libdir}/samba/valid.dat
%{_bindir}/rpcclient
%{_bindir}/smbcacls
%{_bindir}/smbmount
%{_bindir}/smbmnt
%{_bindir}/smbumount
%{_bindir}/findsmb
%{_mandir}/man8/smbmnt.8*
%{_mandir}/man8/smbmount.8*
%{_mandir}/man8/smbumount.8*
%{_mandir}/man8/smbspool.8*
%{_mandir}/man8/mount.cifs.8*
%{_bindir}/nmblookup
%{_bindir}/smbclient
%{_bindir}/smbprint
%{_bindir}/smbspool
%{_bindir}/smbtar
%{_bindir}/net
%{_bindir}/smbtree
%{_mandir}/man1/findsmb.1*
%{_mandir}/man1/nmblookup.1*
%{_mandir}/man1/rpcclient.1*
%{_mandir}/man1/smbcacls.1*
%{_mandir}/man1/smbclient.1*
%{_mandir}/man1/smbtar.1*
%{_mandir}/man1/smbtree.1*
%{_mandir}/man8/net.8*
#%{_mandir}/ja/man1/smbtar.1*
#%{_mandir}/ja/man1/smbclient.1*
#%{_mandir}/ja/man1/nmblookup.1*

%files common
%defattr(-, root, root, 0755)
%config(noreplace) %{_sysconfdir}/samba/smb.conf
%config(noreplace) %{_sysconfdir}/samba/lmhosts
%config %{_initrddir}/winbind

%dir %{_libdir}/samba/
%dir %{_datadir}/samba/
%dir %{_datadir}/samba/codepages/
%dir %{_sysconfdir}/samba/

%{_libdir}/samba/charset/
%{_libdir}/samba/*.msg
%{_libdir}/libnss_wins.so
/%{_lib}/libnss_wins.so.2
%{_libdir}/libnss_winbind.so
/%{_lib}/libnss_winbind.so.2
/%{_lib}/security/pam_winbind.so
%{_libdir}/libsmbclient.a
%{_libdir}/libsmbclient.so
%{_includedir}/libsmbclient.h
# %{_bindir}/make_smbcodepage
%{_bindir}/testparm
%{_bindir}/testprns
%{_bindir}/smbpasswd
# %{_bindir}/make_printerdef
%{_bindir}/wbinfo
# %{_bindir}/editreg
%{_bindir}/ntlm_auth
%{_bindir}/pdbedit
%{_bindir}/profiles
%{_bindir}/smbcquotas
#%{_bindir}/vfstest
%{_sbindir}/winbindd
# %{_datadir}/samba/codepages/*
# %{_mandir}/man1/make_smbcodepage.1*
%{_mandir}/man1/log2pcap.1*
%{_mandir}/man1/ntlm_auth.1*
%{_mandir}/man1/profiles.1*
%{_mandir}/man1/smbcquotas.1*
%{_mandir}/man1/testparm.1*
%{_mandir}/man1/testprns.1*
%{_mandir}/man5/smb.conf.5*
%{_mandir}/man5/lmhosts.5*
%{_mandir}/man8/smbpasswd.8*
%{_mandir}/man1/wbinfo.1*
%{_mandir}/man8/winbindd.8*
%{_mandir}/man1/vfstest.1*

# #%lang(ja) %{_mandir}/ja/man1/make_smbcodepage.1*
#%lang(ja) %{_mandir}/ja/man1/testparm.1*
#%lang(ja) %{_mandir}/ja/man1/testprns.1*
#%lang(ja) %{_mandir}/ja/man5/smb.conf.5*
#%lang(ja) %{_mandir}/ja/man5/lmhosts.5*
#%lang(ja) %{_mandir}/ja/man8/smbpasswd.8*

%changelog
* Wed Dec 17 2003 Dag Wieers <dag@wieers.com> - 3.0.1-0
- Updated to release 3.0.1.

* Thu Sep 25 2003 Dag Wieers <dag@wieers.com> - 3.0.0-1
- Updated to release 3.0.0.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 3.0.0-0.rc3
- Updated to release 3.0.0rc3.

* Sat Aug 30 2003 Dag Wieers <dag@wieers.com> - 3.0.0-0.rc2
- Updated to release 3.0.0rc2.

* Tue Aug 19 2003 Dag Wieers <dag@wieers.com> - 3.0.0-0.rc1
- Initial package. (using DAR)
