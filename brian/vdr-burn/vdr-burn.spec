# TODO: disksize 4420?  4462 was too big sometimes with 0.0.x

%define pname     burn
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define videodir  %(vdr-config --videodir   2>/dev/null || echo ERROR)
%define vardir    %(vdr-config --vardir     2>/dev/null || echo ERROR)
%define vdruser   %(vdr-config --user       2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

%define pre     pre21
%define gver    0.1.3

Name:           vdr-%{pname}
Version:        0.1.0
Release:        0.7.%{pre}%{?dist}
Summary:        DVD writing plugin for VDR

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.xeatre.tv/community/burn/
Source0:        http://linux.kompiliert.net/contrib/%{name}-%{version}-%{pre}.tgz
Source1:        %{name}.conf
Source2:        http://www.muempf.de/down/genindex-%{gver}.tar.gz
Patch0:         %{name}-%{version}-pre21-config.patch
Patch1:         http://www.saunalahti.fi/~rahrenbe/vdr/patches/vdr-burn-cvs-subpicture-id.diff.gz
Patch2:         %{name}-%{version}-pre21-finnish.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47
BuildRequires:  boost-devel
BuildRequires:  gd-devel
Requires:       vdr(abi) = %{apiver}
Requires:       vdrsync
Requires:       m2vrequantiser
Requires:       dvdauthor
Requires:       mjpegtools
Requires:       dvd+rw-tools
Requires:       %{_datadir}/fonts/bitstream-vera/Vera.ttf
# gd-devel < 2.0.33-9.3 bug workaround (gdlib-config --libs)
BuildRequires:  fontconfig-devel

%description
This plugin enables VDR to write compliant DVDs from VDR recordings
while being able to control the process and to watch progress from
inside VDRs on-screen-display.  If the selected recordings don't fit
the DVD, the video tracks are requantized (shrinked) automatically.
The created menus support multipage descriptions (in case the
recording summary exceeds one page).


%prep
%setup -q -c -a 2
cd burn
find -name CVS | xargs rm -rf
chmod -c -x *.[ch] genindex/*.[ch] proctools/*.cc proctools/*.h README
%patch0
%patch1
%patch2
sed -i -e 's|/var/lib/vdr/|%{vardir}/|g' chain-archive.c jobs.c vdrburn-*.sh
cd ../genindex-%{gver}
sed -i -e 's/-g -O2/$(RPM_OPT_FLAGS)/' Makefile
f=README ; iconv -f iso-8859-1 -t utf-8 -o ../README.genindex $f
cd ..


%build
make -C burn %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all
make -C genindex-%{gver} %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}/bin
install -pm 755 burn/libvdr-%{pname}.so.%{apiver} $RPM_BUILD_ROOT%{plugindir}
install -pm 755 burn/*.sh burn/burn-buffers genindex-%{gver}/genindex \
  $RPM_BUILD_ROOT%{plugindir}/bin
install -dm 755 $RPM_BUILD_ROOT%{configdir}/plugins/burn/skins
cp -pR burn/burn/* $RPM_BUILD_ROOT%{configdir}/plugins/burn
rm -rf $RPM_BUILD_ROOT%{configdir}/plugins/burn/{counters,fonts/*}
ln -s %{_datadir}/fonts/bitstream-vera/Vera.ttf \
  $RPM_BUILD_ROOT%{configdir}/plugins/burn/fonts/
install -Dpm 644 burn/burn/counters/standard \
  $RPM_BUILD_ROOT%{vardir}/burn/counters/standard
install -Dpm 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf


%clean
rm -rf $RPM_BUILD_ROOT


%post
if [ $1 -gt 1 ] ; then # maybe upgrading from < 0.1.0?
  %{__perl} -pi -e 's/^.*(burnmark|handlearchived)\.sh.*\n$//' \
    %{configdir}/reccmds.conf >/dev/null 2>&1 || :
fi


%files
%defattr(-,root,root,-)
%doc burn/COPYING burn/HISTORY burn/README README.genindex
%config(noreplace) %{_sysconfdir}/sysconfig/vdr-plugins.d/%{pname}.conf
%config(noreplace) %{configdir}/plugins/%{pname}/
%{plugindir}/bin/burn-buffers
%{plugindir}/bin/genindex
%{plugindir}/bin/vdrburn-archive.sh
%{plugindir}/bin/vdrburn-dvd.sh
%{plugindir}/libvdr-%{pname}.so.%{apiver}
%defattr(-,%{vdruser},root)
%config(noreplace) %{vardir}/burn/


%changelog
* Sun Jan  7 2007 Ville Skyttä <ville.skytta at iki.fi> - 0.1.0-0.7.pre21
- Rebuild for VDR 1.4.5.

* Tue Dec 12 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.1.0-0.6.pre21
- 0.1.0-pre21, include private copy of genindex (0.1.3) for now.

* Sat Nov  4 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-16
- Rebuild for VDR 1.4.4.

* Fri Oct 06 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0.009-15
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-14
- Rebuild for VDR 1.4.3.

* Sun Aug  6 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-13
- Rebuild for VDR 1.4.1-3.

* Sun Jun 11 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-12
- Rebuild for VDR 1.4.1.

* Sun Apr 30 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-11
- Rebuild for VDR 1.4.0.

* Mon Apr 17 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-10
- Rebuild/adjust for VDR 1.3.47, require versioned vdr(abi).
- Trim pre-RLO %%changelog entries.

* Sun Mar 26 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-9
- Rebuild for VDR 1.3.45.

* Sat Mar 18 2006 Thorsten Leemhuis <fedora at leemhuis.info> - 0.0.009-8
- drop 0.lvn

* Wed Mar  1 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.8
- Decrease default DVD size to 4420 to accommodate more requant inaccuracy.
- Rebuild for VDR 1.3.44.

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sun Feb 19 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.7
- Rebuild for VDR 1.3.43.

* Sun Feb  5 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.6
- Rebuild for VDR 1.3.42.

* Sun Jan 22 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.5
- Rebuild for VDR 1.3.40.

* Sun Jan 15 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.4
- Rebuild for VDR 1.3.39.

* Sun Jan  8 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.3
- Rebuild for VDR 1.3.38.

* Sat Dec 31 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.2
- Q'n'd fix for ISO creation with recordings whose title contain "/".
- Fix storing of the "clean up after # jobs" configuration option.
- Don't chmod everything in results to 0777 in author only mode.
- Use tcmplex-panteltje by default again.
- Translation improvements.
- Fix up some paths in README.
- Ship TODO.

* Sun Nov 13 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.009-0.lvn.1
- 0.0.009 + Finnish translations from Rolf Ahrenberg, config patch
  applied upstream.

* Sat Nov 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.007-0.lvn.1
- 0.0.007, endstatus and burndefault patches applied/obsoleted upstream.

* Sun Nov  6 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6k-0.lvn.2
- Rebuild for VDR 1.3.36.

* Tue Nov  1 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6k-0.lvn.1
- 0.0.6k, commands and VDR >= 1.3.25 patches applied upstream.
- Improve default burn settings.
- Fix burn status at end when not verifying.

* Mon Oct  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6g-1.lvn.8.pre3
- Rebuild for VDR 1.3.34.

* Sun Sep 25 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6g-1.lvn.7.pre3
- Rebuild for VDR 1.3.33.

* Sun Sep 11 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6g-1.lvn.6.pre3
- Rebuild for VDR 1.3.32.

* Tue Aug 30 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6g-1.lvn.5.pre3
- Rebuild for VDR 1.3.31.

* Sun Aug 21 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6g-1.lvn.4.pre3
- Rebuild for VDR 1.3.30.

* Fri Aug 19 2005 Dams <anvil[AT]livna.org> - 0.0.6g-1.lvn.3.pre3
- Redirected vdr-config invocation standard error to /dev/null

* Tue Aug 16 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6g-1.lvn.2.pre3
- Try to avoid build system problems by not using %%expand with vdr-config.

* Fri Aug 12 2005 Ville Skyttä <ville.skytta at iki.fi> - 0.0.6g-1.lvn.1.pre3
- Update URLs.
