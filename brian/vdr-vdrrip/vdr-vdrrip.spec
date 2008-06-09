%define pname     vdrrip
%define plugindir %(vdr-config --plugindir  2>/dev/null || echo ERROR)
%define configdir %(vdr-config --configdir  2>/dev/null || echo ERROR)
%define apiver    %(vdr-config --apiversion 2>/dev/null || echo ERROR)

Name:           vdr-%{pname}
Version:        0.3.0
Release:        1
Summary:        VDR recordings format converter

Group:          Applications/Multimedia
License:        GPL
URL:            http://www.berlios.de/vdr/
Source0:        http://www.berlios.de/vdr/downloads/%{name}-%{version}.tgz
Source1:	vdrrip.init
Source2:	vdrrip.sysconfig
Source3:	vdrripsplit.sh
Patch1:         02_maketempdir.dpatch
Patch2:         03_greppid2.dpatch
Patch3:         05_fix-dvdparameter.dpatch
Patch4:         06_fix-ogm-ac3-vdrsync-dev.dpatch
Patch5:         07_preserve-queue-owner.dpatch
Patch6:         11_fix-identify-aspect.dpatch
Patch7:         91_vdrrip+dvd-0.3.0-1.3.7.dpatch
Patch8:         vdrrip-0.3.0-paths.patch
Patch9:         vdrrip-0.3.0-queue-bg.patch
Patch10:        vdrrip-dvdnav2dvdread.patch
Patch11:        vdrrip-dvdread-inttypes.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  vdr-devel >= 1.3.47 
Requires:       vdr(abi) = %{apiver} mplayer

%description
VDR plugin for converting recordings into other formats like xvid, ogm, avi, divx, mpeg4

%prep
%setup -q -n %{pname}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1


%build
#./configure
make %{?_smp_mflags} LIBDIR=. VDRDIR=%{_libdir}/vdr all


%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT%{plugindir}
install -dm 755 $RPM_BUILD_ROOT/usr/bin/
install -pm 755 libvdr-%{pname}.so $RPM_BUILD_ROOT%{plugindir}/libvdr-%{pname}.so.%{apiver}
install -Dpm 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/vdrrip
install -m644 scripts/queuehandler.sh.conf $RPM_BUILD_ROOT%{_bindir}/
install -m755 scripts/queuehandler.sh $RPM_BUILD_ROOT%{_bindir}/
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -pm 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/vdrripsplit.sh
sed -e 's|/usr/lib/vdr/|%{plugindir}/|' < %{SOURCE2} \
  > $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdrrip
chmod 644 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/vdrrip


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING HISTORY README
%{plugindir}/libvdr-%{pname}.so.%{apiver}
%{_bindir}/vdrripsplit.sh
%{_bindir}/queuehandler.sh
%dir %{plugindir}
%dir %{_sysconfdir}
%config(noreplace) %{_bindir}/queuehandler.sh.conf
%{_initrddir}
%config(noreplace) %{_sysconfdir}


%changelog

