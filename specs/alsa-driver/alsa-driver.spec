# $Id$
# Authority: matthias
# ExcludeDist: fc2

# Is this a preversion?
#define prever rc2

# Comma separated list of cards for which to compile a driver
%{!?cards: %{expand: %%define cards all}}

# "uname -r" output of the kernel to build for, the running one
# if none was specified with "--define 'kernel <uname -r>'"
%{!?kernel: %{expand: %%define kernel %(uname -r)}}

%define kversion %(echo %{kernel} | sed -e s/smp// -)
%define krelver  %(echo %{kversion} | tr -s '-' '_')
%if %(echo %{kernel} | grep -c smp)
    %{expand:%%define ksmp -smp}
    %{expand:%%define kernel_type smp}
%else
    %{expand:%%define kernel_type up}
%endif

Summary: The Advanced Linux Sound Architecture (ALSA) base files
Name: alsa-driver
Version: 1.0.5a
Release: %{?prever:0.%{prever}.}1%{?dist}
License: GPL
Group: System Environment/Base
Source0: ftp://ftp.alsa-project.org/pub/driver/%{name}-%{version}%{?prever}.tar.bz2
Source1: alsa-makedev.d.txt
Patch0: alsa-driver-depmod.patch
URL: http://www.alsa-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: kernel-source = %{kversion}, MAKEDEV

%description
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. ALSA has the following
significant features: Efficient support for all types of audio interfaces,
from consumer soundcards to professional multichannel audio interfaces,
fully modularized sound drivers, SMP and thread-safe design, user space
library (alsa-lib) to simplify application programming and provide higher
level functionality as well as support for the older OSS API, providing
binary compatibility for most OSS programs.

This package contains the ALSA /dev entries and basic development files.

Available rpmbuild rebuild options :
--without : isapnp sequencer oss

You may also recompile for given cards only by calling rpmbuild with :
--define "cards card1,card2,card3"
(the default is "cards all")

You may also recompile for a given kernel version and arch with :
--define "kernel <uname -r output>"
(for example "kernel 2.4.20-9")
--target <arch>


%package -n kernel%{?ksmp}-module-alsa
Summary: The Advanced Linux Sound Architecture (ALSA) kernel drivers
Release: %{release}_%{krelver}%{?dist}
Group: System Environment/Kernel
Requires: alsa-driver >= 0.9.0
Requires: kernel%{?ksmp} = %{kversion}, /sbin/depmod
Provides: kernel-modules
%{?ksmp:Provides: kernel-module-alsa = %{version}-%{release}_%{krelver}}

%description -n kernel%{?ksmp}-module-alsa
The Advanced Linux Sound Architecture (ALSA) provides audio and MIDI
functionality to the Linux operating system. ALSA has the following
significant features: Efficient support for all types of audio interfaces,
from consumer soundcards to professional multichannel audio interfaces,
fully modularized sound drivers, SMP and thread-safe design, user space
library (alsa-lib) to simplify application programming and provide higher
level functionality as well as support for the older OSS API, providing
binary compatibility for most OSS programs.

This package contains the ALSA kernel modules for the Linux kernel package :
%{kversion} (%{_target_cpu}%{?ksmp:, SMP}).


%prep
%setup -n %{name}-%{version}%{?prever}
%patch0 -p1 -b .nodepmod


%build
# We fool configure with these CFLAGS to not have 686 instructions on 386
CFLAGS="-D__module__%{_target_cpu} -D__module__%{kernel_type}" \
%configure \
    --with-redhat=yes \
    --with-kernel=/usr/src/linux-%{kversion} \
    --with-moddir=/lib/modules/%{kernel}/kernel/sound \
    %{?_without_isapnp:--with-isapnp=no} \
    %{?_without_sequencer:--with-sequencer=no} \
    %{?_without_oss:--with-oss=no} \
    --with-cards=%{cards}

# The good old workaround... again
touch include/linux/workqueue.h

%{__make} %{?_smp_mflags} MODFLAGS="-DMODULE=1 -D__BOOT_KERNEL_H_ -D__MODULE_KERNEL_%{_target_cpu}=1 %{?ksmp:-D__BOOT_KERNEL_SMP=1} %{!?ksmp:-D__BOOT_KERNEL_UP=1}"


%install
%{__rm} -rf %{buildroot}

mkdir -p %{buildroot}/etc/rc.d/init.d/
%{__make} install \
    IUSER=`id -un` \
    IGROUP=`id -gn` \
    DESTDIR=%{buildroot}

# Install and generate all the device stuff
%{__install} -m 644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/makedev.d/alsa
cp -a %{_sysconfdir}/makedev.d/00macros %{buildroot}%{_sysconfdir}/makedev.d/
%{__rm} -f devices

# Create entry list
/dev/MAKEDEV \
    -c %{buildroot}%{_sysconfdir}/makedev.d \
    -d %{buildroot}/dev -M alsa | sed 's|%{buildroot}||g' > device.list

# Remove from the included docs
%{__rm} -f doc/Makefile

# Remove for default rpm 4.1 to not fail
%{__rm} -f %{buildroot}%{_sysconfdir}/makedev.d/00macros
%{__rm} -f %{buildroot}/etc/rc.d/init.d/alsasound


%pre
test -L /dev/snd && rm -f /dev/snd 2>/dev/null 2>&1 || :

%post -n kernel%{?ksmp}-module-alsa
/sbin/depmod -a -F /boot/System.map-%{kernel} %{kernel} >/dev/null 2>&1 || :

%postun -n kernel%{?ksmp}-module-alsa
/sbin/depmod -a -F /boot/System.map-%{kernel} %{kernel} >/dev/null 2>&1 || :


%clean
%{__rm} -rf %{buildroot}


%files -f device.list
%defattr(-, root, root, 0755)
%doc CARDS-STATUS COPYING FAQ README TODO WARNING
%doc alsa-kernel/Documentation/ doc/
%{_sysconfdir}/makedev.d/alsa
%{_includedir}/sound

%files -n kernel%{?ksmp}-module-alsa
%defattr(-, root, root, 0755)
/lib/modules/%{kernel}/kernel/sound


%changelog
* Thu Jul  8 2004 Matthias Saou <http://freshrpms.net/> 1.0.5a-1
- Update to 1.0.5a.

* Thu Apr 15 2004 Matthias Saou <http://freshrpms.net/> 1.0.4-1
- Update to 1.0.4.

* Thu Feb 19 2004 Matthias Saou <http://freshrpms.net/> 1.0.2c-1
- Update to 1.0.2c.

* Thu Jan 29 2004 Matthias Saou <http://freshrpms.net/> 1.0.2-1
- Update to 1.0.2.
- Fix the kernel_type in CFLAGS.

* Sat Jan 10 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-2
- Force --with-redhat=yes configure option and touch workqueue.h.

* Fri Jan  9 2004 Matthias Saou <http://freshrpms.net/> 1.0.1-1
- Update to 1.0.1.
- Removed serialmidi patch.

* Tue Dec  9 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc2.1
- Update to 1.0.0rc2.

* Tue Dec  2 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.rc1.1
- Update to 1.0.0rc1.
- Removed obsolete (yes, again!) Red Hat Linux kernel workaround.

* Mon Nov 24 2003 Matthias Saou <http://freshrpms.net/> 1.0.0-0.pre2.1
- Update to 1.0.0pre2.

* Sun Nov  2 2003 Matthias Saou <http://freshrpms.net/> 0.9.8-3
- Rebuild for Fedora Core 1.
- Added a quick and ugly compile fix for serialmidi.c.

* Mon Oct 27 2003 Matthias Saou <http://freshrpms.net/> 0.9.8-2
- Added workaround to have Red Hat kernel detected with > 2.4.20 too.
- Added workaround to have i386 and i586 modules not compiled with i686 or
  higher CFLAGS.
- Removed the "pre" macro.

* Mon Oct 27 2003 Matthias Saou <http://freshrpms.net/> 0.9.8-1
- Added kernel-modules provides.

* Fri Oct  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.7.

* Sun Aug  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.6.

* Wed Jul  9 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.5.

* Thu Jun 12 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.4.
- Removed workqueue workaround, as it's taken care of by configure.
- Changed $CONSOLE to $ALLWRITE in the makedev script...

* Sun May 25 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3c.
- Major changes in the makedev.d entry for the new devices.

* Fri May  2 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3a.

* Thu May  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.3.
- Renamed alsa-kernel to kernel-module-alsa.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Mar 19 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.2.

* Mon Mar 17 2003 Matthias Saou <http://freshrpms.net/>
- Removed now unneeded vmalloc patch.

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc8d.
- Update to 0.9.1!

* Mon Mar  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc8.
- Removed CFLAGS patch, use new MODFLAGS instead.

* Wed Feb 12 2003 Matthias Saou <http://freshrpms.net/>
- Merge fixes for /sbin/depmod dep and its post/postun scripts.
- Add CFLAGS patch and changes to rebuild for any arch with just the
  right kernel-source installed.
- Minor cleanups inherent to the above.

* Mon Feb  3 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc7.
- Added ability to recompile against non-running kernel.

* Mon Nov 16 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc6.

* Fri Oct 25 2002 Matthias Saou <http://freshrpms.net/>
- Silent the %%post and %%postun scriplets to avoid unresolved symbol
  warnings during upgrades.

* Wed Oct 23 2002 Matthias Saou <http://freshrpms.net/>
- Update to 0.9.0rc4, then rc5.

* Tue Oct  1 2002 Matthias Saou <http://freshrpms.net/>
- Removed the dependency about alsa-driver in alsa-kernel to fix apt problems.

* Sun Sep 29 2002 Matthias Saou <http://freshrpms.net/>
- Added -smp to alsa-kernel packages for SMP systems (needs testing).

* Fri Sep 27 2002 Matthias Saou <http://freshrpms.net/>
- Moved rpmbuild --without options to the description.
- Rebuild for Red Hat Linux 8.0.
- Fixed the /sbin/depmod -a that was run for the wrong sub-package, doh!

* Tue Sep 17 2002 Matthias Saou <http://freshrpms.net/>
- Fixed yet another (last?) bug on SMP systems.

* Sun Sep  8 2002 Matthias Saou <http://freshrpms.net/>
- Fixed build on SMP systems, thanks to Chris Ckloiber.

* Thu Aug 29 2002 Matthias Saou <http://freshrpms.net/>
- Fixed extra files problem with rpm 4.1.
- Added support for disabling isapnp, sequencer and oss.
- Added support to easily modify to build only drivers for specific cards.
- Simplified the device list creation ("alsa" alias in the makedev.d entry).
- Fixed reversed links in the /dev entries.

* Wed Aug 28 2002 Matthias Saou <http://freshrpms.net/>
- Fix the makedev file that didn't like the CVS tag.
- New sub-package -kernel with only the kernel module (to have multiple
  installations of it easily).
- Fixed kernel arch detection by invoking rpm to query kernel package ;-)

* Tue Aug 27 2002 Matthias Saou <http://freshrpms.net/>
- Spec file rewrite.
- Added makedev.d stuff to have device files included cleanly.

