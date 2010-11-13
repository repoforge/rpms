# $Id$
# Authority: dag
# Upstream:

%define real_name dcc-dccd

Summary: Distributed Checksum Clearinghouse anti-spam tool
Name: dcc
Version: 1.2.39
Release: 1.2%{?dist}
License: BSD-like
Group: Applications/Internet
URL: http://www.rhyolite.com/anti-spam/dcc/

Source:	dcc-dccd.tar.Z
Patch0: dcc-1.2.2-sysv.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: sendmail-devel >= 8.12
Requires: perl

%description
Distributed Checksum Clearinghouse or DCC is a cooperative,
distributed system intended to detect "bulk" mail or mail sent to
many people. It allows individuals receiving a single mail message
to determine that many other people have been sent essentially
identical copies of the message and so reject the message. It can
identify some unsolicited bulk mail using "spam traps" and other
detectors, but that is not its focus.

The DCC can be viewed as a tool for end users to enforce their
right to "opt-in" to streams of bulk mail by refusing all bulk mail
except from sources in a "white list."  White lists are generally
the responsibility of DCC clients, since only they know which bulk
mail they solicited.

NB to use DCC to reject SPAM you need to configure
%{_datadir}/dcc/dcc_conf and either use procmail or sendmail to
feed the messages to DCC

%package cgi
Summary: The cgi-scripts for managing mail delivery on a DCC enabled server
Group: Applications/Internet
Requires: httpd
Requires: %{name} = %{version}-%{release}

%description cgi
Example set of cgi-scripts to allow users to point-and-click
manage their own DCC whitelists and thus what is delivered to
them.  Allows overriding of site level lists.  The scripts give
controlled access to the whitelists which are otherwise in
protected directory space (owned by dcc).

NB these scripts need configured after installation

%package milter
Summary: Distributed Checksum Clearinghouse Milter Interface
Group: Applications/Internet
Obsoletes: dcc-sendmail
Requires: sendmail
Requires: sendmail-cf
Requires: %{name} = %{version}-%{release}

%description sendmail
Dccm is a daemon built with the sendmail milter interface intended
to connect sendmail to DCC servers.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep

%setup -n %{real_name}-%{version}
%patch0 -p0

%{__cat} <<EOF >webusers.conf
### put users in here
EOF

%{__cat} <<EOF >dcc.httpd

ScriptAlias /dcc-bin /var/www/dcc-bin

<Directory /var/www/dcc-bin>

	<IfModule mod_access.c>
		Order deny,allow
		Deny from all
		allow from 127.0.0.1
	</IfModule>

	SSLCipherSuite ALL:!ADH:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP
	SSLRequireSSL
	ErrorDocument 403 /dcc-bin/http2https

	AuthType Basic
	AuthName "DCC user"
	AuthUserFile %{_localstatedir}/dcc/userdirs/webusers
	require valid-user

</Directory>
EOF

# fix defaults
find . -type f | xargs perl -pi -e "s|/usr/local|%{_prefix}|g"
find . -type f | xargs perl -pi -e "s|/var/dcc|%{_localstatedir}/dcc|g"

%build
CFLAGS=$RPM_OPT_FLAGS
export CFLAGS
CXXFLAGS=$RPM_OPT_FLAGS
export CXXFLAGS
FFLAGS=$RPM_OPT_FLAGS
export FFLAGS

./configure \
    --libexecdir=%{_sbindir} \
    --mandir=%{_mandir} \
    --bindir=%{_bindir} \
    --with-sendmail \
    --with-dccm \
    --homedir=%{_localstatedir}/dcc \
    --with-uid=dcc \
    --with-cgibin=/var/www/dcc-bin \
    --with-rundir=/var/run/dcc \
    --with-db-memory=32

perl -p -i -e "s:\".*\":\"%{_sbindir}\": if m/define\s+DCC_LIBEXECDIR/ ;" include/dcc_config.h

make

# make extras
make -C dccifd/dccif-test

%install
%{__rm} -rf %{buildroot}

# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

install -d %{buildroot}%{_initrddir}
install -d %{buildroot}%{_sysconfdir}/cron.daily
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}/var/run/dcc
install -d %{buildroot}%{_localstatedir}/dcc/{log,userdirs/{local,esmtp,cyrus,procmail}}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_mandir}
install -d %{buildroot}%{_libdir}
install -d %{buildroot}%{_includedir}/dcc

export INST_UID="`id -u`"
export INST_GID="`id -g`"

make MANOWN=$INST_UID MANGRP=$INST_GID DCC_SUID=$INST_UID DCC_OWN=$INST_UID \
    DCC_GRP=$INST_GID BINOWN=$INST_UID GRP=$INST_GID INSTALL="install -C" \
    DCC_PROTO_HOMEDIR=%{buildroot}%{_localstatedir}/dcc \
    DCC_CGIBINDIR=%{buildroot}/var/www/dcc-bin \
    DCC_LIBEXECDIR=%{buildroot}%{_sbindir} \
    DCC_BINDIR=%{buildroot}%{_sbindir} \
    BINDIR=%{buildroot}%{_bindir} \
    MANDIR=%{buildroot}%{_mandir}/man \
    install

install -m0755 misc/cron-dccd %{buildroot}%{_sysconfdir}/cron.daily/dccd
install -m0755 misc/rcDCC %{buildroot}%{_initrddir}/dccd
install -m0600 homedir/flod %{buildroot}%{_localstatedir}/dcc/flod

# move some binaries in place, wierd stuff...
for i in dbclean dblist dccd dccifd dccsight wlist; do
    mv %{buildroot}%{_bindir}/$i %{buildroot}%{_sbindir}/
done

# install extras
install -m0755 dccifd/dccif-test/dccif-test %{buildroot}%{_sbindir}/
install -m0755 dccifd/dccif-test/dccif-test.pl %{buildroot}%{_sbindir}/
install -m0755 dccifd/dccif.pl %{buildroot}%{_sbindir}/

install -d %{buildroot}%{_datadir}/sendmail-cf/feature
install -m0644 misc/dcc.m4 %{buildroot}%{_datadir}/sendmail-cf/feature/
install -m0644 misc/dccdnsbl.m4 %{buildroot}%{_datadir}/sendmail-cf/feature/
install -m0644 misc/dict-attack-aliases %{buildroot}%{_localstatedir}/dcc/
install -m0755 misc/filter-dict-attack %{buildroot}%{_sbindir}/
mv %{buildroot}%{_bindir}/dccm %{buildroot}%{_sbindir}/

# Set some initial logging, but no rejections
perl -p -i -e "s/BRAND=\$/BRAND=%{version}-%{release}/ ; s/DCCM_LOG_AT=\$/\$&10/ ; " \
	%{buildroot}%{_localstatedir}/dcc/dcc_conf

%{__install} -Dp -m0644 dcc.httpd %{buildroot}%{_sysconfdir}/httpd/conf.d/dcc.conf
%{__install} -Dp -m0644 webusers.conf %{buildroot}%{_localstatedir}/dcc/userdirs/webusers

# prepare for docs inclusion
cp misc/README README.misc
cp homedir/README README.homedir
cp cgi-bin/README README.cgi-bin

# fix strange attribs
chmod 644 CHANGES LICENSE README* *.txt *.html

# install devel files
install -m0644 dccd/*.h %{buildroot}%{_includedir}/dcc/
install -m0644 dcclib/*.h %{buildroot}%{_includedir}/dcc/
install -m0644 include/*.h %{buildroot}%{_includedir}/dcc/
install -m0644 srvrlib/*.h %{buildroot}%{_includedir}/dcc/
install -m0755 dcclib/libdcc.a %{buildroot}%{_libdir}/
install -m0755 srvrlib/libsrvr.a %{buildroot}%{_libdir}/
install -m0755 thrlib/libthr.a %{buildroot}%{_libdir}/

# house cleaning
rm -f %{buildroot}/var/www/dcc-bin/README
rm -f %{buildroot}%{_sbindir}/rcDCC
rm -f %{buildroot}%{_sbindir}/cron-dccd
rm -f %{buildroot}%{_sbindir}/logger
rm -f %{buildroot}%{_sbindir}/updatedcc

%pre
%_pre_useradd dcc %{_localstatedir}/dcc /bin/sh DCC_User

%post
%_post_service dccd

# this causes a hang if not connected to the internet
# deactivate it for now... user should read man pages
# instead...
#%{_bindir}/cdcc info > %{_localstatedir}/dcc/map.txt || :

%preun
%_preun_service dccd

%postun
%_postun_userdel dcc

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES FAQ.txt INSTALL.txt LICENSE README.homedir README.misc
%doc FAQ.html INSTALL.html cdcc.html dbclean.html dblist.html
%doc dcc.html dccd.html dccifd.html dccproc.html dccsight.html

%config(noreplace) %attr(0755,root,root) %{_sysconfdir}/cron.daily/dccd
%config(noreplace) %attr(0755,root,root) %{_initrddir}/dccd

%config(noreplace) %attr(0600,dcc,dcc) %{_localstatedir}/dcc/ids
%config(noreplace) %attr(0600,dcc,dcc) %{_localstatedir}/dcc/map
%config(noreplace) %attr(0600,dcc,dcc) %{_localstatedir}/dcc/map.txt
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/dcc_conf
#%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/dcc_db
#%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/dcc_db.hash
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/flod
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/whiteclnt
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/whitecommon
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/whitelist
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/grey_flod
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/grey_whitelist

%attr(4755,root,root) %{_bindir}/cdcc
%attr(4755,root,root) %{_bindir}/dccproc

%attr(0755,root,root) %{_sbindir}/dbclean
%attr(0755,root,root) %{_sbindir}/dblist
%attr(0755,root,root) %{_sbindir}/dccd
%attr(0755,root,root) %{_sbindir}/dccifd
%attr(0755,root,root) %{_sbindir}/newwebuser
%attr(0755,root,root) %{_sbindir}/start-dccd
%attr(0755,root,root) %{_sbindir}/start-dccifd
%attr(0755,root,root) %{_sbindir}/stop-dccd
%attr(0755,root,root) %{_sbindir}/wlist
%attr(4755,root,root) %{_sbindir}/dccsight
%attr(0755,root,root) %{_sbindir}/start-grey

# rrdtool stuff
%attr(0755,root,root) %{_sbindir}/dcc-stats-collect
%attr(0755,root,root) %{_sbindir}/dcc-stats-graph
%attr(0755,root,root) %{_sbindir}/dcc-stats-init
%attr(0755,root,root) %{_sbindir}/stats-get

# extras
%attr(0755,root,root) %{_sbindir}/dccif-test
%attr(0755,root,root) %{_sbindir}/dccif-test.pl
%attr(0755,root,root) %{_sbindir}/dccif.pl
%attr(0755,root,root) %{_sbindir}/fetch-testmsg-whitelist

%attr(0755,dcc,dcc) %dir %{_localstatedir}/dcc
%attr(0755,dcc,dcc) %dir %{_localstatedir}/dcc/log
%attr(0755,dcc,dcc) %dir %{_localstatedir}/dcc/userdirs
%attr(0755,dcc,dcc) %dir %{_localstatedir}/dcc/userdirs/local
%attr(0755,dcc,dcc) %dir %{_localstatedir}/dcc/userdirs/cyrus
%attr(0755,dcc,dcc) %dir %{_localstatedir}/dcc/userdirs/procmail
%attr(0755,dcc,dcc) %dir %{_localstatedir}/dcc/userdirs/esmtp
%attr(0755,dcc,dcc) %dir /var/run/dcc

%attr(0644,root,root) %{_mandir}/man8/cdcc.8*
%attr(0644,root,root) %{_mandir}/man8/dbclean.8*
%attr(0644,root,root) %{_mandir}/man8/dblist.8*
%attr(0644,root,root) %{_mandir}/man8/dcc.8*
%attr(0644,root,root) %{_mandir}/man8/dccd.8*
%attr(0644,root,root) %{_mandir}/man8/dccifd.8*
%attr(0644,root,root) %{_mandir}/man8/dccproc.8*
%attr(0644,root,root) %{_mandir}/man8/dccsight.8*

%files milter
%defattr(-, root, root, 0755)
%doc dccm.html
%config(noreplace) %attr(0644,dcc,dcc) %{_localstatedir}/dcc/dict-attack-aliases
%attr(0755,root,root) %{_sbindir}/dccm
%attr(0755,root,root) %{_sbindir}/filter-dict-attack
%attr(0755,root,root) %{_sbindir}/hackmc
%attr(0755,root,root) %{_sbindir}/na-spam
%attr(0755,root,root) %{_sbindir}/ng-spam
%attr(0755,root,root) %{_sbindir}/start-dccm
%attr(0644,root,root) %{_datadir}/sendmail-cf/feature/dcc.m4
%attr(0644,root,root) %{_datadir}/sendmail-cf/feature/dccdnsbl.m4
%attr(0644,root,root) %{_mandir}/man8/dccm.8*

%files		cgi
%defattr(-, root, root, 0755)
%doc README.cgi-bin
%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/httpd/conf.d/Z15_dcc.conf
%config(noreplace) %attr(0644,root,root) %{_localstatedir}/dcc/userdirs/webusers
%attr(0755,root,root) /var/www/dcc-bin/chgpasswd
%attr(0755,root,root) /var/www/dcc-bin/common
%attr(0755,root,root) /var/www/dcc-bin/edit-whiteclnt
%attr(0755,root,root) /var/www/dcc-bin/http2https
%attr(0755,root,root) /var/www/dcc-bin/list-log
%attr(0755,root,root) /var/www/dcc-bin/list-msg
%attr(0755,root,root) /var/www/dcc-bin/webuser-notify

%files devel
%defattr(-, root, root, 0755)
%attr(0644,root,root) %{_includedir}/dcc/*.h
%attr(0755,root,root) %{_libdir}/*.a

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.2.39-1.2
- Rebuild for Fedora Core 5.

* Fri Apr 08 2004 Dag Wieers <dag@wieers.com> - 1.2.39-1
- Cosmetic cleanup.

* Mon Apr 5 2004 Edward Rudd <rpms@outoforder.cc>
- upgraded to 1.2.39
- fixed %%install so to remove files when not packaging sendmail support

* Fri Mar 5 2004 Edward Rudd <rpms@outoforder.cc>
- upgraded to 1.2.32
- cleaned up %%files section

* Thu Nov 20 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2.16-1mdk
- 1.2.16
- added %%{_sbindir}/fetch-testmsg-whitelist
- nuked %%{_sbindir}/updatedcc

* Sun Sep 14 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2.7-1mdk
- 1.2.7
- added the %%{_localstatedir}/dcc/grey_whitelist file

* Tue Sep 02 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2.2-1mdk
- 1.2.2
- rediffed P0

* Wed Aug 13 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.1.45-2mdk
- fix hang in %%post

* Tue Aug 05 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.1.45-1mdk
- 1.1.45

* Wed Jul 30 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.1.44-1mdk
- 1.1.44

* Mon Jul 14 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.1.43-1mdk
- 1.1.43
- major spec file rework

* Wed May 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.36-1mdk
- from Michael A Nachbaur <mike@nachbaur.com> :
	- Version 1.1.36
	- Changed spec file to only install proc code
	- Changed to accomodate Mandrake RPM requirements

* Wed Jul 3 2002 Andrew Macpherson <andrew@oa5.com>
- Version 1.1.4
- Checkpoint against changes and patches
- Add sub-package for the cgi-management tools
- Delete  hooks to pre-build databases, this is now done in makeinstall.

* Sat May 25 2002 Andrew Macpherson <andrew@oa5.com>
- Version 1.1.2.a
- Patch free version that assumes Vernon will make
- changes to Man page autoconf, and homedir/Makefile.in

* Sat May 25 2002 Andrew Macpherson <andrew@oa5.com>
- Version 1.1.2
- Big changes to the sources by Vernon Schryver mean that
- patches can be largely eliminated.  Still need to
- replace the man page installation code in the original
- tar, but the reworked FreBSD autoconf code works for me, and
- the homedir/Makefile patch is a preview of code proposed
- by Vernon for the next release

- Moving installation location of 3 scripts into the doc
- directory, as they are not really common-use.

- Setup as client-only using the publicly-listed anonymous
- servers, and include the OA5 servers as well, though they
- are not for public listing

- Do not start dccd/dccm on install

- Moved messing with dcc_conf settings to pre-packaging vs install script

- Created skeleton userdirs for per recipient logging

- rpm -e , droped deleting databases in favour of removing
- Home directory on complete remove vs upgrade

* Mon May 15 2002 Andrew Macpherson <andrew@oa5.com>
- Version 1.0.47
- Basic setup, fighting the appalling autoconf (I hate that package)
- to try to get things to install in sensible places
- gave up and overwrote makefiles

- Make an initial setup that will let people run
- stand alone.  Considered and rejected configuring to use
- anonymous clients against publicly available servers

- Patch the rc script so that chkconfig will operate
