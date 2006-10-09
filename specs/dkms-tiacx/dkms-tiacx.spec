# $Id$
# Authority: matthias

%define dkms_name tiacx

Summary: Driver for Texas Instruments' ACX100/ACX111 wireless network chips
Name: dkms-tiacx
Version: 0.4.7
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://www.kernel.org/pub/linux/kernel/people/linville/
Source: http://www.kernel.org/pub/linux/kernel/people/linville/tiacx.tar.bz2
Patch0: dkms-tiacx-0.4.7-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc
Requires: acx100-firmware, acx111-firmware
Requires(pre): dkms
Requires(post): dkms

%description
Driver (Linux kernel module) for network interface cards based on Texas
Instruments' ACX100/ACX111 wireless network chips.


%prep
%setup -c %{name}-%{version}
%patch0 -p0 -b .build


%build


%install
%{__rm} -rf %{buildroot}

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
%{__cp} -a drivers/net/wireless/tiacx/{*.h,*.c,Makefile} \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{version}
MAKE[0]="make -C ${kernel_source_dir} M=${dkms_tree}/%{dkms_name}/%{version}/build CONFIG_ACX_PCI=m CONFIG_ACX_USB=m"
CLEAN[0]="make -C ${kernel_source_dir} M=${dkms_tree}/%{dkms_name}/%{version}/build CONFIG_ACX_PCI=m CONFIG_ACX_USB=m clean"
BUILT_MODULE_NAME[0]=acx-common
BUILT_MODULE_NAME[1]=acx-pci
BUILT_MODULE_NAME[2]=acx-usb
DEST_MODULE_LOCATION[0]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[1]=/kernel/drivers/net/wireless
DEST_MODULE_LOCATION[2]=/kernel/drivers/net/wireless
AUTOINSTALL="YES"
EOF


%clean
%{__rm} -rf %{buildroot}


%post
# Add to DKMS registry
dkms add -m %{dkms_name} -v %{version} -q --rpm_safe_upgrade
# Build now
dkms build -m %{dkms_name} -v %{version} -q
dkms install -m %{dkms_name} -v %{version} -q

%preun
# Remove all versions from DKMS registry
dkms remove -m %{dkms_name} -v %{version} --all -q --rpm_safe_upgrade


%files
%defattr(-, root, root, 0755)
%doc drivers/net/wireless/tiacx/README
%{_usrsrc}/%{dkms_name}-%{version}/


%changelog
* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 0.4.7-1
- Initial RPM release.

