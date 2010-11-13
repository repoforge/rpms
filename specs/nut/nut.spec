# $Id$
# Authority: yury
# Upstream: Nut-packaging list <nut-packaging$lists,alioth,debian,org>

### EL2 ships with nut-0.45.0-3
%{?el2:# Tag: rfx}

%define nut_uid 57
%define nut_gid 57

%define initdir /etc/rc.d/init.d
%define cgidir  /var/www/nut-cgi-bin
%define piddir  /var/run/nut
%define modeldir /sbin

Summary: Network UPS Tools
Name: nut
Version: 2.4.1
Release: 10%{?dist}
Group: Applications/System
License: GPLv2+
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
Url: http://www.networkupstools.org/
Source: http://www.networkupstools.org/source/2.4/%{name}-%{version}.tar.gz
Source1: ups.init
Source2: ups.sysconfig

Patch0: nut-2.2.1-conf.patch

# sent upstream, for nut <= 2.4.1
Patch2: nut-2.2.2-udevusb.patch


Patch3: nut-2.2.2-halpath.patch

Requires: nut-client => 2.4.0 hal
Requires(pre): hal
Requires(post): fileutils chkconfig initscripts
Requires(postun): fileutils chkconfig initscripts

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: dbus-glib-devel
BuildRequires: elfutils-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: gd-devel
BuildRequires: hal-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtool
BuildRequires: libX11-devel
BuildRequires: libXpm-devel
BuildRequires: neon-devel
BuildRequires: net-snmp-devel
BuildRequires: netpbm-devel
BuildRequires: openssl-devel
BuildRequires: pkgconfig
BuildRequires: powerman-devel
BuildRequires: libusb-devel

%description
These programs are part of a developing project to monitor the assortment
of UPSes that are found out there in the field. Many models have serial
ports of some kind that allow some form of state checking. This
capability has been harnessed where possible to allow for safe shutdowns,
live status tracking on web pages, and more.

%package client
Group: Applications/System
Summary: Network UPS Tools client monitoring utilities
Requires(post): chkconfig
Requires(preun): chkconfig
Requires(pre): /usr/sbin/useradd hal

%description client
This package includes the client utilities that are required to monitor a
ups that the client host has access to, but where the UPS is physically
attached to a different computer on the network.

%package cgi
Group: Applications/System
Summary: CGI utilities for the Network UPS Tools
Requires: %{name}-client = %{version}-%{release} webserver
Requires(pre): /usr/sbin/useradd hal

%description cgi
This package includes CGI programs for accessing UPS status via a web
browser.

%package xml
Group: Applications/System
Summary: XML UPS driver for the Network UPS Tools
Requires: %{name}-client = %{version}-%{release}

%description xml
This package adds the netxml-ups driver, that allows NUT to monitor a XML
capable UPS.

%package hal
Summary: UPS Monitoring Software
Group: Applications/System
Requires: hal
Conflicts: apcupsd, %{name}

%description hal
This package contains the HAL enabled version of the drivers. You can use
this for most USB connected UPSes that are powering a single system with a
graphical desktop.

%package devel
Group: Development/Libraries
Summary: Development files for NUT Client
Requires: %{name}-client = %{version}-%{release} webserver openssl-devel

%description devel
This package contains the development header files and libraries
necessary to develop NUT client applications.

%prep
%setup -q
%patch0 -p1 -b .conf
%patch2 -p1 -b .udevusb
%patch3 -p1 -b .halpath

%build
autoreconf -i
%configure \
    --with-user=%{name} \
    --with-group=uucp \
    --with-statepath=%{piddir} \
    --with-pidpath=%{piddir} \
    --with-altpidpath=%{piddir} \
    --sysconfdir=%{_sysconfdir}/ups \
    --with-cgipath=%{cgidir} \
    --with-drvpath=%{modeldir} \
    --with-all \
    --with-ipv6 \
    --with-gd-libs \
    --with-linux-hiddev=%{_includedir}/linux/hiddev.h \
    --with-pkgconfig-dir=%{_libdir}/pkgconfig \
    --disable-static \
    --libdir=%{_libdir}

#remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%{__make} %{?_smp_mflags}

# fix old enconding manpages
mv man/upscode2.8 man/upscode2.8.iso
iconv -f ISO8859-1 -t UTF-8 -o man/upscode2.8 man/upscode2.8.iso
mv man/bcmxcp.8 man/bcmxcp.8.iso
iconv -f ISO8859-1 -t UTF-8 -o man/bcmxcp.8 man/bcmxcp.8.iso
mv man/bcmxcp_usb.8 man/bcmxcp_usb.8.iso
iconv -f ISO8859-1 -t UTF-8 -o man/bcmxcp_usb.8 man/bcmxcp_usb.8.iso
rm -f man/*.iso

%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}%{modeldir} \
         %{buildroot}%{_sysconfdir}/sysconfig \
         %{buildroot}%{_sysconfdir}/udev/rules.d \
         %{buildroot}%{piddir} \
         %{buildroot}%{_localstatedir}/lib/ups \
         %{buildroot}%{initdir} \
         %{buildroot}%{_libexecdir} \
         %{buildroot}%{_datadir}/hal/fdi/information/20thirdparty

%{__make} install DESTDIR=%{buildroot}

install -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/ups
install -m 755 %{SOURCE1} %{buildroot}%{initdir}/ups

install -m 644 man/gamatronic.*  %{buildroot}%{_mandir}/man8/

install -m 644 scripts/hal/ups-nut-device.fdi \
        %{buildroot}%{_datadir}/hal/fdi/information/20thirdparty/20-ups-nut-device.fdi

%{__rm} -rf %{buildroot}%{_prefix}/html
%{__rm} -f %{buildroot}%{_libdir}/*.la

pushd conf; 
make install DESTDIR=%{buildroot}
for file in %{buildroot}%{_sysconfdir}/ups/*.sample
do
   mv $file %{buildroot}%{_sysconfdir}/ups/`basename $file .sample`
done
popd

mv %{buildroot}/lib/udev/rules.d/52-nut-usbups.rules %{buildroot}/lib/udev/rules.d/62-nut-usbups.rules

# fix encoding
for fe in ./docs/cables/powerware.txt
do
  iconv -f iso-8859-1 -t utf-8 <$fe >$fe.new
  touch -r $fe $fe.new
  mv -f $fe.new $fe
done


%pre
/usr/sbin/useradd -c "Network UPS Tools" -u %{nut_uid}  \
        -s /bin/false -r -d %{_localstatedir}/lib/ups %{name} 2> /dev/null || :
/usr/sbin/usermod -G uucp %{name}

%pre client
/usr/sbin/useradd -c "Network UPS Tools" -u %{nut_uid} \
        -s /bin/false -r -d %{_localstatedir}/lib/ups %{name} 2> /dev/null || :
/usr/sbin/usermod -G uucp %{name}

%pre cgi
/usr/sbin/useradd -c "Network UPS Tools" -u %{nut_uid} \
        -s /bin/false -r -d %{_localstatedir}/lib/ups %{name} 2> /dev/null || :
/usr/sbin/usermod -G uucp %{name}

%post client
/sbin/chkconfig --add ups
/sbin/ldconfig
exit 0

%preun client
if [ "$1" = "0" ]; then
    /sbin/service ups stop > /dev/null 2>&1
    /sbin/chkconfig --del ups
fi
/sbin/ldconfig
exit 0

%postun client
if [ "$1" -ge "1" ]; then
    /sbin/service ups condrestart > /dev/null 2>&1
fi
/sbin/ldconfig
exit 0

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog AUTHORS MAINTAINERS README docs UPGRADING INSTALL NEWS
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/nut.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/ups.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsd.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsd.users
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/sysconfig/ups
%attr(644,root,root) /lib/udev/rules.d/62-nut-usbups.rules
%{modeldir}/*
%exclude %{modeldir}/netxml-ups
%{_sbindir}/upsd
%{_bindir}/upslog
%{_datadir}/cmdvartab
%{_datadir}/driver.list
%{_mandir}/man5/ups.conf.5.gz
%{_mandir}/man5/upsd.conf.5.gz
%{_mandir}/man5/upsd.users.5.gz
%{_mandir}/man8/apcsmart.8.gz
%{_mandir}/man8/bcmxcp.8*
%{_mandir}/man8/bcmxcp_usb.8.gz
%{_mandir}/man8/belkin.8.gz
%{_mandir}/man8/bestfcom.8.gz
%{_mandir}/man8/belkinunv.8.gz
%{_mandir}/man8/bestups.8.gz
%{_mandir}/man8/bestuferrups.8.gz
%{_mandir}/man8/blazer.8.gz
%{_mandir}/man8/cyberpower.8.gz
%{_mandir}/man8/dummy-ups.8.gz
%{_mandir}/man8/everups.8.gz
%{_mandir}/man8/etapro.8.gz
%{_mandir}/man8/gamatronic.8.gz
%{_mandir}/man8/genericups.8.gz
%{_mandir}/man8/isbmex.8.gz
%{_mandir}/man8/liebert.8.gz
%{_mandir}/man8/masterguard.8.gz
%{_mandir}/man8/megatec.8.gz
%{_mandir}/man8/megatec_usb.8.gz
%{_mandir}/man8/metasys.8.gz
%{_mandir}/man8/microdowell.8.gz
%{_mandir}/man8/mge-utalk.8.gz
%{_mandir}/man8/mge-shut.8.gz
%{_mandir}/man8/nutupsdrv.8.gz
%{_mandir}/man8/oneac.8.gz
%{_mandir}/man8/optiups.8.gz
%{_mandir}/man8/powercom.8.gz
%{_mandir}/man8/powerman-pdu.8.gz
%{_mandir}/man8/powerpanel.8.gz
%{_mandir}/man8/rhino.8.gz
%{_mandir}/man8/richcomm_usb.8.gz
%{_mandir}/man8/safenet.8.gz
%{_mandir}/man8/snmp-ups.8.gz
%{_mandir}/man8/solis.8*
%{_mandir}/man8/tripplite.8.gz
%{_mandir}/man8/tripplite_usb.8.gz
%{_mandir}/man8/tripplitesu.8.gz
%{_mandir}/man8/victronups.8.gz
%{_mandir}/man8/upscode2.8*
%{_mandir}/man8/upsd.8.gz
%{_mandir}/man8/upsdrvctl.8.gz
%{_mandir}/man8/usbhid-ups.8.gz

%files client
%defattr(-,root,root)
%attr(755,root,root) %{initdir}/ups
%dir %{_sysconfdir}/ups
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upsmon.conf
%config(noreplace) %attr(640,root,nut) %{_sysconfdir}/ups/upssched.conf
%dir %attr(750,nut,nut) %{_localstatedir}/lib/ups
%dir %attr(750,nut,nut) %{piddir}
%{_bindir}/upsc
%{_bindir}/upscmd
%{_bindir}/upsrw
%{_sbindir}/upsmon
%{_sbindir}/upssched
%{_bindir}/upssched-cmd
%{_libdir}/libupsclient.so.*
%{_mandir}/man5/upsmon.conf.5.gz
%{_mandir}/man5/upssched.conf.5.gz
%{_mandir}/man8/upsc.8.gz
%{_mandir}/man8/upscmd.8.gz
%{_mandir}/man8/upsrw.8.gz
%{_mandir}/man8/upslog.8.gz
%{_mandir}/man8/upsmon.8.gz
%{_mandir}/man8/upssched.8.gz

%files cgi
%defattr(-,root,root,-)
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/hosts.conf
%config(noreplace) %attr(600,nut,root) %{_sysconfdir}/ups/upsset.conf
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/upsstats.html
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/ups/upsstats-single.html
%{cgidir}/
%{_mandir}/man5/hosts.conf.5.gz
%{_mandir}/man5/upsstats.html.5.gz
%{_mandir}/man5/upsset.conf.5.gz
%{_mandir}/man8/upsimage.cgi.8.gz
%{_mandir}/man8/upsstats.cgi.8.gz
%{_mandir}/man8/upsset.cgi.8.gz

%files xml
%defattr(-,root,root)
%{modeldir}/netxml-ups
%doc %{_mandir}/man8/netxml-ups.8.gz

%files hal
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog MAINTAINERS NEWS README UPGRADING docs/nut-hal.txt
%{_datadir}/hal/fdi/information/20thirdparty/20-ups-nut-device.fdi
%{_libexecdir}/hald-addon*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_mandir}/man3/upscli*
%{_libdir}/libupsclient.so
%{_libdir}/pkgconfig/libupsclient.pc

%changelog
* Fri Dec 25 2009 Yury V. Zaytsev <yury@shurup.com> - 2.4.1-10
- Ported over RPMForge with minor changes.
- Updated HAL patch for EL.
- Back to uucp group.

* Thu Nov 05 2009 Michal Hlavinka <mhlavink@redhat.com> - 2.4.1-9
- spec cleanup

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2.4.1-8
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 20 2009 Michal Hlavinka <mhlavink@redhat.com> - 2.4.1-6
- fix coexistence with virtualbox (#488368)

* Wed May 20 2009 Michal Hlavinka <mhlavink@redhat.com> - 2.4.1-5
- add requires for hal (#501687)

* Fri Apr 17 2009 Michal Hlavinka <mhlavink@redhat.com> - 2.4.1-4
- change group even for existing nut user (#495999)

* Tue Apr 14 2009 Michal Hlavinka <mhlavink@redhat.com> - 2.4.1-3
- udev changed group from uucp to dialout, follow the change (#494020)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Michal Hlavinka <mhlavink@redhat.com> 2.4.1-1
- update to 2.4.1
- added support for microdowell ups

* Mon Feb 16 2009 Michal Hlavinka <mhlavink@redhat.com> 2.4.0-1
- update to new stable branch 2.4

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> 2.2.2-6
- rebuild with new openssl

* Thu Dec 18 2008 Michal Hlavinka <mhlavink@redhat.com> 2.2.2-5
- remove rpath, fix libtool

* Wed Dec 17 2008 Michal Hlavinka <mhlavink@redhat.com> 2.2.2-4
- fix #476850 - tripplite_usb driver segfaults when UPS on battery

* Mon Sep 15 2008 Tomas Smetana <tsmetana@redhat.com> 2.2.2-3
- fix #461374 - add missing udev rules

* Mon Aug 25 2008 Tomas Smetana <tsmetana@redhat.com> 2.2.2-2
- fix requirements in spec file
- build a separate hal package

* Mon May 12 2008 Tomas Smetana <tsmetana@redhat.com> 2.2.2-1
- new upstream version

* Tue Feb 12 2008 Tomas Smetana <tsmetana@redhat.com> 2.2.1-3
- fix compilation error with new glibc headers

* Tue Feb 12 2008 Tomas Smetana <tsmetana@redhat.com> 2.2.1-2
- rebuild (gcc-4.3)

* Wed Jan 09 2008 Tomas Smetana <tsmetana@redhat.com> 2.2.1-1
- new upstream version

* Wed Dec 05 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-6.2
- rebuild

* Thu Nov 29 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-6.1
- init script update, fix a typo

* Wed Nov 28 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-6
- fix forgotten bug in init script
- do not hardcode the uucp group in udev patch

* Tue Nov 27 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-5
- fix udev rules and hal information files
- fix init script

* Wed Sep 19 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-4
- fix manpages encodings
- run ldconfig after client (un)install
- fix HAL support

* Thu Sep 06 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-3
- fix wrong libssl flags in devel, fix devel package dependencies

* Wed Aug 15 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-2
- fix #249028 - usb udev rules
- update initscript and sysconfig file
- fix calls to open() for compatibility with the new glibc

* Fri Jul 13 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-1.1
- rebuild

* Fri Jul 13 2007 Tomas Smetana <tsmetana@redhat.com> 2.2.0-1
- new upstream version (Resolves: #248074)
- initscripts update
- spec file cleanup

* Mon May 07 2007 Arnaud Quette <aquette-dev@gmail.com> 2.1.0-1
- update to 2.1.0 development tree
- HAL, ...

* Mon Mar 26 2007 Than Ngo <than@redhat.com> 2.0.5-3
- cleanup

* Tue Jan 23 2007 Karsten Hopp <karsten@redhat.com> 2.0.5-2
- rename fatal to fatal_with_errno in ipv6 patch
- fix filelist

* Tue Jan 23 2007 Karsten Hopp <karsten@redhat.com> 2.0.5-1
- update to 2.0.5

* Wed Nov 29 2006 Karsten Hopp <karsten@redhat.com> 2.0.4-2
- rebuild with new net-snmp-libs
- disable nut-2.0.1-bad.patch, not required

* Tue Nov 21 2006 Than Ngo <than@redhat.com> - 2.0.4-1
- add IPv6 support, thanks to Dan KopeÄek (#198394)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.0.3-2.1
- rebuild

* Tue May 16 2006 Than Ngo <than@redhat.com> 2.0.3-2 
- fix #191914, BR fontconfig-devel for cgi

* Mon Apr 24 2006 Than Ngo <than@redhat.com> 2.0.3-1
- update to 2.0.3
- drop nut-2.0.2-buffer.patch, it's included in new upstream
- add udev rule #189674, #187105

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.0.2-6.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.0.2-6.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 03 2006 Radek Vokal <rvokal@redhat.com> 2.0.2-6
- rebuilt against new libnetsnmp

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 23 2005 Than Ngo <than@redhat.com> 2.0.2-5
- fix for modular X

* Wed Nov 09 2005 Than Ngo <than@redhat.com> 2.0.2-4
- rebuilt

* Mon Nov 07 2005 Than Ngo <than@redhat.com> 2.0.2-3 
- rebuilt

* Thu Nov 03 2005 Than Ngo <than@redhat.com> 2.0.2-2
- rebuilt against new libnetsnmp

* Wed Jul 20 2005 Than Ngo <than@redhat.com> 2.0.2-1
- fix compiler warnings #156027
- fix pid issue  #159450
- fix wrong ownership and permissions #159449, #141123
- update to 2.0.2

* Thu Mar 10 2005 Than Ngo <than@redhat.com> 2.0.1-1
- 2.0.1
- fix uninit local variable, #131773

* Wed Dec 08 2004 Than Ngo <than@redhat.com> 2.0.0-7
- don't requires libusb-devel on s390/s390x
- add %%{release} in buildroot 

* Thu Nov 25 2004 Miloslav Trmac <mitr@redhat.com> - 2.0.0-6
- Convert newhidups.8 to UTF-8

* Tue Oct 05 2004 Than Ngo <than@redhat.com> 2.0.0-5
- more buildrequires
- don't build on s390/s390x

* Thu Aug 26 2004 Nalin Dahyabhai <nalin@redhat.com> 2.0.0-4
- fix syntax error in -client postun scriptlet (#131040)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 10 2004 Than Ngo <than@redhat.com> 2.0.0-2
- fixed permission problem, bug #122867

* Fri Apr 02 2004 Than Ngo <than@redhat.com> 2.0.0-1
- 2.0.0

* Sat Feb 14 2004 Than Ngo <than@redhat.com> 1.4.1-3 
- add some missing drivers

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 11 2004 Than Ngo <than@redhat.com> 1.4.1-1
- 1.4.1
- fixed permission problem (bug #115290)

* Wed Sep 24 2003 Mike McLean <mikem@redhat.com> 1.4.0-3
- fixed 'nut' user problem with nut-cgi (bug#104872)

* Mon Sep 15 2003 Than Ngo <than@redhat.com> 1.4.0-2
- added missing hidups driver (bug #104412)

* Tue Sep 09 2003 Than Ngo <than@redhat.com> 1.4.0-1
- 1.4.0
- fixed permission problem (bug #103023)
- fixed rpm file list (bug #90848)
- added support multiple drivers, thanks to Gilbert E. Detillieux (bug #79465)

* Thu Jun 26 2003 Than Ngo <than@redhat.com> 1.2.2-3
- Add variable to ups sysconfig file for upsd (bug #97900)

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed May  7 2003 Than Ngo <than@redhat.com> 1.2.2-1
- 1.2.2

* Tue May 06 2003 Phil Knirsch <pknirsch@redhat.com> 1.2.0-7
- Bumped release and rebuilt because of new gd version.

* Thu Feb 13 2003 Than Ngo <than@redhat.com> 1.2.0-6
- build with correct userid #84199
- fix directory permission

* Tue Feb 11 2003 Than Ngo <than@redhat.com> 1.2.0-5
- add user nut, bug #81500 
- fix permission issue, bug #81524, #83997
- own /etc/ups, bug #73959

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Jan  8 2003 Thomas Woerner <twoerner@redhat.com> 1.2.0-3
- added html templates for cgi scripts (#78532)
- added hidups driver (#80334)

* Wed Dec  18 2002 Dan Walsh <dwalsh@redhat.com> 1.2.0-2
- Fix service description

* Wed Nov  6 2002 han Ngo <than@redhat.com> 1.2.0-1
- update to 1.2.0

* Mon Nov  4 2002 Than Ngo <than@redhat.com> 1.00-1
- update to 1.00

* Wed Jul 31 2002 Than Ngo <than@redhat.com> 0.45.4-5
- Fixed wrong CMDSCRIPT (bug #69817)

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 02 2002 Than Ngo <than@redhat.com> 0.45.4-3
- fix forced shutdown (bug #65824, #60516)
- enable hidups driver
- add missing manages (bug #65188)

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Feb 26 2002 Than Ngo <than@redhat.com> 0.45.4-1
- update to 0.45.4

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Dec 14 2001 Than Ngo <than@redhat.com> 0.45.3-1
- update to 0.45.2
- fix bug #57417

* Mon Nov 27 2001 Than Ngo <than@redhat.com> 0.45.2-1
- update to 0.45.2
- clean up some patch files for 0.45.2

* Tue Jul 24 2001 Than Ngo <than@redhat.com> 0.45.0-3
- fix build dependencies (bug #49858)

* Fri Jul  6 2001 Than Ngo <than@redhat.com> 0.45.0-2
- rebuild

* Wed Jun 13 2001 Than Ngo <than@redhat.com>
- update to 0.45.0
- add some patches from alane@geeksrus.net (bug #44361, #44363)

* Sun Apr 22 2001 Than Ngo <than@redhat.com>
- add all available UPS drivers (Bug #36937)

* Fri Apr 13 2001 Than Ngo <than@redhat.com>
- update to 0.44.3 (Bug #35255)

* Fri Feb  9 2001 Than Ngo <than@redhat.com>
- fixed typo (Bug #26535)

* Tue Feb  6 2001 Trond Eivind Glomsrd <teg@redhat.com>
- Fix some of the i18n
- make it exit cleanly if not configured

* Fri Jan 26 2001 Than Ngo <than@redhat.com>
- initscript internationalisation

* Thu Jan 11 2001 Than Ngo <than@redhat.com>
- fixed init script error (bug #23525)

* Sat Oct 21 2000 Than Ngo <than@redhat.com>
- update to 0.44.1

* Tue Aug 01 2000 Than Ngo <than@redhat.de>
- rebuilt with Michael changes

* Mon Jul 31 2000 Michael Stefaniuc <mstefani@redhat.com>
- changed /etc/sysconfig/ups to adress the changes in 0.44.0
- moved /etc/sysconfig/ups to the server package
- changed the initscript
- small config file patch

* Fri Jul 28 2000 Than Ngo <than@redhat.de>
- fixed initscripts so that condrestart doesn't return 1 when the test fails

* Mon Jul 24 2000 Than Ngo <than@redhat.de>
- nut CGIs is disable as default (Bug #14282)

* Tue Jul 18 2000 Than Ngo <than@redhat.de>
- update to 0.44.0
- inits back to rc.d/init.d, using service to fire them up

* Wed Jul 12 2000 Than Ngo <than@redhat.de>
- fix initscript and specfile, it should work with 6.x and 7.x
- add --with-statepath and --sysconfdir to %%configure (thanks Michael)

* Sat Jul 08 2000 Than Ngo <than@redhat.de>
- add Prereq: /etc/init.d

* Tue Jun 27 2000 Than Ngo <than@redhat.de>
- don't prereq, only require initscripts

* Mon Jun 26 2000 Than Ngo <than@redhat.de>
- /etc/rc.d/init.d -> /etc/init.d
- prereq initscripts >= 5.20

* Fri Jun 16 2000 Bill Nottingham <notting@redhat.com>
- don't run by default

* Mon Jun 12 2000 Preston Brown <pbrown@redhat.com>
- adopted for Winston.  Use our new path macros.
- change nocgi pkg to a cgi pkg (inclusive rather than exclusive).
- new init script

* Sat May 06 2000 <bo-rpm@vircio.com> (0.43.2-1)
- Updated Package to new release

* Thu Jan 20 2000 <bo-rpm@vircio.com> (0.42.2-1)
- Updated package to new release
- Dropped bestups patch since that is fixed in 0.42.2

* Sat Dec 18 1999 <bo-rpm@vircio.com> (0.42.1-4)
- Package now uses chkconfig

* Sat Dec 18 1999 <bo-rpm@vircio.com> (0.42.1-3)
- applied an improved patch to deal with the 
  bestups string length issue.

* Sat Dec 11 1999 <bo-rpm@vircio.com> (0.42.1-1)
- fixed string length in bestups.c line 279.

* Sat Dec 11 1999 <bo-rpm@vircio.com> (0.42.1-1)
- upgraded package to 0.42.1 from 0.42.0

* Mon Dec 6 1999 <bo-rpm@vircio.com> (0.42.0-8)
- added requirement of nut-client for nut.

* Mon Dec 6 1999 <bo-rpm@vircio.com> (0.42.0-7)
- removed overlapping files between the nut and nut-client rpms

* Mon Nov 23 1999 <bo-rpm@vircio.com> (0.42.0-6)
- stop ups before uninstalling

* Mon Nov 23 1999 <bo-rpm@vircio.com> (0.42.0-5)
- build against gd 1.6.3

* Thu Nov 03 1999 <bo-rpm@vircio.com> (0.42.0-4)
- Initial build of nut (well almost).
- Removed chmod from the make file so that the package
  does not have to be built as root.....
