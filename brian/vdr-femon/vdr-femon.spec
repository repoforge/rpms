%define pname     femon
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        1.1.0
Release:        5%{?dist}
Summary:        DVB frontend status monitor plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.saunalahti.fi/~rahrenbe/vdr/femon/
Source0:        http://www.saunalahti.fi/~rahrenbe/vdr/femon/files/%{name}-%{version}.tgz
Source1:        %{name}.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.4.0
BuildRequires:  sed >= 3.95
Requires:       vdr(abi) = %{apiver}

%description
DVB frontend status monitor is a plugin that displays some signal
information parameters of the current tuned channel on VDR's OSD.  You
can zap through all your channels and the plugin should be monitoring
always the right frontend.  The transponder and stream information are
also available in advanced display modes.


%prep
%setup -q -n %{pname}-%{version}
f=HISTORY ; iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f


%build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr STRIP=/bin/true


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{plugindir}/libvdr-%{pname}.so.%{apiver}


%changelog
* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-5
- Rebuild for VDR 1.4.5.

* Mon Dec  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-4
- First Fedora Extras build.

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-1
- 1.1.0, build for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.1-2
- Rebuild for VDR 1.4.1-3.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.1-1
- 1.0.1, build for VDR 1.4.1.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.0.0-1
- 1.0.0, build for VDR 1.4.0.

* Sun Apr 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.9-1
- 0.9.9.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.8-3
- Rebuild/adjust for VDR 1.3.47, require versioned vdr(abi).
- Trim pre-RLO %%changelog entries.

* Sun Mar 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.8-2
- Rebuild for VDR 1.3.45.

* Wed Mar  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.8-1
- 0.9.8.

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.7-0.lvn.2
- Rebuild for VDR 1.3.44.

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.7-0.lvn.1
- 0.9.7, built for VDR 1.3.43.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.6-0.lvn.3
- Rebuild for VDR 1.3.42.

* Thu Jan 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.6-0.lvn.2
- Grr.  Upstream re-released 0.9.6 with minor additional fixes.

* Wed Jan 25 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.6-0.lvn.1
- 0.9.6.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.5-0.lvn.4
- Rebuild for VDR 1.3.40.

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.5-0.lvn.3
- Rebuild for VDR 1.3.39.

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.9.5-0.lvn.2
- Rebuild for VDR 1.3.38.

* Sun Nov 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.5-0.lvn.1
- 0.9.5.

* Sun Nov  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.4-0.lvn.3
- Rebuild for VDR 1.3.36.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.4-0.lvn.2
- Rebuild for VDR 1.3.35.

* Thu Oct  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.4-0.lvn.1
- 0.9.4.
- Rebuild for VDR 1.3.34.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.3-0.lvn.3
- Rebuild for VDR 1.3.33.

* Sun Sep 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.3-0.lvn.2
- Rebuild for VDR 1.3.32.

* Mon Aug 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.3-0.lvn.1
- 0.9.3.
- Rebuild for VDR 1.3.31.

* Sun Aug 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.2-0.lvn.2
- Rebuild for VDR 1.3.30.

* Tue Aug 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.2-0.lvn.1
- 0.9.2.
- Try to avoid build system problems by not using %%expand with vdr-config.

* Sat Aug 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.9.1-1.lvn.1
- Improve description.
