# $Id$
# Authority: dries
# Upstream: Lee Howard <faxguy$howardsilvan,com>

%define faxspool    /var/spool/hylafax

Summary:   an enterprise-strength fax server
Name:      hylafax
Version:   5.2.5
Release:   1%{?dist}
License:   libtiff and BSD with advertising
Group:     Applications/Communications
URL:       http://hylafax.sourceforge.net

Source:    http://dl.sf.net/sourceforge/hylafax/hylafax-%{version}.tar.gz
Source1:   hylafax_rh.init
Source2:   hylafax_daily.cron
Source3:   hylafax_hourly.cron

BuildRequires: libtiff-devel, zlib-devel, gcc, gcc-c++, pam-devel, openldap-devel
Requires:    ghostscript, gawk, sharutils, mailx, crontabs
Conflicts:   mgetty-sendfax

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
HylaFAX(tm) is a enterprise-strength fax server supporting
Class 1 and 2 fax modems on UNIX systems. It provides spooling
services and numerous supporting fax management tools. 
The fax clients may reside on machines different from the server
and client implementations exist for a number of platforms including 
windows.

%prep
%setup

%build
# - Can't use the configure macro because HylaFAX configure script does
#   not understand the config options used by that macro
STRIP=':' \
./configure \
        --with-DIR_BIN=%{_bindir} \
        --with-DIR_SBIN=%{_sbindir} \
        --with-DIR_LIB=%{_libdir} \
        --with-DIR_LIBEXEC=%{_sbindir} \
        --with-DIR_LIBDATA=%{_sysconfdir}/hylafax \
        --with-DIR_LOCKS=/var/lock \
        --with-LIBDIR=%{_libdir} \
        --with-TIFFBIN=%{_bindir} \
        --with-DIR_MAN=%{_mandir} \
        --with-PATH_GSRIP=%{_bindir}/gs \
        --with-DBLIBINC=%{_includedir} \
        --with-TIFFINC=%{_includedir} \
        --with-LIBTIFF="-ltiff" \
        --with-DIR_SPOOL=%{faxspool} \
        --with-AFM=no \
        --with-AWK=%{_bindir}/gawk \
        --with-PATH_VGETTY=/sbin/vgetty \
        --with-PATH_GETTY=/sbin/mgetty \
        --with-PAGESIZE=A4 \
        --with-PATH_DPSRIP=%{faxspool}/bin/ps2fax \
        --with-PATH_IMPRIP="" \
        --with-SYSVINIT=%{_initrddir}/hylafax \
        --with-INTERACTIVE=no

# can't use %{?_smp_mflags} because it breaks libfaxutil dso building
make OPTIMIZER="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

# install: make some dirs...
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,cron.hourly} 
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/hylafax
mkdir -p -m 755 $RPM_BUILD_ROOT%{_initrddir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_bindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_libdir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{_mandir}
mkdir -p -m 755 $RPM_BUILD_ROOT%{faxspool}/config

# install: binaries and man pages 
# FAXUSER, FAXGROUP, SYSUSER and SYSGROUP are set to the current user to
# avoid warnings about chown/chgrp if the user building the SRPM is not root; 
# they are set to the correct values with the RPM attr macro
make install -e \
        FAXUSER=`id -u` \
        FAXGROUP=`id -g` \
        SYSUSER=`id -u` \
        SYSGROUP=`id -g` \
        BIN=$RPM_BUILD_ROOT%{_bindir} \
        SBIN=$RPM_BUILD_ROOT%{_sbindir} \
        LIBDIR=$RPM_BUILD_ROOT%{_libdir} \
        LIBDATA=$RPM_BUILD_ROOT%{_sysconfdir}/hylafax \
        LIBEXEC=$RPM_BUILD_ROOT%{_sbindir} \
        SPOOL=$RPM_BUILD_ROOT%{faxspool} \
        MAN=$RPM_BUILD_ROOT%{_mandir} \
        INSTALL_ROOT=$RPM_BUILD_ROOT

# install: remaining files
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/hylafax
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/hylafax
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/cron.hourly/hylafax

# Prepare docdir by removing non-doc files
# Remove files that are not needed on Linux
rm -f $RPM_BUILD_ROOT%{_sbindir}/{faxsetup.irix,faxsetup.bsdi}
rm -f $RPM_BUILD_ROOT%{faxspool}/bin/{ps2fax.imp,ps2fax.dps}

rm -f $RPM_BUILD_ROOT%{faxspool}/COPYRIGHT

%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
if [ "$1" = "1" ]; then
    /sbin/chkconfig --add %{name}
fi

%preun
if [ "$1" = "0" ]; then
    /sbin/chkconfig --del %{name}
    /sbin/service %{name} stop >/dev/null 2>&1 || :
fi

%postun
/sbin/ldconfig
if [ "$1" = "1" ]; then
    /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi


%files
%defattr(-,root,root,-)
%doc CHANGES CONTRIBUTORS COPYRIGHT README TODO VERSION
%attr(755,root,root) %{_initrddir}/hylafax
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/cron.daily/hylafax
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/cron.hourly/hylafax
%{_libdir}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %{_mandir}/*/*
%attr(755,root,root) %dir %{_sysconfdir}/hylafax
%attr(755,root,root) %dir %{_sysconfdir}/hylafax/faxmail
%attr(755,root,root) %dir %{_sysconfdir}/hylafax/faxmail/application
%attr(755,root,root) %dir %{_sysconfdir}/hylafax/faxmail/image
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/hylafax/faxcover.ps
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/hylafax/faxmail.ps
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/hylafax/hfaxd.conf
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/hylafax/pagesizes
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/hylafax/typerules
%attr(755,root,root) %{_sysconfdir}/hylafax/faxmail/application/pdf
%attr(755,root,root) %{_sysconfdir}/hylafax/faxmail/application/octet-stream
%attr(755,root,root) %{_sysconfdir}/hylafax/faxmail/image/tiff
%attr(-,uucp,uucp) %dir %{faxspool}
%attr(-,uucp,uucp) %dir %{faxspool}/archive
%attr(-,uucp,uucp) %dir %{faxspool}/client
%attr(-,root,root) %dir %{faxspool}/config
%attr(-,root,root) %dir %{faxspool}/dev
%attr(-,uucp,uucp) %dir %{faxspool}/docq
%attr(-,uucp,uucp) %dir %{faxspool}/doneq
%attr(-,uucp,uucp) %dir %{faxspool}/etc
%attr(-,uucp,uucp) %dir %{faxspool}/info
%attr(-,uucp,uucp) %dir %{faxspool}/log
%attr(-,uucp,uucp) %dir %{faxspool}/pollq
%attr(-,uucp,uucp) %dir %{faxspool}/recvq
%attr(-,uucp,uucp) %dir %{faxspool}/sendq
%attr(-,uucp,uucp) %dir %{faxspool}/status
%attr(-,uucp,uucp) %dir %{faxspool}/tmp
%attr(755,root,root) %{faxspool}/bin/
%attr(-,root,root) %{faxspool}/config/*
%attr(-,root,root) %{faxspool}/etc/dpsprinter.ps
%attr(-,root,root) %{faxspool}/etc/cover.templ
%attr(-,root,root) %{faxspool}/etc/lutRS18.pcf
%attr(-,uucp,uucp) %config(noreplace) %{faxspool}/FIFO
%attr(-,root,root) %config(noreplace) %{faxspool}/etc/dialrules*
%attr(-,uucp,uucp) %config(noreplace) %{faxspool}/etc/xferfaxlog
%attr(-,uucp,uucp) %config(noreplace) %{faxspool}/etc/hosts.hfaxd

%changelog
* Thu Jun 19 2008 Dries Verachtert <dries@ulyssis.org> - 5.2.5-1
- Some minor changes for rpmforge.

* Mon Apr 28 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.4-3
- openldap-devel and pam-devel build dependencies

* Wed Apr 23 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.4-1
- update to 5.2.4

* Sat Mar 29 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.3-1
- update to 5.2.3

* Fri Jan 18 2008 Lee Howard <faxguy@howardsilvan.com> - 5.2.2-1
- make licensing BSD, initscript is not config, remove libtiff dependency

* Thu Nov 8 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.11-1
- add libtiff dependency

* Thu Aug 2 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.7-1
- update to 5.1.7

* Sat Jul 14 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.6-1
- accomodate MIMEConverter script location change

* Fri Mar 23 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.2-1
- made faxq's FIFO "noreplace" to keep upgrades from messing up a running faxq

* Thu Mar  8 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.1-1
- update to 5.1.1

* Thu Feb 22 2007 Lee Howard <faxguy@howardsilvan.com> - 5.1.0-1
- update to 5.1.0

* Thu Jan 11 2007 Lee Howard <faxguy@howardsilvan.com> - 5.0.4-1
- update to 5.0.4

* Tue Jan 1 2007 Lee Howard <faxguy@howardsilvan.com> - 5.0.3-1
- update to 5.0.3

* Wed Dec 13 2006 Lee Howard <faxguy@howardsilvan.com> - 5.0.2-1
- update to 5.0.2

* Wed Nov 1 2006 Lee Howard <faxguy@howardsilvan.com> - 5.0.0-1
- update to 5.0.0
- disable build of debuginfo package
- change ownership of config and dev to root,root
- move changelog to the end of the spec file

* Mon Sep 18 2006 Lee Howard <faxguy@howardsilvan.com> - 4.3.0.11-1
- update to 4.3.0.1

* Tue Apr 11 2006 Lee Howard <faxguy@howardsilvan.com> - 4.2.5.6-1
- update to 4.2.5.6

* Tue Apr 11 2006 Lee Howard <faxguy@howardsilvan.com> - 4.2.5.5-1
- initial 4.2.5.5 build
