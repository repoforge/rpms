%define pname     subtitles
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.5.0
Release:        1%{?dist}
Summary:        DVB subtitles plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://virtanen.org/vdr/subtitles/
Source0:        http://virtanen.org/vdr/subtitles/files/%{name}-%{version}.tgz
Source1:        %{name}.conf
Patch0:         http://zap.tartarus.org/~ds/debian/dists/unstable/main/source/vdr-plugin-subtitles_0.4.0-1.ds.diff.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.48
Requires:       vdr(abi) = %{apiver}

%description
There are two subtitling services specified in the DVB standards.  One
is the teletext subtitles and the other one is DVB subtitles.  The
main difference between these two is that the teletext subtitles are
text (sent via teletext service) and DVB subtitles are pixel-based
graphics.  This plugin implements a DVB subtitles decoder for VDR.
The plugin decodes and displays the subtitles and also adds the
selected subtitling streams to the VDR recordings.


%prep
%setup -q -n %{pname}-%{version}
find . -type d -name CVS | xargs rm -r
chmod -c 644 *
%patch0 -p1
#{__patch} -i debian/patches/02_enable_selection.dpatch
sed -i -e 's/"0.4.0"/"0.5.0"/' debian/patches/03_constness.dpatch
%{__patch} -i debian/patches/03_constness.dpatch
%{__patch} -i debian/patches/99_transparency_percentage.dpatch
sed -i -e '/^DVBDIR/d' -e 's|-I$(DVBDIR)/include||' Makefile


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
install -dm 755 $RPM_BUILD_ROOT%{configdir}/plugins
touch $RPM_BUILD_ROOT%{configdir}/plugins/subchannels.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}
%ghost %{configdir}/plugins/subchannels.conf


%changelog
* Sun Jan 28 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.5.0-1
- 0.5.0.

* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-7
- Rebuild for VDR 1.4.5.

* Sun Nov 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-6
- First FE build.
- Update Darren's patchkit to 0.4.0-1.ds.

* Sat May  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.4.0-1
- 0.4.0.

* Mon May  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.11-2
- Sync with 0.3.11-1.ds, enable transparency percentage patch.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.11-1
- 0.3.11 + 0.3.10-5.ds, build for VDR 1.4.0.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-8
- Rebuild/adjust for VDR 1.3.47, require versioned vdr(abi).
- Trim pre-RLO %%changelog entries.

* Sun Mar 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-7
- Rebuild for VDR 1.3.45.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.3.10-6
- drop 0.lvn from release

* Sun Mar  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-0.lvn.6
- Sync with 0.3.10-3.ds.

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-0.lvn.5
- Rebuild for VDR 1.3.44.

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Feb 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-0.lvn.4
- Sync with 0.3.10-2.ds.

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-0.lvn.3
- Sync with 0.3.10-1.ds, rebuild for VDR 1.3.43.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-0.lvn.2
- Rebuild for VDR 1.3.42.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.10-0.lvn.1
- 0.3.10.
- Rebuild for VDR 1.3.40.

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.13
- Rebuild for VDR 1.3.39.

* Tue Jan 10 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.12
- More fixes for VDR 1.3.38 from Rolf Ahrenberg.

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.11
- Rebuild/patch for VDR 1.3.38.

* Mon Nov 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.10
- Rebuild for VDR 1.3.37.

* Sun Nov  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.9
- Rebuild for VDR 1.3.36.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.8
- Rebuild for VDR 1.3.35.

* Mon Oct  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.7
- Rebuild for VDR 1.3.34.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.6
- Rebuild for VDR 1.3.33.

* Sun Sep 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.5
- Rebuild for VDR 1.3.32.

* Sun Aug 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.4
- Rebuild for VDR 1.3.31.

* Sun Aug 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.3
- Rebuild for VDR 1.3.30.

* Tue Aug 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.2
- Try to avoid build system problems by not using %%expand with vdr-config.

* Sat Aug 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1.lvn.1
- Convert docs to UTF-8.
