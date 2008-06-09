# TODO:
# - mplayer.sh:
#   - patch to allow playing audio files (currently insists to find video)
#   - audio CD support?

%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define videodir  %(vdr-config --videodir   2>/dev/null || echo ERROR)
%define audiodir  %(vdr-config --audiodir   2>/dev/null || echo ERROR)
%define datadir   %(vdr-config --datadir    2>/dev/null || echo ERROR)
%define cachedir  %(vdr-config --cachedir   2>/dev/null || echo ERROR)
%define vardir    %(vdr-config --vardir     2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)
%define vdr_user  %(vdr-config --user       2>/dev/null || echo ERROR)

Name:           vdr-mp3
Version:        0.9.15
Release:        5%{?dist}
Summary:        Sound playback plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.muempf.de/
Source0:        http://www.muempf.de/down/%{name}-%{version}.tar.gz
Source1:        http://batleth.sapienti-sat.org/projects/VDR/versions/mplayer.sh-0.8.7.tar.gz
Source2:        %{name}-mediasources.sh
Source3:        %{name}-mp3.conf
Source4:        %{name}-mplayer.conf
Source5:        %{name}-mplayer-minimal.sh
Patch0:         %{name}-mplayer.sh-0.8.7-lircrc.patch
Patch1:         %{name}-mplayer.sh-framedrop.patch
Patch2:         %{name}-mplayer.sh-identify.patch
Patch3:         %{name}-mplayer.sh-0.8.7-defaults.patch
Patch4:         %{name}-0.9.15-lastdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.4.0
BuildRequires:  libsndfile-devel >= 1.0.0
BuildRequires:  libvorbis-devel
BuildRequires:  %{__perl}
BuildRequires:  libmad-devel
BuildRequires:  libid3tag-devel
Requires:       vdr(abi) = %{apiver}
Requires:       netpbm-progs
Requires:       mjpegtools >= 1.8.0
Requires:       file

%description
The MP3 plugin adds audio playback capability to VDR.  Supported audio
formats are those supported by libmad, libsndfile and libvorbis.

%package     -n vdr-mplayer
Summary:        MPlayer plugin for VDR
Group:          Applications/Multimedia
BuildRequires:  %{__perl}
Requires:       vdr(abi) = %{apiver}
Requires:       mplayer >= 1.0-0.lvn.0.19.pre7

%description -n vdr-mplayer
The MPlayer plugin adds the ability to call MPlayer from within VDR,
allowing to replay all video formats supported by MPlayer over VDR's
primary output device.


%prep
%setup -q -n mp3-%{version} -a 1
%patch0
%patch1
%patch2
%patch3 -p1
%patch4
%{__perl} -pi -e \
  's|CFGFIL=.*|CFGFIL="%{configdir}/plugins/mplayer.sh.conf"|' \
  mplayer.sh
%{__perl} -pi -e \
  's|"/var/cache/images/mp3"|"%{cachedir}/mp3/images"|' \
  data-mp3.c README
%{__perl} -pi -e \
  's|"/video/plugins/DVD-VCD"|"%{datadir}/DVD-VCD"| ;
   s|^MPLAYER=.*|MPLAYER="mplayer"|' \
  mplayer.sh.conf
for f in HISTORY MANUAL README ; do
  iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done
sed -e 's|/var/lib/vdr|%{vardir}|' %{SOURCE4} > %{name}-mplayer.conf


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr WITH_OSS_OUTPUT=1 all
echo "%{audiodir};Local hard drive;0" > mp3sources.conf
echo "%{datadir}/DVD-VCD;DVD or VCD;0" > mplayersources.conf


%install
rm -rf $RPM_BUILD_ROOT

# Common dirs
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT%{configdir}/plugins
install -dm 755 $RPM_BUILD_ROOT%{plugindir}/bin
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d

# Common files
install -pm 755 %{SOURCE2} $RPM_BUILD_ROOT%{plugindir}/bin/mediasources.sh
install -pm 755 examples/mount.sh.example \
  $RPM_BUILD_ROOT%{plugindir}/bin/mount.sh

# MP3 files
install -pm 755 libvdr-mp3.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -pm 644 mp3sources.conf $RPM_BUILD_ROOT%{configdir}/plugins
install -pm 755 examples/image_convert.sh.example \
  $RPM_BUILD_ROOT%{plugindir}/bin/image_convert.sh
%{__perl} -pe 's|/var/cache/vdr/|%{cachedir}/|' %{SOURCE3} \
  > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/mp3.conf
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/mp3.conf
install -dm 755 $RPM_BUILD_ROOT%{cachedir}/mp3/images
i=$RPM_BUILD_ROOT%{cachedir}/mp3/id3info.cache ; > $i ; chmod 644 $i

# MPlayer files
install -pm 755 libvdr-mplayer.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT%{datadir}/DVD-VCD
touch $RPM_BUILD_ROOT%{datadir}/DVD-VCD/{DVD,VCD}
chmod 644 $RPM_BUILD_ROOT%{datadir}/DVD-VCD/*
install -pm 644 mplayersources.conf mplayer.sh.conf \
  $RPM_BUILD_ROOT%{configdir}/plugins
install -pm 755 mplayer.sh $RPM_BUILD_ROOT%{plugindir}/bin/mplayer.sh
install -pm 755 %{SOURCE5} $RPM_BUILD_ROOT%{plugindir}/bin/mplayer-minimal.sh
install -pm 644 %{name}-mplayer.conf \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/mplayer.conf
install -dm 755 $RPM_BUILD_ROOT%{vardir}
i=$RPM_BUILD_ROOT%{vardir}/global.mplayer.resume ; > $i ; chmod 644 $i


%clean
rm -rf $RPM_BUILD_ROOT


%post
if [ $1 -eq 1 ] ; then
  %{plugindir}/bin/mediasources.sh \
    >> %{configdir}/plugins/mp3sources.conf || :
else
  if ! grep %{audiodir} %{configdir}/plugins/mp3sources.conf &>/dev/null ; then
    echo "%{audiodir}" >> %{configdir}/plugins/mp3sources.conf || :
  fi
  r=global.mplayer.resume
  if [ -f %{videodir}/$r -a ! -f %{vardir}/$r ] ; then
    mv %{videodir}/$r %{vardir}/$r
  fi
fi

%post -n vdr-mplayer
if [ $1 -eq 1 ] ; then
  %{plugindir}/bin/mediasources.sh \
    >> %{configdir}/plugins/mplayersources.conf || :
fi


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY MANUAL README examples/mount.sh.example
%doc examples/mp3sources.conf.example examples/network.sh.example
%config(noreplace) %{configdir}/plugins/mp3sources.conf
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/mp3.conf
%{plugindir}/libvdr-mp3.so.%{apiver}
%{plugindir}/bin/image_convert.sh
%{plugindir}/bin/mediasources.sh
%{plugindir}/bin/mount.sh
%defattr(-,%{vdr_user},root,-)
%dir %{cachedir}/mp3/
%dir %{cachedir}/mp3/images/
%ghost %{cachedir}/mp3/id3info.cache

%files -n vdr-mplayer
%defattr(-,root,root,-)
%doc COPYING HISTORY MANUAL README examples/mplayer.sh.example
%doc examples/mount.sh.example
%config(noreplace) %{configdir}/plugins/mplayer*.conf
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/mplayer.conf
%{plugindir}/libvdr-mplayer.so.%{apiver}
%{plugindir}/bin/mediasources.sh
%{plugindir}/bin/mount.sh
%{plugindir}/bin/mplayer*.sh
%{datadir}/DVD-VCD/
%defattr(-,%{vdr_user},root,-)
%ghost %{vardir}/global.mplayer.resume


%changelog
* Sun Feb 25 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-5
- Apply upstream patch to check availability of last dir before accessing it.
- Update mplayer.sh to 0.8.7.

* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-4
- Rebuild for VDR 1.4.5.

* Sat Nov  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-3
- Rebuild for VDR 1.4.4.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.9.15-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-1
- 0.9.15, build for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.6.pre14
- Rebuild for VDR 1.4.1-3.

* Sun Jul 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.5.pre14
- 0.9.15pre14 + Rolf Ahrenberg's Finnish patch.
- Plugin C(XX)FLAGS and zlib patches applied upstream.
- Re-enable MP3 plugin; it supposedly works just fine in most setups
  (still not in my vdr-dxr3 one though).

* Mon Jul 24 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.5.pre10
- Patch to get plugin C(XX)FLAGS properly applied from Make.config.

* Sun Jul 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.4.pre10
- Include accidentally dropped mplayer.sh.conf.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.3.pre10
- Rebuild for VDR 1.4.1.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.2.pre10
- 0.9.15pre10, build for VDR 1.4.0.
- Move -mplayer global resume file to /var/lib/vdr.

* Sun Apr 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.2.pre6
- Require versioned vdr(abi) also in -mplayer.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.15-0.1.pre6
- 0.9.15pre6, i18n fix applied upstream.
- Rebuild/adjust for VDR 1.3.47, require versioned vdr(abi).
- Trim pre-RLO %%changelog entries.

* Sun Mar 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-8
- Rebuild for VDR 1.3.45.
- Disable mp3 plugin, it doesn't work properly with NPTL (#844).

* Sat Mar 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-7
- Get rid of superfluous direct dependency on zlib (#813).

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.9.14-6
- drop 0.lvn from release

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.lvn.6
- Rebuild for VDR 1.3.44.

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.lvn.5
- Rebuild for VDR 1.3.43.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.lvn.4
- Rebuild for VDR 1.3.42.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.lvn.3
- Fix button translations with VDR >= 1.3.38.
- Add mplayer-minimal.sh, an alternative MPlayer launcher script.
- Rebuild for VDR 1.3.40.

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.lvn.2
- Rebuild for VDR 1.3.39.

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.14-0.lvn.1
- 0.9.14.
- Patch to fix build with gcc 4.1.
- Rebuild for VDR 1.3.38.

* Mon Nov 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.10
- Rebuild for VDR 1.3.37.

* Sun Nov  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.9
- Rebuild for VDR 1.3.36.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.8
- Rebuild for VDR 1.3.35.

* Mon Oct  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.7
- Rebuild for VDR 1.3.34.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.6
- Rebuild for VDR 1.3.33.

* Sun Sep 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.5
- Rebuild for VDR 1.3.32.

* Sun Aug 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.4
- Rebuild for VDR 1.3.31.

* Sun Aug 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.3
- Rebuild for VDR 1.3.30.
- Add audiodir to mp3sources.conf.

* Tue Aug 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.2
- Try to avoid build system problems by not using %%expand with vdr-config.

* Sat Aug 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.13-1.lvn.1
- Improve descriptions, convert docs to UTF-8.
