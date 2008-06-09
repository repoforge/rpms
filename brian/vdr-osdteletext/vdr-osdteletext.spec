%define pname     osdteletext
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define cachedir  %(vdr-config --cachedir   2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)
%define vdr_user  %(vdr-config --user       2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.5.1
Release:        27%{?dist}
Summary:        OSD teletext plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.wiesweg-online.de/linux/linux.html
Source0:        http://www.wiesweg-online.de/linux/vdr/%{name}-%{version}.tgz
Source1:        %{name}.conf
Patch0:         %{name}-0.5.1-i18n.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
Requires:       vdr(abi) = %{apiver}

%description
The OSD teletext plugin displays teletext directly on VDR's on-screen
display, with sound and video from the current channel playing in the
background.


%prep
%setup -q -n %{pname}-%{version}
%patch0
for f in HISTORY README.DE ; do
  iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done
sed -i -e '/^DVBDIR/d' -e 's|-I$(DVBDIR)/include||' Makefile
sed -i -e s/VDRVERSION/APIVERSION/g Makefile


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr libvdr-%{pname}.so


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT%{cachedir}/osdteletext
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d
sed -e 's|/var/cache/vdr/|%{cachedir}/|' < %{SOURCE1} \
  > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/osdteletext.conf
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/*.conf


%clean
rm -rf $RPM_BUILD_ROOT


%preun
if [ $1 -eq 0 ] ; then
  rm -rf %{cachedir}/osdteletext/*
fi


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README*
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}
%attr(-,%{vdr_user},root) %{cachedir}/osdteletext/


%changelog
* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-27
- Rebuild for VDR 1.4.5.

* Sun Nov 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-26
- First FE build.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-20
- Rebuild for VDR 1.4.0.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-19
- Rebuild/adjust for VDR 1.3.47, require versioned vdr(abi).
- Trim pre-RLO %%changelog entries.

* Sun Mar 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-18
- Rebuild for VDR 1.3.45.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.5.1-17
- drop 0.lvn from release

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.17
- Rebuild for VDR 1.3.44.

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.16
- Rebuild for VDR 1.3.43.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.15
- Rebuild for VDR 1.3.42.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.14
- Fix translations with VDR >= 1.3.38.
- Rebuild for VDR 1.3.40.

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.13
- Rebuild for VDR 1.3.39.

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.12
- Rebuild for VDR 1.3.38.

* Mon Nov 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.11
- Rebuild for VDR 1.3.37.

* Sun Nov  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.10
- Rebuild for VDR 1.3.36.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.9
- Rebuild for VDR 1.3.35.

* Mon Oct  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.8
- Rebuild for VDR 1.3.34.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.7
- Rebuild for VDR 1.3.33.

* Sun Sep 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.6
- Rebuild for VDR 1.3.32.

* Sun Aug 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.5
- Rebuild for VDR 1.3.31.

* Sun Aug 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.4
- Rebuild for VDR 1.3.30.

* Tue Aug 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.3
- Sync with re-re-released upstream 0.5.1 tarball, cache dir is now
  stabilized at %%{cachedir}/osdteletext.
- Try to avoid build system problems by not using %%expand.
- Honor "vdr-config --user".
- Improve description.

* Fri Aug 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.2
- Sync with re-released upstream 0.5.1 tarball.

* Thu Aug 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.5.1-0.lvn.1
- 0.5.1.
