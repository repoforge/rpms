Name:           dvb-apps
Version:        1.1.1
Release:        7%{?dist}
Summary:        Utility, demo and test applications using the Linux DVB API

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.linuxtv.org/wiki/index.php/LinuxTV_dvb-apps
Source0:        http://www.linuxtv.org/downloads/linuxtv-dvb-apps-%{version}.tar.bz2
# Source1 created with Source99
Source1:        %{name}-tuningfiles-20060923.tar.bz2
Source2:        http://www.gnu.org/licenses/COPYING
Source99:       %{name}-tuningfiles-snapshot.sh
Patch0:         %{name}-optflags.patch
Patch1:         %{name}-paths.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libusb-devel
BuildRequires:  kernel-headers >= 2.6.16

%description
%{summary}.


%prep
%setup -q -n linuxtv-%{name}-%{version} -a 1
%patch0 -p1
%patch1 -p1
cd util
install -pm 644 av7110_loadkeys/README ../README.av7110_loadkeys
install -pm 644 scan/README ../README.scandvb
install -pm 644 szap/README ../README.szap
install -pm 644 ttusb_dec_reset/README ../README.ttusb_dec_reset
chmod 644 dvbnet/net_start.* scan/{atsc,dvb-?}/*
mv scan/dvb-t/fr-Alen?on scan/dvb-t/fr-Alençon
mv scan/dvb-t/fr-Besan?on scan/dvb-t/fr-Besançon
for f in scan/{atsc,dvb-?}/* ; do
    file $f | grep -q CRLF && sed -i -e 's/\r//' $f
    file $f | grep -q ISO-8859 && \
        iconv -f iso-8859-1 -t utf-8 $f > $f.utf8 && mv $f.utf8 $f
done
cd ..
rm -rf include
install -pm 644 %{SOURCE2} COPYING


%build
make CC="%{__cc}" # %{?_smp_mflags}
make %{?_smp_mflags} CC="%{__cc}" -C util/ttusb_dec_reset


%install
rm -rf $RPM_BUILD_ROOT
cd util
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 av7110_loadkeys/av7110_loadkeys $RPM_BUILD_ROOT%{_bindir}
install -pm 755 av7110_loadkeys/evtest $RPM_BUILD_ROOT%{_bindir}/av7110_evtest
install -pm 755 dvbdate/dvbdate $RPM_BUILD_ROOT%{_bindir}
install -pm 755 dvbnet/dvbnet $RPM_BUILD_ROOT%{_bindir}
install -pm 755 dvbtraffic/dvbtraffic $RPM_BUILD_ROOT%{_bindir}
install -pm 755 scan/scan $RPM_BUILD_ROOT%{_bindir}/scandvb
install -pm 755 szap/?zap $RPM_BUILD_ROOT%{_bindir}
install -pm 755 szap/femon $RPM_BUILD_ROOT%{_bindir}
install -pm 755 ttusb_dec_reset/ttusb_dec_reset $RPM_BUILD_ROOT%{_bindir}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/dvb-apps
cp -pR scan/dvb-? scan/atsc av7110_loadkeys/*.rc{5,mm} \
    $RPM_BUILD_ROOT%{_datadir}/dvb-apps
cd ..


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README* TODO util/dvbnet/net_start.* util/szap/channels.conf-dvb*
%{_bindir}/*
%{_datadir}/dvb-apps/


%changelog
* Mon Oct  2 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1.1-7
- Rebuild.

* Sat Sep 23 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1.1-6
- Include updated set of initial tuning data files from upstream hg (#203328).

* Tue Aug 29 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1.1-5
- Rebuild.

* Thu May 18 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1.1-4
- Include ATSC initial tuning data files.

* Thu May 18 2006 David Woodhouse <dwmw2@infradead.org> - 1.1.1-2
- Rebuild (to unfix kernel-headers on older distros)

* Thu May 18 2006 David Woodhouse <dwmw2@infradead.org> - 1.1.1-1
- Update to dvb-apps 1.1.1 (add ATSC functionality)
- Fix kernel-headers BR

* Tue Feb 21 2006 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-2
- Rebuild.

* Sun Jul 17 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-1
- Include a copy of the GPL.

* Thu Jun 30 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-0.4
- Update URL.

* Sun May 29 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-0.3
- Rebuild for FC4.

* Wed Apr 20 2005 Ville Skyttä <ville.skytta at iki.fi> - 1.1.0-0.2
- Switch to recent glibc-kernheaders which includes userspace DVB headers.

* Sun Dec 26 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.1.0-0.1
- Remove unnecessary Epochs.

* Mon Oct  4 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:1.1.0-0.scop.1
- First build, loosely based on Mandrake's 1.1.0-4mdk.

