# $Id$
# Authority: matthias

%define gkplugindir	%{_libdir}/gkrellm2/plugins

%define weatherver	2.0.6
%define xmmsver		2.1.20
%define setiver		0.7.0b
%define dnetver		0.12.1
%define volumever	2.1.13
%define mailwatchver	2.4.2
%define snmpver		0.21
%define radiover	2.0.4
%define wirelessver	2.0.3
%define aclockver	0.3.2
%define kamver		2.0.0
%define reminderver	2.0.0
%define moonver		0.6
%define multipingver	2.0.2
%define whover		0.5
%define x86ver		0.0.2
%define ssver		2.6
%define shootver	0.4.2
%define flynnver	0.8
%define	ledsver		0.8.1
%define bgchgver        0.1.2
%define trayver         1.02
%define cpufreqver      0.5.2
%define alltraxver      0.2
%define hdplopver       0.9.6

Summary: Some neat plugins for GKrellM
Name: gkrellm-plugins
Version: 2.2.4
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://web.wt.net/~billw/gkrellm/Plugins.html
Source0: http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/gkrellweather-%{weatherver}.tgz
Source1: http://gkrellm.luon.net/files/gkrellmms-%{xmmsver}.tar.gz
Source2: http://xavier.serpaggi.free.fr/seti/seti-%{setiver}.tar.bz2
Source3: http://download.sf.net/gkrelldnet/gkrelldnet-%{dnetver}.tar.gz
Source4: http://gkrellm.luon.net/files/gkrellm-volume-%{volumever}.tar.gz
Source5: http://gkrellm.luon.net/files/gkrellm-mailwatch-%{mailwatchver}.tar.gz
Source6: http://triq.net/gkrellm/gkrellm_snmp-%{snmpver}.tar.gz
Source7: http://gkrellm.luon.net/files/gkrellm-radio-%{radiover}.tar.gz
Source8: http://gkrellm.luon.net/files/gkrellmwireless-%{wirelessver}.tar.gz
Source9: http://www.geocities.com/m_muthukumar/gkrellaclock-%{aclockver}.tar.gz
Source10: http://download.sf.net/gkrellkam/gkrellkam_%{kamver}.tar.gz
Source11: http://web.wt.net/~billw/gkrellm/Plugins/gkrellm-reminder-%{reminderver}.tar.gz
Source12: http://download.sf.net/gkrellmoon/gkrellmoon-%{moonver}.tar.gz
#Source13:
Source14: http://kmlinux.fjfi.cvut.cz/~makovick/gkrellm/gkrellm-multiping-%{multipingver}.tgz
#Source15: http://sperion.vuse.vanderbilt.edu/kirk/gkrellmwho2.tgz
Source16: http://anchois.free.fr/gkx86info2-%{x86ver}.tar.gz
Source17: http://web.wt.net/~billw/gkrellmss/gkrellmss-%{ssver}.tar.gz
Source18: http://download.sf.net/gkrellshoot/gkrellshoot-%{shootver}.tar.gz
Source19: http://horus.comlab.uni-rostock.de/flynn/gkrellflynn-%{flynnver}.tar.gz
Source20: http://heim.ifi.uio.no/~oyvinha/gkleds/gkleds-%{ledsver}.tar.gz
Source21: http://www.bender-suhl.de/stefan/comp/sources/gkrellmbgchg2-%{bgchgver}.tar.gz
Source22: http://sweb.cz/tripie/gkrellm/trayicons/dist/gkrellm-trayicons-%{trayver}.tar.gz
Source23: http://iacs.epfl.ch/~winkelma/gkrellm2-cpufreq/gkrellm2-cpufreq-%{cpufreqver}.tar.gz
Source24: http://invalid.url/alltraxclock2_%{alltraxver}-1.tar.gz
Source25: http://hules.free.fr/wmhdplop/wmhdplop-%{hdplopver}.tar.gz
Patch0: http://xavier.serpaggi.free.fr/seti/seti-0.7.0b-gkrellm2.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gkrellm-devel >= 2.1.0, gtk2-devel, perl

%description
This is a "previously small but now bigger and bigger" ;-)  collection of
plugins for GKrellM, the GNU Krell Monitor.


%package media
Summary: Multimedia plugins for GKrellM
Group: Applications/System
Requires: gkrellm >= 2.1.0, xmms, esound, fftw
# gkrellmms
BuildRequires: gtk+-devel, xmms-devel
BuildRequires: esound-devel, fftw-devel
# gkrellmss
BuildRequires: gettext

%description media
This package contains the following multimedia plugins for GKrellM, the GNU
Krell Monitor : xmms, volume, radio and esd meter.


%package misc
Summary: Amusement and miscellaneous plugins for GKrellM
Group: Applications/System
Requires: gkrellm >= 2.1.0
Requires: perl(LWP::UserAgent)
# wmhdplop
BuildRequires: imlib2-devel

%description misc
This package contains the following amusements plugins for GKrellM, the GNU
Krell Monitor : Seti@HOME, distributed.net, weather, moon clock, analog clock,
gkrellkam, Flynn and background change.


%package utils
Summary: System and network utility plugins for GKrellM
Group: Applications/System
Requires: gkrellm >= 2.1.0, ImageMagick

%description utils
This package contains the following utility plugins for GKrellM, the GNU
Krell Monitor : ACPI monitor, mail watch, wireless network monitor, multi
ping utility, x86 cpu speed, screenshot/lock and reminder.

For the cpufreq plugin, you might want to use visudo and add the following :
<your user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqset [0-9]*
<your user> ALL = (root) NOPASSWD: /usr/sbin/cpufreqsetgovernor [a-z]


%package snmp
Summary: SNMP monitoring plugin for GKrellM.
Group: Applications/System
Requires: gkrellm >= 2.1.0, net-snmp
BuildRequires: net-snmp-devel

%description snmp
This is a snmp monitoring plugin for GKrellM, the GNU Krell Monitor.


%prep
%setup -T -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8 -a9 -a10 -a11 -a12 -a14 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -c %{name}-%{version}
# -a13 -a15
%patch0 -p0
# Fix for multiping
%{__perl} -pi.orig -e \
    's|/usr/local/lib/gkrellm2/plugins|%{_libdir}/gkrellm2/plugins|g' \
    gkrellm-multiping-%{multipingver}/multiping.c


%build
%{__mkdir} plugins/ bin/ sbin/ man5/
# Nearly no configure macro here, hence manual exports...
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
( cd gkrellweather-%{weatherver} ; make PREFIX=%{_prefix} ; mv *.so ../plugins// ; cp GrabWeather ../bin/ )
# gkrellmms contains locales, skipping them for now.
( cd gkrellmms ; make ; mv *.so ../plugins/ )
( cd seti-%{setiver} ; make ; mv *.so ../plugins/ )
( cd gkrelldnet-%{dnetver} ; make ; mv *.so ../plugins/ ; cp dnetw ../bin/ )
# volume plugin contains locales, skipping them for now.
( cd gkrellm-volume ; make ; mv *.so ../plugins/ )
( cd gkrellm-mailwatch ; make ; mv *.so ../plugins/ )
# cd gkrellm_snmp-%{snmpver} ; make ; mv *.so ../plugins/ )
# radio has locales as well...
( cd gkrellm-radio ; make ; mv *.so ../plugins/ )
( cd gkrellmwireless ; make ; mv *.so ../plugins/ )
( cd gkrellAclock-%{aclockver} ; make ; mv *.so ../plugins/ )
( cd gkrellkam-%{kamver} ; make ; mv *.so ../plugins/ ; mv *.5 ../man5/ )
( cd gkrellm-reminder-%{reminderver} ; make ; mv *.so ../plugins/ )
( cd gkrellmoon-%{moonver} ; make ; mv *.so ../plugins/ )
( cd gkrellm-multiping-%{multipingver} ; make ; mv *.so ../plugins/ ; cp pinger ../plugins/ )
#( cd gkrellmwho2 ; make ; mv *.so ../plugins/ )
( cd gkrellmss-%{ssver} ; make ; mv src/*.so ../plugins/ )
( cd gkrellShoot-%{shootver} ; make ; mv *.so ../plugins/ )
( cd gkrellflynn-%{flynnver} ; make gkrellm2 ; mv *.so ../plugins/ )
( cd gkleds-%{ledsver} ; make ; mv *.so ../plugins/ )
( cd gkrellmbgchg2-%{bgchgver} ; make ; mv *.so ../plugins/ )
( cd gkrellm-trayicons-%{trayver} ; make ; mv *.so ../plugins/ )
( cd gkrellm2-cpufreq-%{cpufreqver} ; make ; mv *.so ../plugins/ ; cp cpufreqset cpufreqsetgovernor ../sbin/ )
( cd alltraxclock2_%{alltraxver} ; make ; mv *.so ../plugins/ )
( cd wmhdplop-%{hdplopver} ; ./configure && make ; mv gkhdplop.so ../plugins/ )
%ifarch %ix86
( cd gkx86info%{x86ver} ; ./build ; mv *.so ../plugins/ )
%endif


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{gkplugindir}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_sbindir}
%{__install} -m 0755 plugins/* %{buildroot}%{gkplugindir}/
%{__install} -m 0755 bin/*     %{buildroot}%{_bindir}/
%{__install} -m 0755 sbin/*    %{buildroot}%{_sbindir}/
# Man pages
%{__mkdir_p} %{buildroot}%{_mandir}/man5
%{__install} -m 644 `find . -type f -name "*.5"` %{buildroot}%{_mandir}/man5/


%clean
%{__rm} -rf %{buildroot}


%files media
%defattr(-, root, root, 0755)
%{gkplugindir}/gkrellmms.so
%{gkplugindir}/volume.so
%{gkplugindir}/radio.so
%{gkplugindir}/gkrellmss.so

%files misc
%defattr(-, root, root, 0755)
%{gkplugindir}/seti.so
# Code needs cleanup to compile on non x86
%ifarch %{ix86}
%{gkplugindir}/gkrelldnet.so
%{_bindir}/dnetw
%endif
%{gkplugindir}/gkrellmoon.so
%{gkplugindir}/gkrellaclock.so
%{gkplugindir}/gkrellweather.so
%{_bindir}/GrabWeather
%{gkplugindir}/gkrellkam2.so
%{_mandir}/man5/gkrellkam*
%{gkplugindir}/gkrellflynn.so
%{gkplugindir}/gkrellmbgchg.so
%{gkplugindir}/trayicons.so
%{gkplugindir}/alltraxclock.so
%{gkplugindir}/gkhdplop.so

%files utils
%defattr(-, root, root, 0755)
%{_sbindir}/cpufreqset
%{_sbindir}/cpufreqsetgovernor
%{gkplugindir}/mailwatch.so
%{gkplugindir}/wireless.so
%{gkplugindir}/reminder.so
%{gkplugindir}/multiping.so
%{gkplugindir}/pinger
%{gkplugindir}/gkrellshoot.so
# Code needs cleanup to compile on non x86
%ifarch %{ix86}
%{gkplugindir}/gkleds.so
%endif
%{gkplugindir}/cpufreq.so
%ifarch %ix86
%{gkplugindir}/gkx86info.so
%endif

#%files snmp
#%defattr(-, root, root, 0755)
#%{gkplugindir}/gkrellm_snmp.so


%changelog
* Tue Mar  1 2005 Matthias Saou <http://freshrpms.net/> 2.2.4-1
- Fix build dep to imlib2-devel for hdplop.
- Disable non building dnetc and leds for non-x86. Later fixing required.

* Thu Nov  4 2004 Matthias Saou <http://freshrpms.net/> 2.2.4-1
- Updated shoot, cpufreq and volume plugins.
- Updated file name for gk86info2.
- Known gkrellm2 alltraxclock web page seems gone :-(
- Added hdplop.
- Fixed gkrellweather and multiping paths, thanks to Kevin Otte for reporting.

* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 2.2.0-1
- Updated plugins and added tray icon and cpufreq plugins.

* Wed Feb  4 2004 Matthias Saou <http://freshrpms.net/> 2.1.12-4
- Updated all plugins from luon.net (xmms, volume, wireless, radio).
- Removed obsolete gkacpi plugin, gkrellm handles temp and battery on its own.

* Sun Nov 23 2003 Matthias Saou <http://freshrpms.net/> 2.1.12-3
- Updated gkacpi to 0.5 + patch from Ronny Buchmann.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 2.1.12-2
- Rebuild for Fedora Core 1.
- Updated volume plugin.

* Thu Jun 19 2003 Matthias Saou <http://freshrpms.net/>
- Updates xmms (2.1.12), mailwatch (2.4.2) and volume (2.1.8).

* Mon Jun 16 2003 Matthias Saou <http://freshrpms.net/>
- Updates xmms (2.1.11), mailwatch (2.4.1), weather (2.0.6), gkacpi2 (0.4).
- Added bgchg2 (0.0.5).
- Readded snmp (0.19-pre4), but still disabled (problems with net-snmp).
- Removed all obsolete plugins.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Update mailwatch (2.3.1), gkrellmms (2.1.9).

* Tue Mar 11 2003 Matthias Saou <http://freshrpms.net/>
- Exclude gkx86info on non-x86 platforms.

* Wed Jan 29 2003 Matthias Saou <http://freshrpms.net/>
- Added gkleds 0.8.1.

* Sun Jan 26 2003 Ville Skyttä <ville.skytta at iki.fi> - 2:2.1.6-fr1
- Updated multiping (2.0.2), gkrellmms (2.1.7), volume (2.1.7),
  mailwatch (2.2.2), radio (2.0.3) and gkrelldnet (0.12.1).
- Rebuilt with GKrellm 2.1.6.

* Sun Jan  5 2003 Ville Skyttä <ville.skytta at iki.fi> - 2:2.1.4-fr1
- Updated gkrellmoon (0.6), gkrellweather (2.0.5), gkrellm-radio (2.0.2),
  gkrellmms (2.1.6), mailwatch (2.1), wireless (2.0.2) and gkrelldnet (0.12).
- Re-added gkrellm-reminder (2.0.0).
- Rebuilt with GKrellM 2.1.4.

* Thu Nov 28 2002 Matthias Saou <http://freshrpms.net/>
- Updated gkrellmms to 2.1.5.

* Wed Nov 20 2002 Ville Skyttä <ville.skytta at iki.fi> - 2:2.1.0-fr5
- Updated gkrellweather, gkrellmms, gkrellmwireless and volume plugins.

* Tue Oct 29 2002 Matthias Saou <http://freshrpms.net/>
- Added gkrellm2 versions of gkrellmkam, gkx86 and gkrellmoon.

* Mon Oct 21 2002 Matthias Saou <http://freshrpms.net/>
- Re-added gkrellmss, I missed that one!
- Replaced gkrellmPing by multiping (deactivated, bad binary search path!).
- Added Flynn ;-)

* Sat Oct 19 2002 Ville Skyttä <ville.skytta at iki.fi> 2:2.1.0-fr2
- Re-added GkrellWeather.

* Fri Oct 11 2002 Ville Skyttä <ville.skytta at iki.fi> 2:2.1.0-fr1
- Re-added GkACPI.
- Rebuild with GKrellM 2.1.0.

* Wed Oct  9 2002 Ville Skyttä <ville.skytta at iki.fi> 2:2.0.4-fr2
- Re-added SETI@Home, built with patch from the author homepage.

* Sun Oct  6 2002 Ville Skyttä <ville.skytta at iki.fi> 2:2.0.4-fr1
- Rebuild with Red Hat 8.0 and GKrellM 2.0.4.
- Update aclock, gkrelldnet, gkrellmms, volume, mailwatch, wireless, radio
  and gkrellshoot.
- Remove acpi, gkrinn, gamma, ping, mouse, snmp, gkrellmss, earth_anim,
  logwatch, seti, who, gnome, consolewatch, moon clock, newsticker, gkrellkam,
  reminder, x86info, taskman and weather for now (they don't build with 2.0
  or have missing requirements).

* Wed Jul 31 2002 Ville Skyttä <ville.skytta at iki.fi> 2:1.2.13-fr1
- Updated gkacpi, gkrelldnet, gkrellshoot, gkrellm-radio, gkrellmms and
  consolewatch.
- Added gamma.
- Removed gkrellmms patch, no longer needed.
- Fixed incorrect note about gkrellmss in changelog of 1.2.11-fr1.
- Use $RPM_OPT_FLAGS when compiling.
- BuildRequires gtk+-devel and db1-devel.
- Rebuilt with GKrellM 1.2.13.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 7.3.

* Tue Apr  2 2002 Ville Skyttä <ville.skytta at iki.fi> 1.2.11-fr1
- Added Gk-Taskman and GKrellShoot.
- Added a patch for gkrellmms to make it compile with 1.2.11.
- Updated aclock, gkrellkam, gkrellm-newsticker, radio, reminder and seti.
- Didn't update gkrellmss because 0.4 would require fftw, which we don't have.
- Rebuilt with GKrellM 1.2.11.

* Tue Jan  8 2002 Ville Skyttä <ville.skytta at iki.fi>
- Updated seven plugins : seti, gkrelldnet, mailwatch, gkrellm-radio,
  gkrellkam, gkrellm-newsticker and reminder.
- GKrellKam now actually belongs to a package (misc) :)
- Added missing requirements for gnome, newsticker and snmp.
- Rebuilt with GKrellM 1.2.8

* Fri Oct 12 2001 Matthias Saou <http://freshrpms.net/>
- Updated at last! So many plugins were added that I've decided to now
  package into categories and not as individual RPMs any more.
- New packages include : earth_anim, gkrellAclock, gkrellkam, newsticker,
  reminder, gkrellmoon, gkrinn, glogwatch, gkacpi, gkrellmouse,
  gkrellmPing, gkrellmwho, x86info, gkrellmss, gkrellm-gnome, consolewatch.
- FIXME : Need to add the Gnome applet :-)

* Fri Apr 20 2001 Matthias Saou <http://freshrpms.net/>
- Updated five plugins : weather, dnet, mailwatch, snmp and radio.
- Rebuilt for Red Hat 7.1.

* Thu Feb 15 2001 Matthias Saou <http://freshrpms.net/>
- Updated three plugins : dnetc, seti and snmp.
- Added two plugins : radio and wireless.

* Tue Jan 30 2001 Matthias Saou <http://freshrpms.net/>
- Split all the plugins in individual packages.

* Mon Jan 29 2001 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

