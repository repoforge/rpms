# $Id$
# Authority: matthias

# DistExclude: el2 rh7 rh9 el3 el4 el5

%define real_name madwifi-ng

Summary: Multiband Atheros Driver for Wireless Fidelity
Name: madwifi
Version: 0.9.4
%define real_version r2598-20070725
Release: 0.1.r2598
License: GPL
Group: System Environment/Kernel
URL: http://madwifi.org/
#Source: http://downloads.sf.net/madwifi/madwifi-.tar.bz2
Source: http://snapshots.madwifi.org/madwifi-trunk-current.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: gcc, make
Requires(post): dkms
Requires(preun): dkms
Provides: dkms-madwifi = %{version}-%{release}

%description
MadWifi is short for Multiband Atheros Driver for Wireless Fidelity. It
provides a Linux kernel device driver for Atheros-based Wireless LAN
devices. The driver works such that your WLAN card will appear as a normal
network interface in the system. Additionally there is support for the
Wireless Extensions API. This allows you to configure the device using
common wireless tools (ifconfig, iwconfig and friends).


%prep
%setup -n %{real_name}-%{real_version}


%build
# Tools build
export CFLAGS="%{optflags}"
%{__make} -C tools %{?_smp_mflags} \
    BINDIR=%{_bindir} \
    MANDIR=%{_mandir}


%install
%{__rm} -rf %{buildroot}

%define dkms_name madwifi
%define dkms_vers %{version}-%{release}
%define quiet -q

# Tools install
%{__make} -C tools install \
    DESTDIR=%{buildroot} \
    STRIP=true \
    BINDIR=%{_bindir} \
    MANDIR=%{_mandir}

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/
%{__cp} -a ath/ ath_hal/ ath_rate/ hal/ include/ net80211/ scripts/ \
    BuildCaps.inc kernelversion.c Makefile Makefile.inc release.h \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{dkms_vers}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{dkms_vers}
MAKE[0]="make modules KERNELPATH=${kernel_source_dir}"
BUILT_MODULE_NAME[0]=ath_pci
BUILT_MODULE_LOCATION[0]=ath
BUILT_MODULE_NAME[1]=ath_hal
BUILT_MODULE_LOCATION[1]=ath_hal
BUILT_MODULE_NAME[2]=wlan
BUILT_MODULE_LOCATION[2]=net80211
BUILT_MODULE_NAME[3]=wlan_acl
BUILT_MODULE_LOCATION[3]=net80211
BUILT_MODULE_NAME[4]=wlan_ccmp
BUILT_MODULE_LOCATION[4]=net80211
BUILT_MODULE_NAME[5]=wlan_scan_ap
BUILT_MODULE_LOCATION[5]=net80211
BUILT_MODULE_NAME[6]=wlan_scan_sta
BUILT_MODULE_LOCATION[6]=net80211
BUILT_MODULE_NAME[7]=wlan_tkip
BUILT_MODULE_LOCATION[7]=net80211
BUILT_MODULE_NAME[8]=wlan_wep
BUILT_MODULE_LOCATION[8]=net80211
BUILT_MODULE_NAME[9]=wlan_xauth
BUILT_MODULE_LOCATION[9]=net80211
BUILT_MODULE_NAME[10]=ath_rate_amrr
BUILT_MODULE_LOCATION[10]=ath_rate/amrr
BUILT_MODULE_NAME[11]=ath_rate_onoe
BUILT_MODULE_LOCATION[11]=ath_rate/onoe
BUILT_MODULE_NAME[12]=ath_rate_sample
BUILT_MODULE_LOCATION[12]=ath_rate/sample
DEST_MODULE_LOCATION[0]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[1]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[2]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[3]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[4]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[5]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[6]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[7]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[8]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[9]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[10]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[11]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[12]=/kernel/drivers/net/wireless
AUTOINSTALL="YES"
EOF


%clean
%{__rm} -rf %{buildroot}


%post
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
# Rebuild and make available for the currenty running kernel
dkms build -m %{dkms_name} -v %{dkms_vers} %{?quiet} || :
dkms install -m %{dkms_name} -v %{dkms_vers} %{?quiet} --force || :

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{dkms_vers} %{?quiet} --all || :


%files
%defattr(-,root,root,-)
%doc COPYRIGHT README THANKS
#doc docs/users-guide.pdf docs/WEP-HOWTO.txt
%{_bindir}/*
%{_mandir}/man8/*
%{_usrsrc}/%{dkms_name}-%{dkms_vers}/


%changelog
* Mon Jul 23 2007 Matthias Saou <http://freshrpms.net/> 0.9.4-0.1.r2594
- Update to svn trunk to compile with F7 2.6.22 kernels (madwifi #1434).

* Tue Mar 20 2007 Matthias Saou <http://freshrpms.net/> 0.9.3-2
- Commit with the new "ath_hal" directory added.
- Commit with the two new ath_rate_amrr and ath_rate_onoe modules added.

* Mon Mar 19 2007 Matthias Saou <http://freshrpms.net/> 0.9.3-1
- Update to 0.9.3, which works with 2.6.20+ kernels.
- Remove no longer needed 2.6.18-config patch.
- Update noWerr patch (kept just in case the same happens again).

* Tue Jan  9 2007 Matthias Saou <http://freshrpms.net/> 0.9.2.1-2
- Add patch to remove -Werr since warnings are printed with recent FC6 kernels.

* Mon Dec 11 2006 Matthias Saou <http://freshrpms.net/> 0.9.2.1-1
- Update to 0.9.2.1 security fix release.

* Tue Oct 10 2006 Matthias Saou <http://freshrpms.net/> 0.9.2-2
- Add the rpm release to the dkms module version, to make updating the module
  to a fixed same version work (--rpm_safe_upgrade doesn't work as advertised).
- Force modules install so that the same version can be overwritten instead of
  uninstalled by the old package's %%preun when updating.
- Add build time quiet flag for the scriplets. Undefine to do verbose testing.

* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 0.9.2-1.1
- Add dkms-madwifi provides.
- Use %%{dkms_name} macro for the usr/src directory name.

* Fri Oct  6 2006 Matthias Saou <http://freshrpms.net/> 0.9.2-1
- Initial RPM release.

