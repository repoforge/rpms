# TODO: noSignal.pes would be better placed in datadir somewhere

%define pname     xine
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.7.9
Release:        6%{?dist}
Summary:        Xine playback plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://home.vr-web.de/~rnissl/
Source0:        http://home.vr-web.de/~rnissl/%{name}-%{version}.tgz
Source1:        %{name}.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
BuildRequires:  xine-lib-devel >= 1.0.0
Requires:       vdr(abi) = %{apiver}

%description
This package provides a "software only" playback plugin for VDR, using
Xine as the backend.


%prep
%setup -q -n %{pname}-%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 data/noSignal.mpg \
  $RPM_BUILD_ROOT%{configdir}/plugins/xine/noSignal.mpg
install -Dpm 755 xineplayer $RPM_BUILD_ROOT%{plugindir}/bin/xineplayer
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc HISTORY MANUAL README data/noSignal-completelyBlack.mpg
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%config(noreplace) %{configdir}/plugins/xine/
%{plugindir}/bin/xineplayer
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog
* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.7.9-6
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.9-5
- Pass -r by default to the plugin to enable remote control from xine.
- Rebuild for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.9-4
- Rebuild for VDR 1.4.1-3.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.9-3
- Rebuild for VDR 1.4.1.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.9-2
- Rebuild for VDR 1.4.0.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.9-1
- 0.7.9, adjust for VDR 1.3.47, require versioned vdr(abi).
- Trim pre-RLO %%changelog entries.

* Mon Mar 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.8-1
- 0.7.8, rebuild for VDR 1.3.45.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.7.6-7
- drop 0.lvn from release

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.6-1.lvn.7
- Rebuild/patch for VDR 1.3.44.

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.6-1.lvn.6
- Rebuild for VDR 1.3.43.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.6-1.lvn.5
- Rebuild/patch for VDR 1.3.42.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.6-1.lvn.4
- Rebuild for VDR 1.3.40.

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.6-1.lvn.3
- Rebuild for VDR 1.3.39.

* Thu Jan 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.6-1.lvn.2
- Rebuild for VDR 1.3.38.
- Sync with 0.7.6-6.ds.

* Mon Jan  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.7.6-1.lvn.1
- First livna release.
- Sync with 0.7.6-4.ds.
