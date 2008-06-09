%define pname     remote
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.3.9
Release:        1%{?dist}
Summary:        Extended remote control plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.escape-edv.de/endriss/vdr/
Source0:        http://www.escape-edv.de/endriss/vdr/%{name}-%{version}.tgz
Source1:        %{name}.conf
Patch0:         http://zap.tartarus.org/~ds/debian/dists/unstable/main/source/vdr-plugin-remote_0.3.8-2.ds.diff.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
Requires:       vdr(abi) = %{apiver}

%description
This plugin extends VDR's remote control capabilities, adding support
for Linux input devices, keyboards (tty), TCP connections, and LIRC.


%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1
patch -p1 -i debian/patches/01_debian.dpatch
patch -p1 -i debian/patches/02_no_abort.dpatch
patch -p1 -i debian/patches/03_eventX.dpatch
sed -i -e 's/0\.3\.8/0.3.9/g' debian/patches/04_constness.dpatch
patch -p1 -i debian/patches/04_constness.dpatch
sed -i -e 's|include Make.config|include $(VDRDIR)/Make.config|' Makefile
for f in CONTRIBUTORS HISTORY ; do
    iconv -f iso-8859-1 -t utf-8 $f > $f.utf-8 ; mv $f.utf-8 $f
done


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
make install LIBDIR=. VDRDIR=%{_libdir}/vdr # ugh
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CONTRIBUTORS COPYING FAQ HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog
* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.3.9-1
- 0.3.9, build for VDR 1.4.5.

* Sat Nov  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-3
- Rebuild for VDR 1.4.4.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.3.8-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.8-1
- 0.3.8, build for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.7-3
- Rebuild for VDR 1.4.1-3.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.7-2
- Rebuild for VDR 1.4.1.

* Sun May 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.7-1
- 0.3.7.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.6-4
- Sync with 0.3.6-1.ds, build for VDR 1.4.0.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.6-3
- Rebuild/adjust for VDR 1.3.47, require versioned vdr(abi).
- Trim pre-RLO %%changelog entries.

* Sun Mar 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.6-2
- Rebuild for VDR 1.3.45.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.3.6-1
- drop 0.lvn from release

* Sun Mar  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.6-0.lvn.1
- 0.3.6 + 0.3.5-1.ds.

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.5-0.lvn.5
- Rebuild for VDR 1.3.44.

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Tue Feb 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.5-0.lvn.4
- Sync with 0.3.5-2.ds.

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.5-0.lvn.3
- Sync with 0.3.5-1.ds, rebuild for VDR 1.3.43.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.5-0.lvn.2
- Rebuild for VDR 1.3.42.

* Wed Jan 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.5-0.lvn.1
- 0.3.5.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.4-0.lvn.4
- Rebuild for VDR 1.3.40.

* Sat Jan 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.4-0.lvn.3
- Fix plugin filename (#738).

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.4-0.lvn.2
- Rebuild for VDR 1.3.39.

* Mon Jan  9 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.3.4-0.lvn.1
- 0.3.4 + 1.ds.
- Rebuild for VDR 1.3.38.

* Mon Nov 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.10
- Rebuild for VDR 1.3.37.

* Sun Nov  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.9
- Rebuild for VDR 1.3.36.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.8
- Rebuild for VDR 1.3.35.

* Mon Oct  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.7
- Rebuild for VDR 1.3.34.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.6
- Rebuild for VDR 1.3.33.

* Sun Sep 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.5
- Rebuild for VDR 1.3.32.

* Sun Aug 28 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.4
- Rebuild for VDR 1.3.31.

* Sun Aug 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.3
- Rebuild for VDR 1.3.30.

* Tue Aug 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.2
- Try to avoid build system problems by not using %%expand with vdr-config.

* Sun Aug 14 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.3.3-1.lvn.1
- Improve description, convert docs to UTF-8.
