# TODO, maybe some day:
# - livebuffer patch, http://www.vdr-portal.de/board/thread.php?threadid=37309
# - channelfilter patch, http://www.u32.de/vdr.html#patches
# - UTF-8 patch, http://www.free-x.de/utf8/

%define videodir  /srv/vdr
%define audiodir  /srv/audio
%define plugindir %{_libdir}/vdr
%define configdir %{_sysconfdir}/vdr
%define datadir   %{_datadir}/vdr
%define cachedir  %{_var}/cache/vdr
%define rundir    %{_var}/run/vdr
%define vardir    %{_var}/lib/vdr
%define logdir    %{_var}/log/vdr
%define vdr_user  vdr
%define vdr_group video
# From APIVERSION in config.h
%define apiver    1.4.5

Name:           vdr
Version:        1.4.5
Release:        5%{?dist}.bs
Summary:        Video Disk Recorder

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.cadsoft.de/vdr/
Source0:        ftp://ftp.cadsoft.de/vdr/%{name}-%{version}.tar.bz2
Source1:        %{name}.init
Source2:        %{name}.sysconfig
Source4:        %{name}-udev.rules
Source5:        %{name}-reccmds.conf
Source6:        %{name}-commands.conf
Source7:        %{name}-runvdr.sh
Source8:        %{name}.consoleperms
Source9:        %{name}-config.sh
Source10:       %{name}-README.package
Source11:       %{name}-skincurses.conf
Source12:       %{name}-sky.conf
Source13:       %{name}-timercmds.conf
Source14:       %{name}-shutdown.sh
Patch0:         %{name}-channel+epg.patch
Patch1:         http://zap.tartarus.org/~ds/debian/dists/unstable/main/source/vdr_1.4.5-1.ds.diff.gz
Patch2:         http://www.saunalahti.fi/~rahrenbe/vdr/patches/vdr-1.4.5-liemikuutio-1.13.diff.gz
Patch3:         %{name}-1.4.1-paths.patch
Patch4:         %{name}-1.4.1-dumpable.patch
Patch5:         ftp://ftp.cadsoft.de/vdr/Developer/vdr-1.4.5-1.diff
Patch6:         ftp://ftp.cadsoft.de/vdr/Developer/vdr-1.4.5-2.diff
Patch7:         channelscan-vdr.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libjpeg-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig
BuildRequires:  perl(File::Spec)
Requires:       udev
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Provides:       vdr(abi) = %{apiver}

%description
VDR implements a complete digital set-top-box and video recorder.
It can work with signals received from satellites (DVB-S) as well as
cable (DVB-C) and terrestrial (DVB-T) signals.  At least one DVB card
is required to run VDR.

%package        devel
Summary:        Development files for VDR
Group:          Development/Libraries
Requires:       pkgconfig
Provides:       vdr-devel(api) = %{apiver}

%description    devel
%{summary}.

%package        skincurses
Summary:        Shell window skin plugin for VDR
Group:          Applications/Multimedia
%if 0%{?_with_plugins:1}
BuildRequires:  ncurses-devel
%endif
Requires:       vdr(abi) = %{apiver}

%description    skincurses
The skincurses plugin implements a VDR skin that works in a shell
window, using only plain text output.

%package        sky
Summary:        Sky Digibox plugin for VDR
Group:          Applications/Multimedia
Requires:       vdr(abi) = %{apiver}

%description    sky
The sky plugin implements a new device for VDR, which is based on the
MPEG2 encoder card described at linuxtv.org/mpeg2/kfir.xml.  It allows
you to connect the analog a/v output of your Sky Digibox to VDR, so
that you can enjoy the full recording flexibility of VDR with your Sky
subscription.  You will need a Sky Digibox and a valid subscription in
order to use this plugin.


%prep
%setup -q
%patch0 -p1
%patch1 -p1
#patch -i debian/patches/02_latin-1.dpatch
patch -i debian/patches/02_plugin_missing.dpatch
patch -i debian/patches/02_reload.dpatch
# sort_options would be nice, but it conflicts with channel+epg which is nicer
#patch -i debian/patches/02_sort_options.dpatch
#patch -i debian/patches/03_no-data_timeout.dpatch
#patch -i debian/patches/03_settime_segfault.dpatch
#patch -i debian/patches/04_cmdsubmenu.dpatch
#patch -i debian/patches/05_nissl_dvbplayer.dpatch
#patch -i debian/patches/06_recording_readonly.dpatch
patch -i debian/patches/06_recording_scan_speedup.dpatch
patch -i debian/patches/07_blockify_define.dpatch
#patch -i debian/patches/09_increase_epgscan_timeout.dpatch
patch -i debian/patches/10_livelock.dpatch
patch -i debian/patches/11_atsc.dpatch
echo "DEFINES += -DHAVE_ATSC" >> Makefile
#patch -i debian/patches/12_skinclassic_icons.dpatch
#patch -i debian/patches/15_cut_compensate_start_time.dpatch
patch -i debian/patches/19_debian_osdbase_maxitems.dpatch
patch -i debian/patches/opt-20_epgsearch.dpatch
#patch -i debian/patches/opt-20_liemikuutio.dpatch
patch -i debian/patches/opt-20_subtitles_0.4.0_ttxtsubs_0.0.5.dpatch
patch -i debian/patches/opt-20_suspend.dpatch
patch -i debian/patches/opt-20_vdr-timer-info.dpatch
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# Fix up paths
sed -i -e 's|\b\(ConfigDirectory = \)VideoDirectory;|\1"%{configdir}";|' vdr.c
sed -i \
  -e 's|__CACHEDIR__|%{cachedir}|'   \
  -e 's|__CONFIGDIR__|%{configdir}|' \
  -e 's|__PLUGINDIR__|%{plugindir}|' \
  -e 's|__VIDEODIR__|%{videodir}|'   \
  epg2html.pl vdr.1 vdr.c PLUGINS/src/sky/README

# Fix up man page section
sed -i -e 's/\bvdr\(\s*\)(1)/vdr\1(8)/' HISTORY UPDATE-1.2.0 vdr.5
sed -i -e 's/\bvdr\([\. ]\)1\b/vdr\18/' HISTORY vdr.1

for f in CONTRIBUTORS HISTORY* UPDATE-1.4.0 ; do
  iconv -f iso-8859-1 -t utf-8 -o $f.utf8 $f && mv $f.utf8 $f
done

sed -i -e 's/epg2html.pl/epg2html/' CONTRIBUTORS HISTORY epg2html.pl
sed -i -e 's/svdrpsend.pl/svdrpsend/' HISTORY
sed -i -e 's/getskyepg.pl/getskyepg/' \
  PLUGINS/src/sky/{getskyepg.pl,README,HISTORY}

cp -p %{SOURCE5} reccmds.conf
cp -p %{SOURCE13} timercmds.conf
sed -e 's|/srv/audio|%{audiodir}|' %{SOURCE6} > commands.conf
# Unfortunately these can't have comments in them, so ship 'em empty.
cat /dev/null > channels.conf
cat /dev/null > remote.conf
cat /dev/null > setup.conf
cat /dev/null > timers.conf

install -pm 644 %{SOURCE10} README.package

# Would like to do "files {channels,setup,timers}.conf" from config dir
# only, but rename() in cSafeFile barks "device or resource busy", cf.
# http://lists.suse.com/archive/suse-programming-e/2003-Mar/0051.html
cat << EOF > %{name}.rwtab
dirs	%{cachedir}
files	%{configdir}
files	%{vardir}
EOF


%build

# Intentionally not using %{version} or %{apiver} here, see %check
vdrver=$(sed -ne '/define VDRVERSION/s/^.*"\(.*\)".*$/\1/p' config.h)
apiver=$(sed -ne '/define APIVERSION/s/^.*"\(.*\)".*$/\1/p' config.h)

cat << EOF > vdr.pc
videodir=%{videodir}
audiodir=%{audiodir}
plugindir=%{plugindir}
configdir=%{configdir}
datadir=%{datadir}
cachedir=%{cachedir}
rundir=%{rundir}
vardir=%{vardir}
logdir=%{logdir}
user=%{vdr_user}
group=%{vdr_group}
apiversion=$apiver

Name: VDR
Description: Video Disk Recorder
Version: $vdrver
EOF

cat << EOF > Make.config
CC           = %{__cc}
CXX          = %{__cxx}

ifeq (\$(RPM_OPT_FLAGS),)
  CFLAGS     = $RPM_OPT_FLAGS
  CXXFLAGS   = $RPM_OPT_FLAGS -Wall -Woverloaded-virtual
else
  CFLAGS     = \$(RPM_OPT_FLAGS)
  CXXFLAGS   = \$(RPM_OPT_FLAGS) -Wall -Woverloaded-virtual
endif
ifdef PLUGIN
  CFLAGS    += -fPIC
  CXXFLAGS  += -fPIC
endif

PLUGINLIBDIR = \$(DESTDIR)\$(shell pkg-config vdr --variable=plugindir)
VIDEODIR     = \$(DESTDIR)\$(shell pkg-config vdr --variable=videodir)
LIBDIR       = \$(PLUGINLIBDIR)

VDR_USER     = %{vdr_user}
EOF

export PKG_CONFIG_PATH=$(pwd)
make %{?_smp_mflags} all include-dir
%if 0%{?_with_plugins:1}
make %{?_smp_mflags} -C PLUGINS/src/skincurses LIBDIR=. all
make %{?_smp_mflags} -C PLUGINS/src/sky        LIBDIR=. all
%endif


%install
rm -rf $RPM_BUILD_ROOT

abs2rel() { perl -MFile::Spec -e 'print File::Spec->abs2rel(@ARGV)' "$@" ; }

install -Dpm 755 vdr $RPM_BUILD_ROOT%{_sbindir}/vdr

install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 svdrpsend.pl $RPM_BUILD_ROOT%{_bindir}/svdrpsend
install -pm 755 epg2html.pl $RPM_BUILD_ROOT%{_bindir}/epg2html

install -Dpm 644 vdr.1 $RPM_BUILD_ROOT%{_mandir}/man8/vdr.8
install -Dpm 644 vdr.5 $RPM_BUILD_ROOT%{_mandir}/man5/vdr.5

install -dm 755 $RPM_BUILD_ROOT%{configdir}/plugins
install -pm 644 *.conf $RPM_BUILD_ROOT%{configdir}

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d

install -dm 755 $RPM_BUILD_ROOT%{configdir}/themes
touch $RPM_BUILD_ROOT%{configdir}/themes/{classic,sttng}-default.theme

install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/vdr
sed -i \
  -e 's|/usr/sbin/|%{_sbindir}/|'  \
  -e 's|/etc/vdr/|%{configdir}/|g' \
  -e 's|/var/lib/vdr/|%{vardir}/|' \
  -e 's|VDR_USER|%{vdr_user}|'     \
  -e 's|VDR_GROUP|%{vdr_group}|'   \
  $RPM_BUILD_ROOT%{_initrddir}/vdr

install -pm 755 %{SOURCE7} $RPM_BUILD_ROOT%{_sbindir}/runvdr
sed -i \
  -e 's|/usr/sbin/|%{_sbindir}/|'                    \
  -e 's|/etc/sysconfig/|%{_sysconfdir}/sysconfig/|g' \
  -e 's|/usr/lib/vdr\b|%{plugindir}|'                \
  -e 's|VDR_PLUGIN_VERSION|%{apiver}|'               \
  $RPM_BUILD_ROOT%{_sbindir}/runvdr

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
sed -e 's|/usr/lib/vdr/|%{plugindir}/|' < %{SOURCE2} \
  > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr

install -dm 755 $RPM_BUILD_ROOT%{videodir}
install -dm 755 $RPM_BUILD_ROOT%{audiodir}

install -dm 755 $RPM_BUILD_ROOT%{plugindir}/bin
sed -e 's|/var/lib/vdr/|%{vardir}/|' < %{SOURCE14} \
  > $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-shutdown.sh
chmod 755 $RPM_BUILD_ROOT%{plugindir}/bin/%{name}-shutdown.sh
install -dm 755 $RPM_BUILD_ROOT%{cachedir}
touch $RPM_BUILD_ROOT%{cachedir}/epg.data
install -dm 755 $RPM_BUILD_ROOT%{datadir}/logos
install -dm 755 $RPM_BUILD_ROOT%{rundir}
install -dm 755 $RPM_BUILD_ROOT%{vardir}
touch $RPM_BUILD_ROOT%{vardir}/acpi-wakeup
install -dm 755 $RPM_BUILD_ROOT%{logdir}

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d
sed -e 's/VDR_GROUP/%{vdr_group}/' < %{SOURCE4} \
  > $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/51-%{name}.rules
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/*-%{name}.rules

install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/security/console.perms.d
sed -e 's/VDR_GROUP/%{vdr_group}/' < %{SOURCE8} \
  > $RPM_BUILD_ROOT%{_sysconfdir}/security/console.perms.d/95-%{name}.perms
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/security/console.perms.d/*%{name}.perms

install -Dpm 644 %{name}.rwtab $RPM_BUILD_ROOT%{_sysconfdir}/rwtab.d/%{name}

# devel
install -Dpm 644 vdr.pc $RPM_BUILD_ROOT%{_libdir}/pkgconfig/vdr.pc
install -pm 755 %{SOURCE9} $RPM_BUILD_ROOT%{_bindir}/vdr-config
install -pm 755 newplugin $RPM_BUILD_ROOT%{_bindir}/vdr-newplugin
install -dm 755 $RPM_BUILD_ROOT%{_libdir}/vdr/include/vdr
install -pm 644 Make.config $RPM_BUILD_ROOT%{_libdir}/vdr
install -dm 755 $RPM_BUILD_ROOT%{_includedir}/{vdr,libsi}
cp -pLR include/* $RPM_BUILD_ROOT%{_includedir}/
ln -s $(abs2rel %{_includedir}/vdr/config.h %{_libdir}/vdr) \
  $RPM_BUILD_ROOT%{_libdir}/vdr

# plugins
%if 0%{?_with_plugins:1}
install -pm 755 PLUGINS/src/skincurses/libvdr-skincurses.so.%{apiver} \
  $RPM_BUILD_ROOT%{plugindir}
install -pm 644 %{SOURCE11} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf
install -pm 755 PLUGINS/src/sky/libvdr-sky.so.%{apiver} \
  $RPM_BUILD_ROOT%{plugindir}
install -pm 644 %{SOURCE12} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/sky.conf
install -pm 755 PLUGINS/src/sky/getskyepg.pl \
  $RPM_BUILD_ROOT%{_bindir}/getskyepg
install -Dpm 644 PLUGINS/src/sky/channels.conf.sky \
  $RPM_BUILD_ROOT%{configdir}/plugins/sky/channels.conf.sky
%endif


%check
export PKG_CONFIG_PATH=$RPM_BUILD_ROOT%{_libdir}/pkgconfig
if [ "$(pkg-config vdr --variable=apiversion)" != "%{apiver}" ] ; then
    echo "ERROR: API version mismatch in vdr.pc / package / config.h" ; exit 1
fi


%clean
rm -rf $RPM_BUILD_ROOT


%pre
%{_sbindir}/groupadd -r video 2>/dev/null || :
%{_sbindir}/useradd -c "Video Disk Recorder" -d %{videodir} \
  -g %{vdr_group} -M -n -r -s /sbin/nologin %{vdr_user} 2>/dev/null || :

%post
/sbin/chkconfig --add vdr

%preun
if [ $1 -eq 0 ] ; then
    %{_initrddir}/vdr stop >/dev/null 2>&1 || :
    /sbin/chkconfig --del vdr
fi

%postun
[ $1 -gt 0 ] && %{_initrddir}/vdr try-restart >/dev/null || :


%files
%defattr(-,root,root,-)
%doc CONTRIBUTORS COPYING HISTORY* INSTALL MANUAL README* UPDATE-1.[24].0
%config(noreplace) %{_sysconfdir}/sysconfig/vdr
%config(noreplace) %{_sysconfdir}/udev/rules.d/*-%{name}.rules
%config(noreplace) %{_sysconfdir}/security/console.perms.d/*-%{name}.perms
%config(noreplace) %{_sysconfdir}/rwtab.d/%{name}
%config %{_sysconfdir}/sysconfig/vdr-plugins.d/
%{_initrddir}/vdr
%{_bindir}/epg2html
%{_bindir}/svdrpsend
%{_sbindir}/runvdr
%{_sbindir}/vdr
%dir %{plugindir}/
%dir %{plugindir}/bin/
%{plugindir}/bin/%{name}-shutdown.sh
%{datadir}/
%{_mandir}/man[58]/vdr.[58]*
%defattr(-,%{vdr_user},%{vdr_group},-)
%dir %{rundir}/
# TODO: tighten this (root:root ownership to some files/dirs)?
%dir %{configdir}/
%dir %{configdir}/plugins/
%dir %{configdir}/themes/
%ghost %{configdir}/themes/*.theme
%config(noreplace) %{configdir}/*.conf
%dir %{videodir}/
%dir %{audiodir}/
%defattr(-,%{vdr_user},root,-)
%dir %{logdir}/
%dir %{vardir}/
%ghost %{vardir}/acpi-wakeup
%dir %{cachedir}/
%ghost %{cachedir}/epg.data

%files devel
%defattr(-,root,root,-)
%doc COPYING PLUGINS.html
%{_bindir}/vdr-config
%{_bindir}/vdr-newplugin
%{_includedir}/libsi/
%{_includedir}/vdr/
%{_libdir}/pkgconfig/vdr.pc
%dir %{_libdir}/vdr/
%{_libdir}/vdr/Make.config
%{_libdir}/vdr/config.h

%if 0%{?_with_plugins:1}
%files skincurses
%defattr(-,root,root,-)
%doc PLUGINS/src/skincurses/COPYING PLUGINS/src/skincurses/HISTORY
%doc PLUGINS/src/skincurses/README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/skincurses.conf
%{plugindir}/libvdr-skincurses.so.%{apiver}

%files sky
%defattr(-,root,root,-)
%doc PLUGINS/src/sky/COPYING PLUGINS/src/sky/HISTORY
%doc PLUGINS/src/sky/README PLUGINS/src/sky/lircd.conf.sky
%{_bindir}/getskyepg
%config(noreplace) %{configdir}/plugins/sky/channels.conf.sky
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/sky.conf
%{plugindir}/libvdr-sky.so.%{apiver}
%endif

%changelog
* Sat Feb 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.5-4
- Upstream 1.4.5-2.

* Sun Jan 28 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.5-3
- Upstream 1.4.5-1, refresh other patches.
- Fix xineliboutput plugin name in sysconfig's VDR_PLUGIN_ORDER.
- Delay a bit in the init script's stop function for clean shutdown.
- Update CDDA_TRANSPORT workaround status in commands.conf abcde example.
- Improve /sbin/halt.local explanation in README.package.
- Minor specfile cleanups.

* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.4.5-2
- 1.4.5, Darren Salt's 1.4.4-1.ds.
- Make it possible to disable installed plugins in plugin sysconfig snippet.
- Add shutdown script, document ACPI wakeup usage in README.package.
- Shut down earlier by default for better experience with the -s option.
- Include INSTALL in docs, it contains useful post-install info.
- Improve remote control examples in udev rules snippet.
- Honor $TMPDIR when running with core dumps enabled.
- Add read only root/temporary state config.
- Add ttxtsubs to default plugin order list.
- Include log dir for plugins.

* Sat Nov  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.4-1
- 1.4.4.
- Apply epgsearch and timer info patches.
- Mark console.perms snippet noreplace again.

* Sun Oct 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.3-3
- Apply upstream 1.4.3-1 maintenance patch.
- Sync with 1.4.3-1.ds, update liemikuutio patch to 1.13.
- Drop no longer needed README.plugins.d, README.package is enough (#190343).

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 1.4.3-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.3-1
- 1.4.3, 1.4.2-1.ds, liemikuutio 1.12.

* Sun Sep  3 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.2-2
- 1.4.2-1, liemikuutio 1.10.

* Sun Aug 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.2-1
- 1.4.2, syscall and maintenance patches applied upstream.

* Mon Aug 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-11
- Set device permissions in both console.perms and udev (#202132).
- Implement restart and DVB module reload functionality roughly like
  upstream runvdr does it.

* Fri Aug 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-10
- Fix build with recent kernel headers where _syscallX are no longer visible.
- Drop ia64 patch (superseded by the above) and the thread poison patch.

* Fri Aug 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-9
- Set device permissions using console.perms instead of udev rules
  to work around new pam trumping udev config (#202132).

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-8
- Apply upstream 1.4.1-3 maintenance patch.

* Sun Jul 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-7
- Apply upstream 1.4.1-2 maintenance patch.
- Use VFAT compatible recording names by default.

* Sun Jul 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-6
- Don't use %%bcond_with to appease buildsys.

* Sat Jul 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-5
- Update liemikuutio patch to 1.8.
- Patch dumpability to work with PR_SET_DUMPABLE changes in recent kernels,
  add corresponding warning to sysconfig snippet comment.

* Sat Jul  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-4
- Update liemikuutio patch to 1.7.
- Conditionally build the skincurses and sky plugins; disabled by default,
  rebuild with "--with plugins" to enable.
- Make symlinks relative.

* Fri Jun 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-3
- Move headers to %%{_includedir}.
- Add README.package to docs, describing some aspects of the package (#1063).
- Add LIBDIR to Make.config to ease local plugin builds (#1063).
- Update VDR_PLUGIN_ORDER in sysconfig snippet, loading potential output
  plugins before others.  See commentary in the file for details.
- Add example how to affect OSD time/date formats to sysconfig snippet.

* Sun Jun 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-2
- 1.4.1-1 + 1.4.1-1.ds.
- Drop glibc-kernheaders dependency from -devel too.
- Make -devel multilib friendly, add pkgconfig file.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.1-1
- 1.4.1, liemikuutio 1.6.

* Mon May 29 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.0-5
- Address some review notes in #190343 comment 2:
- Add example udev rule for predictable remote control device naming.
- Drop glibc-kernheaders build dependency.
- Specfile cleanups.

* Sun May 28 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.0-4
- Apply upstream 1.4.0-2 maintenance patch.

* Sun May 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.0-3
- Apply upstream 1.4.0-1 maintenance patch.
- Drop unneeded version check from %%check.

* Mon May  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.0-2
- Sync with 1.4.0-1.ds.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.4.0-1
- 1.4.0 + 1.3.48-1.ds, re-enable reload patch.

* Sun Apr 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.48-1
- 1.3.48, no need to rebuild plugins, woo-hoo!

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.47-1
- 1.3.47 + the usual patchwork.
- Trim pre-RLO %%changelog entries.
- Add vdr(abi) and vdr-devel(api) versioned Provides for plugin versioning
  and --version and --apiversion to vdr-config, see HISTORY.
- Use sed instead of perl for edits during the build.
- Temporarily disable reload/SIGUSR1 patch.

* Sun Apr  9 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.46-1
- 1.3.46 + the usual patchwork.

* Sun Mar 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.45-1
- 1.3.45 + 1.3.44-2.ds + Rofa's mute fix.

* Thu Mar 09 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- switch to new release field

* Sun Mar  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.44-0.lvn.2
- Sync with 1.3.44-1.ds, apply Rolf Ahrenberg's readline fix.

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.44-0.lvn.1
- 1.3.44, include Marko Mäkelä's suspend patch.
- Move runvdr to %%{_sbindir} and make it option-compatible with the
  upstream one.  If VDR_INIT is non-empty in the environment, automatic
  command line building is enabled.  The init script still does that.
  Also makes the init script and runvdr easier to adapt to alternative
  init systems such as initng (#781).

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Feb 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.43-0.lvn.2
- Sync with 1.3.43-1.ds.

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.43-0.lvn.1
- 1.3.43 + 1.3.42-2.ds + Rolf Ahrenberg's audiotracks patch.
- Drop Reinhard Nißl's dvbplayer patch at least for now.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.42-0.lvn.1
- 1.3.42; dumpable, menu-in-replay and constness patches applied upstream.
- Make udev rules work as expected with later udev versions.

* Sun Jan 29 2006 Ville Skyttä <ville.skytta at iki.fi>
- 1.3.41; Finnish, EPG null title and LIRC reconnect patches
  applied/obsoleted upstream.
- Revert back to Udo Richter's more general purpose "menu in replay" patch.

* Sat Jan 28 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.40-0.lvn.3
- Patch LIRC support to try to reconnect if lircd connection is lost.
- Update liemikuutio patch to 1.2.

* Mon Jan 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.40-0.lvn.2
- Replace EPG null title crash fix with upstream one.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.40-0.lvn.1
- 1.3.40, key macro and SVDRP CLRE crash patches applied upstream.
- Replace menu tweak patch with one from Luca Olivetti.

* Wed Jan 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.39-0.lvn.3
- Fix sysconfig stupidity introduced in 0.lvn.2, _only_ DAEMON_COREFILE_LIMIT
  was taken into account :P

* Mon Jan 16 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.39-0.lvn.2
- Apply upstream key macro and SVDRP CLRE crash patches.
- Source sysconfig snippet again in init script (so that eg.
  DAEMON_COREFILE_LIMIT etc works as expected).

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.39-0.lvn.1
- 1.3.39 + the usual patch shuffling, kudos to Rolf Ahrenberg and Udo
  Richter.

* Wed Jan 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.38-0.lvn.4
- Apply upstream menu fix patch.
- Add some comments to sysconfig file.

* Tue Jan 10 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.38-0.lvn.3
- Sync with 1.3.38-2.ds.

* Mon Jan  9 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.38-0.lvn.2
- Sync with 1.3.38-1.ds.
- Remove references to the removed ca.conf from the manpage.

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.38-0.lvn.1
- 1.3.38, su/capabilities stuff, low disk space crash, CAN-2005-0071,
  audio pids and timed recording deletion patches applied upstream.
- Patch to allow core dumps and startup script simplifications with the
  newly introduced set[ug]id functionality.
- Patch to fix gettid usage (includes).
- enAIO patchset replaced by liemikuutio 1.0.
- Updated Finnish translations.

* Wed Jan  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.3.37-0.lvn.3
- Fix syntax error in sysconfig file (#714, Scott Tsai).
- Change built-in default of epg.data location to %%{cachedir}, drop it
  from the sysconfig file and update docs.

* Sat Dec 10 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.37-0.lvn.2
- Apply "low disk space" message crash from Andreas Brachold.
- Apply upstream fix for 2nd audio pid and live DD on encrypted channels.
- Add (commented out) sysconfig and console.perms.d samples for setting and
  retaining VDR-friendly CD/DVD drive permissions.
- Sync with 1.3.37-1.ds.

* Mon Nov 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.37-0.lvn.1
- 1.3.37.

* Sat Nov 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.36-0.lvn.2
- Default config improvements.
- Sync with 1.3.36-1.ds.

* Sun Nov  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.36-0.lvn.1
- 1.3.36, recording end crash fix applied upstream.
- Don't load LIRC unconditionally, pass --lirc by default in sysconfig/vdr.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.35-0.lvn.1
- 1.3.35 + Joachim Wilke's recording end crash fix; Finnish, daemon and
  infloop patches applied upstream.

* Sun Oct 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.34-0.lvn.2
- Update enAIO patch to 2.7.
- Apply daemon and menu infinite loop patches from Enrico Scholz.

* Fri Oct  7 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.34-0.lvn.1
- 1.3.34 + 1.3.34-1.ds + Rolf Ahrenberg's Finnish i18n fixes.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.33-0.lvn.1
- 1.3.33.
- Sync with 1.3.32-1.ds.
- Apply enAIO patch.

* Fri Sep 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.32-0.lvn.2
- Fix init script on multilib archs (#596, Jussi Lehtola).

* Sun Sep 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.32-0.lvn.1
- 1.3.32, bunch of patches applied upstream.
- Drop main package dependency from -devel.

* Sun Aug 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.31-0.lvn.1
- 1.3.31 + upstream warnings fix + Reinhard Nißl's patch bomb.
- Ship plugin creator script in -devel.

* Mon Aug 22 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.30-0.lvn.2
- Don't use stuff from the su/capabilities patch by default, it causes
  problems with getting core dumps if plugins crash.
- Simplify things by splitting stuff from init script to separate launcher.
- Sync with 1.3.30-1.ds, fix a warning in the svdrp grab patch.
- Add audio CD ripping example to commands.conf.

* Sun Aug 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.30-0.lvn.1
- 1.3.30, PPC/unaligned patch no longer needed.
- Tune default plugin load order, add muggle.
- Minor init script improvements.

* Wed Aug 17 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.29-0.lvn.2
- Sync with Darren Salt's 1.3.29-1.ds.
- Drop dvbplayer patch; no longer needed for recent recordings.
- Patch/hack (from reiserfsprogs) to fix PPC build (asm/unaligned.h).
- Start up earlier/shut down later by default at boot/shutdown.
- Add vardir for storing non-cache, non-video data; and audiodir for
  audio plugins.

* Mon Aug 15 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.29-0.lvn.1
- 1.3.29, Finnish patch applied upstream.

* Sat Aug 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.28-1.lvn.2
- Apply Rolf Ahrenberg's newest Finnish patch.
- Drop historical conflict with an old vdr-dxr3 snapshot.

* Thu Aug 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.3.28-1.lvn.1
- Truncate config files in more portable manner during build.
