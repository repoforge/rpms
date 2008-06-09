# TODO: should be proxy friendlier by using relative URLs!

%define pname     wapd
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)
%define vdr_user  %(vdr-config --user       2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.8
Release:        16%{?dist}
Summary:        WAP remote control interface for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://vdr.heiligenmann.de/vdr/plugins/wapd.html
Source0:        http://vdr.heiligenmann.de/download/%{name}-%{version}.tgz
Source1:        %{name}-waphosts
Source2:        %{name}-wapaccess
Source3:        %{name}-proxy.conf
Source4:        %{name}.conf
Patch0:         %{name}-0.8-1338i18n.patch
Patch1:         %{name}-0.8-1341.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
Requires:       vdr(abi) = %{apiver}

%description
The wapd plugin enables VDR to be remotely controlled using a WML interface
with WML enabled browsers such as mainstream mobile phones.


%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1
%patch1
iconv -f iso-8859-1 -t utf-8 HISTORY > HISTORY.utf8 ; mv HISTORY.utf8 HISTORY
sed -i -e 's|/video/plugins|%{configdir}/plugins|' README
sed -i -e '/^DVBDIR/d' -e 's|-I$(DVBDIR)/include||' Makefile
sed -i -e s/VDRVERSION/APIVERSION/g Makefile
install -pm 644 %{SOURCE3} %{name}-httpd.conf
 

%build
# LIBDIR is where the compiled object is copied during build
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -pm 755 libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -Dpm 755 wappasswd $RPM_BUILD_ROOT%{_bindir}/wappasswd
install -Dpm 640 %{SOURCE1} $RPM_BUILD_ROOT%{configdir}/plugins/waphosts
install -Dpm 640 %{SOURCE2} $RPM_BUILD_ROOT%{configdir}/plugins/wapaccess
install -Dpm 644 %{SOURCE4} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README %{name}-httpd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%{_bindir}/wappasswd
%{plugindir}/libvdr-%{pname}.so.%{apiver}
%defattr(-,%{vdr_user},root,-)
%config(noreplace) %{configdir}/plugins/wapaccess
%config(noreplace) %{configdir}/plugins/waphosts


%changelog
* Sat Mar 24 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.8-16
- Improvement suggestions from #219097: drop build dependency on sed,
  improve summary and description.

* Sun Dec 10 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8-15
- Trim pre VDR 1.4.0 changelog entries.

* Sat Nov  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8-14
- Install optional Apache proxy snippet as doc, not in-place.
- Build for VDR 1.4.4.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.8-13
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8-12
- Rebuild for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8-11
- Rebuild for VDR 1.4.1-3.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8-10
- Rebuild for VDR 1.4.1.
- Add mod_deflate sample to example proxy config.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.8-9
- Rebuild for VDR 1.4.0.
