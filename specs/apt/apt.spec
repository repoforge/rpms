# $Id$
# Authority: dag
# Upstream: Panu Matilainen <pmatilai$laiskiainen,org>

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')

%{?dtag: %{expand: %%define %dtag 1}}

%{?rh8:%define _without_elfutils 1}

%{?rh7:%define _without_elfutils 1}
%{?rh7:%define _without_python22 1}
%{?rh7:%define _without_rpm42 1}

%{?el2:%define _without_elfutils 1}
%{?el2:%define _without_pkgconfig 1}
%{?el2:%define _without_python22 1}
%{?el2:%define _without_rpm42 1}

%{?rh6:%define _without_elfutils 1}
%{?rh6:%define _without_pkgconfig 1}
%{?rh6:%define _without_python22 1}
%{?rh6:%define _without_rpm42 1}

Summary: Debian's Advanced Packaging Tool with RPM support
Name: apt
Version: 0.5.15lorg3.94a
Release: 4
License: GPL
Group: System Environment/Base
URL: http://apt-rpm.org/

#Source0: http://apt-rpm.org/releases/apt-%{version}.tar.bz2
Source0: http://apt-rpm.org/testing/apt-%{version}.tar.bz2
Source19: comps2prio.xsl
Source51: upgradevirt.lua
Patch0: apt-0.5.15lorg3.2-ppc.patch
Patch1: apt-0.5.15lorg3.x-cache-corruption.patch
Patch3: apt-0.5.15lorg3.94-gcc43.patch
Patch4: apt-0.5.15lorg3.94a-screen-width-detection.patch
Patch5: apt-0.5.15lorg3.94a-output-streams.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: bison
BuildRequires: bzip2-devel
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: libstdc++-devel
BuildRequires: libtool
BuildRequires: libxml2-devel >= 2.6.16
BuildRequires: ncurses-devel
BuildRequires: readline-devel
BuildRequires: rpm-devel >= 3.0.5
BuildRequires: sqlite-devel
BuildRequires: zlib-devel
%{!?_without_elfutils:BuildRequires: beecrypt-devel, elfutils-devel}
%{?_without_elfutils:BuildRequires: libelf}
%{!?_without_pkgconfig:BuildRequires: pkgconfig >= 0.9}
%{!?_without_python22:BuildRequires: python-devel >= 2.2}

%{?rh8:BuildRequires: libelf-devel}
%{!?rh6:BuildRequires: bzip2-devel, libstdc++-devel, docbook-utils}

Requires: bzip2-libs
Requires: chkconfig
Requires: gnupg
Requires: ldconfig
Requires: libstdc++
Requires: libxml2 >= 2.6.16
Requires: rpm >= 3.0.5
Requires: zlib

%description
A port of Debian's apt tools for RPM based distributions, or at least
originally for Conectiva and now Red Hat Linux. It provides the apt-get
utility that provides a simpler, safer way to install and upgrade packages.
APT features complete installation ordering, multiple source capability and
several other unique features.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package -n python-apt
Summary: Python bindings for libapt-pkg
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: apt-python <= %{version}-%{release}
Provides: apt-python = %{version}-%{release}

%description -n python-apt
The python-apt package contains a module which allows python programs
to access the APT library interface.

%prep
%setup
%patch0 -p1 -b .ppc
%patch1 -p0 -b .mmap
%patch3 -p1 -b .gcc43
%patch4 -p1 -b .screenwidth
%patch5 -p1 -b .outputstreams

### Fix docs to reference correct paths
%{__perl} -pi -e '
        s|\bconfigure-index\.gz\b|configure-index|g;
        s|/usr/share/doc/apt/|%{_docdir}/%{name}-%{version}/|g;
    ' doc/apt.ent doc/*/apt.ent.* doc/offline.sgml contrib/apt-wrapper/apt.ent

%{__install} -Dp -m644 %{SOURCE19} comps2prio.xsl

%{?el5:name='Red Hat Enterprise'; version='5'}
%{?el4:name='Red Hat Enterprise'; version='4'}
%{?el3:name='Red Hat Enterprise'; version='3'}
%{?el2:name='Red Hat Enterprise'; version='2.1'}
%{?fc7:name='Fedora Core'; version='7'}
%{?fc6:name='Fedora Core'; version='6'}
%{?fc5:name='Fedora Core'; version='5'}
%{?fc4:name='Fedora Core'; version='4'}
%{?fc3:name='Fedora Core'; version='3'}
%{?fc2:name='Fedora Core'; version='2'}
%{?fc1:name='Fedora Core'; version='1'}
%{?rh9:name='Red Hat'; version='9'}
%{?rh8:name='Red Hat'; version='8.0'}
%{?rh7:name='Red Hat'; version='7.3'}
%{?rh6:name='Red Hat'; version='6.2'}

%{__cat} <<EOF >rpmpriorities
Essential:
  authconfig
  basesystem
  bash
  centos-release
  coreutils
  cpio
  e2fsprogs
  ed
  fedora-release
  file
  filesystem
  glibc
  grub
  hdparm
  hotplug
  initscripts
  iproute
  iputils
  kbd
  kudzu
  libgcc
  losetup
  passwd
  procps
  raidtools
  readline
  redhat-release
  rpm
  rsyslog
  setserial
  setup
  shadow-utils
  sh-utils
  sysklogd
  SysVinit
  sysvinit
  udev
  util-linux
  util-linux-ng
  vim-minimal
EOF

%{__cat} <<EOF >sources.list
### Add your custom repositories here or in /etc/apt/sources.list.d/
EOF

%{__cat} <<'EOF' >os.list
# Name: Operating system and updates

### Red Hat Enterprise Linux
#repomd http://mirror.centos.org centos/$(VERSION)/os/$(ARCH)
#repomd http://mirror.centos.org centos/$(VERSION)/updates/$(ARCH)
#repomd http://mirror.centos.org centos/$(VERSION)/extras/$(ARCH)
#repomd http://mirror.centos.org centos/$(VERSION)/fasttrack/$(ARCH)
#repomd http://mrepo rhel$(VERSION)s-$(ARCH)/RPMS.os
#repomd http://mrepo rhel$(VERSION)s-$(ARCH)/RPMS.updates
#rpm http://mrepo rhel$(VERSION)s-$(ARCH) os updates

### Fedora Core Linux
%{!?fedora:#}repomd http://ayo.freshrpms.net fedora/linux/$(VERSION)/$(ARCH)/core
%{!?fedora:#}repomd http://ayo.freshrpms.net fedora/linux/$(VERSION)/$(ARCH)/updates
#rpm http://ayo.freshrpms.net fedora/linux/$(VERSION)/$(ARCH) core updates

### Red Hat Linux
%{!?rhl:#}repomd http://ayo.freshrpms.net redhat/$(VERSION)/$(ARCH)/os
%{!?rhl:#}repomd http://ayo.freshrpms.net redhat/$(VERSION)/$(ARCH)/updates
#rpm http://ayo.freshrpms.net redhat/$(VERSION)/$(ARCH) os updates
EOF

%{__cat} <<EOF >apt.conf
// User customizable configuration

RPM {
    // Uncomment to disable GPG-signature checking for packages
    // GPG-Check "false";
    // Uncomment to prevent kernel being handled along with (dist-)upgrade
    // Upgrade-Virtual "false";
    // Uncomment to hold packages with modified config files in (dist-)upgrade
    // Preserve-Config "true";
};

// Options for the downloading routines
Acquire {
    // Retries "1";
    // http::Proxy "http://user:password@proxy-server.domain.tld:port/";
    // http::Proxy "http://proxy-server.domain.tld:port/";
};
EOF

%{__cat} <<EOF >default.conf
// These are "factory defaults", DO NOT CHANGE!
// Put your customizations to /etc/apt/apt.conf instead, those will
// override any setting in here.

APT {
    Get {
        Show-Versions "true";
    }
    DistroVersion "$version";
};

RPM {
    // Always check GPG keys and automatically import new ones
    GPG-Check "true";
    GPG-Import "true";
    Allow-Duplicated {
        "^gpg-pubkey$";
        "^kernel$";
        "^kernel-bigmem$";
        "^kernel-devel$";
        "^kernel-enterprise$";
        "^kernel-headers$";
        "^kernel-hugemem$";
        "^kernel-largesmp$";
        "^kernel-smp$";
        "^kernel-source$";
        "^kernel-unsupported$";
        "^kernel-xen$";
    };
    Order "true";
};

// Options for the downloading routines
Acquire {
    http::User-Agent "APT-HTTP/1.3";
};

Scripts {
    Init { "gpg-import.lua"; };
    PM {
        Pre { "gpg-check.lua"; };
        Post { "upgradevirt.lua"; };
    };
    AptGet {
        Upgrade { "upgradevirt.lua"; };
        DistUpgrade {"upgradevirt.lua"; };
        Install::SelectPackage { "upgradevirt.lua"; };
        Install::PreResolve { "upgradevirt.lua"; };
        Install::TranslateArg { "upgradevirt.lua"; };
    };
    Synaptic {
        DistUpgrade { "upgradevirt.lua"; };
    };
};

// upgradevirt.lua specific item - make newly installed kernel default
Kernel {
    // As of FC3+, the kernel packages take care of this automatically
    //Set-Default "true";
    Module-Prefix {
        "kernel-module-";
        "kmod-";
    };
};
EOF

%{__cat} <<'EOF' >apt.sysv
#!/bin/bash
#
# Init file to enable/disable automatice upgrades by apt
#
# Written by Dag Wieërs <dag@wieers.com>
#
# chkconfig: - 50 01
# description: Enable daily apt upgrade using cron.
#
# processname: apt-get
# config: /etc/apt/

source /etc/rc.d/init.d/functions

lockfile="/var/lock/subsys/apt"

RETVAL=0

start() {
    echo -n $"Enabling daily apt upgrade in cron: "
    touch "$lockfile" && success || failure
    RETVAL=$?
    echo
}

stop() {
    echo -n $"Disabling daily apt upgrade in cron: "
    rm -f "$lockfile" && success || failure
    RETVAL=$?
    echo
}

restart() {
    stop
    start
}
case "$1" in
  start)
    start
    ;;
  stop)
    stop
    ;;
  restart|force-reload)
    restart
    ;;
  reload)
    ;;
  condrestart)
    [ -f "$lockfile" ] && restart
    ;;
  status)
    if [ -f $lockfile ]; then
        echo $"Daily apt upgrade is enabled in cron."
        RETVAL=0
    else
        echo $"Daily apt upgrade is disabled in cron."
        RETVAL=3
    fi
    ;;
  *)
    echo $"Usage: $0 {start|stop|status|restart|reload|force-reload|condrestart}"
    exit 1
esac

exit $RETVAL
EOF

%{__cat} <<EOF >apt.sysconfig
### Actually perform updates or only check what's available [yes|no]
CHECK_ONLY=no

### Hold back packages with modified configuration files [yes|no]
PRESERVE_CONFIG=no

### Any extra parameters you want to pass to dist-upgrade
EXTRA_OPTIONS=
EOF

%{__cat} <<'EOF' >apt.cron
#!/bin/sh

[ ! -f /var/lock/subsys/apt ] && exit 0

[ -f /etc/sysconfig/apt ] && source /etc/sysconfig/apt

[ $CHECK_ONLY == "yes" ] && OPTS="$OPTS --check-only"
[ $PRESERVE_CONFIG == "yes" ] && OPTS="$OPTS -o rpm::preserve-config=true"
OPTS="$OPTS $EXTRA_OPTIONS"

if /usr/bin/apt-get -qq update; then
    /usr/bin/apt-get dist-upgrade -qq --check-only
    if [ $? -eq 100 ]; then
        /usr/bin/apt-get -q -y $OPTS dist-upgrade
    fi
fi
EOF

%build
%{?_without_pkgconfig:export PKG_CONFIG="/bin/true"}
%{?_without_pkgconfig:export LIBXML2_CFLAGS="$(xml2-config --cflags)"}
%{?_without_pkgconfig:export LIBXML2_LIBS="$(xml2-config --libs)"}
%configure \
    --program-prefix="%{?_program_prefix}" \
    --includedir="%{_includedir}/apt-pkg" \
    --disable-dependency-tracking \
    --disable-static
%{__make} %{?_smp_mflags}

%if %{!?_without_python22:1}0
%{__make} -C python PYTHON="%{__python}" %{?_smp_mflags}
%{__python} -O -c "import py_compile; py_compile.compile('python/apt.py')"
%endif

#xsltproc -o rpmpriorities comps2prio.xsl %{_datadir}/comps/%{_build_arch}/comps.xml

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" includedir="%{_includedir}/apt-pkg"
%find_lang %{name}

%{__install} -d -m0755 %{buildroot}%{_sysconfdir}/apt/{apt.conf.d,gpg,sources.list.d}/
%{__install} -d -m0755 %{buildroot}%{_libdir}/apt/scripts/
%{__install} -Dp -m0644 apt.conf %{buildroot}%{_sysconfdir}/apt/apt.conf
%{__install} -Dp -m0644 default.conf %{buildroot}%{_sysconfdir}/apt/apt.conf.d/default.conf
#%{__install} -Dp -m0644 sources.list %{buildroot}%{_sysconfdir}/apt/sources.list
%{__install} -Dp -m0644 os.list %{buildroot}%{_sysconfdir}/apt/sources.list.d/os.list
%{__install} -Dp -m0644 rpmpriorities %{buildroot}%{_sysconfdir}/apt/rpmpriorities
touch %{buildroot}%{_sysconfdir}/apt/{preferences,vendors.list}

### Install the LUA scripts
%{__install} -Dp -m0644 contrib/allow-duplicated/allow-duplicated.conf %{buildroot}%{_sysconfdir}/apt/apt.conf.d/allow-duplicated.conf
%{__install} -Dp -m0755 contrib/allow-duplicated/allow-duplicated.lua %{buildroot}%{_datadir}/apt/scripts/allow-duplicated.lua
%{__install} -Dp -m0644 contrib/apt-groupinstall/apt-groupinstall.conf %{buildroot}%{_sysconfdir}/apt/apt.conf.d/apt-groupinstall.conf
%{__install} -Dp -m0755 contrib/apt-groupinstall/apt-groupinstall.lua %{buildroot}%{_datadir}/apt/scripts/apt-groupinstall.lua
%{__install} -Dp -m0755 contrib/apt-groupinstall/groupinstall-backend-comps.py %{buildroot}%{_datadir}/apt/scripts/groupinstall-backend-comps.py
touch %{buildroot}%{_datadir}/apt/scripts/groupinstall-backend-comps.py{c,o}
%if %{!?_without_rpm42:1}0
%{__install} -Dp -m0755 contrib/gpg-check/gpg-check.lua %{buildroot}%{_datadir}/apt/scripts/gpg-check.lua
%{__install} -Dp -m0755 contrib/gpg-check/gpg-import.lua %{buildroot}%{_datadir}/apt/scripts/gpg-import.lua
%endif
%{__install} -Dp -m0644 contrib/log/log.conf %{buildroot}%{_sysconfdir}/apt/apt.conf.d/log.conf
%{__install} -Dp -m0755 contrib/log/log.lua %{buildroot}%{_datadir}/apt/scripts/log.lua
%{__install} -Dp -m0755 %{SOURCE51} %{buildroot}%{_datadir}/apt/scripts/upgradevirt.lua

%if %{!?_without_python22:1}0
### Install the python bindings
mkdir -p %{buildroot}%{python_sitearch}/
%{__install} -Dp -m0755 python/_apt.so %{buildroot}%{python_sitearch}/_apt.so
%{__install} -Dp -m0644 python/apt.py %{buildroot}%{python_sitearch}/apt.py
touch %{buildroot}%{python_sitearch}/apt.py{c,o}
%endif

### Install the cronjob
%{__install} -Dp -m0755 apt.sysv %{buildroot}%{_initrddir}/apt
%{__install} -Dp -m0755 apt.cron %{buildroot}%{_sysconfdir}/cron.daily/apt
%{__install} -Dp -m0644 apt.sysconfig %{buildroot}%{_sysconfdir}/sysconfig/apt

### Clean up docs
find contrib/ -type f -exec %{__chmod} a-x {} \;

%post
/sbin/ldconfig
/sbin/chkconfig --add apt

%preun
if [ $1 -eq 0 ] ; then
    /sbin/service apt stop &>/dev/null || :
    /sbin/chkconfig --del apt
fi

%postun -p /sbin/ldconfig

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ABOUT* AUTHORS* ChangeLog COPYING* lua/COPYRIGHT TODO comps2prio.xsl contrib/ doc/examples/
%doc %{_mandir}/man5/apt.conf.5*
%doc %{_mandir}/man5/apt_preferences.5*
%doc %{_mandir}/man5/sources.list.5*
%doc %{_mandir}/man5/vendors.list.5*
%doc %{_mandir}/man8/apt-cache.8*
%doc %{_mandir}/man8/apt-cdrom.8*
%doc %{_mandir}/man8/apt-config.8*
%doc %{_mandir}/man8/apt-get.8*
%doc %{_mandir}/man8/apt.8*
%dir %{_sysconfdir}/apt/
%config(noreplace) %{_sysconfdir}/apt/apt.conf
%config(noreplace) %{_sysconfdir}/apt/preferences
#config(noreplace) %{_sysconfdir}/apt/sources.list
%config(noreplace) %{_sysconfdir}/apt/vendors.list
%config %{_sysconfdir}/apt/rpmpriorities
%config %{_sysconfdir}/apt/apt.conf.d/
%config(noreplace) %{_sysconfdir}/apt/gpg/
%config(noreplace) %{_sysconfdir}/apt/sources.list.d/
%config(noreplace) %{_sysconfdir}/sysconfig/apt
%config %{_sysconfdir}/cron.daily/apt
%config %{_initrddir}/apt
%{_bindir}/apt-cache
%{_bindir}/apt-cdrom
%{_bindir}/apt-config
%{_bindir}/apt-get
%{_bindir}/apt-shell
%{_bindir}/countpkglist
%{_bindir}/genbasedir
%{_bindir}/genpkglist
%{_bindir}/gensrclist
%{_datadir}/apt/
%{_libdir}/apt/
%{_libdir}/libapt-pkg.so.*
%{_localstatedir}/cache/apt/
%{_localstatedir}/lib/apt/

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/apt-pkg/
%{_libdir}/libapt-pkg.so
%{_libdir}/pkgconfig/libapt-pkg.pc
%exclude %{_libdir}/libapt-pkg.la

%if %{!?_without_python22:1}0
%files -n python-apt
%defattr(-, root, root, 0755)
%{python_sitearch}/_apt.so
%{python_sitearch}/apt.py
%ghost %{python_sitearch}/apt.pyc
%ghost %{python_sitearch}/apt.pyo
%endif

%changelog
* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.94a-4
- Added patches. (Vladislav Bogdanov)

* Wed Oct 29 2008 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.94a-3
- Released 0.5.15lorg3.94a as stable.

* Thu Jun 12 2008 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.94a-2
- Improved default configuration.
- Added pkglog.lua by default.

* Wed Jun 11 2008 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.94a-1
- Updated to release 0.5.15lorg3.94a.

* Wed Jun 11 2008 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.94-1
- Added patches from Fedora.
- Updated to release 0.5.15lorg3.94.

* Fri Jun 23 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.2-1
- Updated to release 0.5.15lorg3.2.

* Sun Jun 04 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.1-4
- Fixed APT::DistroVersion.

* Sun Jun 04 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.1-3
- Added APT::DistroVersion and RPM::Order to apt.conf.

* Mon May 29 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.1-2
- Fixed a segfault with the new createrepo -n output.

* Tue May 23 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3.1-1
- Updated to 0.5.15lorg3.1.

* Thu Apr 27 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3-3
- Added patch to handle no-epoch on <= RH9.

* Tue Apr 25 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3-2
- Added patch to allow synaptic to build.

* Mon Apr 24 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3-1
- Updated to 0.5.15lorg3.

* Tue Apr 11 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg3-0.rc1
- Updated to 0.5.15lorg3-rc1.

* Sun Mar 05 2006 Dag Wieers <dag@wieers.com> - 0.5.15lorg2-0.20060301
- Experimental version from Panu with repomd and multilib support.

* Mon Jan 02 2005 Dries Verachtert <dries@ulyssis.org> - 0.5.15cnc7-1
- Added libtoolize and autoreconf fix for Fedora Core 5, thanks
  to Stephen Clement.
- Updated to release 0.5.15cnc7.

* Sat Nov 20 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-4
- Added readline-devel as buildrequirement for apt-shell.

* Thu Jul 01 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-3
- Fix for apt-bug triggered by mach.

* Fri Jun 04 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-2
- Make apt understand about architectures.

* Tue Mar 23 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc6-1
- Updated to release 0.5.15cnc6.

* Sat Jan 24 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc1-1
- Added RHAS21 repository.

* Sun Jan 04 2004 Dag Wieers <dag@wieers.com> - 0.5.15cnc5-0
- Updated to release 0.5.15cnc5.

* Sat Dec 06 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc4-1
- Disabled the epoch promotion behaviour on RH9.

* Thu Dec 04 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc4-0
- Updated to release 0.5.15cnc4.

* Tue Nov 25 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc3-0
- Updated to release 0.5.15cnc3.

* Mon Nov 10 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc2-0
- Updated to release 0.5.15cnc2.

* Mon Nov 10 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc1-1
- Fixed apt pinning.
- Added RHFC1 repository.

* Sat Nov 08 2003 Dag Wieers <dag@wieers.com> - 0.5.15cnc1-0
- Updated to release 0.5.15cnc1.

* Sun Oct 26 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc6-1
- Added RHEL3 repository.

* Tue Jun 10 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc6-0
- Added newrpms and enable it by default.
- Updated to release 0.5.5cnc6.

* Tue Jun 03 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-4
- Added freshrpms and enable it by default.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-3
- Work around a bug in apt (apt.conf).

* Fri May 30 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-2
- Moved sources.list to sources.d/

* Wed Apr 16 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc5-1
- Updated to release 0.5.5cnc5.

* Tue Apr 08 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc4.1-2
- RH90 repository rename from redhat/9.0 to redhat/9.

* Sat Apr 05 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc4.1-1
- FreshRPMS fixes to repository locations.

* Sun Mar 09 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc4.1-0
- Updated to release 0.5.5cnc4.1.

* Fri Feb 28 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc3-0
- Updated to release 0.5.5cnc3.

* Tue Feb 25 2003 Dag Wieers <dag@wieers.com> - 0.5.5cnc2-0
- Updated to release 0.5.5cnc2.

* Mon Feb 10 2003 Dag Wieers <dag@wieers.com> - 0.5.4cnc9-0
- Initial package. (using DAR)
