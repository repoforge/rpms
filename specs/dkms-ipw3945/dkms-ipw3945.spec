# $Id$
# Authority: matthias
# Dist: nodist

%define dkms_name ipw3945

Summary: Driver for Intel® PRO/Wirelss 3945 network adaptors
Name: dkms-ipw3945
Version: 1.1.0
Release: 1
License: GPL
Group: System Environment/Kernel
URL: http://ipw3945.sourceforge.net/
Source: http://dl.sf.net/ipw3945/ipw3945-%{version}.tgz
Patch0: ipw3945-1.1.0-ieee80211_api.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
Requires: gcc
Requires: ipw3945-firmware, ipw3945d
Requires(pre): dkms
Requires(post): dkms

%description
Driver (Linux kernel module) for Intel® PRO/Wirelss 3945 network adaptors.


%prep
%setup -n ipw3945-%{version}
%patch0 -p1 -b .ieee80211_api


%build


%install
%{__rm} -rf %{buildroot}

# Kernel module sources install for dkms
%{__mkdir_p} %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/
%{__cp} -a *.h *.c Makefile snapshot/ \
    %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/

# Configuration for dkms
%{__cat} > %{buildroot}%{_usrsrc}/%{dkms_name}-%{version}/dkms.conf << 'EOF'
PACKAGE_NAME=%{dkms_name}
PACKAGE_VERSION=%{version}
BUILT_MODULE_NAME[0]=ipw3945
DEST_MODULE_LOCATION[0]=/kernel/drivers/net/wireless
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
%doc CHANGES ISSUES LICENSE* README.ipw3945
%{_usrsrc}/%{dkms_name}-%{version}/


%changelog
* Mon Oct  9 2006 Matthias Saou <http://freshrpms.net/> 1.1.0-1
- Initial RPM release.

